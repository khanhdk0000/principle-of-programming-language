import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *


class CheckSuite(unittest.TestCase):

    def test_redeclared_global_variable(self):
        """Redeclared global variable"""
        input = """Var: x;
                    Var: x;
            Function: main
            Body:
            EndBody.
                    """
        expect = str(Redeclared(Variable(), "x"))
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_redeclared_gloal_variable_same_line(self):
        """Redeclared global variable on same line"""
        input = """Var: a,b,c,a;
            Function: main
            Body:
            EndBody.
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
            Function: main
            Body:
            EndBody.
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

    def test_do_while_condition(self):
        """test return function type inferrence func declaration before"""
        input = """
        Function: main
        Body:
            Var: x;
        Do
            x = 1;
        While x EndDo.
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Dowhile(([], [Assign(Id("x"), IntLiteral(1))]), Id("x"))))
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_array_para(self):
        """test return function type inferrence func declaration before"""
        input = """
        Function: main
        Body:
            Var: x = 15;
            foo(x);
        EndBody.
        Function: foo
        Parameter: a[2][3]
        Body:
            Return True;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id('foo'), [Id('x')])))
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_array_assign_type(self):
        """test return function type inference func declaration before"""
        input = """
        Var: a[1] = {0};

        Function: foo
        Parameter: x
        Body:
            Return a;
        EndBody.

        Function: main
        Body:
            foo(0)[0] = foo(0.0)[0];
        EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id('foo'), [FloatLiteral(0.0)])))
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_many_return(self):
        """"""
        input = """
        Function: main
        Body:
            Var: x = 10;
            If x > 10 Then
                Return 1;
            ElseIf x == 10 Then
                Return 0;
            Else
                Return True;
            EndIf.
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_function_assign_declared_below(self):
        """test return function type inferrence func declaration before"""
        input = """
        Function: main
        Body:
            Var: x = 5, y;
            y = foo(x);
        EndBody.

        Function: foo
        Parameter: a
        Body:
            Return a * 5;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(Id('y'), CallExpr(Id('foo'), [Id('x')]))))
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_for_infer_type(self):
        """test return function type inference func declaration before"""
        input = """
        Function: main
        Body:
            Var: i,x,z;
            x = i -. 10.5;
            For(i = 0, i < 10, 1) Do
                z = z + 1;
            EndFor.
        EndBody.
        """
        expect = str(TypeMismatchInStatement(
            For(Id("i"), IntLiteral(0), BinaryOp("<", Id("i"), IntLiteral(10)), IntLiteral(1),
                ([], [Assign(Id("z"), BinaryOp("+", Id("z"), IntLiteral(1)))]))))
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_for_bool(self):
        """test return function type inference func declaration before"""
        input = """
        Function: main
        Body:
            Var: i,x,z;
            x = i -. 10.5;
            For(i = 0, i + 10, 1) Do
                z = z + 1;
            EndFor.
        EndBody.
        """
        expect = str(TypeMismatchInStatement(
            For(Id("i"), IntLiteral(0), BinaryOp("+", Id("i"), IntLiteral(10)), IntLiteral(1),
                ([], [Assign(Id("z"), BinaryOp("+", Id("z"), IntLiteral(1)))]))))
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_return_wrong_type(self):
        """test return function type inference func declaration before"""
        input = """
        Function: main
        Body:
            Var: x;
            x = x + foo();
        EndBody.

        Function: foo
        Body:
            Return "string";
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(StringLiteral('string'))))
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_type(self):
        """Simple program: main"""
        input = """
        Function: main
        Parameter: x, y ,z
        Body:
            y = x || (x>z);
        EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp('>', Id('x'), Id('z'))))
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_if_unknown(self):
        """Simple program: main"""
        input = """
        Var: a[2][2] = {{1,2},{3,4}};
        Function: main
        Body:
            Var: r, b;
            If foo(10) Then
                r = r + a[1][1];
            Else
                Return True;
            EndIf.
        EndBody.

        Function: foo
        Parameter: x
        Body:
            If x % 2 == 0 Then
                Return x + 1;
            Else
                Return x + 2;
            EndIf.
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(BinaryOp('+', Id('x'), IntLiteral(1)))))
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_for_unknown(self):
        """Simple program: main"""
        input = """
        Var: a[2][2] = {{1.5,2.3},{3.9,4.7}};
        Function: main
        Body:
            foo(a[0][1]);
        EndBody.

        Function: foo
        Parameter: x
        Body:
            Var: ans = 0,i;
            For(i = x, i < 10, 1) Do
                ans = ans * 2;
            EndFor.
            Return ans;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(
            For(Id("i"), Id("x"), BinaryOp("<", Id("i"), IntLiteral(10)), IntLiteral(1),
                ([], [Assign(Id("ans"), BinaryOp("*", Id("ans"), IntLiteral(2)))]))))
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_return_type(self):
        """Simple program: main"""
        input = """
        Var: a[2][2] = {{1,2},{3,4}};
        Function: main
        Body:
            foo(a[0][1]);
        EndBody.

        Function: foo
        Parameter: x
        Body:
            Var: ans = 0,i;
            For(i = x, i < 10, 1) Do
                ans = ans * 2;
            EndFor.
            Return ans;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(Id('ans'))))
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_for_infer_third_expr(self):
        """Simple program: main"""
        input = """
        Var: a[2][2] = {{1,2},{3,4}};
        Function: main
        Body:
            Var: i, a, b;
            For(i = a, i != 100, b) Do
                printStrLn("correct");
            EndFor.
            foo(a,b);
        EndBody.

        Function: foo
        Parameter: x, y
        Body:
            x = x + 1;
            y = y -. 5.7;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp('-.', Id('y'), FloatLiteral(5.7))))
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_for_infer_bool_expr(self):
        """Simple program: main"""
        input = """
        Var: a[2][2] = {{1,2},{3,4}};
        Function: main
        Body:
            Var: i, a, b;
            For(i = a, b, 1) Do
                printStrLn("correct");
            EndFor.
            foo(a,b);
        EndBody.

        Function: foo
        Parameter: x, y
        Body:
            y = x == 10;
            x = False;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('x'), BooleanLiteral(False))))
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_while_infer(self):
        """Simple program: main"""
        input = """
        Var: a[2][2] = {{1,2},{3,4}};
        Function: main
        Body:
            Var: i, a, b;
            While i Do
                printStrLn("correct");
            EndWhile.
            a = foo(i) + 15;
        EndBody.

        Function: foo
        Parameter: x
        Body:
            Var: y;
            y = (x + 5) * 4;
            Return y;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp('+', Id('x'), IntLiteral(5))))
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_do_while_infer(self):
        """Simple program: main"""
        input = """
        Var: a[2][2] = {{1,2},{3,4}};
        Function: main
        Body:
            Var: x;
            Do
                x = 1;
            While x EndDo.
        EndBody.

        """
        expect = str(TypeMismatchInStatement(Dowhile(([], [Assign(Id("x"), IntLiteral(1))]), Id("x"))))
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_array_assign_type_before(self):
        """test return function type inference func declaration before"""
        input = """
        Var: a[1] = {0};

        Function: main
        Body:
            foo(0)[0] = foo(0.0)[0];
        EndBody.

        Function: foo
        Parameter: x
        Body:
            Return a;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(ArrayCell(CallExpr(Id('foo'), [IntLiteral(0)]), [IntLiteral(0)]),
                                                 ArrayCell(CallExpr(Id('foo'), [FloatLiteral(0.0)]), [IntLiteral(0)]))))
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_for_type_61(self):
        """test for statement in complex form"""
        input = """
        Var: x;

        Function: main
        Parameter: x
        Body:
            If True Then
                If True Then
                    main(10.5);
                    x = 120;
                EndIf.
            EndIf.
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('x'), IntLiteral(120))))
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_type1(self):
        """Simple program: main"""
        input = """
        Var: a = 1, b[5];
        Function: main
        Body:
            a = b;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('a'), Id('b'))))
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_infer_type(self):
        """Simple program: main"""
        input = """
        Function: main
        Parameter: x
        Body:
            If main(main(5)) Then EndIf.
        EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id('main'), [IntLiteral(5)])))
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_infer_type2(self):
        """Simple program: main"""
        input = """
        Function: main
        Parameter: a, x
        Body:
            Var: y = 1;
            y = a + foo(x);
        EndBody.

        Function: foo
        Parameter: x
        Body:
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(Id('y'), BinaryOp('+', Id('a'), CallExpr(Id('foo'), [Id('x')])))))
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_infer_type3(self):
        """Simple program: main"""
        input = """
        Function: main
        Parameter: a,b,c
        Body:
            Var: d, e;
            e = main(b, main(d, c, a), a + d);
            e = 3.0;
            Return 3;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(Id('e'), CallExpr(Id('main'), [Id('b'), CallExpr(Id('main'),
                                                                                                  [Id('d'), Id('c'),
                                                                                                   Id('a')]),
                                                                                BinaryOp('+', Id('a'), Id('d'))]))))
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_undeclared(self):
        """Simple program: main"""
        input = """
        Function: main
        Body:
            Var: a;
            a = foo;
        EndBody.

        Function: foo
        Parameter: x
        Body:
            Return x + 10;
        EndBody.
        """
        expect = str(Undeclared(Identifier(), 'foo'))
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_array_para2(self):
        """Simple program: main"""
        input = """
                Var: x[2] = {True, False};
                Function: main
                Parameter: a[2]
                Body:
                    main(x);
                    a[0] = 1;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('a'), [IntLiteral(0)]), IntLiteral(1))))
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_infer_para(self):
        """Simple program: main"""
        input = """
                Var: a[2];
                Function: main
                Parameter: x
                Body:
                    If a[a[0]] Then EndIf.
                EndBody.
                """
        expect = str(TypeMismatchInExpression(ArrayCell(Id('a'), [ArrayCell(Id('a'), [IntLiteral(0)])])))
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_array_para3(self):
        """Simple program: main"""
        input = """
        Var: arr[3] = {"game", "play", "witcher"};
        Function: main
        Body:
            Var: res;
            res = !foo(arr);
        EndBody.
        
        Function: foo
        Parameter: a[3]
        Body:
            a[1] = True;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('a'), [IntLiteral(1)]), BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_same_name(self):
        """Simple program: main"""
        input = """
                Function: main
                Body:
                    Var: foo = 0;
                    foo = foo + foo();
                EndBody.
                Function: foo
                Body:
                    Return True;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Return(BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input, expect, 467))

    # def test_shit(self):
    #     """Simple program: main"""
    #     input = """
    #     Function: main
    #     Body:
    #         Var: x = 15;
    #         foo(x);
    #     EndBody.
    #     Function: foo
    #     Parameter: a[2][3]
    #     Body:
    #         Return True;
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInExpression(ArrayCell(Id('a'), [ArrayCell(Id('a'), [IntLiteral(0)])])))
    #     self.assertTrue(TestChecker.test(input, expect, 500))

    # ################################################

    # tham
    # # 1
    # def test_undeclared_var_1(self):
    #     """test undeclared var c in function main"""
    #     input = """
    #        Var: a[2] = {1, 2};
    #        Var: f = 12.5;
    #
    #        Function: main
    #        Parameter: p
    #        Body:
    #            c = 10;
    #        EndBody.
    #        """
    #     expect = str(Undeclared(Identifier(), "c"))
    #     self.assertTrue(TestChecker.test(input, expect, 401))
    #
    # # 2
    # def test_undeclared_var_2(self):
    #     """test undeclared var c in function main in distinguish with function"""
    #     input = """
    #        Var: a[2] = {1, 2};
    #        Var: f = 12.5;
    #
    #        Function: c
    #        Parameter: d
    #        Body:
    #        EndBody.
    #
    #        Function: main
    #        Parameter: p
    #        Body:
    #            c = 10;
    #        EndBody.
    #        """
    #     expect = str(Undeclared(Identifier(), "c"))
    #     self.assertTrue(TestChecker.test(input, expect, 402))
    #
    # # 3
    # def test_undeclared_function_3(self):
    #     """test undeclared function b called in function main"""
    #     input = """
    #        Var: a[2] = {1, 2};
    #        Var: f = 12.5;
    #
    #        Function: main
    #        Parameter: p
    #        Body:
    #            b();
    #        EndBody.
    #        """
    #     expect = str(Undeclared(Function(), "b"))
    #     self.assertTrue(TestChecker.test(input, expect, 403))
    #
    # # 4
    # def test_undeclared_function_4(self):
    #     """test undeclared function b called in function main in distinguish with var"""
    #     input = """
    #        Var: a[2] = {1, 2};
    #        Var: b = 12.5;
    #
    #        Function: main
    #        Parameter: p
    #        Body:
    #            b();
    #        EndBody.
    #
    #        Function: c
    #        Parameter: d
    #        Body:
    #            d = 15.5;
    #        EndBody.
    #        """
    #     expect = str(Undeclared(Function(), "b"))
    #     self.assertTrue(TestChecker.test(input, expect, 404))
    #
    # # 5
    # def test_undeclared_var_5(self):
    #     """test undeclared function d called in function main where d in different scope"""
    #     input = """
    #        Var: a[2] = {1, 2};
    #        Var: b = 12.5;
    #
    #        Function: main
    #        Parameter: p
    #        Body:
    #            d = 12.0;
    #        EndBody.
    #
    #        Function: c
    #        Parameter: d
    #        Body:
    #            d = 15.5;
    #        EndBody.
    #
    #        Function: f
    #        Body:
    #            Var: d;
    #        EndBody.
    #        """
    #     expect = str(Undeclared(Identifier(), "d"))
    #     self.assertTrue(TestChecker.test(input, expect, 405))
    #
    # # Test Redeclared
    # # 6
    # def test_redeclared_var_6(self):
    #     """test redeclared var a in global scope same type"""
    #     input = """
    #        Var: a[2] = {1, 2};
    #        Var: a[3] = {True, False, True};
    #
    #        Function: main
    #        Parameter: p
    #        Body:
    #        EndBody.
    #        """
    #     expect = str(Redeclared(Variable(), "a"))
    #     self.assertTrue(TestChecker.test(input, expect, 406))
    #
    # # 7
    # def test_redeclared_var_7(self):
    #     """test redeclared var a in global scope different type"""
    #     input = """
    #        Var: a[2] = {1, 2};
    #        Var: a;
    #
    #        Function: main
    #        Parameter: p
    #        Body:
    #        EndBody.
    #        """
    #     expect = str(Redeclared(Variable(), "a"))
    #     self.assertTrue(TestChecker.test(input, expect, 407))
    #
    # # 8
    # def test_redeclared_var_8(self):
    #     """test redeclared var a in function scope"""
    #     input = """
    #        Function: main
    #        Parameter: p
    #        Body:
    #            Var: a[2] = {1, 2}, a;
    #        EndBody.
    #        """
    #     expect = str(Redeclared(Variable(), "a"))
    #     self.assertTrue(TestChecker.test(input, expect, 408))
    #
    # # 9
    # def test_redeclared_var_9(self):
    #     """test redeclared var a in inner scope"""
    #     input = """
    #        Function: main
    #        Parameter: p
    #        Body:
    #            If True Then
    #                Var: a[2] = {1, 2}, a;
    #            EndIf.
    #        EndBody.
    #        """
    #     expect = str(Redeclared(Variable(), "a"))
    #     self.assertTrue(TestChecker.test(input, expect, 409))
    #
    # # 10
    # def test_redeclared_var_10(self):
    #     """test redeclared var a in inner of inner scope"""
    #     input = """
    #        Function: main
    #        Parameter: p
    #        Body:
    #            If True Then
    #                While True Do
    #                    Var: a[2] = {1, 2}, a;
    #                EndWhile.
    #            EndIf.
    #        EndBody.
    #        """
    #     expect = str(Redeclared(Variable(), "a"))
    #     self.assertTrue(TestChecker.test(input, expect, 410))
    #
    # # 11
    # def test_redeclared_function_11(self):
    #     """test redeclared function main"""
    #     input = """
    #        Function: main
    #        Parameter: p
    #        Body:
    #        EndBody.
    #
    #        Function: main
    #        Body:
    #        EndBody.
    #        """
    #     expect = str(Redeclared(Function(), "main"))
    #     self.assertTrue(TestChecker.test(input, expect, 411))
    #
    # # 12
    # def test_redeclared_function_12(self):
    #     """test redeclared function main and main variable"""
    #     input = """
    #        Var: main = 10;
    #        Function: main
    #        Parameter: p
    #        Body:
    #        EndBody.
    #        """
    #     expect = str(Redeclared(Function(), "main"))
    #     self.assertTrue(TestChecker.test(input, expect, 412))
    #
    # # 13
    # def test_redeclared_function_13(self):
    #     """test redeclared function main and main variable with composite form"""
    #     input = """
    #        Var: main[2][3] = {{1, 2, 3}, {4, 5, 6}};
    #        Function: main
    #        Parameter: p
    #        Body:
    #        EndBody.
    #        """
    #     expect = str(Redeclared(Function(), "main"))
    #     self.assertTrue(TestChecker.test(input, expect, 413))
    #
    # # Test Return Statement
    # # Test Type Inferrence
    # # 14
    # def test_return_function_type_14(self):
    #     """test return function type func declaration behind"""
    #     input = """
    #        Var: a = 10;
    #        Function: main
    #        Parameter: p
    #        Body:
    #            p = a + foo();
    #        EndBody.
    #
    #        Function: foo
    #        Body:
    #            Return 12.5;
    #        EndBody.
    #        """
    #     expect = str(TypeMismatchInStatement(Return(FloatLiteral(12.5))))
    #     self.assertTrue(TestChecker.test(input, expect, 414))
    #
    # # 15
    # def test_return_function_type_15(self):
    #     """test return function type func declaration before"""
    #     input = """
    #        Var: a = 10;
    #
    #        Function: foo
    #        Body:
    #            Return 12.5;
    #        EndBody.
    #
    #        Function: main
    #        Parameter: p
    #        Body:
    #            p = a + foo();
    #        EndBody.
    #        """
    #     expect = str(TypeMismatchInExpression(
    #         BinaryOp("+", Id("a"), CallExpr(Id("foo"), []))))
    #     self.assertTrue(TestChecker.test(input, expect, 415))
    #
    # # 16
    # def test_return_function_type_16(self):
    #     """test return function type return an array type of int but called as array type of float"""
    #     input = """
    #        Var: a[2][3];
    #
    #        Function: foo
    #        Body:
    #            Var: b[2][3];
    #            b[2][3] = 12;
    #            Return b;
    #        EndBody.
    #
    #        Function: main
    #        Parameter: p
    #        Body:
    #            p = 12.5;
    #            p = 12.5 +. foo()[4][4];
    #        EndBody.
    #        """
    #     expect = str(TypeMismatchInExpression(BinaryOp("+.", FloatLiteral(12.5),
    #                                                    ArrayCell(CallExpr(Id("foo"), []),
    #                                                              [IntLiteral(4), IntLiteral(4)]))))
    #     self.assertTrue(TestChecker.test(input, expect, 416))
    #
    # # 17
    # def test_return_function_type_17(self):
    #     """test return function type foo no Return"""
    #     input = """
    #        Var: a[2][3] = {{1, 2, 3}, {3, 4, 5}};
    #
    #        Function: foo
    #        Parameter: p[2][3]
    #        Body:
    #        EndBody.
    #
    #        Function: main
    #        Parameter: p
    #        Body:
    #            p = 12.5;
    #            p = foo(a);
    #        EndBody.
    #        """
    #     expect = str(TypeMismatchInStatement(
    #         Assign(Id("p"), CallExpr(Id("foo"), [Id("a")]))))
    #     self.assertTrue(TestChecker.test(input, expect, 417))
    #
    # # 18
    # def test_return_function_type_18(self):
    #     """test return function type infer x in foo"""
    #     input = """
    #        Var: a[2][3] = {{1, 2, 3}, {3, 4, 5}};
    #
    #        Function: main
    #        Parameter: p
    #        Body:
    #            p = 12.5;
    #            p = foo(a);
    #        EndBody.
    #
    #        Function: foo
    #        Parameter: p[2][3]
    #        Body:
    #            Var: x = 10;
    #            Return x;
    #        EndBody.
    #        """
    #     expect = str(TypeMismatchInStatement(Return(Id("x"))))
    #     self.assertTrue(TestChecker.test(input, expect, 418))
    #
    # # 19
    # def test_return_function_type_19(self):
    #     """test return function type return inferred to float but inferred to int when called"""
    #     input = """
    #        Var: a[2][3] = {{1, 2, 3}, {3, 4, 3}};
    #
    #        Function: foo
    #        Body:
    #            Return a;
    #        EndBody.
    #
    #        Function: c
    #        Parameter: b[2][3]
    #        Body:
    #            Return 15.6;
    #        EndBody.
    #
    #        Function: main
    #        Parameter: p
    #        Body:
    #            p = 10;
    #            p = c(foo());
    #        EndBody.
    #        """
    #     expect = str(TypeMismatchInStatement(
    #         Assign(Id('p'), CallExpr(Id('c'), [CallExpr(Id('foo'), [])]))))
    #     self.assertTrue(TestChecker.test(input, expect, 419))
    #
    # # 20
    # def test_return_function_type_20(self):
    #     """test return function type return array type of int but called as float"""
    #     input = """
    #        Var: a[2][3];
    #
    #        Function: foo
    #        Body:
    #            Var: b[2][3];
    #            b[2][3] = 12;
    #            Return b;
    #        EndBody.
    #
    #        Function: main
    #        Parameter: p
    #        Body:
    #            p = 12.5;
    #            p = 12.5 +. foo();
    #        EndBody.
    #        """
    #     expect = str(TypeMismatchInExpression(
    #         BinaryOp("+.", FloatLiteral(12.5), CallExpr(Id("foo"), []))))
    #     self.assertTrue(TestChecker.test(input, expect, 420))
    #
    # # 21
    # def test_return_function_type_21(self):
    #     """test return function type return array type of int but called as float in reverse order"""
    #     input = """
    #        Var: a[2][3];
    #
    #        Function: main
    #        Parameter: p
    #        Body:
    #            p = 12.5;
    #            p = 12.5 +. foo();
    #        EndBody.
    #
    #        Function: foo
    #        Body:
    #            Var: b[2][3];
    #            b[2][3] = 12;
    #            Return b;
    #        EndBody.
    #        """
    #     expect = str(TypeMismatchInStatement(Return(Id("b"))))
    #     self.assertTrue(TestChecker.test(input, expect, 421))
    #
    # # # 22
    # # def test_return_function_type_infer_22(self):
    # #     """test return function type inferrence return an array type of int but called as array type of float in reverse order"""
    # #     input = """
    # #     Var: a[2][3];
    #
    # #     Function: main
    # #     Parameter: p
    # #     Body:
    # #         p = 12.5;
    # #         p = 12.5 +. foo()[4][4];
    # #     EndBody.
    #
    # #     Function: foo
    # #     Body:
    # #         Var: b[2][3];
    # #         b[2][3] = 12;
    # #         Return b;
    # #     EndBody.
    # #     """
    # #     expect = str(TypeMismatchInExpression(BinaryOp("+.", FloatLiteral(12.5),
    # #                                                    ArrayCell(CallExpr(Id("foo"), []), [IntLiteral(4), IntLiteral(4)]))))
    # #     self.assertTrue(TestChecker.test(input, expect, 422))
    #
    # # 23
    # def test_return_function_type_23(self):
    #     """test return function type return an array type of int but called as array type of float in reverse order"""
    #     input = """
    #
    #        Function: a
    #        Parameter: p[2][3]
    #        Body:
    #            Return 12.5;
    #        EndBody.
    #
    #        Function: b
    #        Body:
    #            Var: p[2][3];
    #            p[2][3] = 12;
    #            Return a(p);
    #        EndBody.
    #
    #        Function: main
    #        Parameter: p
    #        Body:
    #            Return 10 + b();
    #        EndBody.
    #        """
    #     expect = str(TypeMismatchInExpression(BinaryOp("+", IntLiteral(10), CallExpr(Id("b"), []))))
    #     self.assertTrue(TestChecker.test(input, expect, 423))
    #
    # # 24
    # def test_return_function_type_24(self):
    #     """test return function type return void but used as function call"""
    #     input = """
    #
    #        Function: a
    #        Body:
    #        EndBody.
    #
    #        Function: main
    #        Parameter: p
    #        Body:
    #            p = a();
    #        EndBody.
    #        """
    #     expect = str(TypeMismatchInStatement(Assign(Id("p"), CallExpr(Id("a"), []))))
    #     self.assertTrue(TestChecker.test(input, expect, 424))
    #
    # # 25
    # def test_return_function_type_25(self):
    #     """test return function type return unknown var"""
    #     input = """
    #
    #        Function: a
    #        Body:
    #            Var: x;
    #            Return x;
    #        EndBody.
    #
    #        Function: main
    #        Parameter: p
    #        Body:
    #        EndBody.
    #        """
    #     expect = str(TypeCannotBeInferred(Return(Id("x"))))
    #     self.assertTrue(TestChecker.test(input, expect, 425))
    #
    # # Test Assignment Statement
    # # 26
    # def test_assignment_type_26(self):
    #     """test assignment stmt simple lhs unknown simple rhs unknown"""
    #     input = """
    #        Function: main
    #        Parameter: p
    #        Body:
    #            Var: x;
    #            p = x;
    #        EndBody.
    #        """
    #     expect = str(TypeCannotBeInferred(Assign(Id("p"), Id("x"))))
    #     self.assertTrue(TestChecker.test(input, expect, 426))
    #
    # # 27
    # def test_assignment_type_27(self):
    #     """test assignment stmt simple lhs int simple rhs inferred"""
    #     input = """
    #        Function: main
    #        Parameter: p
    #        Body:
    #            Var: x;
    #            p = 10;
    #            p = x;
    #            Return 12.5 + x;
    #        EndBody.
    #        """
    #     expect = str(TypeMismatchInExpression(BinaryOp("+", FloatLiteral(12.5), Id("x"))))
    #     self.assertTrue(TestChecker.test(input, expect, 427))
    #
    # # 28
    # def test_assignment_type_28(self):
    #     """test assignment stmt simple lhs inferred rhs int"""
    #     input = """
    #        Function: main
    #        Parameter: p
    #        Body:
    #            Var: x = 10;
    #            p = x;
    #            Return 12.5 + p;
    #        EndBody.
    #        """
    #     expect = str(TypeMismatchInExpression(BinaryOp("+", FloatLiteral(12.5), Id("p"))))
    #     self.assertTrue(TestChecker.test(input, expect, 428))
    #
    # # 29
    # def test_assignment_type_29(self):
    #     """test assignment stmt simple lhs array type unknown rhs int"""
    #     input = """
    #        Var: a[2][3];
    #
    #        Function: main
    #        Parameter: p
    #        Body:
    #            Var: x = 10;
    #            a[1][2] = x;
    #            Return 12.5 + a[1][2];
    #        EndBody.
    #        """
    #     expect = str(TypeMismatchInExpression(
    #         BinaryOp("+", FloatLiteral(12.5), ArrayCell(Id("a"), [IntLiteral(1), IntLiteral(2)]))))
    #     self.assertTrue(TestChecker.test(input, expect, 429))
    #
    # # 30
    # def test_assignment_type_30(self):
    #     """test assignment stmt simple lhs array type of int rhs unknown"""
    #     input = """
    #        Var: a[2][3] = {{1, 2, 3}, {3, 4, 5}};
    #
    #        Function: main
    #        Parameter: p
    #        Body:
    #            Var: x;
    #            a[1][2] = x;
    #            Return 12.5 + x;
    #        EndBody.
    #        """
    #     expect = str(TypeMismatchInExpression(BinaryOp("+", FloatLiteral(12.5), Id("x"))))
    #     self.assertTrue(TestChecker.test(input, expect, 430))
    #
    # # 31
    # def test_assignment_type_31(self):
    #     """test assignment stmt simple lhs array type of int rhs array type unknown"""
    #     input = """
    #        Var: a[2][3] = {{1, 2, 3}, {3, 4, 5}};
    #        Var: b[2];
    #
    #        Function: main
    #        Parameter: p
    #        Body:
    #            a[1][2] = b[0];
    #            Return 12.5 + b[0];
    #        EndBody.
    #        """
    #     expect = str(TypeMismatchInExpression(BinaryOp("+", FloatLiteral(12.5), ArrayCell(Id("b"), [IntLiteral(0)]))))
    #     self.assertTrue(TestChecker.test(input, expect, 431))
    #
    # # 32
    # def test_assignment_type_32(self):
    #     """test assignment stmt simple lhs array type unknown rhs array type int"""
    #     input = """
    #        Var: a[2][3] = {{1, 2, 3}, {3, 4, 5}};
    #        Var: b[2];
    #
    #        Function: main
    #        Parameter: p
    #        Body:
    #            b[0] = a[1][2];
    #            Return 12.5 + b[0];
    #        EndBody.
    #        """
    #     expect = str(TypeMismatchInExpression(BinaryOp("+", FloatLiteral(12.5), ArrayCell(Id("b"), [IntLiteral(0)]))))
    #     self.assertTrue(TestChecker.test(input, expect, 432))
    #
    # # 33
    # def test_assignment_type_33(self):
    #     """test assignment stmt simple lhs array type unknown rhs function call"""
    #     input = """
    #        Var: b[2];
    #
    #        Function: a
    #        Body:
    #            Return 10;
    #        EndBody.
    #
    #        Function: main
    #        Parameter: p
    #        Body:
    #            b[0] = a();
    #            Return 12.5 + b[0];
    #        EndBody.
    #        """
    #     expect = str(TypeMismatchInExpression(BinaryOp("+", FloatLiteral(12.5), ArrayCell(Id("b"), [IntLiteral(0)]))))
    #     self.assertTrue(TestChecker.test(input, expect, 433))
    #
    # # 34
    # def test_assignment_type_34(self):
    #     """test assignment stmt simple lhs array type boolean rhs function call unknown return type"""
    #     input = """
    #        Var: b[2] = {True, False};
    #
    #        Function: main
    #        Parameter: p
    #        Body:
    #            b[0] = a();
    #        EndBody.
    #
    #        Function: a
    #        Body:
    #            Return 10;
    #        EndBody.
    #        """
    #     expect = str(TypeMismatchInStatement(Return(IntLiteral(10))))
    #     self.assertTrue(TestChecker.test(input, expect, 434))
    #
    # # 35
    # def test_assignment_type_35(self):
    #     """test assignment stmt complex form"""
    #     input = """
    #        Var: b[2] = {0, 1};
    #
    #        Function: main
    #        Parameter: p
    #        Body:
    #            b[0] = a() + a() + 10 - p;
    #            p = 10;
    #        EndBody.
    #
    #        Function: a
    #        Body:
    #            Return True;
    #        EndBody.
    #        """
    #     expect = str(TypeMismatchInStatement(Return(BooleanLiteral(True))))
    #     self.assertTrue(TestChecker.test(input, expect, 435))
    #
    # # 36
    # def test_assignment_type_36(self):
    #     """test assignment stmt complex form"""
    #     input = """
    #        Var: b[2] = {0, 1};
    #
    #        Function: a
    #        Body:
    #            Return 10;
    #        EndBody.
    #
    #        Function: main
    #        Parameter: p[2][3]
    #        Body:
    #            b[0] = a() + p[1][1] + 10 - p[2][1];
    #            p[0][1] = 10.5;
    #        EndBody.
    #        """
    #     expect = str(
    #         TypeMismatchInStatement(Assign(ArrayCell(Id("p"), [IntLiteral(0), IntLiteral(1)]), FloatLiteral(10.5))))
    #     self.assertTrue(TestChecker.test(input, expect, 436))

    ########################
