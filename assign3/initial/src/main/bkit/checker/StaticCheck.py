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
            Symbol("float_of_int", MType([IntType()], FloatType())),
            Symbol("int_of_string", MType([StringType()], IntType())),
            Symbol("string_of_int", MType([IntType()], StringType())),
            Symbol("float_of_string", MType([StringType()], FloatType())),
            Symbol("string_of_float", MType([FloatType()], StringType())),
            Symbol("bool_of_string", MType([StringType()], BoolType())),
            Symbol("string_of_bool", MType([BoolType()], StringType())),
            Symbol("read", MType([], StringType())),
            Symbol("printLn", MType([], VoidType())),
            Symbol("printStr", MType([StringType()], VoidType())),
            Symbol("printStrLn", MType([StringType()], VoidType()))]

    def check(self):
        return self.visit(self.ast, self.global_envi)

    def search(self, name, lst):
        for x in lst:
            for y in x:
                if name == y.name:
                    return y
        return None

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

    def checkRedeclare(self, sym, typ, envi):
        if self.search(sym.name, envi):
            raise Redeclared(typ, sym.name)
        return sym

    def visitProgram(self, ast, c):
        name = []
        for i in ast.decl:
            if isinstance(i, VarDecl):
                c.append(i.accept(self, c))
            else:
                func_name = i.name.name
                name.append(func_name)
                self.checkRedeclare(Symbol(func_name, Unknown()), Function(), [c])
                para = []
                for j in i.param:
                    para_sym = Symbol(j.variable.name, Unknown())
                    para_tem = self.checkRedeclare(para_sym, Parameter(), [para])
                    para.append(para_tem)
                c.append(Symbol(func_name, FunctionType(para, Unknown())))
        if 'main' not in name:
            raise NoEntryPoint()
        for x in ast.decl:
            if isinstance(x, FuncDecl):
                x.accept(self, c)

    def visitVarDecl(self, ast, c):
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
        ret_type = None
        # for x in ast.param:
        #     para_sym = Symbol(x.variable.name, Unknown())
        #     para_tem = self.checkRedeclare(para_sym, Parameter(), [local])
        #     local.append(para_tem)
        #     para_len += 1
        func_sym = self.search(ast.name.name, [c])
        for i in ast.body[0]:
            tem_var = i.accept(self, func_sym.mtype.param + local)
            local.append(tem_var)
        for j in ast.body[1]:
            j.accept(self, (func_sym.mtype.param + local, c, func_sym.mtype.rtype, func_sym.name))
        # func = Symbol(ast.name.name, FunctionType(local, ret_type))
        # return func

    def visitAssign(self, ast, c):
        lhs = ast.lhs.accept(self, c)
        rhs = ast.rhs.accept(self, c)
        if isinstance(lhs, Unknown) and isinstance(rhs, Unknown):
            raise TypeCannotBeInferred(ast)
        lhs_name = self.get_name(ast.lhs)
        rhs_name = self.get_name(ast.rhs)
        if isinstance(lhs, ArrayType):
            lhs = lhs.eletype
        if isinstance(rhs, ArrayType):
            rhs = rhs.eletype
        if isinstance(lhs, Unknown):
            sym = self.search(lhs_name, [c[0], c[1]])
            lhs = self.infer_type(sym, rhs)
        if isinstance(rhs, Unknown):
            sym = self.search(rhs_name, [c[0], c[1]])
            rhs = self.infer_type(sym, lhs)
        if type(rhs) != type(lhs):
            raise TypeMismatchInStatement(ast)

    def visitCallStmt(self, ast, c):
        para_list = []
        predefine = False
        tem_call_stmt = self.search(ast.method.name, [c[1]])
        if tem_call_stmt is None:
            raise Undeclared(Function(), ast.method.name)
        if tem_call_stmt in self.global_envi[:12]:
            para_list = tem_call_stmt.mtype.intype
            predefine = True
        else:
            para_list = tem_call_stmt.mtype.param
        if len(para_list) != len(ast.param):
            raise TypeMismatchInStatement(ast)
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
        exp1 = ast.expr1.accept(self, c)
        exp2 = ast.expr2.accept(self, c)
        exp3 = ast.expr3.accept(self, c)
        lst = [idx, exp1, exp3]
        if any(not isinstance(x, IntType) for x in lst):
            raise TypeMismatchInStatement(ast)
        if not isinstance(exp2, BoolType):
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
        if isinstance(exp, Unknown) and isinstance(c[2], Unknown):
            raise TypeCannotBeInferred(ast)
        sym = self.search(c[3], [c[0], c[1]])
        if isinstance(c[2], Unknown):
            self.infer_type(sym, exp)
        if isinstance(exp, Unknown):
            name = self.get_name(ast.expr)
            sym = self.search(name, [c[0], c[1]])
            exp = self.infer_type(sym, c[2])
        if sym.mtype.rtype != exp:
            raise TypeMismatchInStatement(ast)

    def get_operator_type(self, op):
        if op in ['+', '-', '*', '\\', '%', '==', '!=', '<', '>', '<=', '>=']:
            return IntType()
        elif op in ['+,', '-.', '*.', '\\.', '=/=', '<.', '>.', '<=.', '>=.']:
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
        lhs_type = ast.left.accept(self, c)
        rhs_type = ast.right.accept(self, c)
        op_type = self.get_operator_type(ast.op)

        # Check if array type
        if isinstance(lhs_type, ArrayType):
            lhs_type = lhs_type.eletype
        if isinstance(rhs_type, ArrayType):
            rhs_type = rhs_type.eletype

        if isinstance(lhs_type, FunctionType):
            lhs_type = lhs_type.rtype
            if isinstance(lhs_type, ArrayType):
                lhs_type = lhs_type.eletype
        if isinstance(rhs_type, FunctionType):
            rhs_type = rhs_type.rtype
            if isinstance(rhs_type, ArrayType):
                rhs_type = rhs_type.eletype

        # get name
        lhs_name = self.get_name(ast.left)
        rhs_name = self.get_name(ast.right)

        # Update type if unknown
        if isinstance(lhs_type, Unknown):
            sym = self.search(lhs_name, [c[0], c[1]])
            lhs_type = self.infer_type(sym, op_type)
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
        para_list = []
        predefine = False
        tem_call_stmt = self.search(ast.method.name, [c[1]])
        if tem_call_stmt is None:
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
        return tem_call_stmt.mtype.rtype

    def visitId(self, ast, c):
        tem_id = self.search(ast.name, [c[0], c[1]])
        if tem_id is None:
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
