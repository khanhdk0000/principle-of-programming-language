from functools import reduce
from abc import ABC


# visitor pattern
# class Expr(ABC):
#     def accept(self, visitor):
#         pass
#
# class ExprVisitor(ABC):
#     pass
#
# class Eval(ExprVisitor):
#     def visitIntLit(self, expr):
#         return expr.num
#
#     def visitFloatLit(self, expr):
#         return expr.num
#
#     def visitUnExp(self, expr):
#         if expr.operator == "+":
#             return expr.operand.accept(self)
#         elif expr.operator == '-':
#             return -expr.operand.accept(self)
#
#     def visitBiExp(self, expr):
#         if expr.operator == "+":
#             return expr.left.accept(self) + expr.right.accept(self)
#         elif expr.operator == "-":
#             return expr.left.accept(self) - expr.right.accept(self)
#         elif expr.operator == "*":
#             return expr.left.accept(self) * expr.right.accept(self)
#         elif expr.operator == "/":
#             return expr.left.accept(self) / expr.right.accept(self)
#
#
# class PrintPrefix(ExprVisitor):
#     def visitIntLit(self, expr):
#         return str(expr.num) + ' '
#
#     def visitFloatLit(self, expr):
#         return str(expr.num) + ' '
#
#     def visitUnExp(self, expr):
#         return str(expr.operator == '-' and '-.' or expr.operator) + ' ' + expr.operand.accept(self)
#
#     def visitBiExp(self, expr):
#         return str(expr.operator == '-' and '-.' or expr.operator) \
#                + ' ' + expr.left.accept(self) + expr.right.accept(self)
#
#
# class PrintPostfix(ExprVisitor):
#     def visitIntLit(self, expr):
#         return str(expr.num) + ' '
#
#     def visitFloatLit(self, expr):
#         return str(expr.num) + ' '
#
#     def visitUnExp(self, expr):
#         return expr.operand.accept(self)  + str(expr.operator == '-' and '-.' or expr.operator) + ' '
#
#     def visitBiExp(self, expr):
#         return expr.left.accept(self) + expr.right.accept(self) \
#                + str(expr.operator == '-' and '-.' or expr.operator) + ' '
#
# class IntLit(Expr):
#     def __init__(self, num=0):
#         self.num = num
#
#     def accept(self, visitor):
#         return visitor.visitIntLit(self)
#
# class FloatLit(Expr):
#     def __init__(self, num=0.0):
#         self.num = num
#
#     def accept(self, visitor):
#         return visitor.visitFloatLit(self)
#
# class BinExp(Expr):
#     def __init__(self, left, operator, right):
#         self.operator = operator
#         self.left = left
#         self.right = right
#
#     def accept(self, visitor):
#         return visitor.visitBiExp(self)
#
# class UnExp(Expr):
#     def __init__(self, operator, operand):
#         self.operator = operator
#         self.operand = operand
#
#     def accept(self, visitor):
#         return visitor.visitUnExp(self)

# from abc import ABC
#
# class Expr(ABC):
#     pass
#
# class IntLit(Expr):
#     def __init__(self, num=0):
#         self.num = num
#
#     def eval(self):
#         return self.num
#
#     def printPrefix(self):
#         return str(self.num) + ' '
#
# class FloatLit(Expr):
#     def __init__(self, num=0.0):
#         self.num = num
#     def eval(self):
#         return self.num
#     def printPrefix(self):
#         return str(self.num) + ' '
#
# class BinExp(Expr):
#     def __init__(self, left, operator, right):
#         self.operator = operator
#         self.left = left
#         self.right = right
#
#     def eval(self):
#         if self.operator == "+":
#             return self.left.eval() + self.right.eval()
#         elif self.operator == "-":
#             return self.left.eval() - self.right.eval()
#         elif self.operator == "*":
#             return self.left.eval() * self.right.eval()
#         elif self.operator == "/":
#             return self.left.eval() / self.right.eval()
#
#     def printPrefix(self):
#         return str(self.operator == '-' and '-.' or self.operator) + ' ' + self.left.printPrefix() + self.right.printPrefix()
#
# class UnExp(Expr):
#     def __init__(self, operator, operand):
#         self.operator = operator
#         self.operand = operand
#
#     def eval(self):
#         if self.operator == "+":
#             return self.operand.eval()
#         elif self.operator == "-":
#             return -self.operand.eval()
#
#     def printPrefix(self):
#         return str(self.operator == '-' and '-.' or self.operator) + ' ' + self.operand.printPrefix()


# High order

#
#
# def compose(*functions):
#     if len(functions) >= 2:
#         return functools.reduce(lambda f, g: lambda x: f(g(x)), functions)
#     print("compose() missing 1 required positional argument")
#
#
# def increase(x):
#     return x + 1
#
#
# def square(x):
#     return x ** 2
#
#
# def double(x):
#     return x * 2
#
#
# ans = compose(increase, square, double)
# print(ans(3))

# def dist(lst,n):
#     return list(map(lambda x: (x,n), lst))
#
#
# print(dist([1,2,3],4))


# def flatten(lst):
#     return reduce(lambda x, y: x + y, lst, [])

#
# print(flatten([[1,2,3],[4,5],[6,7]]))

# def lessThan(lst,n):
#     return list(filter(lambda x: x < n, lst))
#
# print(lessThan([1,2,3,4,5],4))

# def lstSquare(n):
#     if n:
#         return lstSquare(n-1) + [n**2]
#     return []
#
#
# print(lstSquare(3))

# def dist(lst,n):
#     if len(lst) == 0:
#         return []
#     return [(lst[0], n)] + dist(lst[1:], n)
#
# print(dist([1,2,3],4))

# def flatten(lst):
#     if(len(lst)) == 0:
#         return []
#     return lst[0] + flatten(lst[1:])
#
#
#
# print(flatten([[1,2,3],[4,5],[6,7]]))

# def lessThan(lst,n):
#     if len(lst) == 0:
#         return []
#     return [lst[0]] + lessThan(lst[1:], n)  if lst[0] < n else lessThan(lst[1:], n)
#
# print(lessThan([1,2,3,4,5],4))

# CODE AST
# 1
# class TerminalCount(MPVisitor):
#     def visitProgram(self,ctx:MPParser.ProgramContext):
#         return self.visit(ctx.vardecls()) + 1
#
#     def visitVardecls(self,ctx:MPParser.VardeclsContext):
#         return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())
#
#     def visitVardecltail(self,ctx:MPParser.VardecltailContext):
#         return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail()) if ctx.vardecltail() else 0
#
#     def visitVardecl(self,ctx:MPParser.VardeclContext):
#         return 1 + self.visit(ctx.mptype()) + self.visit(ctx.ids())
#
#     def visitMptype(self,ctx:MPParser.MptypeContext):
#         return 1
#
#     def visitIds(self,ctx:MPParser.IdsContext):
#         return 2 + self.visit(ctx.ids()) if ctx.getChildCount() == 3 else 1

# 2
# class ASTGeneration(MPVisitor):
#     def visitProgram(self,ctx:MPParser.ProgramContext):
#         return Program(self.visit(ctx.vardecls()))
#
#     def visitVardecls(self,ctx:MPParser.VardeclsContext):
#         return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())
#
#     def visitVardecltail(self,ctx:MPParser.VardecltailContext):
#         if ctx.vardecltail():
#             return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())
#         else:
#             return []
#
#     def visitVardecl(self,ctx:MPParser.VardeclContext):
#         return list(map(lambda e: VarDecl(e, ctx.mptype().accept(self)), ctx.ids().accept(self)))
#
#     def visitMptype(self,ctx:MPParser.MptypeContext):
#         return IntType() if ctx.INTTYPE() else FloatType()
#
#     def visitIds(self,ctx:MPParser.IdsContext):
#     return [Id(ctx.ID().getText())] + ctx.ids().accept(self) if ctx.getChildCount() > 1 else [Id(ctx.ID().getText())]

# 3
# class ASTGeneration(MPVisitor):
#     def visitProgram(self,ctx:MPParser.ProgramContext):
#         return ctx.exp().accept(self)
#
#     def visitExp(self,ctx:MPParser.ExpContext):
#         if ctx.ASSIGN():
#             return Binary(ctx.ASSIGN().getText(), ctx.term().accept(self), ctx.exp().accept(self))
#         return ctx.term().accept(self)
#
#     def visitTerm(self,ctx:MPParser.TermContext):
#         if ctx.COMPARE():
#             return Binary(ctx.COMPARE().getText(), ctx.factor(0).accept(self), ctx.factor(1).accept(self))
#         return ctx.factor(0).accept(self)
#
#
#     def visitFactor(self,ctx:MPParser.FactorContext):
#         if ctx.ANDOR():
#             return Binary(ctx.ANDOR().getText(), ctx.factor().accept(self), ctx.operand().accept(self))
#         return ctx.operand().accept(self)
#
#     def visitOperand(self,ctx:MPParser.OperandContext):
#         if ctx.ID():
#             return Id(ctx.ID().getText())
#         if ctx.INTLIT():
#             return IntLiteral(ctx.INTLIT().getText())
#         if ctx.BOOLIT():
#             return BooleanLiteral(ctx.BOOLIT().getText())
#         return ctx.exp().accept(self)

# 4
# class ASTGeneration(MPVisitor):
#     def visitProgram(self,ctx:MPParser.ProgramContext):
#         return Program(reduce(lambda x, y: x + y.accept(self), ctx.vardecl(), []))
#
#     def visitVardecl(self,ctx:MPParser.VardeclContext):
#         return list(map(lambda e: VarDecl(e, ctx.mptype().accept(self)), ctx.ids().accept(self)))
#
#     def visitMptype(self,ctx:MPParser.MptypeContext):
#         return IntType() if ctx.INTTYPE() else FloatType()
#
#     def visitIds(self,ctx:MPParser.IdsContext):
#         return [Id(x.getText()) for x in ctx.ID()]

# 5
# class ASTGeneration(MPVisitor):
#     def visitProgram(self,ctx:MPParser.ProgramContext):
#         return ctx.exp().accept(self)
#
#     def visitExp(self,ctx:MPParser.ExpContext):
#         return reduce(lambda x, y: Binary(y[0].getText(), y[1].accept(self), x),
#                       zip(ctx.ASSIGN()[::-1], ctx.term()[-2::-1]), ctx.term()[-1].accept(self))
#
#     def visitTerm(self,ctx:MPParser.TermContext):
#         if ctx.COMPARE():
#             return Binary(ctx.COMPARE().getText(), ctx.factor(0).accept(self), ctx.factor(1).accept(self))
#         return ctx.factor(0).accept(self)
#
#     def visitFactor(self, ctx: MPParser.FactorContext):
#         return reduce(lambda x, y: Binary(y[0].getText(), x, y[1].accept(self)),
#                       zip(ctx.ANDOR(), ctx.operand()[1:]), ctx.operand()[0].accept(self))
#
#     def visitOperand(self, ctx: MPParser.OperandContext):
#         if ctx.ID():
#             return Id(ctx.ID().getText())
#         if ctx.INTLIT():
#             return IntLiteral(ctx.INTLIT().getText())
#         if ctx.BOOLIT():
#             return BooleanLiteral(ctx.BOOLIT().getText())
#         return ctx.exp().accept(self)


# class A:
#     def accept(self, v):
#         print("A")
#         v.visitA(self)
#
# class B(A):
#     def accept(self, v):
#         print("B")
#         v.visitB(self)
#
# class C(A):
#     def accept(self, v):
#         print('C')
#         v.visitC(self)
#
# class Visitor:
#     def visitA(self, x):
#         return x.accept(self)
#
#     def visitB(self, x):
#         pass
#
#     def visitC(self, x):
#         pass

# x = A()
# x.accept(Visitor())
# y = B()
# y.accept(Visitor())


# class A:
#     def foo(self):
#         print('A')
#
# class B(A):
#     pass
#
# class C(B):
#     pass
#
# class D(A):
#     def foo(self):
#         print('D')
#
# class E(A):
#     pass
#
# class F(D, E):
#     def foo(self):
#         print('F')
#
# class G(C,F,D):
#     pass
#
# x = G()
# x.foo()


# class A:
#     def func1(self):
#         print("A")
#     def func2(self): pass
#
#
# class B(A):
#     def func1(self):
#         print("B")
#
#
# for x in [A(), B()]:
#     x.func1()
#     x.func2()

# lst = [1, 3, 4, 5]
# print(list(map(lambda i: sum(lst[:i+1]), range(len(lst)))))
#
#
# def func(a):
#     if len(a) > 0:
#         return func(a[:-1]) + [sum(a)]
#     return []

# def make_pretty(func):
#     def inner():
#         print("I got decorated")
#         func()
#     return inner
#
# @make_pretty
# def ordinary():
#     print("I am ordinary")
#
# ordinary()

# def log_decorator(func):
#     def inner(*arg):
#         print(func.__name__+" is running")
#         return func(*arg)
#     return inner
#
# @log_decorator
# def foo(x,y):
#     return x*y
#
# print(foo(3,4))

# lst = [1.5, 2, 'b', 'cd', 3]
# print(reduce(lambda x, y:x*y,list(filter(lambda x: isinstance(x, int),lst)),1))


# Name ##################################

# 1
# class StaticCheck(Visitor):
#
#     def visitProgram(self,ctx:Program,o:object):
#         name_lst = []
#         for x in ctx.decl:
#             name = x.accept(self, name_lst)
#             name_lst.append(name)
#         return
#
#     def visitVarDecl(self,ctx:VarDecl,o:object):
#         if ctx.name in o:
#             raise RedeclaredDeclaration(ctx.name)
#         return ctx.name
#
#     def visitConstDecl(self,ctx:ConstDecl,o:object):
#         if ctx.name in o:
#             raise RedeclaredDeclaration(ctx.name)
#         return ctx.name
#
#     def visitIntType(self,ctx:IntType,o:object):
#         return ctx.val
#
#     def visitFloatType(self,ctx:FloatType,o:object):
#         pass
#     def visitIntLit(self,ctx:IntLit,o:object):
#         pass

# 2
# class StaticCheck(Visitor):
#
#     def visitProgram(self,ctx:Program,o:object):
#         name_lst = []
#         for x in ctx.decl:
#             name = x.accept(self, name_lst)
#             name_lst.append(name)
#
#     def visitVarDecl(self,ctx:VarDecl,o:object):
#         if ctx.name in o:
#             raise RedeclaredVariable(ctx.name)
#         return ctx.name
#
#     def visitConstDecl(self,ctx:ConstDecl,o:object):
#         if ctx.name in o:
#             raise RedeclaredConstant(ctx.name)
#         return ctx.name
#
#     def visitIntType(self,ctx:IntType,o:object):
#         pass
#
#     def visitFloatType(self,ctx:FloatType,o:object):
#         pass
#     def visitIntLit(self,ctx:IntLit,o:object):
#         pass

# 3

# class StaticCheck(Visitor):
#
#     def visitProgram(self,ctx:Program,o:object):
#         name_lst = []
#         for x in ctx.decl:
#             if x.name in name_lst:
#                 if isinstance(x, VarDecl):
#                     raise RedeclaredVariable(x.name)
#                 elif isinstance(x, ConstDecl):
#                     raise RedeclaredConstant(x.name)
#                 else:
#                     raise RedeclaredFunction(x.name)
#             else:
#                 name_lst.append(x.name)
#             if isinstance(x, FuncDecl):
#                 x.accept(self, name_lst)
#
#
#     def visitVarDecl(self, ctx: VarDecl, o: object):
#         pass
#
#     def visitConstDecl(self, ctx: ConstDecl, o: object):
#         pass
#
#         def visitFuncDecl(self, ctx: FuncDecl, o: object):
#         name_lst = []
#         for x in ctx.param:
#             if x.name in name_lst:
#                 if isinstance(x, VarDecl):
#                     raise RedeclaredVariable(x.name)
#                 elif isinstance(x, ConstDecl):
#                     raise RedeclaredConstant(x.name)
#                 else:
#                     raise RedeclaredFunction(x.name)
#             else:
#                 name_lst.append(x.name)
#         for x in ctx.body:
#             if x.name in name_lst:
#                 if isinstance(x, VarDecl):
#                     raise RedeclaredVariable(x.name)
#                 elif isinstance(x, ConstDecl):
#                     raise RedeclaredConstant(x.name)
#                 else:
#                     raise RedeclaredFunction(x.name)
#             else:
#                 name_lst.append(x.name)
#             if isinstance(x,FuncDecl):
#                 x.accept(self, name_lst)
#
#
#
#     def visitIntType(self, ctx: IntType, o: object):
#         pass
#
#     def visitFloatType(self, ctx: FloatType, o: object):
#         pass
#
#     def visitIntLit(self, ctx: IntLit, o: object):
#         pass

# 4
# class StaticCheck(Visitor):
#
#     def visitProgram(self, ctx: Program, o: object):
#         decl = []
#         save = []
#         lst = [decl, save]
#         for i in ctx.decl:
#             name = i.accept(self, lst)
#             decl.append(name)
#             save.append(name)
#         return
#
#     def visitVarDecl(self, ctx: VarDecl, o: object):
#         if ctx.name in o[0]:
#             raise RedeclaredVariable(ctx.name)
#         return ctx.name
#
#     def visitConstDecl(self, ctx: ConstDecl, o: object):
#         if ctx.name in o[0]:
#             raise RedeclaredConstant(ctx.name)
#         return ctx.name
#
#     def visitFuncDecl(self, ctx: FuncDecl, o: object):
#         if ctx.name in o[0]:
#             raise RedeclaredFunction(ctx.name)
#         lst = [[], o[1] + [ctx.name]]
#         for i in ctx.param + ctx.body[0]:
#             name = i.accept(self, lst)
#             lst[0].append(name)
#             lst[1].append(name)
#
#         for k in ctx.body[1]:
#             k.accept(self, lst[1])
#
#         return ctx.name
#
#
#     def visitIntType(self, ctx: IntType, o: object):
#         pass
#
#     def visitFloatType(self, ctx: FloatType, o: object):
#         pass
#
#     def visitIntLit(self, ctx: IntLit, o: object):
#         return ctx.val
#
#     def visitId(self, ctx: Id, o: object):
#         if ctx.name not in o:
#             raise UndeclaredIdentifier(ctx.name)
#         return ctx.name


# Type
# 1
# class StaticCheck(Visitor):
#     ERROR = -1
#     BOOLEAN = 0
#     INT = 1
#     FLOAT = 2
#     INTFLOATTYPE = [INT, FLOAT]
#     BOOLTYPE = BOOLEAN
#
#     def visitBinOp(self, ctx: BinOp, o):
#         e1 = ctx.e1.accept(self, o)
#         e2 = ctx.e2.accept(self, o)
#         if ctx.op in ['+', '-', '*']:
#             if e1 in self.INTFLOATTYPE and e2 in self.INTFLOATTYPE:
#                 if e1 == self.FLOAT or e2 == self.FLOAT:
#                     return_type = self.FLOAT
#                 else:
#                     return_type = self.INT
#             else:
#                 return_type = self.ERROR
#         elif ctx.op == '/':
#             if e1 in self.INTFLOATTYPE and e2 in self.INTFLOATTYPE:
#                 return_type = self.FLOAT
#             else:
#                 return_type = self.ERROR
#         elif ctx.op in ['!', '&&', '||']:
#             if e1 == self.BOOLTYPE and e2 == self.BOOLTYPE:
#                 return_type = self.BOOLEAN
#             else:
#                 return_type = self.ERROR
#         elif ctx.op in ['<','>','==','!=']:
#             if e1 == e2:
#                 return_type = self.BOOLEAN
#             else:
#                 return_type = self.ERROR
#         else:
#             return_type = self.ERROR
#
#         if return_type == self.ERROR:
#             raise TypeMismatchInExpression(ctx)
#         return return_type
#
#     def visitUnOp(self, ctx: UnOp, o):
#         e = ctx.e.accept(self, o)
#         if ctx.op == '-':
#             if e in self.INTFLOATTYPE:
#                 return_type = e
#             else:
#                 return_type = self.ERROR
#         elif ctx.op == '!':
#             if e == self.BOOLTYPE:
#                 return_type = e
#             else:
#                 return_type = self.ERROR
#         else:
#             return_type = self.ERROR
#
#         if return_type == self.ERROR:
#             raise TypeMismatchInExpression(ctx)
#         return return_type
#
#
#     def visitIntLit(self, ctx: IntLit, o):
#         return self.INT
#
#     def visitFloatLit(self, ctx, o):
#         return self.FLOAT
#
#     def visitBoolLit(self, ctx, o):
#         return self.BOOLEAN


# 2
# class StaticCheck(Visitor):
#     ERROR = -1
#     BOOLEAN = 0
#     INT = 1
#     FLOAT = 2
#     INTFLOATTYPE = [INT, FLOAT]
#     BOOLTYPE = [BOOLEAN]
#
#     def visitProgram(self, ctx: Program, o):
#         name = []
#         typ = []
#         lst = [name, typ]
#         for e in ctx.decl:
#             tem = e.accept(self, lst)
#             name.append(tem[0])
#             typ.append(tem[1])
#         ctx.exp.accept(self, lst)
#         return
#
#     def visitVarDecl(self, ctx: VarDecl, o):
#         return ctx.typ.accept(self, ctx.name)
#
#     def visitIntType(self, ctx: IntType, o):
#         return o, self.INT
#
#     def visitFloatType(self, ctx: FloatType, o):
#         return o, self.FLOAT
#
#     def visitBoolType(self, ctx: BoolType, o):
#         return o, self.BOOLEAN
#
#     def visitBinOp(self, ctx: BinOp, o):
#         e1 = ctx.e1.accept(self, o)
#         e2 = ctx.e2.accept(self, o)
#         if ctx.op in ['+', '-', '*']:
#             if e1 in self.INTFLOATTYPE and e2 in self.INTFLOATTYPE:
#                 if e1 == self.FLOAT or e2 == self.FLOAT:
#                     return_type = self.FLOAT
#                 else:
#                     return_type = self.INT
#             else:
#                 return_type = self.ERROR
#         elif ctx.op == '/':
#             if e1 in self.INTFLOATTYPE and e2 in self.INTFLOATTYPE:
#                 return_type = self.FLOAT
#             else:
#                 return_type = self.ERROR
#         elif ctx.op in ['!', '&&', '||']:
#             if e1 in self.BOOLTYPE and e2 in self.BOOLTYPE:
#                 return_type = self.BOOLEAN
#             else:
#                 return_type = self.ERROR
#         elif ctx.op in ['<', '>', '==', '!=']:
#             if e1 == e2:
#                 return_type = self.BOOLEAN
#             else:
#                 return_type = self.ERROR
#         else:
#             return_type = self.ERROR
#
#         if return_type == self.ERROR:
#             raise TypeMismatchInExpression(ctx)
#         return return_type
#
#     def visitUnOp(self, ctx: UnOp, o):
#         e = ctx.e.accept(self, o)
#         if ctx.op == '-':
#             if e in self.INTFLOATTYPE:
#                 return_type = e
#             else:
#                 return_type = self.ERROR
#         elif ctx.op == '!':
#             if e in self.BOOLTYPE:
#                 return_type = e
#             else:
#                 return_type = self.ERROR
#         else:
#             return_type = self.ERROR
#
#         if return_type == self.ERROR:
#             raise TypeMismatchInExpression(ctx)
#         return return_type
#
#     def visitIntLit(self, ctx: IntLit, o):
#         return self.INT
#
#     def visitFloatLit(self, ctx, o):
#         return self.FLOAT
#
#     def visitBoolLit(self, ctx, o):
#         return self.BOOLEAN
#
#     def visitId(self, ctx, o):
#         if ctx.name not in o[0]:
#             raise UndeclaredIdentifier(ctx.name)
#         for i in range(len(o[0])):
#             if ctx.name == o[0][i]:
#                 return o[1][i]

# 3
# class StaticCheck(Visitor):
#     ERROR = -1
#     BOOLEAN = 0
#     INT = 1
#     FLOAT = 2
#     UNASSIGNED = 3
#     name = []
#     typ = []
#
#     def visitProgram(self, ctx: Program, o):
#         name = list(map(lambda x: x.accept(self, o), ctx.decl))
#         typ = [self.UNASSIGNED for x in range(len(name))]
#         self.name = name
#         self.typ = typ
#         lst = [self.name, self.typ]
#         for i in ctx.exp:
#             tem = i.accept(self, lst)
#
#     def visitVarDecl(self, ctx: VarDecl, o):
#         return ctx.name
#
#     def visitAssign(self, ctx: Assign, o):
#         lhs = ctx.lhs.accept(self, o)
#         rhs = ctx.rhs.accept(self, o)
#         if isinstance(ctx.rhs, (IntLit, FloatLit, BoolLit)) and lhs == self.UNASSIGNED:
#             for x in range(len(self.name)):
#                 if ctx.lhs.name == self.name[x]:
#                     self.typ[x] = rhs
#         if isinstance(ctx.rhs, Id) and lhs == self.UNASSIGNED:
#             for x in range(len(self.name)):
#                 if ctx.lhs.name == self.name[x]:
#                     self.typ[x] = rhs
#         tem_lhs = ctx.lhs.accept(self, o)
#         if rhs not in [self.INT, self.FLOAT, self.BOOLEAN]:
#             raise TypeCannotBeInferred(ctx)
#         elif tem_lhs != rhs:
#             raise TypeMismatchInStatement(ctx)
#         return lhs, rhs
#
#     def visitBinOp(self, ctx: BinOp, o):
#         e1 = ctx.e1.accept(self, o)
#         e2 = ctx.e2.accept(self, o)
#         if ctx.op in ['+', '-', '*', '/']:
#             if e1 == self.UNASSIGNED:
#                 for x in range(len(self.name)):
#                     if ctx.e1.name == self.name[x]:
#                         self.typ[x] = self.INT
#                 e1 = self.INT
#             if e2 == self.UNASSIGNED:
#                 for x in range(len(self.name)):
#                     if ctx.e2.name == self.name[x]:
#                         self.typ[x] = self.INT
#                 e2 = self.INT
#             if e1 == self.INT and e2 == self.INT:
#                 return_type = self.INT
#             else:
#                 return_type = self.ERROR
#         elif ctx.op in ['+.', '-.', '*.', '/.']:
#             if e1 == self.UNASSIGNED:
#                 for x in range(len(self.name)):
#                     if ctx.e1.name == self.name[x]:
#                         self.typ[x] = self.FLOAT
#                 e1 = self.FLOAT
#             if e2 == self.UNASSIGNED:
#                 for x in range(len(self.name)):
#                     if ctx.e2.name == self.name[x]:
#                         self.typ[x] = self.FLOAT
#                 e2 = self.FLOAT
#             if e1 == self.FLOAT and e2 == self.FLOAT:
#                 return_type = self.FLOAT
#             else:
#                 return_type = self.ERROR
#         elif ctx.op in ['>', '=']:
#             if e1 == self.UNASSIGNED:
#                 for x in range(len(self.name)):
#                     if ctx.e1.name == self.name[x]:
#                         self.typ[x] = self.INT
#                 e1 = self.INT
#             if e2 == self.UNASSIGNED:
#                 for x in range(len(self.name)):
#                     if ctx.e2.name == self.name[x]:
#                         self.typ[x] = self.INT
#                 e2 = self.INT
#             if e1 == self.INT and e2 == self.INT:
#                 return_type = self.BOOLEAN
#             else:
#                 return_type = self.ERROR
#         elif ctx.op in ['>.', '=.']:
#             if e1 == self.UNASSIGNED:
#                 for x in range(len(self.name)):
#                     if ctx.e1.name == self.name[x]:
#                         self.typ[x] = self.FLOAT
#                 e1 = self.FLOAT
#             if e2 == self.UNASSIGNED:
#                 for x in range(len(self.name)):
#                     if ctx.e2.name == self.name[x]:
#                         self.typ[x] = self.FLOAT
#                 e2 = self.FLOAT
#             if e1 == self.FLOAT and e2 == self.FLOAT:
#                 return_type = self.BOOLEAN
#             else:
#                 return_type = self.ERROR
#         elif ctx.op in ['&&', '||', '>b', '=b']:
#             if e1 == self.UNASSIGNED:
#                 for x in range(len(self.name)):
#                     if ctx.e1.name == self.name[x]:
#                         self.typ[x] = self.BOOLEAN
#                 e1 = self.BOOLEAN
#             if e2 == self.UNASSIGNED:
#                 for x in range(len(self.name)):
#                     if ctx.e2.name == self.name[x]:
#                         self.typ[x] = self.BOOLEAN
#                 e2 = self.BOOLEAN
#             if e1 == self.BOOLEAN and e2 == self.BOOLEAN:
#                 return_type = self.BOOLEAN
#             else:
#                 return_type = self.ERROR
#         else:
#             return_type = self.ERROR
#
#         if return_type == self.ERROR:
#             raise TypeMismatchInExpression(ctx)
#         return return_type
#
#     def visitUnOp(self, ctx: UnOp, o):
#         e = ctx.e.accept(self, o)
#         if ctx.op == '-':
#             if e == self.UNASSIGNED:
#                 for x in range(len(self.name)):
#                     if ctx.e.name == self.name[x]:
#                         self.typ[x] = self.INT
#                 e = self.INT
#             if e == self.INT:
#                 return_type = e
#             else:
#                 return_type = self.ERROR
#         elif ctx.op == '-.':
#             if e == self.UNASSIGNED:
#                 for x in range(len(self.name)):
#                     if ctx.e.name == self.name[x]:
#                         self.typ[x] = self.FLOAT
#                 e = self.FLOAT
#             if e == self.FLOAT:
#                 return_type = e
#             else:
#                 return_type = self.ERROR
#         elif ctx.op == '!':
#             if e == self.UNASSIGNED:
#                 for x in range(len(self.name)):
#                     if ctx.e.name == self.name[x]:
#                         self.typ[x] = self.BOOLEAN
#                 e = self.BOOLEAN
#             if e == self.BOOLEAN:
#                 return_type = e
#             else:
#                 return_type = self.ERROR
#         elif ctx.op == 'i2f':
#             if e == self.UNASSIGNED:
#                 for x in range(len(self.name)):
#                     if ctx.e.name == self.name[x]:
#                         self.typ[x] = self.INT
#                 e = self.INT
#             if e == self.INT:
#                 return_type = self.FLOAT
#             else:
#                 return_type = self.ERROR
#         elif ctx.op == 'floor':
#             if e == self.UNASSIGNED:
#                 for x in range(len(self.name)):
#                     if ctx.e.name == self.name[x]:
#                         self.typ[x] = self.FLOAT
#                 e = self.FLOAT
#             if e == self.FLOAT:
#                 return_type = self.INT
#             else:
#                 return_type = self.ERROR
#         else:
#             return_type = self.ERROR
#
#         if return_type == self.ERROR:
#             raise TypeMismatchInExpression(ctx)
#         return return_type
#
#     def visitIntLit(self, ctx: IntLit, o):
#         return self.INT
#
#     def visitFloatLit(self, ctx, o):
#         return self.FLOAT
#
#     def visitBoolLit(self, ctx, o):
#         return self.BOOLEAN
#
#     def visitId(self, ctx, o):
#         if ctx.name not in self.name:
#             raise UndeclaredIdentifier(ctx.name)
#         else:
#             for i in range(len(self.name)):
#                 if ctx.name == self.name[i]:
#                     return self.typ[i]

# JVM

# 1
# class StaticCheck(Visitor):
#
#     def visitProgram(self, ctx: Program, o):
#         decl = []
#         for x in ctx.decl:
#             tem = x.accept(self, decl)
#             decl += [tem]
#         typ = []
#         for s in ctx.stmts:
#             typ += s.accept(self, (decl, typ))
#
#     def visitVarDecl(self, ctx: VarDecl, o):
#         if ctx.name in o:
#             raise Redeclared(ctx)
#         return ctx.name
#
#     def visitBlock(self, ctx: Block, o):
#         decl = []
#         env = o[0]
#         typ = o[1]
#         for x in ctx.decl:
#             tem = x.accept(self, decl)
#             decl += tem
#             env += tem
#             typ = list(filter(lambda j: j[0] != tem, typ))
#         for i in ctx.stmts:
#             typ += i.accept(self, (env, typ))
#         return typ
#
#     def visitAssign(self, ctx: Assign, o):
#         lhs = ctx.lhs.accept(self, o)
#         rhs = ctx.rhs.accept(self, o)
#         rettyp = rhs[0]
#         typ = rhs[1]
#         if lhs[0] != 'Unknown' and rettyp == 'Unknown':
#             typ += [(ctx.rhs.name, lhs[0])]
#             rettyp = lhs[0]
#
#         if lhs[0] != 'Unknown' and rettyp != 'Unknown' and lhs[0] != rettyp:
#             raise TypeMismatchInStatement(ctx)
#         if lhs[0] == 'Unknown' and rettyp == 'Unknown':
#             raise TypeCannotBeInferred(ctx)
#         found = False
#         for i in typ:
#             if ctx.lhs.name == i[0]:
#                 found = True
#                 # if rettyp != i[1]:
#                 #     raise TypeMismatchInStatement(ctx)
#
#         if not found:
#             typ += [(ctx.lhs.name, rettyp)]
#         return typ
#
#     def visitBinOp(self, ctx: BinOp, o):
#         e1 = ctx.e1.accept(self, o)
#         e2 = ctx.e2.accept(self, o)
#         typ = e1[1]
#         for j in e2[1]:
#             found = False
#             for i in typ:
#                 if i[0] == j[0]:
#                     found = True
#                     if i[1] != j[1]:
#                         raise TypeMismatchInExpression(e2)
#             if not found:
#                 typ += [j]
#         acc_typ, ret_typ = '', ''
#         if ctx.op in ["+", "-", "*", "/"]:
#             acc_typ, ret_typ = "Int", "Int"
#         if ctx.op in ["+.", "-.", "*.", "/."]:
#             acc_typ, ret_typ = "Float", "Float"
#         if ctx.op in [">", "="]:
#             acc_typ, ret_typ = "Int", "Bool"
#         if ctx.op in [">.", "=."]:
#             acc_typ, ret_typ = "Float", "Bool"
#         if ctx.op in ["&&", "||", ">b", "=b"]:
#             acc_typ, ret_typ = "Bool", "Bool"
#
#         if e1[0] == "Unknown":
#             e1[0] = acc_typ
#             typ += [(ctx.e1.name, e1[0])]
#         if e2[0] == "Unknown":
#             e2[0] = acc_typ
#             typ += [(ctx.e2.name, e2[0])]
#         if (e1[0] != acc_typ) or (e2[0] != acc_typ):
#             raise TypeMismatchInExpression(ctx)
#
#         return (ret_typ, typ)
#
#     def visitUnOp(self, ctx: UnOp, o):
#         e = ctx.e.accept(self, o)
#         acc_typ, ret_typ = '', ''
#         if ctx.op == '-':
#             acc_typ, ret_typ = 'Int', 'Int'
#         elif ctx.op == '-.':
#             acc_typ, ret_typ = 'Float', 'Float'
#         elif ctx.op == 'i2f':
#             acc_typ, ret_typ = 'Int', 'Float'
#         elif ctx.op == 'floor':
#             acc_typ, ret_typ = 'Float', 'Int'
#         elif ctx.op == '!':
#             acc_typ, ret_typ = 'Bool', 'Bool'
#
#         if e[0] == 'Unknown':
#             e[0] = acc_typ
#             e[1] += [(ctx.e.name, e[1])]
#         if e[0] != acc_typ:
#             raise TypeMismatchInExpression(ctx)
#         return (ret_typ, e[1])
#
#     def visitIntLit(self, ctx: IntLit, o):
#         return ('Int', o[1])
#
#     def visitFloatLit(self, ctx, o):
#         return ('Float', o[1])
#
#     def visitBoolLit(self, ctx, o):
#         return ('Bool', o[1])
#
#     def visitId(self, ctx, o):
#         if ctx.name not in o[0]:
#             raise UndeclaredIdentifier(ctx.name)
#         for x in o[1]:
#             if ctx.name in x[0]:
#                 return (x[1], o[1])
#         return ('Unknown', o[1])
# from typing import List
#
#
# class Symbol:
#     def __init__(self, name: str, stype: type):
#         self.name = name
#         self.stype = stype
#
#     def setType(self, t: type):
#         self.stype = t
#
#
# class FunctionType:
#     def __init__(self, param: List[Symbol], rtype=None):
#         self.param = param
#         self.rtype = rtype
#
#
# class StaticCheck(Visitor):
#     def look_up(self, name, env):
#         for scope in env:
#             for symbol in scope:
#                 if symbol.name == name:
#                     return symbol
#         raise UndeclaredIdentifier(name)
#
#     def infer(self, symbol, infer_type):
#         if symbol.stype == None:
#             symbol.setType(infer_type)
#         return symbol.stype
#
#     def visitProgram(self, ctx: Program, o):
#         env = [[]]
#         [x.accept(self, env) for x in ctx.decl]
#         [y.accept(self, env) for y in ctx.stmts]
#
#     def visitVarDecl(self, ctx: VarDecl, o):
#         for s in o[0]:
#             if ctx.name == s.name:
#                 raise Redeclared(ctx)
#         sym = Symbol(ctx.name, None)
#         o[0].append(sym)
#         return sym
#
#     def visitFuncDecl(self, ctx: FuncDecl, o):
#         for s in o[0]:
#             if ctx.name == s.name:
#                 raise Redeclared(ctx)
#         cur_env = [[]] + o
#         para = [x.accept(self, cur_env) for x in ctx.param] if ctx.param else []
#         func_sym = Symbol(ctx.name, FunctionType(para))
#         o[0].append(func_sym)
#         cur_env[1] = o[0]
#         [i.accept(self, cur_env) for i in ctx.local]
#         [y.accept(self, cur_env) for y in ctx.stmts]
#         return func_sym
#
#     def visitCallStmt(self, ctx: CallStmt, o):
#         func_sym = self.look_up(ctx.name, o)
#         if type(func_sym.stype) != FunctionType:
#             raise UndeclaredIdentifier(ctx.name)
#         param_sym_list = func_sym.stype.param
#         if len(param_sym_list) != len(ctx.args):
#             raise TypeMismatchInStatement(ctx)
#         for param_sym, arg_expr in zip(param_sym_list, ctx.args):
#             ptype = param_sym.stype
#             atype = arg_expr.accept(self, o)
#             if atype == ptype == None:
#                 raise TypeCannotBeInferred(ctx)
#             if atype == None:
#                 arg_sym = self.look_up(arg_expr.name, o)
#                 atype = self.infer(arg_sym, ptype)
#             if ptype == None:
#                 param_sym.setType(atype)
#                 ptype = param_sym.stype
#             if atype != ptype:
#                 raise TypeMismatchInStatement(ctx)
#
#     def visitAssign(self, ctx: Assign, o):
#         lhs = ctx.lhs.accept(self, o)
#         rhs = ctx.rhs.accept(self, o)
#         if lhs == rhs == None:
#             raise TypeCannotBeInferred(ctx)
#         if lhs == None:
#             symbol = self.look_up(ctx.lhs.name, o)
#             lhs = self.infer(symbol, rhs)
#         if rhs == None:
#             symbol = self.look_up(ctx.rhs.name, o)
#             rhs = self.infer(symbol, lhs)
#         if lhs != rhs:
#             raise TypeMismatchInStatement(ctx)
#
#     def visitIntLit(self, ctx: IntLit, o):
#         return int
#
#     def visitFloatLit(self, ctx, o):
#         return float
#
#     def visitBoolLit(self, ctx, o):
#         return bool
#
#     def visitId(self, ctx, o):
#         return self.look_up(ctx.name, o).stype


# def visitIntLiteral(self, ctx, o):
#     return self.emit.emitPUSHICONST(ctx.value, o.frame), IntType()
#
#
# def visitFloatLiteral(self, ctx, o):
#     return self.emit.emitPUSHFCONST(ctx.value, o.frame), FloatType()
#
#
# def visitBinExpr(self, ctx, o):
#     e1, e1_typ = self.visit(ctx.e1, o)
#     e2, e2_typ = self.visit(ctx.e2, o)
#     if ctx.op in ['+', '-']:
#         return e1 + e2 + self.emit.emitADDOP(ctx.op, IntType(), o.frame), IntType()
#     if ctx.op in ['+.', '-.']:
#         return e1 + e2 + self.emit.emitADDOP(ctx.op[0], FloatType(), o.frame), FloatType()
#     if ctx.op in ['*', '/']:
#         return e1 + e2 + self.emit.emitMULOP(ctx.op, IntType(), o.frame), IntType()
#     if ctx.op in ['*.', '/.']:
#         return e1 + e2 + self.emit.emitMULOP(ctx.op[0], FloatType(), o.frame), FloatType()
#
#
# def visitId(self, ctx, o):
#     for x in o.sym:
#         if ctx.name == x.name:
#             if isinstance(x.value.value, int):
#                 return self.emit.emitREADVAR(x.name, x.mtype, x.value.value, o.frame), x.mtype
#             return self.emit.emitGETSTATIC(x.value.value + "/" + ctx.name, x.mtype, o.frame), x.mtype
#
#
# def visitBinExpr(self, ctx, o):
#     e1, e1_typ = ctx.e1.accept(self, o)
#     e2, e2_typ = ctx.e2.accept(self, o)
#     ret_typ = IntType() if isinstance(e1_typ, IntType) and isinstance(e2_typ, IntType) else FloatType()
#     if isinstance(ret_typ, FloatType) or ctx.op == '/':
#         if isinstance(e1_typ, IntType):
#             e1 = e1 + self.emit.emitI2F(o.frame)
#         if isinstance(e2_typ, IntType):
#             e2 = e2 + self.emit.emitI2F(o.frame)
#         ret_typ = FloatType()
#     if ctx.op in ['+', '-']:
#         return e1 + e2 + self.emit.emitADDOP(ctx.op, ret_typ, o.frame), ret_typ
#     elif ctx.op in ['*']:
#         return e1 + e2 + self.emit.emitMULOP(ctx.op, ret_typ, o.frame), ret_typ
#     elif ctx.op == '/':
#         return e1 + e2 + self.emit.emitMULOP(ctx.op, ret_typ, o.frame), FloatType()
#     elif ctx.op in ['>', '<', '>=', '<=', '!=', '==']:
#         return e1 + e2 + self.emit.emitREOP(ctx.op, ret_typ, o.frame), BoolType()
#
#
# # seq
# def visitVarDecl(self, ctx, o):
#     frame = o.frame
#     name = ctx.name
#     typ = ctx.typ
#     if o.frame:
#         idx = frame.getNewIndex()
#         self.emit.printout(self.emit.emitVAR(idx, name, typ, frame.getStartLabel(), frame.getEndLabel()))
#         return Symbol(name, typ, Index(idx))
#     self.emit.printout(self.emit.emitATTRIBUTE(ctx.name, ctx.typ, False, ""))
#     return Symbol(ctx.name, ctx.typ, CName(self.className))
#
#
# def visitId(self, ctx, o):
#     for x in o.sym:
#         if ctx.name == x.name:
#             if isinstance(x.value.value, int):  # local
#                 if o.isLeft:
#                     return self.emit.emitWRITEVAR(x.name, x.mtype, x.value.value, o.frame), x.mtype
#                 else:
#                     return self.emit.emitREADVAR(x.name, x.mtype, x.value.value, o.frame), x.mtype
#             else:
#                 if o.isLeft:
#                     return self.emit.emitPUTSTATIC(x.value.value + "/" + x.name, x.mtype, o.frame), x.mtype
#                 else:
#                     return self.emit.emitGETSTATIC(x.value.value + "/" + x.name, x.mtype, o.frame), x.mtype
#
#
# def visitAssign(self, ctx, o):
#     rhs_code, rhs_typ = ctx.rhs.accept(self, Access(o.frame, o.sym, False))
#     lhs_code, lhs_typ = ctx.lhs.accept(self, Access(o.frame, o.sym, True))
#     self.emit.printout(rhs_code + lhs_code)
#
#
# def visitIf(self, ctx, o):
#     exp_code, exp_typ = ctx.expr.accept(self, Access(o.frame, o.sym, False))
#     self.emit.printout(exp_code)
#     if ctx.estmt:
#         falseLabel = o.frame.getNewLabel()
#         endLabel = o.frame.getNewLabel()
#         self.emit.printout(self.emit.emitIFFALSE(falseLabel, o.frame))
#         ctx.tstmt.accept(self, o)
#         self.emit.printout(self.emit.emitGOTO(endLabel, o.frame))
#         self.emit.printout(self.emit.emitLABEL(falseLabel, o.frame))
#         ctx.estmt.accept(self, o)
#         self.emit.printout(self.emit.emitLABEL(endLabel, o.frame))
#     else:
#         endLabel = o.frame.getNewLabel()
#         self.emit.printout(self.emit.emitIFFALSE(endLabel, o.frame))
#         ctx.tstmt.accept(self, o)
#         self.emit.printout(self.emit.emitLABEL(endLabel, o.frame))
#
#
# def visitWhile(self, ctx, o):
#     o.frame.enterLoop()
#     con_label = o.frame.getContinueLabel()
#     break_label = o.frame.getBreakLabel()
#     self.emit.printout(self.emit.emitLABEL(con_label, o.frame))
#     exp_code, exp_typ = ctx.expr.accept(self, Access(o.frame, o.sym, False))
#     self.emit.printout(exp_code)
#     self.emit.printout(self.emit.emitIFFALSE(break_label, o.frame))
#     ctx.stmt.accept(self, o)
#     self.emit.printout(self.emit.emitGOTO(con_label, o.frame))
#     self.emit.printout(self.emit.emitLABEL(break_label, o.frame))
#     o.frame.exitLoop()


# def visitFuncDecl(self, ctx, o):
#     frame = Frame(ctx.name, ctx.returnType)
#     intype = list(map(lambda x: x.typ, ctx.param))
#     self.emit.printout(self.emit.emitMETHOD(ctx.name, MType(intype, ctx.returnType), True))
#     frame.enterScope(True)
#     [x.accept(self, SubBody(frame, o.sym)) for x in ctx.param + ctx.body[0]]
#     self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
#     [x.accept(self, SubBody(frame, o.sym)) for x in ctx.body[1]]
#     self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
#     self.emit.printout(self.emit.emitENDMETHOD(frame))
#     frame.exitScope()
#     return Symbol(ctx.name, MType([], ctx.returnType), CName(self.className))




