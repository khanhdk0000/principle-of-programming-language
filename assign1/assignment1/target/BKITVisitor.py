# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#global_decl.
    def visitGlobal_decl(self, ctx:BKITParser.Global_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_decl.
    def visitVar_decl(self, ctx:BKITParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_list.
    def visitVar_list(self, ctx:BKITParser.Var_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var.
    def visitVar(self, ctx:BKITParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#scalar.
    def visitScalar(self, ctx:BKITParser.ScalarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#scalar_value.
    def visitScalar_value(self, ctx:BKITParser.Scalar_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#composite.
    def visitComposite(self, ctx:BKITParser.CompositeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#composite_value.
    def visitComposite_value(self, ctx:BKITParser.Composite_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#literal.
    def visitLiteral(self, ctx:BKITParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#arraylit.
    def visitArraylit(self, ctx:BKITParser.ArraylitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_decl_part.
    def visitFunc_decl_part(self, ctx:BKITParser.Func_decl_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_decl.
    def visitFunc_decl(self, ctx:BKITParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#para_decl.
    def visitPara_decl(self, ctx:BKITParser.Para_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#para_list.
    def visitPara_list(self, ctx:BKITParser.Para_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#para.
    def visitPara(self, ctx:BKITParser.ParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#body.
    def visitBody(self, ctx:BKITParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#dimension.
    def visitDimension(self, ctx:BKITParser.DimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr.
    def visitExpr(self, ctx:BKITParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr1.
    def visitExpr1(self, ctx:BKITParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr2.
    def visitExpr2(self, ctx:BKITParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr3.
    def visitExpr3(self, ctx:BKITParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr4.
    def visitExpr4(self, ctx:BKITParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr5.
    def visitExpr5(self, ctx:BKITParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr6.
    def visitExpr6(self, ctx:BKITParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr7.
    def visitExpr7(self, ctx:BKITParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#relational_operator.
    def visitRelational_operator(self, ctx:BKITParser.Relational_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#logical_operator.
    def visitLogical_operator(self, ctx:BKITParser.Logical_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#adding_operator.
    def visitAdding_operator(self, ctx:BKITParser.Adding_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#multiplying_operator.
    def visitMultiplying_operator(self, ctx:BKITParser.Multiplying_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#sign_operator.
    def visitSign_operator(self, ctx:BKITParser.Sign_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#index_operator.
    def visitIndex_operator(self, ctx:BKITParser.Index_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#function_call.
    def visitFunction_call(self, ctx:BKITParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr_list.
    def visitExpr_list(self, ctx:BKITParser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stmt_list.
    def visitStmt_list(self, ctx:BKITParser.Stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stmt.
    def visitStmt(self, ctx:BKITParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#index_expr.
    def visitIndex_expr(self, ctx:BKITParser.Index_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assign_stmt.
    def visitAssign_stmt(self, ctx:BKITParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#if_stmt.
    def visitIf_stmt(self, ctx:BKITParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#if_then_stmt.
    def visitIf_then_stmt(self, ctx:BKITParser.If_then_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#else_stmt.
    def visitElse_stmt(self, ctx:BKITParser.Else_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#for_stmt.
    def visitFor_stmt(self, ctx:BKITParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#while_stmt.
    def visitWhile_stmt(self, ctx:BKITParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#do_while_stmt.
    def visitDo_while_stmt(self, ctx:BKITParser.Do_while_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#break_stmt.
    def visitBreak_stmt(self, ctx:BKITParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#continue_stmt.
    def visitContinue_stmt(self, ctx:BKITParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#call_stmt.
    def visitCall_stmt(self, ctx:BKITParser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#return_stmt.
    def visitReturn_stmt(self, ctx:BKITParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#booleanlit.
    def visitBooleanlit(self, ctx:BKITParser.BooleanlitContext):
        return self.visitChildren(ctx)



del BKITParser