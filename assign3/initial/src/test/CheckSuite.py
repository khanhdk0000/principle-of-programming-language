import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *


class CheckSuite(unittest.TestCase):

    def test_redeclared_global_variable(self):
        """Redeclared global variable"""
        input = """Var: x;
                    Var: x;
                    """
        expect = str(Redeclared(Variable(), "x"))
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_redeclared_gloal_variable_same_line(self):
        """Redeclared global variable on same line"""
        input = """Var: a,b,c,a;
                    """
        expect = str(Redeclared(Variable(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_redeclared_gloal_variable_int_type(self):
        """Redeclared global int"""
        input = """
            Var: a = 10;
            Var: b = 9;
            Var: c,d;
            Var: a = 17;
            """
        expect = str(Redeclared(Variable(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_redeclared_function(self):
        """Redeclared function"""
        input = """
            Function: main
            Body:
                Var: x;
            EndBody.
            Function: foo
            Body:
                Var: x;
            EndBody.
            Function: foo
            Body:
                Var: x;
            EndBody.
            """
        expect = str(Redeclared(Function(), "foo"))
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_redeclared_parameter(self):
        """Redeclared parameter"""
        input = """
            Function: main
            Parameter: a, b, a
            Body:
                Var: x;
            EndBody.
            """
        expect = str(Redeclared(Parameter(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_redeclared_local_variable(self):
        """Redeclared local variable"""
        input = """
            Function: main
            Body:
                Var: x,y;
                Var: y;
            EndBody.
            """
        expect = str(Redeclared(Variable(), "y"))
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_undeclared_variable(self):
        """Undeclared variable"""
        input = """
            Function: main
            Body:
                x = 10;
            EndBody.
            """
        expect = str(Undeclared(Identifier(), "x"))
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_undeclared_variable_different_function(self):
        """Undeclared variable in different function"""
        input = """
            Function: main
            Body:
                Var: a;
            EndBody.
            Function: foo
            Body:
                a = 789;
            EndBody.
            """
        expect = str(Undeclared(Identifier(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_undeclared_function(self):
        """Simple program: main"""
        input = """Function: main
                   Body:
                        foo();
                   EndBody."""
        expect = str(Undeclared(Function(), "foo"))
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_redeclared_function_with_global(self):
        """Simple program: main"""
        input = """Var: a,b;
        Function: main
        Body:
            Var: x;
        EndBody.
        Function: a
        Body:
            Var: y;
        EndBody.
        """
        expect = str(Redeclared(Function(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_redeclared_para(self):
        """Simple program: main"""
        input = """
        Function: main
        Parameter: a, b, c, a
        Body:
            Var: x;
        EndBody.
        """
        expect = str(Redeclared(Parameter(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_redeclared_variable_with_para(self):
        """Simple program: main"""
        input = """
        Function: main
        Parameter: a, b, c
        Body:
            Var: b;
        EndBody.
        """
        expect = str(Redeclared(Variable(), "b"))
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_call_stmt_wrong_length_para(self):
        """Simple program: main"""
        input = """
        Function: foo
        Parameter: x, y
        Body:
            Var: a;
        EndBody.
        Function: main
        Parameter: a, b, c
        Body:
            foo(a);
        EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id('foo'), [Id('a')])))
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_call_stmt_wrong_para_undeclared(self):
        """Simple program: main"""
        input = """
        Function: foo
        Parameter: x, y
        Body:
            Var: a;
        EndBody.
        Function: main
        Parameter: a, b, c
        Body:
            a = 1;
            foo(a, d);
        EndBody.
        """
        expect = str(Undeclared(Identifier(), "d"))
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_bool_expr(self):
        """Simple program: main"""
        input = """
        Function: main
        Body:
            Var: x = True, y = 9, c;
            c = x && y;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp('&&', Id('x'), Id('y'))))
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_call_stmt_wrong_type(self):
        """Simple program: main"""
        input = """
        Var: x;
        Function: foo
        Parameter: x
        Body:
            x = 1;
        EndBody.
        Function: main
        Body:
            x = 1.5;
            foo(x);
        EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id('foo'), [Id('x')])))
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_diff_numofparam_stmt(self):
        """Complex program"""
        input = """Function: main
                   Body:
                        printStrLn();
                    EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"), [])))
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_call_stmt_wrong_para(self):
        """Complex program"""
        input = """
        Var: x;
        Function: foo
        Body:
            Var: x;
            x = 1.5;
        EndBody.
        Function: main
        Body:
            x = 3;
            foo(x);
        EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id('foo'), [Id('x')])))
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_diff_numofparam_expr(self):
        """More complex program"""
        input = """Function: main
                    Body:
                        printStrLn(read(4));
                    EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"), [IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([FuncDecl(Id("main"), [], ([], [
            CallExpr(Id("foo"), [])]))])
        expect = str(Undeclared(Function(), "foo"))
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_diff_numofparam_expr_use_ast(self):
        """More complex program"""
        input = Program([
            FuncDecl(Id("main"), [], ([], [
                CallStmt(Id("printStrLn"), [
                    CallExpr(Id("read"), [IntLiteral(4)])
                ])]))])
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"), [IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_diff_numofparam_stmt_use_ast(self):
        """Complex program"""
        input = Program([
            FuncDecl(Id("main"), [], ([], [
                CallStmt(Id("printStrLn"), [])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"), [])))
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_bool_expr_or(self):
        """Simple program: main"""
        input = """
        Function: main
        Body:
            Var: x, z, ans;
            x = False;
            z = 9.5;
            ans = x || z;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp('||', Id('x'), Id('z'))))
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_wrong_function_para(self):
        """Simple program: main"""
        input = """
        Function: main
        Body:
            f1(2,2.4);
        EndBody.
        Function: f1
        Parameter: a,b
        Body:
            f1(a,b);
            a = b - 5;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp('-', Id('b'), IntLiteral(5))))
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_no_main_function(self):
        """Simple program: main"""
        input = """
        Function: foo
        Body:
        EndBody.
         """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_undeclared_function_2(self):
        """Simple program: main"""
        input = """
        Var: a[2][2] = {{True, True}, {False, False}};
        Var: f = 1;

        Function: main
        Parameter: p
        Body:
        Var: x = 1, y;
        a[2] = 10;
        EndBody.

        Function: c
        Parameter: p[2][2], a
        Body:
        EndBody.
        """
        expect = str(TypeMismatchInExpression(ArrayCell(Id("a"), [IntLiteral(2)])))
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_undeclared_function_3(self):
        """Simple program: main"""
        input = """
        Var: a[2][2] = {{True, True}, {False, False}};
        Var: f = 1;

        Function: main
        Parameter: p
        Body:
        Var: x = 1, y;
        a[2][2] = 10;
        EndBody.

        Function: c
        Parameter: p[2][2], a
        Body:
        EndBody.
        """
        expect = str(
            TypeMismatchInStatement(Assign(ArrayCell(Id("a"), [IntLiteral(2), IntLiteral(2)]), IntLiteral(10))))
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_undeclared_function_4(self):
        """Simple program: main"""
        input = """
        Var: a[2][2] = {{True, True}, {False, False}};
        Var: f = 1;

        Function: main
        Parameter: p
        Body:
        Var: x = 1, y;
        a[2 + 3][True] = True;
        EndBody.

        Function: c
        Parameter: p[2][2], a
        Body:
        EndBody.
        """
        expect = str(TypeMismatchInExpression(
            ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(2), IntLiteral(3)), BooleanLiteral(True)])))
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_array(self):
        """Simple program: main"""
        input = """
        Var: a[2][2];
        Function: main
        Parameter: p
        Body:
            p = a[2][1] + 5;
            foo(1.2, 3.4);
        EndBody.

        Function: foo
        Parameter: b, c
        Body:
            Var: x, y;
            x = b +. 5.7;
            y = c +. a[1][2];
        EndBody.
        """
        expect = str(
            TypeMismatchInExpression(BinaryOp('+.', Id('c'), ArrayCell(Id('a'), [IntLiteral(1), IntLiteral(2)]))))
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_array_unary(self):
        """Simple program: main"""
        input = """
        Var: a[2][2];
        Function: main
        Parameter: p
        Body:
            p = a[2][1] -. 9.5;
            foo(True, False);
        EndBody.

        Function: foo
        Parameter: b, c
        Body:
            Var: x, y;
            x = b;
            y = !a[1][2];
        EndBody.
        """
        expect = str(
            TypeMismatchInExpression(UnaryOp('!', ArrayCell(Id('a'), [IntLiteral(1), IntLiteral(2)]))))
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_if(self):
        """Simple program: main"""
        input = """
        Var: a[2][2], b = 8.9;
        Function: main
        Parameter: x
        Body:
            Var: b = 5;
            If b + 10 Then
                x = 15;
            EndIf.
        EndBody.
        """
        expect = str(
            TypeMismatchInStatement(
                If([(BinaryOp("+", Id("b"), IntLiteral(10)), [], [Assign(Id("x"), IntLiteral(15))])], ([], []))))
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_if_else(self):
        """Simple program: main"""
        input = """
        Var: a[2][2], b = 8.9;
        Function: main
        Parameter: x
        Body:
            Var: b = 5;
            If b < 10 Then
                x = 15;
            Else
                Var: k = 10.8, res;
                res = k + x;
            EndIf.
        EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp('+', Id('k'), Id('x'))))
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_if_elseif(self):
        """Simple program: main"""
        input = """
        Var: a[2][2], b = 8.9;
        Function: main
        Parameter: x
        Body:
            Var: b = 5;
            If b == 10 Then
                x = 15;
            ElseIf b - 10 Then
                x = 20;
            EndIf.
        EndBody.
        """
        expect = str(TypeMismatchInStatement(If(
            [(BinaryOp("==", Id("b"), IntLiteral(10)), [], [Assign(Id("x"), IntLiteral(15))]),
             (BinaryOp("-", Id("b"), IntLiteral(10)), [], [Assign(Id("x"), IntLiteral(20))])], ([], []))))
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_for(self):
        """Simple program: main"""
        input = """
        Function: main
        Body:
            Var: x, i = 0;
            For(i = 1, i + 10, 1) Do
                x = x + 1;
            EndFor.
        EndBody.
        """
        expect = str(TypeMismatchInStatement(
            For(Id("i"), IntLiteral(1), BinaryOp("+", Id("i"), IntLiteral(10)), IntLiteral(1),
                ([], [Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(1)))]))))
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_for2(self):
        """Simple program: main"""
        input = """
        Function: main
        Body:
            Var: x, i = 0;
            For(i = 1.5, i < 10, 1) Do
                x = x + 1;
            EndFor.
        EndBody.
        """
        expect = str(TypeMismatchInStatement(
            For(Id("i"), FloatLiteral(1.5), BinaryOp("<", Id("i"), IntLiteral(10)), IntLiteral(1),
                ([], [Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(1)))]))))
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_while(self):
        """Simple program: main"""
        input = """
        Function: main
        Parameter: x
        Body:
            Var: a = 7.9;
            x = 0;
            While x - 5 Do
                Var: a;
                x = x + a;
            EndWhile.
        EndBody.
        """
        expect = str(TypeMismatchInStatement(
            While(BinaryOp("-", Id("x"), IntLiteral(5)),
                  ([VarDecl(Id("a"), [], None)], [Assign(Id("x"), BinaryOp("+", Id("x"), Id("a")))]))))
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_do_while(self):
        """Simple program: main"""
        input = """
        Function: main
        Parameter: num
        Body:
            Do
                num = num + 1;
            While num * 100 EndDo.
        EndBody.
        """
        expect = str(TypeMismatchInStatement(
            Dowhile(([], [Assign(Id("num"), BinaryOp("+", Id("num"), IntLiteral(1)))]),
                    BinaryOp("*", Id("num"), IntLiteral(100)))))
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_return(self):
        """Simple program: main"""
        input = """
        Var: a = 10;
        Function: main
        Parameter: p
        Body:
            p = a + foo();
        EndBody.

        Function: foo
        Body:
            Return 12.5;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(FloatLiteral(12.5))))
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_return_up(self):
        """Simple program: main"""
        input = """
        Var: a = 10;
        Function: foo
        Body:
            Return 12.5;
        EndBody.

        Function: main
        Parameter: p
        Body:
            p = a + foo();
        EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp('+', Id('a'), CallExpr(Id("foo"), []))))
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_return3(self):
        """Simple program: main"""
        input = """
        Var: a[2][3] = {{1, 2}, {3, 4}};

        Function: foo
        Body:
            Return a;
        EndBody.

        Function: c
        Parameter: b[2][3]
        Body:
            Return 15.6;
        EndBody.

        Function: main
        Parameter: p
        Body:
            p = 10;
            p = c(foo());
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('p'), CallExpr(Id('c'), [CallExpr(Id('foo'), [])]))))
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_return_function_type_infer_16(self):
        """test return function type inferrence func declaration before"""
        input = """
        Var: a[2][3] = {{1, 2}, {3, 4}};

        Function: foo
        Body:
        Var: b[2][3];
        b[2][3] = 12.5;
            Return b;
        EndBody.

        Function: main
        Parameter: p
        Body:
        p = 10;
        p = 10 + foo()[2][3];
        EndBody.
        """
        expect = str(TypeMismatchInExpression(
            BinaryOp('+', IntLiteral(10), ArrayCell(CallExpr(Id('foo'), []), [IntLiteral(2), IntLiteral(3)]))))
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_shit(self):
        """Simple program: main"""
        input = Program(
            [
                FuncDecl(
                    Id('main'),
                    [],
                    ([VarDecl(Id('x'), [1], ArrayLiteral([IntLiteral(0)]))],
                     [Assign(ArrayCell(Id('x'), [IntLiteral(0)]), FloatLiteral(0))]),
                )
            ]
        )
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('x'), [IntLiteral(0)]), FloatLiteral(0))))
        self.assertTrue(TestChecker.test(input, expect, 500))
