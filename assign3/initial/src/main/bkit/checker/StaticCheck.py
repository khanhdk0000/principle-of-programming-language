"""
 * @author nhphung
"""
from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
from AST import *
from Visitor import *
from StaticError import *
from functools import *


class Type(ABC):
    __metaclass__ = ABCMeta
    pass


class Prim(Type):
    __metaclass__ = ABCMeta
    pass


class IntType(Prim):
    pass


class FloatType(Prim):
    pass


class StringType(Prim):
    pass


class BoolType(Prim):
    pass


class VoidType(Type):
    pass


class Unknown(Type):
    pass


@dataclass
class ArrayType(Type):
    dimen: List[int]
    eletype: Type

    def set_type(self, typ):
        self.eletype = typ


@dataclass
class MType:
    intype: List[Type]
    restype: Type


@dataclass
class Symbol:
    name: str
    mtype: Type

    def set_type(self, typ):
        self.mtype = typ


# Function type to represent function
class FunctionType(Type):
    def __init__(self, param: List[Symbol], restype=None):
        self.param = param
        self.restype = restype

    def set_type(self, typ):
        self.restype = typ


class StaticChecker(BaseVisitor):
    def __init__(self, ast):
        self.ast = ast
        self.global_envi = [
            Symbol("int_of_float", MType([FloatType()], IntType())),
            Symbol("float_to_int", MType([IntType()], FloatType())),
            Symbol("int_of_string", MType([StringType()], IntType())),
            Symbol("string_of_int", MType([IntType()], StringType())),
            Symbol("float_of_string", MType([StringType()], FloatType())),
            Symbol("string_of_float", MType([FloatType()], StringType())),
            Symbol("bool_of_string", MType([StringType()], BoolType())),
            Symbol("string_of_bool", MType([BoolType()], StringType())),
            Symbol("read", MType([], StringType())),
            Symbol("printLn", MType([], VoidType())),
            Symbol("print", MType([StringType()], VoidType())),
            Symbol("printStrLn", MType([StringType()], VoidType()))]

    def check(self):
        return self.visit(self.ast, self.global_envi)

    # Search for a symbol inside a given list with name
    def search(self, name, lst):
        for x in lst:
            for y in x:
                if name == y.name:
                    return y
        return None

    # change the type of the symbol
    def infer_type(self, symbol, infer_type):
        if isinstance(symbol.mtype, ArrayType):
            symbol.mtype.set_type(infer_type)
            return symbol.mtype.eletype
        elif isinstance(symbol.mtype, FunctionType):
            if isinstance(symbol.mtype.restype, ArrayType):
                symbol.mtype.restype.set_type(infer_type)
                return symbol.mtype.restype.eletype
            else:
                symbol.mtype.set_type(infer_type)
                return symbol.mtype.restype
        elif isinstance(symbol.mtype, Unknown):
            symbol.set_type(infer_type)
        return symbol.mtype

    # Check if a variable is redeclared and return that symbol
    def checkRedeclare(self, sym, typ, envi):
        # The typ is the type of the symbol (Variable, Function, Parameter, Identifier)
        if self.search(sym.name, envi):
            raise Redeclared(typ, sym.name)
        return sym

    def get_operator_type(self, op):
        # Get the type based on the operator
        if op in ['+', '-', '*', '\\', '%', '==', '!=', '<', '>', '<=', '>=']:
            return IntType()
        elif op in ['+.', '-.', '*.', '\\.', '=/=', '<.', '>.', '<=.', '>=.']:
            return FloatType()
        elif op in ['!', '&&', '||']:
            return BoolType()

    def get_name(self, var):
        # Get the name of the identifier, array of call expression
        if isinstance(var, Id):
            return var.name
        elif isinstance(var, ArrayCell):
            return var.arr.name if isinstance(var.arr, Id) else var.arr.method.name
        elif isinstance(var, CallExpr):
            return var.method.name

    def visitProgram(self, ast, c):
        name = []  # The list of all function declaration name
        # Loop through all declarations first time to get the name and the parameter in case of function

        for i in ast.decl:
            # If variable declaration, append to the environment
            if isinstance(i, VarDecl):
                c.append(i.accept(self, c))
            # If function initialize symbol with function type and parameter of unknown type
            else:
                func_name = i.name.name
                name.append(func_name)
                # Check redeclare of function declaration
                self.checkRedeclare(Symbol(func_name, Unknown()), Function(), [c])
                para = []
                for j in i.param:
                    # the type of function is Unknown if there is no array type parameter, otherwise it's array type
                    para_sym = Symbol(j.variable.name, ArrayType(j.varDimen, Unknown())) if len(j.varDimen) > 0 \
                        else Symbol(j.variable.name, Unknown())
                    para_tem = self.checkRedeclare(para_sym, Parameter(), [para])
                    para.append(para_tem)
                # Append the function with declared parameters into environment
                c.append(Symbol(func_name, FunctionType(para, Unknown())))

        # Check if there is function name main, if not raise no entry point
        if 'main' not in name:
            raise NoEntryPoint()
        # Second loop is to check every part of the program
        for x in ast.decl:
            if isinstance(x, FuncDecl):
                x.accept(self, c)

    def visitVarDecl(self, ast, c):
        # Initialize a variable and check if it is redeclared
        if len(ast.varDimen) > 0:
            # Composite variable
            if ast.varInit:
                tem = Symbol(ast.variable.name, ast.varInit.accept(self, c))
            else:
                tem = Symbol(ast.variable.name, ArrayType(ast.varDimen, Unknown()))
        else:
            # Scalar variable
            tem = Symbol(ast.variable.name, ast.varInit.accept(self, c)) if ast.varInit else Symbol(ast.variable.name,
                                                                                                    Unknown())
        return self.checkRedeclare(tem, Variable(), [c])

    def visitFuncDecl(self, ast, c):
        local = []
        func_sym = self.search(ast.name.name, [c])  # Search for the function symbol

        for i in ast.body[0]:
            # visit the variable declaration and append to the local env, also check if any variable
            # declaration has same name as parameter
            tem_var = i.accept(self, func_sym.mtype.param + local)
            local.append(tem_var)

        for j in ast.body[1]:
            # visit statement with
            # c[0]: local env with parameter and variable declaration
            # c[1]: global env
            # c[2]: the name of function so other stmt can search for the function symbol
            j.accept(self, [func_sym.mtype.param + local, c, func_sym.name])

    def visitAssign(self, ast, c):
        c = c[:3] + [ast]  # append the ast so the expression can raise with the whole statement (Typecannotbeinfer)
        lhs = ast.lhs.accept(self, c)
        rhs = ast.rhs.accept(self, c)

        lhs_name = self.get_name(ast.lhs)
        rhs_name = self.get_name(ast.rhs)
        # If the dimension of the two array is wrong, raise
        if isinstance(lhs, ArrayType) and isinstance(rhs, ArrayType):
            if lhs.dimen != rhs.dimen:
                raise TypeMismatchInStatement(ast)
        if isinstance(lhs, ArrayType) and not isinstance(rhs, ArrayType):
            raise TypeMismatchInStatement(ast)
        if not isinstance(lhs, ArrayType) and isinstance(rhs, ArrayType):
            raise TypeMismatchInStatement(ast)

        lhs = self.get_type(lhs)
        rhs = self.get_type(rhs)
        # If both side of the assignment is unknown
        if isinstance(lhs, Unknown) and isinstance(rhs, Unknown):
            raise TypeCannotBeInferred(ast)

        # Lhs can not be void type
        if isinstance(lhs, Unknown) and not isinstance(rhs, VoidType):
            sym = self.search(lhs_name, [c[0], c[1]])
            lhs = self.infer_type(sym, rhs)
        if isinstance(rhs, Unknown):
            sym = self.search(rhs_name, [c[0], c[1]])
            rhs = self.infer_type(sym, lhs)
        if type(rhs) != type(lhs):
            raise TypeMismatchInStatement(ast)

    def get_type(self, i):
        # get the type of different ast properties
        if isinstance(i, ArrayType):
            return i.eletype
        elif isinstance(i, FunctionType):
            return i.restype
        elif isinstance(i, MType):
            return i.restype
        return i

    def visitCallStmt(self, ast, c):
        c = c[:3] + [ast]
        predefine = False  # variable to check if the call stmt is in the 12 predefined method
        # only search in c[1] as function reside in global
        func_sym = self.search(ast.method.name, [c[0], c[1]])
        # raise undeclare if call sym is not of type function of mtype
        if func_sym is None:
            raise Undeclared(Function(), ast.method.name)
        if not isinstance(func_sym.mtype, (FunctionType, MType)):
            raise Undeclared(Function(), ast.method.name)

        # Check if the call stmt is in the 12 predefined functions
        if func_sym in self.global_envi[:12]:
            para_list = func_sym.mtype.intype
            predefine = True
            ret_typ = func_sym.mtype.restype
        else:
            para_list = func_sym.mtype.param
            ret_typ = func_sym.mtype.restype

        # Call stmt must be of void type
        if isinstance(ret_typ, Unknown):
            ret_typ = self.infer_type(func_sym, VoidType())
        if not isinstance(ret_typ, VoidType):
            raise TypeMismatchInStatement(ast)

        # The length of parameter list of function and the call stmt must be the same
        if len(para_list) != len(ast.param):
            raise TypeMismatchInStatement(ast)

        # check every element of para list and argument list
        for para_sym, arg_exp in zip(para_list, ast.param):  # TODO: what if stmt: main(main(5))
            ptype = para_sym.mtype if not predefine else para_sym
            arg_typ = arg_exp.accept(self, c)

            # if one of the var is of para type, the other must be of para type
            if isinstance(ptype, ArrayType) and not isinstance(arg_typ, ArrayType):
                raise TypeMismatchInStatement(ast)
            if not isinstance(ptype, ArrayType) and isinstance(arg_typ, ArrayType):
                raise TypeMismatchInStatement(ast)

            ptype = self.get_type(ptype)
            arg_typ = self.get_type(arg_typ)
            if isinstance(ptype, Unknown) and isinstance(arg_typ, Unknown):
                raise TypeCannotBeInferred(ast)
            if isinstance(ptype, Unknown):
                ptype = self.infer_type(para_sym, arg_typ)
            if isinstance(arg_typ, Unknown):
                name = self.get_name(arg_exp)
                sym = self.search(name, [c[0], c[1]])
                arg_typ = self.infer_type(sym, ptype)
            if type(ptype) != type(arg_typ):
                raise TypeMismatchInStatement(ast)

    def visitCallExpr(self, ast, c):
        predefine = False
        func_sym = self.search(ast.method.name, [c[0], c[1]])
        if func_sym is None:
            raise Undeclared(Function(), ast.method.name)
        if not isinstance(func_sym.mtype, (FunctionType, MType)):
            raise Undeclared(Function(), ast.method.name)
        # Check if the call stmt is in the 12 predefined functions
        if func_sym in self.global_envi[:12]:
            para_list = func_sym.mtype.intype
            predefine = True
        else:
            para_list = func_sym.mtype.param

        # The length of parameter list of function and the call exp must be the same
        if len(para_list) != len(ast.param):
            raise TypeMismatchInExpression(ast)

        for para_sym, arg_exp in zip(para_list, ast.param):
            ptype = para_sym.mtype if not predefine else para_sym

            # this part is to infer the type of the function immediately if its type is unknown
            # it is used when the para type is call expr, infer it before visit it.
            if isinstance(arg_exp, CallExpr):
                name = self.get_name(arg_exp)
                sym = self.search(name, [c[0], c[1]])
                arg_typ = sym.mtype.restype
                if isinstance(ptype, Unknown):
                    ptype = self.infer_type(para_sym, arg_typ)
            arg_typ = arg_exp.accept(self, c)

            # if one of the var is of para type, the other must be of para type
            if isinstance(ptype, ArrayType) and not isinstance(arg_typ, ArrayType):
                raise TypeMismatchInStatement(c[3])
            if not isinstance(ptype, ArrayType) and isinstance(arg_typ, ArrayType):
                raise TypeMismatchInStatement(c[3])

            ptype = self.get_type(ptype)
            arg_typ = self.get_type(arg_typ)
            if isinstance(ptype, Unknown) and isinstance(arg_typ, Unknown):
                raise TypeCannotBeInferred(c[3])
            if isinstance(ptype, Unknown):
                ptype = self.infer_type(para_sym, arg_typ)
            if isinstance(arg_typ, Unknown):
                name = self.get_name(arg_exp)
                sym = self.search(name, [c[0], c[1]])
                arg_typ = self.infer_type(sym, ptype)
            if type(ptype) != type(arg_typ):
                raise TypeMismatchInExpression(ast)
        # search for the function again to get the correct type after being inferred
        check = self.search(ast.method.name, [c[1]])
        return check.mtype

    def visitIf(self, ast, c):
        c = c[:3] + [ast]
        # loop through the if then part
        for x in ast.ifthenStmt:
            # if the exp is of type callexpr, array then infer the type before read it
            if isinstance(x[0], (CallExpr, ArrayCell)):
                name = self.get_name(x[0])
                sym = self.search(name, [c[0], c[1]])
                # If Unknown, infer bool, else raise
                tem_typ = self.get_type(sym.mtype)
                if isinstance(tem_typ, Unknown):
                    self.infer_type(sym, BoolType())
                elif not isinstance(tem_typ, BoolType):
                    raise TypeMismatchInStatement(ast)

            exp = x[0].accept(self, c)
            exp = self.get_type(exp)
            # If exp is unknown, infer type bool
            if isinstance(exp, Unknown):
                name = self.get_name(x[0])
                sym = self.search(name, [c[0], c[1]])
                exp = self.infer_type(sym, BoolType())

            # Check if the first expression is of bool type
            if not isinstance(exp, BoolType):
                raise TypeMismatchInStatement(ast)

            local = []
            for y in x[1]:
                tem_var = y.accept(self, local)
                local.append(tem_var)
            for z in x[2]:
                z.accept(self, [local + c[0], c[1], c[2]])
        # The else part(only 1 tuple)
        else_local = []
        for i in ast.elseStmt[0]:
            tem_else_var = i.accept(self, else_local)
            else_local.append(tem_else_var)
        for k in ast.elseStmt[1]:
            k.accept(self, [else_local + c[0], c[1], c[2]])

    def visitFor(self, ast, c):
        c = c[:3] + [ast]

        # # Infer the int type for the idx before visiting it if it is function or array
        # if isinstance(ast.idx1, (CallExpr, ArrayCell)):
        #     name = self.get_name(ast.idx1)
        #     sym = self.search(name, [c[0], c[1]])
        #     self.infer_type(sym, IntType())
        idx = ast.idx1.accept(self, c)
        idx = self.get_type(idx)
        # If first, second and fourth expr is unknown, infer type int
        if isinstance(idx, Unknown):
            name = self.get_name(ast.idx1)
            sym = self.search(name, [c[0], c[1]])
            idx = self.infer_type(sym, IntType())
        if not isinstance(idx, IntType):
            raise TypeMismatchInStatement(ast)

        # Infer type int for expr1 before visiting it
        if isinstance(ast.expr1, (CallExpr, ArrayCell)):
            name = self.get_name(ast.expr1)
            sym = self.search(name, [c[0], c[1]])
            # If Unknown, infer int, else raise
            tem_typ = self.get_type(sym.mtype)
            if isinstance(tem_typ, Unknown):
                self.infer_type(sym, IntType())
            elif not isinstance(tem_typ, IntType):
                raise TypeMismatchInStatement(ast)

        exp1 = ast.expr1.accept(self, c)
        exp1 = self.get_type(exp1)
        # Check if expression 1 is of int type
        if isinstance(exp1, Unknown):
            name = self.get_name(ast.expr1)
            sym = self.search(name, [c[0], c[1]])
            exp1 = self.infer_type(sym, IntType())
        if not isinstance(exp1, IntType):
            raise TypeMismatchInStatement(ast)

        # Infer type bool for expr2 before visiting it
        if isinstance(ast.expr2, (CallExpr, ArrayCell)):
            name = self.get_name(ast.expr2)
            sym = self.search(name, [c[0], c[1]])
            # If Unknown, infer bool, else raise
            tem_typ = self.get_type(sym.mtype)
            if isinstance(tem_typ, Unknown):
                self.infer_type(sym, BoolType())
            elif not isinstance(tem_typ, BoolType):
                raise TypeMismatchInStatement(ast)

        exp2 = ast.expr2.accept(self, c)
        exp2 = self.get_type(exp2)
        # Check if expression 2 is of bool type
        if isinstance(exp2, Unknown):
            name = self.get_name(ast.expr2)
            sym = self.search(name, [c[0], c[1]])
            exp2 = self.infer_type(sym, BoolType())
        if not isinstance(exp2, BoolType):
            raise TypeMismatchInStatement(ast)

        # Infer type int for expr3 before visiting it
        if isinstance(ast.expr3, (CallExpr, ArrayCell)):
            name = self.get_name(ast.expr3)
            sym = self.search(name, [c[0], c[1]])
            # If Unknown, infer bool, else raise
            tem_typ = self.get_type(sym.mtype)
            if isinstance(tem_typ, Unknown):
                self.infer_type(sym, BoolType())
            elif not isinstance(tem_typ, BoolType):
                raise TypeMismatchInStatement(ast)

        exp3 = ast.expr3.accept(self, c)
        exp3 = self.get_type(exp3)
        # Check if expression 3 is of int type
        if isinstance(exp3, Unknown):
            name = self.get_name(ast.expr3)
            sym = self.search(name, [c[0], c[1]])
            exp3 = self.infer_type(sym, IntType())
        if not isinstance(exp3, IntType):
            raise TypeMismatchInStatement(ast)

        local = []
        for i in ast.loop[0]:
            tem_var = i.accept(self, local)
            local.append(tem_var)
        for k in ast.loop[1]:
            k.accept(self, [local + c[0], c[1], c[2]])

    def visitWhile(self, ast, c):
        c = c[:3] + [ast]
        # Infer type bool for expr before visiting it
        if isinstance(ast.exp, (CallExpr, ArrayCell)):
            name = self.get_name(ast.exp)
            sym = self.search(name, [c[0], c[1]])
            # If Unknown, infer bool, else raise
            tem_typ = self.get_type(sym.mtype)
            if isinstance(tem_typ, Unknown):
                self.infer_type(sym, BoolType())
            elif not isinstance(tem_typ, BoolType):
                raise TypeMismatchInStatement(ast)

        exp = ast.exp.accept(self, c)
        exp = self.get_type(exp)
        # Check if the expression is of bool type, if not update otherwise raise
        if isinstance(exp, Unknown):
            name = self.get_name(ast.exp)
            sym = self.search(name, [c[0], c[1]])
            exp = self.infer_type(sym, BoolType())
        if not isinstance(exp, BoolType):
            raise TypeMismatchInStatement(ast)
        local = []
        for i in ast.sl[0]:
            tem_var = i.accept(self, local)
            local.append(tem_var)
        for k in ast.sl[1]:
            k.accept(self, [local + c[0], c[1], c[2]])

    def visitDowhile(self, ast, c):
        c = c[:3] + [ast]
        local = []
        for i in ast.sl[0]:
            tem_var = i.accept(self, local)
            local.append(tem_var)
        for k in ast.sl[1]:
            k.accept(self, [local + c[0], c[1], c[2]])

        # Infer type bool for expr before visiting it
        if isinstance(ast.exp, (CallExpr, ArrayCell)):
            name = self.get_name(ast.exp)
            sym = self.search(name, [c[0], c[1]])
            # If Unknown, infer bool, else raise
            tem_typ = self.get_type(sym.mtype)
            if isinstance(tem_typ, Unknown):
                self.infer_type(sym, BoolType())
            elif not isinstance(tem_typ, BoolType):
                raise TypeMismatchInStatement(ast)

        exp = ast.exp.accept(self, c)
        exp = self.get_type(exp)
        # Check if expression of bool type after the stmt list
        if isinstance(exp, Unknown):
            name = self.get_name(ast.exp)
            sym = self.search(name, [c[0], c[1]])
            exp = self.infer_type(sym, BoolType())
        if not isinstance(exp, BoolType):
            raise TypeMismatchInStatement(ast)

    def visitReturn(self, ast, c):
        c = c[:3] + [ast]
        exp = ast.expr.accept(self, c) if ast.expr else VoidType()
        sym = self.search(c[2], [c[0], c[1]])
        # If both of the expression and the return type is unknown raise
        if isinstance(exp, ArrayType) and isinstance(exp.eletype, Unknown):
            exp = Unknown()
            if isinstance(sym.mtype.restype, Unknown):
                raise TypeCannotBeInferred(ast)
        if isinstance(exp, FunctionType) and isinstance(exp.restype, Unknown):
            exp = Unknown()
        if isinstance(exp, Unknown) and isinstance(sym.mtype.restype, Unknown):
            raise TypeCannotBeInferred(ast)
        # Infer the return type for the function if still unknown
        if isinstance(sym.mtype.restype, Unknown):
            self.infer_type(sym, exp)
        # Infer type for the expression if we already know function return type
        if isinstance(exp, Unknown):
            name = self.get_name(ast.expr)
            sym = self.search(name, [c[0], c[1]])
            exp = self.infer_type(sym, sym.mtype.restype)
        if type(sym.mtype.restype) != type(exp):
            raise TypeMismatchInStatement(ast)

    def check_if_unknown(self, ast, c):
        name = self.get_name(ast)
        sym = self.search(name, [c[0], c[1]])
        if isinstance(sym.mtype, FunctionType):
            return isinstance(sym.mtype.restype, Unknown)
        if isinstance(sym.mtype, ArrayType):
            return isinstance(sym.mtype.eletype, Unknown)

    def visitBinaryOp(self, ast, c):
        # Get type of operator
        op_type = self.get_operator_type(ast.op)

        # infer the type for lhs before visiting it if it is function or array
        if isinstance(ast.left, (CallExpr, ArrayCell)) and self.check_if_unknown(ast.left, c):
            name = self.get_name(ast.left)
            sym = self.search(name, [c[0], c[1]])
            self.infer_type(sym, op_type)
        # Check and infer type for the left
        lhs_type = ast.left.accept(self, c)
        lhs_type = self.get_type(lhs_type)
        lhs_name = self.get_name(ast.left)
        if isinstance(lhs_type, Unknown):
            sym = self.search(lhs_name, [c[0], c[1]])
            lhs_type = self.infer_type(sym, op_type)

        # infer the type for lhs before visiting it if it is function or array
        if isinstance(ast.right, (CallExpr, ArrayCell)) and self.check_if_unknown(ast.right, c):
            name = self.get_name(ast.right)
            sym = self.search(name, [c[0], c[1]])
            self.infer_type(sym, op_type)
        # Check and infer type for the right
        rhs_type = ast.right.accept(self, c)
        rhs_type = self.get_type(rhs_type)
        rhs_name = self.get_name(ast.right)
        if isinstance(rhs_type, Unknown):
            sym = self.search(rhs_name, [c[0], c[1]])
            rhs_type = self.infer_type(sym, op_type)

        # Check type according to operator
        if ast.op in ['+', '-', '*', '\\', '%']:
            if isinstance(lhs_type, IntType) and isinstance(rhs_type, IntType):
                return IntType()
            else:
                raise TypeMismatchInExpression(ast)
        elif ast.op in ['==', '!=', '<', '>', '<=', '>=']:
            if isinstance(lhs_type, IntType) and isinstance(rhs_type, IntType):
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)
        elif ast.op in ['+.', '-.', '*.', '\\.']:
            if isinstance(lhs_type, FloatType) and isinstance(rhs_type, FloatType):
                return FloatType()
            else:
                raise TypeMismatchInExpression(ast)
        elif ast.op in ['=/=', '<.', '>.', '<=.', '>=.']:
            if isinstance(lhs_type, FloatType) and isinstance(rhs_type, FloatType):
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)
        elif ast.op in ['!', '&&', '||']:
            if isinstance(lhs_type, BoolType) and isinstance(rhs_type, BoolType):
                return BoolType()
            raise TypeMismatchInExpression(ast)

    def visitUnaryOp(self, ast, c):
        op_type = self.get_operator_type(ast.op)

        # infer the type for lhs before visiting it if it is function or array
        if isinstance(ast.body, (CallExpr, ArrayCell)) and self.check_if_unknown(ast.body, c):
            name = self.get_name(ast.body)
            sym = self.search(name, [c[0], c[1]])
            self.infer_type(sym, op_type)
        typ = ast.body.accept(self, c)
        typ = self.get_type(typ)

        if isinstance(typ, Unknown):
            name = self.get_name(ast.body)
            sym = self.search(name, [c[0], c[1]])
            typ = self.infer_type(sym, op_type)

        if ast.op == '-' and not isinstance(typ, IntType):
            raise TypeMismatchInExpression(ast)
        elif ast.op == '-.' and not isinstance(typ, FloatType):
            raise TypeMismatchInExpression(ast)
        elif ast.op == '!' and not isinstance(typ, BoolType):
            raise TypeMismatchInExpression(ast)
        return typ

    def visitId(self, ast, c):
        tem_id = self.search(ast.name, [c[0], c[1]])
        if tem_id is None or isinstance(tem_id.mtype, FunctionType):
            raise Undeclared(Identifier(), ast.name)
        return tem_id.mtype

    def visitArrayLiteral(self, ast, c):
        ele_typ = ast.value[0].accept(self, c)
        dim = [len(ast.value)] + (ele_typ.dimen if isinstance(ele_typ, ArrayType) else [])
        if isinstance(ele_typ, ArrayType):
            ele_typ = ele_typ.eletype
        return ArrayType(dim, ele_typ)

    def visitArrayCell(self, ast, c):
        name = self.get_name(ast.arr)
        ast.arr.accept(self, c)
        func_sym = self.search(name, [c[0], c[1]])
        if func_sym is None:
            raise Undeclared(Identifier(), name)
        for x in ast.idx:
            tem = x.accept(self, c)
            if isinstance(tem, Unknown):
                name = self.get_name(x)
                sym = self.search(name, [c[0], c[1]])
                tem = self.infer_type(sym, IntType())
            if not isinstance(tem, IntType):
                raise TypeMismatchInExpression(ast)
        if isinstance(func_sym.mtype, Unknown):
            raise TypeMismatchInExpression(ast)
        if isinstance(func_sym.mtype, FunctionType):
            if isinstance(func_sym.mtype.restype, Unknown):
                raise TypeCannotBeInferred(c[3])
        lst = func_sym.mtype.dimen if isinstance(func_sym.mtype, ArrayType) else func_sym.mtype.restype.dimen
        typ = func_sym.mtype if isinstance(func_sym.mtype, ArrayType) else func_sym.mtype.restype
        if len(lst) != len(ast.idx) or not isinstance(typ, ArrayType):
            raise TypeMismatchInExpression(ast)
        return typ.eletype

    def visitBreak(self, ast, c):
        pass

    def visitContinue(self, ast, c):
        pass

    def visitIntLiteral(self, ast, c):
        return IntType()

    def visitFloatLiteral(self, ast, c):
        return FloatType()

    def visitBooleanLiteral(self, ast, c):
        return BoolType()

    def visitStringLiteral(self, ast, c):
        return StringType()
