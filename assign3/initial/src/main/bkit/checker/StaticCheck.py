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
    def __init__(self, param: List[Symbol], rtype=None):
        self.param = param
        self.rtype = rtype

    def set_type(self, typ):
        self.rtype = typ


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
            if isinstance(symbol.mtype.rtype, ArrayType):
                symbol.mtype.rtype.set_type(infer_type)
                return symbol.mtype.rtype.eletype
            else:
                symbol.mtype.set_type(infer_type)
                return symbol.mtype.rtype
        elif isinstance(symbol.mtype, Unknown):
            symbol.set_type(infer_type)
        return symbol.mtype

    # Check if a variable is redeclared and return that symbol
    def checkRedeclare(self, sym, typ, envi):
        # The typ is the type of the symbol (Variable, Function, Parameter, Identifier)
        if self.search(sym.name, envi):
            raise Redeclared(typ, sym.name)
        return sym

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
            if ast.varInit:
                tem = Symbol(ast.variable.name, ast.varInit.accept(self, c))
            else:
                tem = Symbol(ast.variable.name, ArrayType(ast.varDimen, Unknown()))
        else:
            tem = Symbol(ast.variable.name, ast.varInit.accept(self, c)) if ast.varInit else Symbol(ast.variable.name,
                                                                                                    Unknown())
        return self.checkRedeclare(tem, Variable(), [c])

    def visitFuncDecl(self, ast, c):
        local = []
        # Search for the function symbol
        func_sym = self.search(ast.name.name, [c])

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
            j.accept(self, (func_sym.mtype.param + local, c, func_sym.name))

        func_sym2 = self.search(ast.name.name, [c])
        # If still can't infer type of function after visiting all stmt, infer type VoidType
        if isinstance(func_sym2.mtype.rtype, Unknown):
            self.infer_type(func_sym2, VoidType())

    def visitAssign(self, ast, c):
        lhs = ast.lhs.accept(self, c)
        rhs = ast.rhs.accept(self, c)
        # If both side of the assignment is unknown
        if isinstance(lhs, Unknown) and isinstance(rhs, Unknown):
            raise TypeCannotBeInferred(ast)
        lhs_name = self.get_name(ast.lhs)
        rhs_name = self.get_name(ast.rhs)
        if isinstance(lhs, ArrayType):
            lhs = lhs.eletype
        if isinstance(rhs, ArrayType):
            rhs = rhs.eletype

        # Lhs can not be void type
        if isinstance(lhs, Unknown) and not isinstance(rhs, VoidType):
            sym = self.search(lhs_name, [c[0], c[1]])
            lhs = self.infer_type(sym, rhs)
        if isinstance(rhs, Unknown):
            sym = self.search(rhs_name, [c[0], c[1]])
            rhs = self.infer_type(sym, lhs)
        if type(rhs) != type(lhs):
            raise TypeMismatchInStatement(ast)

    def visitCallStmt(self, ast, c):
        # variable to check if the call stmt is in the 12 predefined method
        predefine = False
        # only search in c[1] as function reside in global
        tem_call_stmt = self.search(ast.method.name, [c[1]])
        # raise undeclare if call sym is not of type function of mtype
        if tem_call_stmt is None or not isinstance(tem_call_stmt.mtype, (FunctionType, MType)):
            raise Undeclared(Function(), ast.method.name)
        if tem_call_stmt in self.global_envi[:12]:
            para_list = tem_call_stmt.mtype.intype
            predefine = True
        else:
            para_list = tem_call_stmt.mtype.param
        # The length of parameter list of function and the call stmt must be the same
        if len(para_list) != len(ast.param):
            raise TypeMismatchInStatement(ast)
        # check every element of para list and argument list
        for para_sym, arg_exp in zip(para_list, ast.param):
            ptype = para_sym.mtype if not predefine else para_sym
            arg_typ = arg_exp.accept(self, c)
            if isinstance(ptype, Unknown) and isinstance(arg_typ, Unknown):
                raise TypeCannotBeInferred(ast)
            if isinstance(ptype, Unknown):
                para_sym.set_type(arg_typ)
                ptype = para_sym.mtype
            if isinstance(arg_typ, Unknown):
                sym = self.search(arg_exp.name, [c[0], c[1]])
                arg_typ = self.infer_type(sym, ptype)
            if type(ptype) != type(arg_typ):
                raise TypeMismatchInStatement(ast)

    def visitIf(self, ast, c):
        for x in ast.ifthenStmt:
            exp = x[0].accept(self, c)
            if not isinstance(exp, BoolType):
                raise TypeMismatchInStatement(ast)
            local = []
            for y in x[1]:
                tem_var = y.accept(self, local)
                local.append(tem_var)
            for z in x[2]:
                z.accept(self, (local + c[0], c[1], c[2]))
        else_local = []
        for i in ast.elseStmt[0]:
            tem_else_var = i.accept(self, else_local)
            else_local.append(tem_else_var)
        for k in ast.elseStmt[1]:
            k.accept(self, (else_local + c[0], c[1], c[2]))

    def visitFor(self, ast, c):
        idx = ast.idx1.accept(self, c)

        if isinstance(idx, Unknown):
            name = self.get_name(ast.idx1)
            sym = self.search(name, [c[0], c[1]])
            idx = self.infer_type(sym, IntType())
        if not isinstance(idx, IntType):
            raise TypeMismatchInStatement(ast)
        exp1 = ast.expr1.accept(self, c)
        if not isinstance(exp1, IntType):
            raise TypeMismatchInStatement(ast)
        exp2 = ast.expr2.accept(self, c)
        if not isinstance(exp2, BoolType):
            raise TypeMismatchInStatement(ast)
        exp3 = ast.expr3.accept(self, c)
        if not isinstance(exp3, IntType):
            raise TypeMismatchInStatement(ast)

        local = []
        for i in ast.loop[0]:
            tem_var = i.accept(self, local)
            local.append(tem_var)
        for k in ast.loop[1]:
            k.accept(self, (local + c[0], c[1], c[2]))

    def visitWhile(self, ast, c):
        exp = ast.exp.accept(self, c)
        if not isinstance(exp, BoolType):
            raise TypeMismatchInStatement(ast)
        local = []
        for i in ast.sl[0]:
            tem_var = i.accept(self, local)
            local.append(tem_var)
        for k in ast.sl[1]:
            k.accept(self, (local + c[0], c[1], c[2]))

    def visitDowhile(self, ast, c):
        local = []
        for i in ast.sl[0]:
            tem_var = i.accept(self, local)
            local.append(tem_var)
        for k in ast.sl[1]:
            k.accept(self, (local + c[0], c[1], c[2]))
        exp = ast.exp.accept(self, c)
        if not isinstance(exp, BoolType):
            raise TypeMismatchInStatement(ast)

    def visitBreak(self, ast, c):
        pass

    def visitContinue(self, ast, c):
        pass

    def visitReturn(self, ast, c):
        exp = ast.expr.accept(self, c) if ast.expr else VoidType()
        sym = self.search(c[2], [c[0], c[1]])
        if isinstance(exp, Unknown) and isinstance(sym.mtype.rtype, Unknown):
            raise TypeCannotBeInferred(ast)
        if isinstance(sym.mtype.rtype, Unknown):
            self.infer_type(sym, exp)
        if isinstance(exp, Unknown):
            name = self.get_name(ast.expr)
            sym = self.search(name, [c[0], c[1]])
            exp = self.infer_type(sym, sym.mtype.rtype)
        if type(sym.mtype.rtype) != type(exp):
            raise TypeMismatchInStatement(ast)

    def get_operator_type(self, op):
        if op in ['+', '-', '*', '\\', '%', '==', '!=', '<', '>', '<=', '>=']:
            return IntType()
        elif op in ['+.', '-.', '*.', '\\.', '=/=', '<.', '>.', '<=.', '>=.']:
            return FloatType()
        elif op in ['!', '&&', '||']:
            return BoolType()

    def get_name(self, var):
        if isinstance(var, Id):
            return var.name
        elif isinstance(var, ArrayCell):
            return var.arr.name if isinstance(var.arr, Id) else var.arr.method.name
        elif isinstance(var, CallExpr):
            return var.method.name

    def visitBinaryOp(self, ast, c):
        # Check type
        op_type = self.get_operator_type(ast.op)

        lhs_type = ast.left.accept(self, c)
        lhs_name = self.get_name(ast.left)
        if isinstance(lhs_type, ArrayType):
            lhs_type = lhs_type.eletype
        if isinstance(lhs_type, FunctionType):
            lhs_type = lhs_type.rtype
            if isinstance(lhs_type, ArrayType):
                lhs_type = lhs_type.eletype
        if isinstance(lhs_type, Unknown):
            sym = self.search(lhs_name, [c[0], c[1]])
            lhs_type = self.infer_type(sym, op_type)

        # right
        rhs_type = ast.right.accept(self, c)
        rhs_name = self.get_name(ast.right)
        if isinstance(rhs_type, ArrayType):
            rhs_type = rhs_type.eletype
        if isinstance(rhs_type, FunctionType):
            rhs_type = rhs_type.rtype
            if isinstance(rhs_type, ArrayType):
                rhs_type = rhs_type.eletype
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
        typ = ast.body.accept(self, c)
        op_type = self.get_operator_type(ast.op)
        if typ == Unknown():
            name = self.get_name(ast.body)
            sym = self.search(name, [c[0], c[1]])
            typ = self.infer_type(sym, op_type)

        if ast.op == '-' and not isinstance(typ, IntType):
            raise TypeMismatchInExpression(ast)
        elif ast.op == '-.' and not isinstance(typ, FloatType):
            raise TypeMismatchInExpression(ast)
        elif ast.op == '!' and not isinstance(typ, BoolType):
            raise TypeMismatchInExpression(ast)

    def visitCallExpr(self, ast, c):
        predefine = False
        tem_call_stmt = self.search(ast.method.name, [c[1]])
        if tem_call_stmt is None or not isinstance(tem_call_stmt.mtype, (FunctionType, MType)):
            raise Undeclared(Function(), ast.method.name)
        if tem_call_stmt in self.global_envi[:12]:
            para_list = tem_call_stmt.mtype.intype
            predefine = True
        else:
            para_list = tem_call_stmt.mtype.param
        if len(para_list) != len(ast.param):
            raise TypeMismatchInExpression(ast)
        for para_sym, arg_exp in zip(para_list, ast.param):
            ptype = para_sym.mtype if not predefine else para_sym
            arg_typ = arg_exp.accept(self, c)
            if isinstance(ptype, Unknown) and isinstance(arg_typ, Unknown):
                raise TypeCannotBeInferred(ast)
            if isinstance(ptype, Unknown):
                para_sym.set_type(arg_typ)
                ptype = para_sym.mtype
            if isinstance(arg_typ, Unknown):
                sym = self.search(arg_exp.name, [c[0], c[1]])
                arg_typ = self.infer_type(sym, ptype)
            if type(ptype) != type(arg_typ):
                raise TypeMismatchInExpression(ast)
        check = self.search(ast.method.name, [c[1]])
        return check.mtype.rtype

    def visitId(self, ast, c):
        tem_id = self.search(ast.name, [c[0], c[1]])
        if tem_id is None or isinstance(tem_id.mtype, FunctionType):
            raise Undeclared(Identifier(), ast.name)
        return tem_id.mtype

    def visitIntLiteral(self, ast, c):
        return IntType()

    def visitFloatLiteral(self, ast, c):
        return FloatType()

    def visitBooleanLiteral(self, ast, c):
        return BoolType()

    def visitStringLiteral(self, ast, c):
        return StringType()

    def visitArrayLiteral(self, ast, c):
        ele_typ = ast.value[0].accept(self, c)
        dim = [len(ast.value)] + (ele_typ.dimen if isinstance(ele_typ, ArrayType) else [])
        if isinstance(ele_typ, ArrayType):
            ele_typ = ele_typ.eletype
        return ArrayType(dim, ele_typ)

    def visitArrayCell(self, ast, c):
        name = self.get_name(ast.arr)
        ast.arr.accept(self, c)
        tem_arr = self.search(name, [c[0], c[1]])
        if tem_arr is None:
            raise Undeclared(Identifier(), name)
        for x in ast.idx:
            tem = x.accept(self, c)
            if isinstance(tem, Unknown):
                sym = self.search(x.name, [c[0], c[1]])
                tem = self.infer_type(sym, IntType())
            if not isinstance(tem, IntType):
                raise TypeMismatchInExpression(ast)
        lst = tem_arr.mtype.dimen if isinstance(tem_arr.mtype, ArrayType) else tem_arr.mtype.rtype.dimen
        typ = tem_arr.mtype if isinstance(tem_arr.mtype, ArrayType) else tem_arr.mtype.rtype
        if len(lst) != len(ast.idx) or not isinstance(typ, ArrayType):
            raise TypeMismatchInExpression(ast)
        return tem_arr.mtype
