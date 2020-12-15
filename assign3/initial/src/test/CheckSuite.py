import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):

    # 1
    def test_redeclared_global_variable(self):
        """Check redeclared global variable"""
        input = """Var: x;
                    Var: x;
            Function: main
            Body:
            EndBody.
                    """
        expect = str(Redeclared(Variable(), "x"))
        self.assertTrue(TestChecker.test(input, expect, 400))

    # 2
    def test_redeclared_gloal_variable_same_declaration(self):
        """Check redeclared global variables same declaration"""
        input = """Var: a,b,c,a;
            Function: main
            Body:
            EndBody.
                    """
        expect = str(Redeclared(Variable(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 401))

    # 3
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

    # 4
    def test_redeclared_function(self):
        """Check redeclared function"""
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
                Var: y;
            EndBody.
            """
        expect = str(Redeclared(Function(), "foo"))
        self.assertTrue(TestChecker.test(input, expect, 403))

    # 5
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

    # 6
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

    # 7
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

    # 8
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

    # 9
    def test_undeclared_function(self):
        """Undeclared function"""
        input = """Function: main
                   Body:
                        foo();
                   EndBody."""
        expect = str(Undeclared(Function(), "foo"))
        self.assertTrue(TestChecker.test(input, expect, 408))

    # 10
    def test_redeclared_function_with_global(self):
        """Redeclared function with global variable"""
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

    # 11
    def test_redeclared_para(self):
        """Redeclared parameter"""
        input = """
        Function: main
        Parameter: a, b, c, b
        Body:
            Var: x;
        EndBody.
        """
        expect = str(Redeclared(Parameter(), "b"))
        self.assertTrue(TestChecker.test(input, expect, 410))

    # 12
    def test_redeclared_variable_with_para(self):
        """Redeclared local variable with parameter variable"""
        input = """
        Function: main
        Parameter: a, b, c
        Body:
            Var: b;
        EndBody.
        """
        expect = str(Redeclared(Variable(), "b"))
        self.assertTrue(TestChecker.test(input, expect, 411))

    # 13
    def test_call_stmt_wrong_length_para(self):
        """Call statement with wrong number of parameters"""
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

    # 14
    def test_call_stmt_wrong_para_undeclared(self):
        """Call statement with undeclared identifier"""
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

    # 15
    def test_bool_expr(self):
        """Check boolean expression"""
        input = """
        Function: main
        Body:
            Var: x = True, y = 9, c;
            c = x && y;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp('&&', Id('x'), Id('y'))))
        self.assertTrue(TestChecker.test(input, expect, 414))

    # 16
    def test_call_stmt_wrong_para_type(self):
        """Call statement with wrong type of parameter"""
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

    # 17
    def test_diff_numofparam_stmt(self):
        """Check statement with different number of parameter"""
        input = """Function: main
                   Body:
                        printStrLn();
                    EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"), [])))
        self.assertTrue(TestChecker.test(input, expect, 416))

    # 18
    def test_call_stmt_wrong_para(self):
        """Call statement with wrong parameter with many same name in different scope"""
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

    # 19
    def test_diff_numofparam_expr(self):
        """Check expression with different parameter"""
        input = """Function: main
                    Body:
                        printStrLn(read(4));
                    EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"), [IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input, expect, 418))

    # 20
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([FuncDecl(Id("main"), [], ([], [
            CallExpr(Id("foo"), [])]))])
        expect = str(Undeclared(Function(), "foo"))
        self.assertTrue(TestChecker.test(input, expect, 419))

    # 21
    def test_diff_numofparam_expr_use_ast(self):
        """More complex program"""
        input = Program([
            FuncDecl(Id("main"), [], ([], [
                CallStmt(Id("printStrLn"), [
                    CallExpr(Id("read"), [IntLiteral(4)])
                ])]))])
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"), [IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input, expect, 420))

    # 22
    def test_diff_numofparam_stmt_use_ast(self):
        """Complex program"""
        input = Program([
            FuncDecl(Id("main"), [], ([], [
                CallStmt(Id("printStrLn"), [])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"), [])))
        self.assertTrue(TestChecker.test(input, expect, 421))

    # 23
    def test_bool_expr_or(self):
        """Check boolean expression or"""
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

    # 24
    def test_wrong_function_para(self):
        """Wrong parameter type"""
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

    # 25
    def test_no_main_function(self):
        """Program with no function main"""
        input = """
        Function: foo
        Body:
        EndBody.
         """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 424))

    # 26
    def test_array_type(self):
        """Array with wrong type assignment"""
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

    # 27
    def test_array_wrong_type_assign(self):
        """Array with wrong type assignment"""
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

    # 28
    def test_array_wrong_type_with_expression(self):
        """Array assignment with wrong type in expression"""
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

    # 29
    def test_array_in_binary(self):
        """Array in binary operation"""
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

    # 30
    def test_array_unary(self):
        """Array in unary operation"""
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

    # 31
    def test_if(self):
        """Check if statement"""
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

    # 32
    def test_if_else(self):
        """Check if else statement"""
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

    # 33
    def test_if_elseif(self):
        """Check if else if statement"""
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

    # 34
    def test_for(self):
        """Check for statement"""
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

    # 35
    def test_for_stmt_wrong_exp1(self):
        """Check for statement wrong expression 1 type"""
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

    # 36
    def test_while_stmt(self):
        """Check while statement"""
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

    # 37
    def test_do_while_stmt(self):
        """Check do while statement"""
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

    # 38
    def test_return(self):
        """Check return statement"""
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

    # 39
    def test_return_wrong_type(self):
        """Return wrong type"""
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

    # 40
    def test_assign_wrong_type(self):
        """Assignment statement with wrong type"""
        input = """
        Var: a[2][2] = {{1, 2}, {3, 4}};

        Function: foo
        Body:
            Return a;
        EndBody.

        Function: c
        Parameter: b[2][2]
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

    # 41
    def test_return_function_type_infer_assign(self):
        """test return function type inferrence function declaration before"""
        input = """
        Var: a[2][3] = {{1, 2, 5}, {3, 4, 6}};

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

    # 42
    def test_do_while_condition(self):
        """Do while condition expression infer before"""
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

    # 43
    def test_array_para(self):
        """Wrong parameter type passed"""
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

    # 44
    def test_array_assign_type(self):
        """Wrong parameter infer type"""
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

    # 45
    def test_many_return(self):
        """Conflicting in return statements"""
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

    # 46
    def test_function_assign_declared_below(self):
        """Check type of parameter"""
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

    # 47
    def test_for_stmt_infer_type(self):
        """wrong type for idx in for statement"""
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

    # 48
    def test_for_bool(self):
        """test for statement wrong bool type"""
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

    # 49
    def test_return_stmt_wrong_type(self):
        """Return statement with wrong type"""
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

    # 50
    def test_type(self):
        """Check order of infer type"""
        input = """
        Function: main
        Parameter: x, y ,z
        Body:
            y = x || (x>z);
        EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp('>', Id('x'), Id('z'))))
        self.assertTrue(TestChecker.test(input, expect, 449))

    # 51
    def test_if_with_return_stmt(self):
        """Check if statement with return statement"""
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
                printLn();
            EndIf.
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(BinaryOp('+', Id('x'), IntLiteral(1)))))
        self.assertTrue(TestChecker.test(input, expect, 450))

    # 52
    def test_for_with_array(self):
        """Check for statement with array"""
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

    # 53
    def test_return_type(self):
        """Check return type in function"""
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

    # 54
    def test_for_infer_third_expr(self):
        """Check type of expr3 in for statement"""
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

    # 55
    def test_for_infer_bool_expr(self):
        """Check for statement boolean expression"""
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

    # 56
    def test_while_infer(self):
        """Check variable inferred by while statement"""
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

    # 57
    def test_do_while_infer(self):
        """Simple program: main"""
        input = """
        Var: a[2][2] = {{1,2},{3,4}};
        Function: main
        Body:
            Var: x;
            Do
                x = 1;
            While foo(x) EndDo.
        EndBody.
        Function: foo
        Parameter: x
        Body:
            Var: y;
            y = !x;
            Return y;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(UnaryOp('!', Id('x'))))
        self.assertTrue(TestChecker.test(input, expect, 456))

    # 58
    def test_array_assign_type_before(self):
        """Check type of function declared after"""
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

    # 59
    def test_if_nested(self):
        """test type of variable inside nested if"""
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

    # 60
    def test_wrong_scalar(self):
        """Check array used as scalar"""
        input = """
        Var: a = 1, b[5];
        Function: main
        Body:
            a = b;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('a'), Id('b'))))
        self.assertTrue(TestChecker.test(input, expect, 459))

    # 61
    def test_infer_type(self):
        """Infer type for function in if"""
        input = """
        Function: main
        Parameter: x
        Body:
            If main(main(5)) Then EndIf.
        EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id('main'), [IntLiteral(5)])))
        self.assertTrue(TestChecker.test(input, expect, 460))

    # 62
    def test_infer_type_para(self):
        """Check infer type for parameter of function"""
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

    # 63
    def test_infer_type_of_function(self):
        """Check infer type for fucntion"""
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
        expect = str(TypeCannotBeInferred(
            Assign(Id('e'), CallExpr(Id('main'), [Id('b'), CallExpr(Id('main'),
                                                                    [Id('d'), Id('c'),
                                                                     Id('a')]),
                                                  BinaryOp('+', Id('a'), Id('d'))]))))
        self.assertTrue(TestChecker.test(input, expect, 462))

    # 64
    def test_undeclared_var_as_func(self):
        """Check function used as scalar"""
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

    # 65
    def test_array_para_wrong_assign_type(self):
        """Wrong assignment to array"""
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

    # 66
    def test_infer_para(self):
        """Check order of infer for parameter"""
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

    # 67
    def test_array_para_wrong_infer_in_diff_func(self):
        """Wrong array assignment in different function"""
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

    # 68
    def test_same_name(self):
        """Same name in same scope"""
        input = """
                Function: main
                Body:
                    Var: foo = 0;
                    foo = foo + foo();
                EndBody.
                Function: foo
                Body:
                    Return 1 + 2;
                EndBody.
                """
        expect = str(Undeclared(Function(), 'foo'))
        self.assertTrue(TestChecker.test(input, expect, 467))

    # 69
    def test_same_name_binary(self):
        """Same name in same scope"""
        input = """
                Function: main
                Body:
                    Var: a = 0, i, foo;
                    i = float_to_int(a) +. foo();
                EndBody.
                Function: foo
                Body:
                    Return 15.5;
                EndBody.
                """
        expect = str(Undeclared(Function(), 'foo'))
        self.assertTrue(TestChecker.test(input, expect, 468))

    # 70
    def test_infer_for_expr1(self):
        """Check infer expression 1 of for statement"""
        input = """
        Function: main
        Body:
            Var: i;
            For(i = foo(foo(15.6)), i < 10, 1) Do
                printStrLn("correct");
            EndFor.
        EndBody.
        Function: foo
        Parameter: x
        Body:
            print("hello");
        EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id('foo'), [FloatLiteral(15.6)])))
        self.assertTrue(TestChecker.test(input, expect, 469))

    # 71
    def test_infer_for_expr2(self):
        """Check infer expression 2 of for statement"""
        input = """
        Function: main
        Body:
            Var: i;
            For(i = 1, foo(foo(False)), 1) Do
                printStrLn("correct");
            EndFor.
        EndBody.
        Function: foo
        Parameter: x
        Body:
            x = x && True;
            print("hello");
            Return 100;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(IntLiteral(100))))
        self.assertTrue(TestChecker.test(input, expect, 470))

    # 72
    def test_infer_for_expr3(self):
        """Check infer expression 3 of for statement"""
        input = """
        Function: main
        Body:
            Var: i;
            For(i = 1, i < 100, foo(foo(9.5))) Do
                printStrLn("correct");
            EndFor.
        EndBody.
        Function: foo
        Parameter: x
        Body:
            print("Cyber");
            Return 100;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id('foo'), [FloatLiteral(9.5)])))
        self.assertTrue(TestChecker.test(input, expect, 471))

    # 73
    def test_infer_for_idx1(self):
        """Check infer idx of for statement"""
        input = """
        Function: main
        Body:
            Var: i;
            For(i = foo(i), bool_of_string("True"), 1) Do
                printStrLn("correct");
            EndFor.
        EndBody.
        Function: foo
        Parameter: x
        Body:
            Var: y, z;
            y = (!z || False) && x;
            Return 100;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(
            BinaryOp('&&', BinaryOp('||', UnaryOp('!', Id('z')), BooleanLiteral(False)), Id('x'))))
        self.assertTrue(TestChecker.test(input, expect, 472))

    # 74
    def test_infer_while_expr(self):
        """Check infer while statement"""
        input = """
        Function: main
        Body:
            Var: a[2] = {True, False};
            While foo(foo(string_of_bool(a[0]))) Do
                printStrLn("martel");
            EndWhile.
        EndBody.
        Function: foo
        Parameter: x
        Body:
            Var: y, z;
            y = (!z || False) && (x > 100);
            Return 100;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(
            CallExpr(Id('foo'), [CallExpr(Id('string_of_bool'), [ArrayCell(Id('a'), [IntLiteral(0)])])])))
        self.assertTrue(TestChecker.test(input, expect, 473))

    # 75
    def test_infer_while_expr_arr(self):
        """Check infer while statement array"""
        input = """
        Function: main
        Body:
            Var: a[2];
            While a[int_of_string(a[1])] Do
                printStrLn("oberyn");
            EndWhile.
        EndBody.
        Function: foo
        Parameter: x
        Body:
            Return 100;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(
            CallExpr(Id('int_of_string'), [ArrayCell(Id('a'), [IntLiteral(1)])])))
        self.assertTrue(TestChecker.test(input, expect, 474))

    # 76
    def test_infer_do_while_expr(self):
        """Check infer do while statement"""
        input = """
        Function: main
        Body:
            Var: a[2];
            Do
                printStrLn("lannister");
            While foo(foo(int_of_string("5"))) EndDo.
        EndBody.
        Function: foo
        Parameter: x
        Body:
            Return True;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(
            CallExpr(Id('foo'), [CallExpr(Id('int_of_string'), [StringLiteral("5")])])))
        self.assertTrue(TestChecker.test(input, expect, 475))

    # 77
    def test_infer_do_while_expr_arr(self):
        """Check infer do while statement array"""
        input = """
        Function: main
        Body:
            Var: a[2];
            Do
                printStrLn("stark");
            While a[int_of_float(a[1])] EndDo.
        EndBody.
        Function: foo
        Parameter: x
        Body:
            Return True;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(
            CallExpr(Id('int_of_float'), [ArrayCell(Id('a'), [IntLiteral(1)])])))
        self.assertTrue(TestChecker.test(input, expect, 476))

    # 78
    def test_arr_infer_type_unary(self):
        """Array infer type in unary operation"""
        input = """
        Function: main
        Body:
            Var: a[2];
            Do
                Var: x;
                x = a[1] + 5;
                x = !a[0];
            While True EndDo.
        EndBody.
        """
        expect = str(TypeMismatchInExpression(
            UnaryOp('!', ArrayCell(Id('a'), [IntLiteral(0)]))))
        self.assertTrue(TestChecker.test(input, expect, 477))

    # 79
    def test_type_scope_inside(self):
        """Check infer type for inside scope"""
        input = """
        Function: main
        Body:
            Var: a[2], x, y = 10.5, t = "15.6";
            x = !(y <. 50.6);
            If True Then
                Var: res, z;
                res = float_of_string(t) +. foo(z);
            EndIf.
        EndBody.
        Function: foo
        Parameter: x
        Body:
            Return 79.6;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(
            Assign(Id('res'),
                   BinaryOp('+.', CallExpr(Id('float_of_string'), [Id('t')]), CallExpr(Id('foo'), [Id('z')])))))
        self.assertTrue(TestChecker.test(input, expect, 478))

    # 80
    def test_for_stmt_wrong_exp3_type(self):
        """Check wrong type for expression 3 of for statement"""
        input = """
        Function: main
        Body:
            Var: a[2], x, y = 10.5, t = "15.6";
            x = !(y <. 50.6);
            If True Then
                Var: res, z;
                For(z = 1, bool_of_string("True"), y) Do
                    printLn();
                EndFor.
            EndIf.
        EndBody.
        """
        expect = str(TypeMismatchInStatement(
            For(Id("z"), IntLiteral(1), CallExpr(Id("bool_of_string"), [StringLiteral("True")]), Id("y"),
                ([], [CallStmt(Id("printLn"), [])]))))
        self.assertTrue(TestChecker.test(input, expect, 479))

    # 81
    def test_return_stmt_itself(self):
        """Check return statement return itself"""
        input = """
        Function: main
        Parameter: k
        Body:
            Var: a[2], x, y = 10.5, t = "15.6";
            x = !(y <. 50.6);
            If True Then
                Var: res, z;
                For(z = 1, bool_of_string("True"), 1) Do
                    printLn();
                    Return 1 + main(main(y));
                EndFor.
            EndIf.
        EndBody.
        """
        expect = str(TypeMismatchInExpression(
            CallExpr(Id('main'), [Id('y')])))
        self.assertTrue(TestChecker.test(input, expect, 480))

    # 82
    def test_unary_infer_function(self):
        """Check infer type function in unary operation"""
        input = """
        Function: main
        Parameter: k
        Body:
            Var: a[2], x, y = 10.5, t = "15.6";
            x = !foo(foo(y));
        EndBody.
        Function: foo
        Parameter: x
        Body:
            Return True;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(
            CallExpr(Id('foo'), [Id('y')])))
        self.assertTrue(TestChecker.test(input, expect, 481))

    # 83
    def test_predefined_function(self):
        """Check predefined function"""
        input = """
        Function: main
        Parameter: x
        Body:
            printLn();
            print(string_of_bool(True));
            read();
        EndBody.
        """
        expect = str(TypeMismatchInStatement(
            CallStmt(Id('read'), [])))
        self.assertTrue(TestChecker.test(input, expect, 482))

    # 84
    def test_type_in_return(self):
        """Check predefined function"""
        input = """
        Function: main
        Body:
            Var: x;
            Return 1 + foo(x);
        EndBody.
        Function: foo
        Parameter: x
        Body:
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Return(BinaryOp('+', IntLiteral(1), CallExpr(Id('foo'), [Id('x')])))))
        self.assertTrue(TestChecker.test(input, expect, 483))

    # 85
    def test_function_type(self):
        """Check return of function"""
        input = """
        Function: foo
        Parameter: a, c, b
        Body:
            b = True;
        EndBody.

        Function: main
        Body:
            Var: x = "targeryen", sum;
            Var: tem;
            x = foo(x, 30.0e+1, sum);
            printStrLn(foo("Aegon", tem, True));
        Return main();
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Return(CallExpr(Id('main'), []))))
        self.assertTrue(TestChecker.test(input, expect, 484))

    # 86
    def test_infer_for_predefine(self):
        """Check predefined function infer type"""
        input = """
        Function: main
        Body:
            Var: x, y = 1;
            Return 2.0 +. float_of_string(foo(x, y));
        EndBody.

        Function: foo
        Parameter: x, y
        Body:
            Return string_of_int(100);
        EndBody."""
        expect = str(TypeCannotBeInferred(Return(BinaryOp('+.', FloatLiteral(2.0), CallExpr(Id('float_of_string'), [
            CallExpr(Id('foo'), [Id('x'), Id('y')])])))))
        self.assertTrue(TestChecker.test(input, expect, 485))

    # 87
    def test_infer_in_return(self):
        """Check return unknown"""
        input = """
        Var: arr[3];
        Function: main
        Body:
            Return arr;
        EndBody."""
        expect = str(TypeCannotBeInferred(Return(Id('arr'))))
        self.assertTrue(TestChecker.test(input, expect, 486))

    # 88
    def test_array_assignment(self):
        """Check array assignment"""
        input = """Var: arr[1][1], brr[1][3], crr[5], drr[5];
        Function: main
        Body:
            crr = {"a", "b", "y", "z", "g"};
            brr = { {1, 2, 3} };
            drr = crr;
            arr = brr;
        EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id('arr'), Id('brr'))))
        self.assertTrue(TestChecker.test(input, expect, 487))

    # 89
    def test_if_infer_and_for(self):
        """Check if and for"""
        input = """
        Function: main
        Body:
            Var: b = 5,i,res,j;
            If i Then
                res = b * b;
            EndIf.
            For(j = 1, string_of_bool(i), j) Do
                x = x + 1;
            EndFor.
        EndBody."""
        expect = str(TypeMismatchInStatement(
            For(Id("j"), IntLiteral(1), CallExpr(Id("string_of_bool"), [Id("i")]), Id("j"),
                ([], [Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(1)))]))))
        self.assertTrue(TestChecker.test(input, expect, 488))

    # 90
    def test_if_infer_and_while(self):
        """Check if and while"""
        input = """
        Function: main
        Body:
            Var: b = 5,i = "True",res,j;
            If bool_of_string(i) Then
                res = b * b;
            ElseIf j Then
                While j == 0 Do
                    res = res + b;
                EndWhile.
            EndIf.
        EndBody."""
        expect = str(TypeMismatchInExpression(
            BinaryOp('==', Id('j'), IntLiteral(0))))
        self.assertTrue(TestChecker.test(input, expect, 489))

    # 91
    def test_if_infer_and_do_while(self):
        """Check if and do while"""
        input = """
        Function: main
        Body:
            Var: b = 9.5,i = "True",res,j;
            If bool_of_string(i) Then
                res = b *. b;
            ElseIf j Then
                Do
                    res = res +. 1.5;
                    printStrLn(string_of_float(res));
                While string_of_bool(j) EndDo.
            EndIf.
        EndBody."""
        expect = str(TypeMismatchInStatement(
            Dowhile(([], [Assign(Id("res"), BinaryOp("+.", Id("res"), FloatLiteral(1.5))),
                          CallStmt(Id("printStrLn"), [CallExpr(Id("string_of_float"), [Id("res")])])]),
                    CallExpr(Id("string_of_bool"), [Id("j")]))))
        self.assertTrue(TestChecker.test(input, expect, 490))

    # 92
    def test_predefine_in_para(self):
        """Check array assignment"""
        input = """
        Function: main
        Body:
            Var: y = 8.9;
            foo(1, int_of_float(y));
        EndBody.

        Function: foo
        Parameter: x, y
        Body:
            Var: res, ans;
            res = x + 100;
            ans = y +. 1000.59;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(
            BinaryOp('+.', Id('y'), FloatLiteral(1000.59))))
        self.assertTrue(TestChecker.test(input, expect, 491))

    # 93
    def test_predefine_in_para_float(self):
        """Check array assignment"""
        input = """
        Function: main
        Body:
            Var: y = 9;
            foo(1, float_to_int(y));
        EndBody.

        Function: foo
        Parameter: x, y
        Body:
            For (x = 1, x <= 100, y) Do
                print("There and back again");
            EndFor.
        EndBody.
        """
        expect = str(TypeMismatchInStatement(
            For(Id("x"), IntLiteral(1), BinaryOp("<=", Id("x"), IntLiteral(100)), Id("y"),
                ([], [CallStmt(Id("print"), [StringLiteral("There and back again")])]))))
        self.assertTrue(TestChecker.test(input, expect, 492))

    # 94
    def test_predefine_in_para_string(self):
        """Check array assignment"""
        input = """
        Function: main
        Body:
            Var: y = 9;
            foo("game of shadow", y);
        EndBody.

        Function: foo
        Parameter: x, y
        Body:
            print(x);
            printStrLn(y);
        EndBody.
        """
        expect = str(TypeMismatchInStatement(
            CallStmt(Id('printStrLn'), [Id('y')])))
        self.assertTrue(TestChecker.test(input, expect, 493))

    # 95
    def test_assign_void_type(self):
        """Check array assignment"""
        input = """
        Function: main
        Body:
            Var: a;
            foo();
            a = foo();
        EndBody.

        Function: foo
        Body:
            print("rog");
            printStrLn("rsa");
        EndBody.
        """
        expect = str(TypeMismatchInStatement(
            Assign(Id('a'), CallExpr(Id('foo'), []))))
        self.assertTrue(TestChecker.test(input, expect, 494))

    # 96
    def test_infer_function_assign(self):
        """Check function infer type"""
        input = """
        Function: main
        Parameter: x, y
        Body:
            Var: z;
            While (True) Do
                z = main(1, main(x, True));
            EndWhile.
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 495))

    # 97
    def test_predefine_bool(self):
        """Check predefine boolean function"""
        input = """
        Function: main
        Body:
            Var: y = 9;
            foo("TLC", bool_of_string(string_of_int(y)));
        EndBody.

        Function: foo
        Parameter: x, y
        Body:
            Var: res;
            print(x);
            res = !!y;
            Return True;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(
            Return(BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input, expect, 496))

    # 98
    def test_variable_out_of_scope(self):
        """Check variable used in another scope"""
        input = """
        Function: main
        Body:
            While True Do
                Var: a;
                a = "WWE";
            EndWhile.
            print(a);
            Return 1;
        EndBody."""
        expect = str(Undeclared(Identifier(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 497))

    # 99
    def test_function_name(self):
        """Check function in different scope"""
        input = """
        Function: foo
        Body:
            print("Now or never");
            Return;
        EndBody.
        Function: goo
        Body:
            foo();
        EndBody.
        Function: main
        Body:
            Var: foo;
            foo();
        EndBody.
        """
        expect = str(Undeclared(Function(), "foo"))
        self.assertTrue(TestChecker.test(input, expect, 498))

    # 100
    def test_same_name_variable(self):
        """Check same name variable in different scope"""
        input = """
        Function: main
        Body:
            Var: a = 1;
            If bool_of_string("True") Then
                Var: a;
                print(string_of_float(a));
            EndIf.
            print(string_of_int(a));
            print();
        EndBody.
        """
        expect = str(TypeMismatchInStatement(
            CallStmt(Id('print'), [])))
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_shit(self):
        """Check same name variable in different scope"""
        input = """
        Function: foo
        Parameter: x
        Body:
            Return 10;
        EndBody.
        Function: main
        Body:
            If foo(foo(5)) Then EndIf.
        EndBody.
        """
        expect = str(TypeMismatchInStatement(
            If([(CallExpr(Id("foo"), [CallExpr(Id("foo"), [IntLiteral(5)])]), [], [])], ([], []))))
        self.assertTrue(TestChecker.test(input, expect, 500))



