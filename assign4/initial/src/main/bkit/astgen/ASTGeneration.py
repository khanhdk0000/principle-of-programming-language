from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *
from functools import reduce


class ASTGeneration(BKITVisitor):
    # Program
    def visitProgram(self, ctx: BKITParser.ProgramContext):
        decl = []
        if ctx.global_decl():
            decl = ctx.global_decl().accept(self) + ctx.func_decl_part().accept(self)
        else:
            decl = ctx.func_decl_part().accept(self)
        return Program(decl)

    # Global declaration part
    def visitGlobal_decl(self, ctx: BKITParser.Global_declContext):
        return reduce(lambda x, y: x + y.accept(self), ctx.var_decl(), [])

    # Variable declaration that returns variable list
    def visitVar_decl(self, ctx: BKITParser.Var_declContext):
        return ctx.var_list().accept(self)

    # Variable list returns actual variable
    def visitVar_list(self, ctx: BKITParser.Var_listContext):
        return list(map(lambda x: x.accept(self), ctx.var()))

    # The variable
    def visitVar(self, ctx: BKITParser.VarContext):
        if ctx.scalar():
            return VarDecl(ctx.scalar().accept(self), [],
                           ctx.literal().accept(self)) if ctx.literal() else VarDecl(
                ctx.scalar().accept(self), [], None)
        else:
            var = ctx.composite().accept(self)
            return VarDecl(var[0], var[1], ctx.literal().accept(self)) if ctx.literal() else VarDecl(
                var[0], var[1], None)

    # The scalar type
    def visitScalar(self, ctx: BKITParser.ScalarContext):
        return Id(ctx.ID().getText())

    # # The value of scalar variable
    # def visitScalar_value(self, ctx: BKITParser.Scalar_valueContext):
    #     if ctx.INTLIT():
    #         if ctx.INTLIT().getText()[:2] in ['0x', '0X']:
    #             return IntLiteral(int(ctx.INTLIT().getText(), 16))
    #         elif ctx.INTLIT().getText()[:2] in ['0o', '0O']:
    #             return IntLiteral(int(ctx.INTLIT().getText(), 8))
    #         else:
    #             return IntLiteral(int(ctx.INTLIT().getText()))
    #     elif ctx.FLOATLIT():
    #         return FloatLiteral(float(ctx.FLOATLIT().getText()))
    #     elif ctx.booleanlit():
    #         return ctx.booleanlit().accept(self)
    #     else:
    #         return StringLiteral(ctx.STRINGLIT().getText())

    # The composite variable
    def visitComposite(self, ctx: BKITParser.CompositeContext):
        return [Id(ctx.ID().getText()), list(map(lambda x: x.accept(self), ctx.dimension()))]

    # Value for composite value
    # def visitComposite_value(self, ctx: BKITParser.Composite_valueContext):
    #     return ctx.arraylit().accept(self)

    # Array literal
    def visitArraylit(self, ctx: BKITParser.ArraylitContext):
        return ArrayLiteral(list(map(lambda x: x.accept(self), ctx.literal())))

    # Literal
    def visitLiteral(self, ctx: BKITParser.LiteralContext):
        if ctx.INTLIT():
            if ctx.INTLIT().getText()[:2] in ['0x', '0X']:
                return IntLiteral(int(ctx.INTLIT().getText(), 16))
            elif ctx.INTLIT().getText()[:2] in ['0o', '0O']:
                return IntLiteral(int(ctx.INTLIT().getText(), 8))
            else:
                return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.booleanlit():
            return ctx.booleanlit().accept(self)
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        else:
            return ctx.arraylit().accept(self)

    # Boolean Literal
    def visitBooleanlit(self, ctx: BKITParser.BooleanlitContext):
        return BooleanLiteral(True if ctx.TRUE() else False)

    # The dimension of index variable
    def visitDimension(self, ctx: BKITParser.DimensionContext):
        return int(ctx.INTLIT().getText())

    # The function declaration part
    def visitFunc_decl_part(self, ctx: BKITParser.Func_decl_partContext):
        return list(map(lambda x: x.accept(self), ctx.func_decl())) if ctx.func_decl() else []

    # Function declaration
    def visitFunc_decl(self, ctx: BKITParser.Func_declContext):
        return FuncDecl(Id(ctx.ID().getText()), ctx.para_decl().accept(self),
                        ctx.body().accept(self)) if ctx.para_decl() else FuncDecl(Id(ctx.ID().getText()), [],
                                                                                  ctx.body().accept(self))

    # Parameter declaration of function declaration
    def visitPara_decl(self, ctx: BKITParser.Para_declContext):
        return ctx.para_list().accept(self)

    # The parameter list
    def visitPara_list(self, ctx: BKITParser.Para_listContext):
        return list(map(lambda x: x.accept(self), ctx.para()))

    # The parameter
    def visitPara(self, ctx: BKITParser.ParaContext):
        if ctx.scalar():
            return VarDecl(ctx.scalar().accept(self), [], None)
        else:
            var = ctx.composite().accept(self)
            return VarDecl(var[0], var[1], None)

    # The body of the function
    def visitBody(self, ctx: BKITParser.BodyContext):
        return ctx.stmt_list().accept(self)

    # The statement list
    def visitStmt_list(self, ctx: BKITParser.Stmt_listContext):
        if ctx.var_decl() and ctx.stmt():
            return reduce(lambda x, y: x + y.accept(self), ctx.var_decl(), []), \
                   list(map(lambda x: x.accept(self), ctx.stmt()))
        elif ctx.var_decl():
            return reduce(lambda x, y: x + y.accept(self), ctx.var_decl(), []), []
        elif ctx.stmt():
            return [], list(map(lambda x: x.accept(self), ctx.stmt()))
        else:
            return [], []

    # The statement
    def visitStmt(self, ctx: BKITParser.StmtContext):
        return ctx.getChild(0).accept(self)

    # Expression
    def visitExpr(self, ctx: BKITParser.ExprContext):
        return BinaryOp(ctx.relational_operator().accept(self), ctx.expr1(0).accept(self),
                        ctx.expr1(1).accept(self)) if ctx.relational_operator() else ctx.expr1(0).accept(self)

    # Relational operator
    def visitRelational_operator(self, ctx: BKITParser.Relational_operatorContext):
        return ctx.getChild(0).getText()

    # Expression 1
    def visitExpr1(self, ctx: BKITParser.Expr1Context):
        return BinaryOp(ctx.logical_operator().accept(self), ctx.expr1().accept(self),
                        ctx.expr2().accept(self)) if ctx.logical_operator() else ctx.expr2().accept(self)

    # Logical operator
    def visitLogical_operator(self, ctx: BKITParser.Logical_operatorContext):
        return ctx.getChild(0).getText()

    # Expression 2
    def visitExpr2(self, ctx: BKITParser.Expr2Context):
        return BinaryOp(ctx.adding_operator().accept(self), ctx.expr2().accept(self),
                        ctx.expr3().accept(self)) if ctx.adding_operator() else ctx.expr3().accept(self)

    # Adding operator
    def visitAdding_operator(self, ctx: BKITParser.Adding_operatorContext):
        return ctx.getChild(0).getText()

    # Expression 3
    def visitExpr3(self, ctx: BKITParser.Expr3Context):
        return BinaryOp(ctx.multiplying_operator().accept(self), ctx.expr3().accept(self),
                        ctx.expr4().accept(self)) if ctx.multiplying_operator() else ctx.expr4().accept(self)

    # Multiplying operator
    def visitMultiplying_operator(self, ctx: BKITParser.Multiplying_operatorContext):
        return ctx.getChild(0).getText()

    # Expression 4
    def visitExpr4(self, ctx: BKITParser.Expr4Context):
        return UnaryOp(ctx.NEGATE().getText(), ctx.expr4().accept(self)) if ctx.NEGATE() else ctx.expr5().accept(self)

    # Expression 5
    def visitExpr5(self, ctx: BKITParser.Expr5Context):
        return UnaryOp(ctx.sign_operator().getText(),
                       ctx.expr5().accept(self)) if ctx.sign_operator() else ctx.expr6().accept(self)

    # Sign operator
    def visitSign_operator(self, ctx: BKITParser.Sign_operatorContext):
        return ctx.getChild(0).getText()

    # Expression 6
    def visitExpr6(self, ctx: BKITParser.Expr6Context):
        return ArrayCell(ctx.expr6().accept(self),
                         ctx.index_operator().accept(self)) if ctx.index_operator() else ctx.expr7().accept(self)

    # Index operator
    def visitIndex_operator(self, ctx: BKITParser.Index_operatorContext):
        return list(map(lambda x: x.accept(self), ctx.expr()))

    # Expression 7
    def visitExpr7(self, ctx: BKITParser.Expr7Context):
        if ctx.expr():
            return ctx.expr().accept(self)
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.function_call():
            return ctx.function_call().accept(self)
        elif ctx.literal():
            return ctx.literal().accept(self)

    # Index expression
    def visitIndex_expr(self, ctx: BKITParser.Index_operatorContext):
        return [ctx.expr7().accept(self), ctx.index_operator().accept(self)]

    # Function call
    def visitFunction_call(self, ctx: BKITParser.Function_callContext):
        return CallExpr(Id(ctx.ID().getText()), ctx.expr_list().accept(self)) if ctx.expr_list() else CallExpr(
            Id(ctx.ID().getText()), [])

    # Expression list
    def visitExpr_list(self, ctx: BKITParser.Expr_listContext):
        return list(map(lambda x: x.accept(self), ctx.expr()))

    # Assign statement
    def visitAssign_stmt(self, ctx: BKITParser.Assign_stmtContext):
        lhs = ctx.scalar().accept(self) if ctx.scalar() else ArrayCell(ctx.index_expr().accept(self)[0],
                                                                                      ctx.index_expr().accept(self)[1])
        return Assign(lhs, ctx.expr().accept(self))

    # If Statement
    def visitIf_stmt(self, ctx: BKITParser.If_stmtContext):
        return If(ctx.if_then_stmt().accept(self), ctx.else_stmt().accept(self))

    # The if then part of if statement
    def visitIf_then_stmt(self, ctx: BKITParser.If_then_stmtContext):
        return list(
            map(lambda x, y: (x.accept(self), y.accept(self)[0], y.accept(self)[1]), ctx.expr(), ctx.stmt_list()))

    # The else part of if statement
    def visitElse_stmt(self, ctx: BKITParser.Else_stmtContext):
        return (ctx.stmt_list().accept(self)[0], ctx.stmt_list().accept(self)[1]) if ctx.stmt_list() else ([], [])

    # The for statement
    def visitFor_stmt(self, ctx: BKITParser.For_stmtContext):
        return For(ctx.scalar().accept(self), ctx.expr(0).accept(self), ctx.expr(1).accept(self),
                   ctx.expr(2).accept(self), ctx.stmt_list().accept(self))

    # The while statement
    def visitWhile_stmt(self, ctx: BKITParser.While_stmtContext):
        return While(ctx.expr().accept(self), ctx.stmt_list().accept(self))

    # The do while statement
    def visitDo_while_stmt(self, ctx: BKITParser.Do_while_stmtContext):
        return Dowhile(ctx.stmt_list().accept(self), ctx.expr().accept(self))

    # The break statement
    def visitBreak_stmt(self, ctx: BKITParser.Break_stmtContext):
        return Break()

    # The continue statement
    def visitContinue_stmt(self, ctx: BKITParser.Continue_stmtContext):
        return Continue()

    # The call statement
    def visitCall_stmt(self, ctx: BKITParser.Call_stmtContext):
        return CallStmt(ctx.function_call().accept(self).method, ctx.function_call().accept(self).param)

    # The return statement
    def visitReturn_stmt(self, ctx: BKITParser.Return_stmtContext):
        return Return(ctx.expr().accept(self) if ctx.expr() else None)

