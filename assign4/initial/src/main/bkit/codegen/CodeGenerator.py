"""
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
"""
from Visitor import BaseVisitor
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod
from typing import List, Tuple
from dataclasses import dataclass
from AST import *
from functools import reduce


class MethodEnv():
    def __init__(self, frame, sym):
        self.frame = frame
        self.sym = sym


class Access():
    def __init__(self, frame, sym, isLeft, isFirst, checkArrayType=False):
        # frame: Frame
        # sym: List[Symbol]
        # isLeft: Boolean
        # isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst
        self.checkArrayType = checkArrayType


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def set_type(self, typ):
        self.mtype = typ


class CName:
    def __init__(self, n):
        self.value = n


class Index:
    def __init__(self, n):
        self.value = n


class Type(ABC):
    pass


class IntType(Type):
    pass


class FloatType(Type):
    pass


class VoidType(Type):
    pass


class ClassType(Type):
    def __init__(self, n):
        self.cname = n


class StringType(Type):
    pass


class BoolType(Type):
    pass


class Unknown(Type):
    pass


@dataclass
class MType(Type):
    intype: List[Type]
    restype: Type


@dataclass
class ArrayType(Type):
    dimen: List[int]
    eletype: Type

    def set_type(self, typ):
        self.eletype = typ


# Function type to represent function
class FunctionType(Type):
    def __init__(self, param: List[Symbol], restype=None):
        self.param = param
        self.restype = restype

    def set_type(self, typ):
        self.restype = typ


class CodeGenerator():
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("read", MType([], StringType()), CName(self.libName)),
                Symbol("printLn", MType([], VoidType()), CName(self.libName)),
                Symbol("printStrLn", MType([StringType()], VoidType()), CName(self.libName)),
                Symbol("print", MType([StringType()], VoidType()), CName(self.libName)),
                Symbol("string_of_int", MType([IntType()], StringType()), CName(self.libName)),
                Symbol("float_of_string", MType([StringType()], FloatType()), CName(self.libName)),
                Symbol("string_of_float", MType([FloatType()], StringType()), CName(self.libName)),
                Symbol("bool_of_string", MType([StringType()], BoolType()), CName(self.libName)),
                Symbol("string_of_bool", MType([BoolType()], StringType()), CName(self.libName)),
                Symbol("int_of_float", MType([FloatType()], IntType()), CName(self.libName)),
                Symbol("float_to_int", MType([IntType()], FloatType()), CName(self.libName)),
                Symbol("int_of_string", MType([StringType()], IntType()), CName(self.libName)),
                ]

    def gen(self, ast, dir_):
        # ast: AST
        # dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)


class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, env, dir_):
        # astTree: AST
        # env: List[Symbol]
        # dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "BKITClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")
        self.libName = "io"

        self.global_envi = env
        self.global_lst = []
        self.local_lst = []
        self.global_arr = []

    def visitProgram(self, ast, c):
        # ast: Program
        # c: Any

        c = self.env
        name = []
        for i in ast.decl:
            if isinstance(i, VarDecl):
                tem = (i.accept(self, [c, False]))
                new_sym = Symbol(tem.name, tem.mtype, CName(self.className))
                c.append(new_sym)
            else:
                func_name = i.name.name
                name.append(func_name)
                para = []
                for j in i.param:
                    para_sym = Symbol(j.variable.name, ArrayType(j.varDimen, Unknown())) if len(j.varDimen) > 0 \
                        else Symbol(j.variable.name, Unknown())
                    para.append(para_sym)
                c.append(Symbol(func_name, FunctionType(para, Unknown()), CName(self.className)))
        for x in ast.decl:
            if isinstance(x, FuncDecl):
                x.accept(self, [c, False])

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        e = MethodEnv(None, c)
        for x in ast.decl:
            if isinstance(x, VarDecl):
                tem = x.accept(self, [e, True])
                self.global_lst.append(tem)
        for x in ast.decl:
            if isinstance(x, FuncDecl):
                x.accept(self, [e, True])
        # generate default constructor
        self.genInit()
        # generate class init if necessary
        self.emit.emitEPILOG()
        return c

    def genGlobal(self, sym):
        for x in self.global_lst:
            ast_tem = x[0]
            global_frame = x[1]
            self.visitAssign(ast_tem, [MethodEnv(global_frame, sym), True])

    def genInit(self):
        methodname, methodtype = "<init>", MType([], VoidType())
        frame = Frame(methodname, methodtype.restype)
        self.emit.printout(self.emit.emitMETHOD(methodname, methodtype, False, frame))
        frame.enterScope(True)
        varname, vartype, varindex = "this", ClassType(self.className), frame.getNewIndex()
        startLabel, endLabel = frame.getStartLabel(), frame.getEndLabel()
        self.emit.printout(self.emit.emitVAR(varindex, varname, vartype, startLabel, endLabel, frame))
        self.emit.printout(self.emit.emitLABEL(startLabel, frame))
        self.emit.printout(self.emit.emitREADVAR(varname, vartype, varindex, frame))
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        self.emit.printout(self.emit.emitLABEL(endLabel, frame))
        self.emit.printout(self.emit.emitRETURN(methodtype.restype, frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))

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
        elif isinstance(var, (CallExpr, CallStmt)):
            return var.method.name
        elif isinstance(var, FuncDecl):
            return var.name.name
        elif isinstance(var, VarDecl):
            return var.variable.name

    def visitVarDecl(self, ast, c):
        # c: MethodEnv
        ass4 = c[1]
        if not ass4:
            c = c[0]
            if len(ast.varDimen) > 0:
                # Composite variable
                if ast.varInit:
                    tem = Symbol(ast.variable.name, ast.varInit.accept(self, [c, False]))
                else:
                    tem = Symbol(ast.variable.name, ArrayType(ast.varDimen, Unknown()))
            else:
                # Scalar variable
                tem = Symbol(ast.variable.name, ast.varInit.accept(self, [c, False])) if ast.varInit else Symbol(
                    ast.variable.name,
                    Unknown())
            return tem
        else:
            is_para = len(c) == 3
            env = c[0]
            frame = env.frame
            sym_lst = env.sym
            name = self.get_name(ast)
            if is_para:
                para_lst = c[2].mtype.param
                sym = self.search(name, [para_lst])
                typ = sym.mtype
                idx = frame.getNewIndex()
                self.emit.printout(self.emit.emitVAR(idx, name, typ, frame.getStartLabel(), frame.getEndLabel(), frame))

                return MethodEnv(frame, [Symbol(name, typ, Index(idx))] + sym_lst)
            else:
                if frame:  # local
                    idx = frame.getNewIndex()
                    typ = ast.varInit.accept(self, [c, False])
                    self.emit.printout(
                        self.emit.emitVAR(idx, name, typ, frame.getStartLabel(), frame.getEndLabel(), frame))
                    ast_tem = Assign(ast.variable, ast.varInit)
                    self.local_lst.append(ast_tem)
                    name = self.get_name(ast.variable)
                    new_lst = [Symbol(name, typ, Index(idx))] + sym_lst
                    return MethodEnv(frame, new_lst)
                else:  # global
                    sym = self.search(name, [sym_lst])
                    typ = sym.mtype
                    self.emit.printout(self.emit.emitATTRIBUTE(name, typ, False, ""))
                    ast_tem = Assign(ast.variable, ast.varInit)
                    name = self.get_name(ast.variable)
                    global_sym = self.search(name, [sym_lst])
                    global_frame = Frame(name, global_sym.mtype)
                    return [ast_tem, global_frame]

    def visitFuncDecl(self, ast, c):
        ass4 = c[1]
        if not ass4:
            c = c[0]
            local = []
            func_sym = self.search(ast.name.name, [c])  # Search for the function symbol
            for i in ast.body[0]:
                tem_var = i.accept(self, [func_sym.mtype.param + local, False])
                local.append(tem_var)
            for j in ast.body[1]:
                j.accept(self, [[func_sym.mtype.param + local, c, func_sym.name], False])
            func_sym = self.search(ast.name.name, [c])
            if isinstance(func_sym.mtype.restype, Unknown):
                self.infer_type(func_sym, VoidType())
        else:
            c = c[0]
            sym_lst = c.sym
            name = self.get_name(ast)
            sym = self.search(name, [sym_lst])
            typ = sym.mtype
            frame = Frame(name, typ)
            self.local_lst.clear()
            isMain = name == 'main' and len(ast.param) == 0 and isinstance(typ.restype, VoidType)
            if sym in self.global_envi[:12]:
                para_list = sym.mtype.intype
            else:
                para_list = list(map(lambda y: y.mtype, sym.mtype.param))
                typ = typ.restype

            if isMain:
                para_list = [ArrayType([], StringType())]
                typ = VoidType()
            self.emit.printout(self.emit.emitMETHOD(name, MType(para_list, typ), True, frame))

            frame.enterScope(True)
            if isMain:
                self.genGlobal(sym_lst)
                self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType([],
                                                                                            StringType()),
                                                     frame.getStartLabel(), frame.getEndLabel(), frame))
            e = MethodEnv(frame, sym_lst)

            for x in ast.param:
                e = x.accept(self, [e, True, sym])

            for x in ast.body[0]:
                e = x.accept(self, [e, True])  # local

            self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
            if len(self.local_lst) > 0:
                new_lst = e.sym
                for z in self.local_lst:
                    self.visitAssign(z, [MethodEnv(frame, new_lst), True])

            for x in ast.body[1]:  # statement
                x.accept(self, [e, True, sym])

            self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
            func_rtyp = self.get_type(typ)
            if isinstance(func_rtyp, (Unknown, VoidType)):
                self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
            self.emit.printout(self.emit.emitENDMETHOD(frame))
            frame.exitScope()

    def visitAssign(self, ast, c):
        ass4 = c[1]
        if not ass4:
            c = c[0]
            lhs = ast.lhs.accept(self, [c, False])
            rhs = ast.rhs.accept(self, [c, False])
            lhs_name = self.get_name(ast.lhs)
            rhs_name = self.get_name(ast.rhs)
            lhs = self.get_type(lhs)
            rhs = self.get_type(rhs)
            if isinstance(lhs, Unknown) and not isinstance(rhs, VoidType):
                sym = self.search(lhs_name, [c[0], c[1]])
                lhs = self.infer_type(sym, rhs)
            if isinstance(rhs, Unknown):
                sym = self.search(rhs_name, [c[0], c[1]])
                rhs = self.infer_type(sym, lhs)
        else:
            c = c[0]
            frame = c.frame
            env = c.sym
            rhs_code, rhs_type = self.visit(ast.rhs, [Access(frame, env, False, True), True])
            lhs_code, lhs_type = self.visit(ast.lhs, [Access(frame, env, True, True), True])
            result = rhs_code + lhs_code
            self.emit.printout(result)
            return False

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
        ass4 = c[1]
        if not ass4:
            c = c[0]
            predefine = False  # variable to check if the call stmt is in the 12 predefined method
            func_sym = self.search(ast.method.name, [c[0], c[1]])
            if func_sym in self.global_envi[:12]:
                para_list = func_sym.mtype.intype
                predefine = True
                ret_typ = func_sym.mtype.restype
            else:
                para_list = func_sym.mtype.param
                ret_typ = func_sym.mtype.restype
            if isinstance(ret_typ, Unknown):
                ret_typ = self.infer_type(func_sym, VoidType())
            for para_sym, arg_exp in zip(para_list, ast.param):
                ptype = para_sym.mtype if not predefine else para_sym
                arg_typ = arg_exp.accept(self, [c, False])

                ptype = self.get_type(ptype)
                arg_typ = self.get_type(arg_typ)
                if isinstance(ptype, Unknown):
                    ptype = self.infer_type(para_sym, arg_typ)
                if isinstance(arg_typ, Unknown):
                    name = self.get_name(arg_exp)
                    sym = self.search(name, [c[0], c[1]])
                    arg_typ = self.infer_type(sym, ptype)
        else:
            c = c[0]
            frame = c.frame
            sym_lst = c.sym
            name = self.get_name(ast)
            sym = self.search(name, [sym_lst])
            typ = sym.mtype
            if isinstance(typ, FunctionType):
                para = list(map(lambda i: i.mtype, typ.param))
                rtyp = typ.restype
                typ = MType(para, rtyp)
            cname = sym.value.value
            param_code = ''
            for x in ast.param:
                access = Access(frame, sym_lst, False, True)
                pCode, pTyp = x.accept(self, [access, True])
                param_code += pCode
            rcode = param_code + self.emit.emitINVOKESTATIC(cname + '/' + name, typ, frame)
            self.emit.printout(rcode)
            return False

    def visitCallExpr(self, ast, c):
        ass4 = c[1]
        if not ass4:
            c = c[0]
            predefine = False
            func_sym = self.search(ast.method.name, [c[0], c[1]])
            # Check if the call stmt is in the 12 predefined functions
            if func_sym in self.global_envi[:12]:
                para_list = func_sym.mtype.intype
                predefine = True
            else:
                para_list = func_sym.mtype.param

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
                arg_typ = arg_exp.accept(self, [c, False])
                if isinstance(arg_typ, FunctionType):
                    arg_typ = self.get_type(arg_typ)
                ptype = para_sym.mtype if not predefine else para_sym
                ptype = self.get_type(ptype)
                arg_typ = self.get_type(arg_typ)
                if isinstance(ptype, Unknown):
                    ptype = self.infer_type(para_sym, arg_typ)
                if isinstance(arg_typ, Unknown):
                    name = self.get_name(arg_exp)
                    sym = self.search(name, [c[0], c[1]])
                    arg_typ = self.infer_type(sym, ptype)
            check = self.search(ast.method.name, [c[1]])
            return check.mtype
        else:
            c = c[0]
            frame = c.frame
            sym_lst = c.sym
            name = self.get_name(ast)
            sym = self.search(name, [sym_lst])
            typ = sym.mtype
            if isinstance(typ, FunctionType):
                para = list(map(lambda i: i.mtype, typ.param))
                rtyp = typ.restype
                typ = MType(para, rtyp)
            cname = sym.value.value
            param_code = ''
            for x in ast.param:
                access = Access(frame, sym_lst, False, True)
                pCode, pTyp = x.accept(self, [access, True])
                param_code += pCode
            rcode = param_code + self.emit.emitINVOKESTATIC(cname + '/' + name, typ, frame)
            return rcode, typ.restype

    def visitIf(self, ast, c):
        ass4 = c[1]
        if not ass4:
            c = c[0]
            for x in ast.ifthenStmt:
                if isinstance(x[0], (CallExpr, ArrayCell)):
                    name = self.get_name(x[0])
                    sym = self.search(name, [c[0], c[1]])
                    # If Unknown, infer bool, else raise
                    tem_typ = self.get_type(sym.mtype)
                    if isinstance(tem_typ, Unknown):
                        self.infer_type(sym, BoolType())
                exp = x[0].accept(self, [c, False])
                exp = self.get_type(exp)
                if isinstance(exp, Unknown):
                    name = self.get_name(x[0])
                    sym = self.search(name, [c[0], c[1]])
                    exp = self.infer_type(sym, BoolType())
                local = []
                for y in x[1]:
                    tem_var = y.accept(self, [local, False])
                    local.append(tem_var)
                for z in x[2]:
                    z.accept(self, [[local + c[0], c[1], c[2]], False])
            else_local = []
            for i in ast.elseStmt[0]:
                tem_else_var = i.accept(self, [else_local, False])
                else_local.append(tem_else_var)
            for k in ast.elseStmt[1]:
                k.accept(self, [[else_local + c[0], c[1], c[2]], False])
        else:
            func_sym = c[2]
            c = c[0]
            frame = c.frame
            sym_lst = c.sym
            ifstmt_lst = ast.ifthenStmt
            is_else = ast.elseStmt == ([], [])
            tem_labelE = Frame('', Unknown())
            tem_labelNext = Frame('', Unknown())
            idx = 0
            end_label = frame.getNewLabel()
            for x in ifstmt_lst:
                exp = x[0]
                var_lst = x[1]
                stmt_lst = x[2]
                e_code, e_typ = exp.accept(self, [Access(frame, sym_lst, False, True), True])
                self.emit.printout(e_code)

                labelE = frame.getNewLabel()
                labelNext = frame.getNewLabel()

                tem_labelE = labelE
                tem_labelNext = labelNext

                if not is_else and idx == len(ifstmt_lst) - 1:
                    lab = labelE
                else:
                    lab = labelNext

                self.emit.printout(self.emit.emitIFFALSE(lab, frame))
                # e = MethodEnv(frame, sym_lst)
                # for i in var_lst:
                #     e = i.accept(self, [e, True])  # local
                #
                # for j in stmt_lst:  # statement
                #     j.accept(self, [e, True, func_sym])

                self.visitVarStmtList([var_lst, stmt_lst], [frame, sym_lst, func_sym])

                self.emit.printout(self.emit.emitGOTO(end_label, frame))
                self.emit.printout(self.emit.emitLABEL(labelNext, frame))
                idx += 1

            if not is_else:
                self.emit.printout(self.emit.emitGOTO(tem_labelNext, frame))
                self.emit.printout(self.emit.emitLABEL(tem_labelE, frame))
                var_lst = ast.elseStmt[0]
                stmt_lst = ast.elseStmt[1]
                e = MethodEnv(frame, sym_lst)
                for i in var_lst:
                    e = i.accept(self, [e, True])  # local

                for j in stmt_lst:  # statement
                    j.accept(self, [e, True, func_sym])
            self.emit.printout(self.emit.emitLABEL(end_label, frame))
            self.emit.printout(self.emit.emitLABEL(tem_labelNext, frame))
            return False

    def visitFor(self, ast, c):
        ass4 = c[1]
        if not ass4:
            c = c[0]
            idx = ast.idx1.accept(self, [c, False])
            idx = self.get_type(idx)
            if isinstance(idx, Unknown):
                name = self.get_name(ast.idx1)
                sym = self.search(name, [c[0], c[1]])
                idx = self.infer_type(sym, IntType())
            if isinstance(ast.expr1, (CallExpr, ArrayCell)):
                name = self.get_name(ast.expr1)
                sym = self.search(name, [c[0], c[1]])
                # If Unknown, infer int, else raise
                tem_typ = self.get_type(sym.mtype)
                if isinstance(tem_typ, Unknown):
                    self.infer_type(sym, IntType())

            exp1 = ast.expr1.accept(self, [c, False])
            exp1 = self.get_type(exp1)
            if isinstance(exp1, Unknown):
                name = self.get_name(ast.expr1)
                sym = self.search(name, [c[0], c[1]])
                exp1 = self.infer_type(sym, IntType())
            if isinstance(ast.expr2, (CallExpr, ArrayCell)):
                name = self.get_name(ast.expr2)
                sym = self.search(name, [c[0], c[1]])
                # If Unknown, infer bool, else raise
                tem_typ = self.get_type(sym.mtype)
                if isinstance(tem_typ, Unknown):
                    self.infer_type(sym, BoolType())
            exp2 = ast.expr2.accept(self, [c, False])
            exp2 = self.get_type(exp2)
            # Check if expression 2 is of bool type
            if isinstance(exp2, Unknown):
                name = self.get_name(ast.expr2)
                sym = self.search(name, [c[0], c[1]])
                exp2 = self.infer_type(sym, BoolType())
            if isinstance(ast.expr3, (CallExpr, ArrayCell)):
                name = self.get_name(ast.expr3)
                sym = self.search(name, [c[0], c[1]])
                # If Unknown, infer bool, else raise
                tem_typ = self.get_type(sym.mtype)
                if isinstance(tem_typ, Unknown):
                    self.infer_type(sym, IntType())

            exp3 = ast.expr3.accept(self, [c, False])
            exp3 = self.get_type(exp3)
            if isinstance(exp3, Unknown):
                name = self.get_name(ast.expr3)
                sym = self.search(name, [c[0], c[1]])
                exp3 = self.infer_type(sym, IntType())
            local = []
            for i in ast.loop[0]:
                tem_var = i.accept(self, [local, False])
                local.append(tem_var)
            for k in ast.loop[1]:
                k.accept(self, [[local + c[0], c[1], c[2]], False])
        else:
            # c[0]: MethodEnv
            func_sym = c[2]
            c = c[0]
            frame = c.frame
            sym_lst = c.sym
            e1_code, e1_typ = ast.expr1.accept(self, [Access(frame, sym_lst, False, True), True])
            id_code, id_typ = ast.idx1.accept(self, [Access(frame, sym_lst, True, True), True])
            self.emit.printout(e1_code + id_code)

            frame.enterLoop()
            strLabel = frame.getNewLabel()
            conLabel = frame.getContinueLabel()
            brkLabel = frame.getBreakLabel()

            e2_code, e2_typ = ast.expr2.accept(self, [Access(frame, sym_lst, False, True), True])
            self.emit.printout(self.emit.emitLABEL(strLabel, frame))
            self.emit.printout(e2_code + self.emit.emitIFFALSE(brkLabel, frame))

            self.visitVarStmtList(ast.loop, [frame, sym_lst, func_sym])

            self.emit.printout(self.emit.emitLABEL(conLabel, frame))

            e3_code, e3_typ = ast.expr3.accept(self, [Access(frame, sym_lst, False, True), True])

            id2_code, id2_typ = ast.idx1.accept(self, [Access(frame, sym_lst, False, True), True])

            self.emit.printout(e3_code + id2_code + self.emit.emitADDOP('+', id2_typ, frame))
            i, it = ast.idx1.accept(self, [Access(frame, sym_lst, True, True), True])
            self.emit.printout(i)
            self.emit.printout(self.emit.emitGOTO(strLabel, frame))
            self.emit.printout(self.emit.emitLABEL(brkLabel, c.frame))
            c.frame.exitLoop()
            return False

    def visitVarStmtList(self, ast, c):
        frame = c[0]
        sym_lst = c[1]
        func_sym = c[2]
        frame.enterScope(False)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        e = MethodEnv(frame, sym_lst)
        for x in ast[0]:
            e = x.accept(self, [e, True])

        local = []
        if len(ast[0]) > 0:
            local = e.sym[:len(ast[0])]
            for z in ast[0]:
                ast_tem = Assign(z.variable, z.varInit)
                self.visitAssign(ast_tem, [MethodEnv(frame, local), True])

        for y in ast[1]:
            y.accept(self, [MethodEnv(frame, local + sym_lst), True, func_sym])
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        frame.exitScope()

    def visitWhile(self, ast, c):
        ass4 = c[1]
        if not ass4:
            c = c[0]
            if isinstance(ast.exp, (CallExpr, ArrayCell)):
                name = self.get_name(ast.exp)
                sym = self.search(name, [c[0], c[1]])
                # If Unknown, infer bool, else raise
                tem_typ = self.get_type(sym.mtype)
                if isinstance(tem_typ, Unknown):
                    self.infer_type(sym, BoolType())

            exp = ast.exp.accept(self, [c, False])
            exp = self.get_type(exp)
            # Check if the expression is of bool type, if not update otherwise raise
            if isinstance(exp, Unknown):
                name = self.get_name(ast.exp)
                sym = self.search(name, [c[0], c[1]])
                exp = self.infer_type(sym, BoolType())
            local = []
            for i in ast.sl[0]:
                tem_var = i.accept(self, [local, False])
                local.append(tem_var)
            for k in ast.sl[1]:
                k.accept(self, [[local + c[0], c[1], c[2]], False])
        else:
            # c[0]: MethodEnv
            func_sym = c[2]
            c = c[0]
            frame = c.frame
            sym_lst = c.sym
            frame.enterLoop()
            conLabel = frame.getContinueLabel()
            brkLabel = frame.getBreakLabel()
            e_code, e_typ = ast.exp.accept(self, [Access(frame, sym_lst, False, True), True])
            self.emit.printout(self.emit.emitLABEL(conLabel, frame))
            self.emit.printout(e_code + self.emit.emitIFFALSE(brkLabel, frame))
            self.visitVarStmtList(ast.sl, [frame, sym_lst, func_sym])
            self.emit.printout(self.emit.emitGOTO(conLabel, frame))
            self.emit.printout(self.emit.emitLABEL(brkLabel, frame))
            frame.exitLoop()
            return False

    def visitDowhile(self, ast, c):
        ass4 = c[1]
        if not ass4:
            c = c[0]
            local = []
            for i in ast.sl[0]:
                tem_var = i.accept(self, [local, False])
                local.append(tem_var)
            for k in ast.sl[1]:
                k.accept(self, [[local + c[0], c[1], c[2]], False])
            if isinstance(ast.exp, (CallExpr, ArrayCell)):
                name = self.get_name(ast.exp)
                sym = self.search(name, [c[0], c[1]])
                tem_typ = self.get_type(sym.mtype)
                if isinstance(tem_typ, Unknown):
                    self.infer_type(sym, BoolType())
            exp = ast.exp.accept(self, [c, False])
            exp = self.get_type(exp)
            if isinstance(exp, Unknown):
                name = self.get_name(ast.exp)
                sym = self.search(name, [c[0], c[1]])
                exp = self.infer_type(sym, BoolType())
        else:
            # c[0]: MethodEnv
            func_sym = c[2]
            c = c[0]
            frame = c.frame
            sym_lst = c.sym
            frame.enterLoop()
            conLabel = frame.getContinueLabel()
            brkLabel = frame.getBreakLabel()
            e_code, e_typ = ast.exp.accept(self, [Access(frame, sym_lst, False, True), True])
            self.emit.printout(self.emit.emitLABEL(conLabel, frame))
            self.visitVarStmtList(ast.sl, [frame, sym_lst, func_sym])
            self.emit.printout(e_code + self.emit.emitIFFALSE(brkLabel, frame))
            self.emit.printout(self.emit.emitGOTO(conLabel, frame))
            self.emit.printout(self.emit.emitLABEL(brkLabel, frame))
            frame.exitLoop()
            return False

    def visitReturn(self, ast, c):
        ass4 = c[1]
        if not ass4:
            c = c[0]
            exp = ast.expr.accept(self, [c, False]) if ast.expr else VoidType()
            sym = self.search(c[2], [c[1]])
            if isinstance(exp, ArrayType) and isinstance(exp.eletype, Unknown):
                exp = Unknown()
            if isinstance(exp, FunctionType) and isinstance(exp.restype, Unknown):
                exp = Unknown()
            tem_exp = self.get_type(exp)
            tem_sym_typ = self.get_type(sym.mtype)

            if isinstance(exp, FunctionType):
                exp = self.get_type(exp)
            # Infer the return type for the function if still unknown
            if isinstance(sym.mtype.restype, Unknown):
                self.infer_type(sym, exp)
            # Infer type for the expression if we already know function return type
            if isinstance(exp, Unknown):
                name = self.get_name(ast.expr)
                sym = self.search(name, [c[0], c[1]])
                sym_typ = self.get_type(sym.mtype)
                exp = self.infer_type(sym, sym_typ)
            if isinstance(exp, FunctionType):
                exp = self.get_type(exp)
            sym_type = self.get_type(sym.mtype)
            if isinstance(exp, ArrayType) and isinstance(sym_type, ArrayType):
                exp = self.get_type(exp)
                sym_type = self.get_type(sym_type)
        else:
            # c[0]: Method
            func_sym = c[2]
            c = c[0]
            frame = c.frame
            sym_lst = c.sym
            ret_type = func_sym.mtype.restype
            if not isinstance(ret_type, VoidType):
                eCode, eType = ast.expr.accept(self, [Access(frame, sym_lst, False, True), True])
                self.emit.printout(eCode)
            self.emit.printout(self.emit.emitRETURN(ret_type, frame))
            return True

    def check_if_unknown(self, ast, c):
        name = self.get_name(ast)
        sym = self.search(name, [c[0], c[1]])
        if isinstance(sym.mtype, FunctionType):
            return isinstance(sym.mtype.restype, Unknown)
        if isinstance(sym.mtype, ArrayType):
            return isinstance(sym.mtype.eletype, Unknown)

    def visitBinaryOp(self, ast, c):
        ass4 = c[1]
        if not ass4:
            c = c[0]
            op_type = self.get_operator_type(ast.op)
            if isinstance(ast.left, (CallExpr, ArrayCell)) and self.check_if_unknown(ast.left, c):
                name = self.get_name(ast.left)
                sym = self.search(name, [c[0], c[1]])
                self.infer_type(sym, op_type)
            lhs_type = ast.left.accept(self, [c, False])
            if not isinstance(lhs_type, ArrayType):
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
            rhs_type = ast.right.accept(self, [c, False])
            if not isinstance(rhs_type, ArrayType):
                rhs_type = self.get_type(rhs_type)
            rhs_name = self.get_name(ast.right)
            if isinstance(rhs_type, Unknown):
                sym = self.search(rhs_name, [c[0], c[1]])
                rhs_type = self.infer_type(sym, op_type)

            # Check type according to operator
            if ast.op in ['+', '-', '*', '\\', '%']:
                if isinstance(lhs_type, IntType) and isinstance(rhs_type, IntType):
                    return IntType()
            elif ast.op in ['==', '!=', '<', '>', '<=', '>=']:
                if isinstance(lhs_type, IntType) and isinstance(rhs_type, IntType):
                    return BoolType()
            elif ast.op in ['+.', '-.', '*.', '\\.']:
                if isinstance(lhs_type, FloatType) and isinstance(rhs_type, FloatType):
                    return FloatType()
            elif ast.op in ['=/=', '<.', '>.', '<=.', '>=.']:
                if isinstance(lhs_type, FloatType) and isinstance(rhs_type, FloatType):
                    return BoolType()
            elif ast.op in ['!', '&&', '||']:
                if isinstance(lhs_type, BoolType) and isinstance(rhs_type, BoolType):
                    return BoolType()
        else:
            c = c[0]
            frame = c.frame
            sym_lst = c.sym
            op_type = self.get_operator_type(ast.op)
            op = ast.op
            e1, e1_typ = ast.left.accept(self, [c, True])
            e2, e2_typ = ast.right.accept(self, [c, True])
            if op in ['+', '-']:
                return e1 + e2 + self.emit.emitADDOP(op, IntType(), frame), IntType()
            elif op in ['+.', '-.']:
                return e1 + e2 + self.emit.emitADDOP(op[0], FloatType(), frame), FloatType()
            elif op in ['*', '\\']:
                return e1 + e2 + self.emit.emitMULOP(op, IntType(), frame), IntType()
            elif op in ['*.', '\\.']:
                return e1 + e2 + self.emit.emitMULOP(op[:-1], FloatType(), frame), FloatType()
            elif op in ['>', '<', '>=', '<=', '!=', '==']:
                return e1 + e2 + self.emit.emitREOP(op, IntType(), frame), BoolType()
            elif op in ['<.', '>.', '<=.', '>=.']:
                return e1 + e2 + self.emit.emitREOP(op[:-1], FloatType(), frame), BoolType()
            elif op in ['=/=']:
                return e1 + e2 + self.emit.emitREOP('!=', FloatType(), frame), BoolType()
            elif op in ['%']:
                return e1 + e2 + self.emit.emitMOD(frame), IntType()
            elif op in ['&&']:
                return e1 + e2 + self.emit.emitANDOP(frame), BoolType()
            elif op in ['||']:
                return e1 + e2 + self.emit.emitOROP(frame), BoolType()

    def visitUnaryOp(self, ast, c):
        ass4 = c[1]
        if not ass4:
            c = c[0]
            op_type = self.get_operator_type(ast.op)
            if isinstance(ast.body, (CallExpr, ArrayCell)) and self.check_if_unknown(ast.body, c):
                name = self.get_name(ast.body)
                sym = self.search(name, [c[0], c[1]])
                self.infer_type(sym, op_type)
            typ = ast.body.accept(self, [c, False])
            typ = self.get_type(typ)
            if isinstance(typ, Unknown):
                name = self.get_name(ast.body)
                sym = self.search(name, [c[0], c[1]])
                typ = self.infer_type(sym, op_type)
            return typ
        else:
            # Access
            c = c[0]
            frame = c.frame
            sym_lst = c.sym
            op = ast.op
            eCode, eType = ast.body.accept(self, [c, True])
            if op in ['-', '-.']:
                return eCode + self.emit.emitNEGOP(eType, frame), eType
            elif op in ['!']:
                return eCode + self.emit.emitNOT(eType, frame), eType

    def visitId(self, ast, c):
        # c[0] : Access
        ass4 = c[1]
        if not ass4:
            c = c[0]
            tem_id = self.search(ast.name, [c[0], c[1]])
            return tem_id.mtype
        else:
            c = c[0]
            frame = c.frame
            sym_lst = c.sym
            name = self.get_name(ast)
            sym = self.search(name, [sym_lst])
            typ = sym.mtype
            isLeft = c.isLeft

            if isLeft:
                if type(sym.value) is CName:
                    code = self.emit.emitPUTSTATIC(self.className + '/' + name, typ, frame)
                else:
                    code = self.emit.emitWRITEVAR(name, typ, sym.value.value, frame)
            else:
                if type(sym.value) is CName:
                    code = self.emit.emitGETSTATIC(self.className + '/' + name, typ, frame)
                else:
                    code = self.emit.emitREADVAR(name, typ, sym.value.value, frame)
            return code, typ

    def visitArrayLiteral(self, ast, c):
        ass4 = c[1]
        if not ass4:
            c = c[0]
            ele_typ = ast.value[0].accept(self, [c, False])
            dim = [len(ast.value)] + (ele_typ.dimen if isinstance(ele_typ, ArrayType) else [])
            if isinstance(ele_typ, ArrayType):
                ele_typ = ele_typ.eletype
            return ArrayType(dim, ele_typ)
        else:
            c = c[0]
            frame = c.frame
            sym_lst = c.sym
            return True, True

    def visitArrayCell(self, ast, c):
        ass4 = c[1]
        if not ass4:
            c = c[0]
            name = self.get_name(ast.arr)
            ast.arr.accept(self, [c, False])
            func_sym = self.search(name, [c[0], c[1]])
            for x in ast.idx:
                tem = x.accept(self, [c, False])
                tem = self.get_type(tem)
                if isinstance(tem, Unknown):
                    name = self.get_name(x)
                    sym = self.search(name, [c[0], c[1]])
                    tem = self.infer_type(sym, IntType())
            lst = []
            if isinstance(func_sym.mtype, ArrayType):
                lst = func_sym.mtype.dimen
            elif isinstance(func_sym.mtype, FunctionType):
                lst = func_sym.mtype.restype.dimen
            typ = func_sym.mtype if isinstance(func_sym.mtype, ArrayType) else func_sym.mtype.restype
            return typ.eletype
        else:
            c = c[0]
            frame = c.frame
            sym_lst = c.sym
            isLeft = c.isLeft
            return True, True

    def visitBreak(self, ast, c):
        ass4 = c[1]
        if not ass4:
            c = c[0]
            pass
        else:
            c = c[0]
            frame = c.frame
            l = c.frame.getBreakLabel()
            self.emit.printout(self.emit.emitGOTO(frame.getBreakLabel(), frame))

    def visitContinue(self, ast, c):
        ass4 = c[1]
        if not ass4:
            c = c[0]
            pass
        else:
            c = c[0]
            frame = c.frame
            sym_lst = c.sym
            self.emit.printout(self.emit.emitGOTO(frame.getContinueLabel(), frame))

    def visitIntLiteral(self, ast, c):
        # c[0] : access
        ass4 = c[1]
        if not ass4:
            c = c[0]
            return IntType()
        else:
            c = c[0]
            frame = c.frame
            sym_lst = c.sym
            return self.emit.emitPUSHICONST(ast.value, frame), IntType()

    def visitFloatLiteral(self, ast, c):
        # c[0] : access
        ass4 = c[1]
        if not ass4:
            c = c[0]
            return FloatType()
        else:
            c = c[0]
            frame = c.frame
            sym_lst = c.sym
            return self.emit.emitPUSHFCONST(str(ast.value), frame), FloatType()

    def visitBooleanLiteral(self, ast, c):
        # c[0] : access
        ass4 = c[1]
        if not ass4:
            c = c[0]
            return BoolType()
        else:
            c = c[0]
            frame = c.frame
            sym_lst = c.sym
            return self.emit.emitPUSHICONST(str(ast.value).lower(), frame), BoolType()

    def visitStringLiteral(self, ast, c):
        # c[0] : access
        ass4 = c[1]
        if not ass4:
            c = c[0]
            return StringType()
        else:
            c = c[0]
            frame = c.frame
            sym_lst = c.sym
            return self.emit.emitPUSHCONST(ast.value, StringType(), frame), StringType()
