import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    # 1
    def test_simple_program_ast(self):
        """Simple program: int main() {} """
        input = """Var:x;"""

        expect = Program([VarDecl(Id("x"), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 300))

    # 2
    def test_scalar_number_declaration_ast(self):
        """Variable declaration scalar """
        input = """Var: a = 5;"""
        expect = Program([VarDecl(Id("a"), [], IntLiteral(5))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    # 3
    def test_multi_var_declaration_ast(self):
        """Multiple variable declarations scalar"""
        input = """Var: a, b, c, d;"""
        expect = Program([VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None), VarDecl(Id("c"), [], None),
                          VarDecl(Id("d"), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 302))

    # 4
    def test_multi_var_declaration_multi_line_ast(self):
        """Multiple variable declarations scalar on many lines"""
        input = """ Var: a;
                    Var: num1;
                    Var: res2;
                    Var: ironMan;
                """
        expect = Program([VarDecl(Id("a"), [], None), VarDecl(Id("num1"), [], None), VarDecl(Id("res2"), [], None),
                          VarDecl(Id("ironMan"), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    # 5
    def test_composite_decl_single_line_init_ast(self):
        """test composite decl 1 line 1 initialized var"""
        input = """Var: y[2] = {12.2e-1, 2.7};"""
        expect = Program([VarDecl(Id("y"), [2], ArrayLiteral([FloatLiteral(1.22), FloatLiteral(2.7)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    # 6
    def test_multi_var_declaration_init_ast(self):
        """Multiple variable declarations initialized """
        input = """Var: c, d = 6, e, f;"""
        expect = Program([VarDecl(Id("c"), [], None), VarDecl(Id("d"), [], IntLiteral(6)), VarDecl(Id("e"), [], None),
                          VarDecl(Id("f"), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    # 7
    def test_composite_var_declaration_ast(self):
        """Composite variable declaration """
        input = """Var: arr[2];"""
        expect = Program(
            [VarDecl(Id("arr"), [2], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 306))

    # 8
    def test_composite_var_declaration_init_ast(self):
        """Composite variable declaration initialized """
        input = """Var: b[2][3]={{1,2,3},{4,5,6}};"""
        expect = Program([VarDecl(Id("b"), [2, 3], ArrayLiteral(
            [ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)]),
             ArrayLiteral([IntLiteral(4), IntLiteral(5), IntLiteral(6)])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 307))

    # 9
    def test_multi_type_var_declaration_init_ast(self):
        """Multiple variable declaration with different type initialized """
        input = """Var: name = "Charles", num = 8.9, isTrue = True, hexNum = 0XABC;"""
        expect = Program([VarDecl(Id("name"), [], StringLiteral("Charles")), VarDecl(Id("num"), [], FloatLiteral(8.9)),
                          VarDecl(Id("isTrue"), [], BooleanLiteral(True)), VarDecl(Id("hexNum"), [], IntLiteral(2748))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    # 10
    def test_multi_line_var_declaration_init_ast(self):
        """Multiple variable declaration on multiple lines with different type initialized """
        input = """ Var: x = 1234, b[2] = {20.e-10, 35e3};
                    Var: arr[2][4] = {{2,3,4,5},{78,89,100,5349}};
                    Var: planet = "Earth";
                    Var: pi = 3.4182354;
                    Var: isCool = True;
                """
        expect = Program([VarDecl(Id("x"), [], IntLiteral(1234)),
                          VarDecl(Id("b"), [2], ArrayLiteral([FloatLiteral(2e-09), FloatLiteral(35000.0)])),
                          VarDecl(Id("arr"), [2, 4], ArrayLiteral(
                              [ArrayLiteral([IntLiteral(2), IntLiteral(3), IntLiteral(4), IntLiteral(5)]),
                               ArrayLiteral([IntLiteral(78), IntLiteral(89), IntLiteral(100), IntLiteral(5349)])])),
                          VarDecl(Id("planet"), [], StringLiteral("Earth")),
                          VarDecl(Id("pi"), [], FloatLiteral(3.4182354)),
                          VarDecl(Id("isCool"), [], BooleanLiteral(True))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 309))

    # 11
    def test_empty_function_ast(self):
        """Empty function"""
        input = """
        Function: main
            Body:
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"), [], ([], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    # 12
    def test_empty_function_with_global_declaration_ast(self):
        """Empty function with global declaration"""
        input = """
        Var: x, y, z = 3, e, f;
        Var: arr[10];
        Var: age = 20;
        Var: isValid = True;
        Var: a[5] = {1,4,3,2,0};
        Function: main
            Body:
            EndBody.
        """
        expect = Program([VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None), VarDecl(Id("z"), [], IntLiteral(3)),
                          VarDecl(Id("e"), [], None), VarDecl(Id("f"), [], None), VarDecl(Id("arr"), [10], None),
                          VarDecl(Id("age"), [], IntLiteral(20)), VarDecl(Id("isValid"), [], BooleanLiteral(True)),
                          VarDecl(Id("a"), [5], ArrayLiteral(
                              [IntLiteral(1), IntLiteral(4), IntLiteral(3), IntLiteral(2), IntLiteral(0)])),
                          FuncDecl(Id("main"), [], ([], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))

    # 13
    def test_empty_function_with_parameter_ast(self):
        """Empty function with parameter"""
        input = """
        Function: foo
        Parameter: a[5], b
        Body:
        EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("a"), [5], None), VarDecl(Id("b"), [], None)], ([], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))

    # 14
    def test_function_with_variable_declaration_ast(self):
        """Empty function with parameter"""
        input = """
        Function: goo
        Body:
            Var: age = 20;
        EndBody.
        """
        expect = Program([FuncDecl(Id("goo"), [], ([VarDecl(Id("age"), [], IntLiteral(20))], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))

    # 15
    def test_arithmetic_expression_ast(self):
        """Arithmetic expression"""
        input = """
        Function: main
        Body:
            x = 1 + 2 - 3 * 4;
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"), [], ([], [Assign(Id("x"), BinaryOp("-", BinaryOp("+", IntLiteral(1),
                                                                                                IntLiteral(2)),
                                                                                  BinaryOp("*", IntLiteral(3),
                                                                                           IntLiteral(4))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))

    # 16
    def test_arithmetic_float_expression_ast(self):
        """Arithmetic float expression"""
        input = """
        Var: x,y;
        Function: main
        Body:
            x = 5.8 -. 1.2 +. 9.0;
            y = 100 *. x \\. 78.9e10;
        EndBody.
        """
        expect = Program([VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None), FuncDecl(Id("main"), [], ([], [
            Assign(Id("x"), BinaryOp("+.", BinaryOp("-.", FloatLiteral(5.8), FloatLiteral(1.2)), FloatLiteral(9.0))),
            Assign(Id("y"), BinaryOp("\.", BinaryOp("*.", IntLiteral(100), Id("x")), FloatLiteral(789000000000.0)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))

    # 17
    def test_sign_expression_ast(self):
        """Sign expression"""
        input = """
        Var: x, y;
        Function: foo
        Body:
            x = -5;
            y = -.10; 
        EndBody.
        """
        expect = Program([VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None), FuncDecl(Id("foo"), [], (
            [], [Assign(Id("x"), UnaryOp("-", IntLiteral(5))), Assign(Id("y"), UnaryOp("-.", IntLiteral(10)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))

    # 18
    def test_logical_not_expression_ast(self):
        """Test logical not expression"""
        input = """
        Var: x,y;
        Function: main
        Body:
            x = !y;
        EndBody.
        """
        expect = Program([VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None),
                          FuncDecl(Id("main"), [], ([], [Assign(Id("x"), UnaryOp("!", Id("y")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 317))

    # 19
    def test_logical_and_expression_ast(self):
        """Test logical and expression"""
        input = """
        Var: x,y;
        Function: koo
        Body:
            x = y && False;
        EndBody.
        """
        expect = Program([VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None), FuncDecl(Id("koo"), [], (
            [], [Assign(Id("x"), BinaryOp("&&", Id("y"), BooleanLiteral(False)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))

    # 20
    def test_logical_or_expression_ast(self):
        """Test logical or expression"""
        input = """
        Var: x,y;
        Function: main
        Body:
            x = y || True;
        EndBody.
        """
        expect = Program([VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None), FuncDecl(Id("main"), [], (
            [], [Assign(Id("x"), BinaryOp("||", Id("y"), BooleanLiteral(True)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))

    # 21
    def test_relational_integer_expression_ast(self):
        """Test relational integer expression"""
        input = """
        Var: x,y,z,t,w,q;
        Function: main
        Body:
            x = y == 5;
            y = x != 0;
            z = x < y;
            t = y > z;
            w = t >= 100;
            q = w <= 200;
        EndBody.
        """
        expect = Program([VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None), VarDecl(Id("z"), [], None),
                          VarDecl(Id("t"), [], None), VarDecl(Id("w"), [], None), VarDecl(Id("q"), [], None),
                          FuncDecl(Id("main"), [], ([], [Assign(Id("x"), BinaryOp("==", Id("y"), IntLiteral(5))),
                                                         Assign(Id("y"), BinaryOp("!=", Id("x"), IntLiteral(0))),
                                                         Assign(Id("z"), BinaryOp("<", Id("x"), Id("y"))),
                                                         Assign(Id("t"), BinaryOp(">", Id("y"), Id("z"))),
                                                         Assign(Id("w"), BinaryOp(">=", Id("t"), IntLiteral(100))),
                                                         Assign(Id("q"), BinaryOp("<=", Id("w"), IntLiteral(200)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))

    # 22
    def test_relational_float_expression_ast(self):
        """Test relational float expression"""
        input = """
        Var: x,y,z,t,w;
        Function: loo
        Body:
            x = y =/= 16.9e32;
            y = x <. 15.e-52;
            z = y >. 9e10;
            t = z <=. 987.3456;
            w = t >=. 0.7;
        EndBody.
        """
        expect = Program([VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None), VarDecl(Id("z"), [], None),
                          VarDecl(Id("t"), [], None), VarDecl(Id("w"), [], None), FuncDecl(Id("loo"), [], ([], [
                Assign(Id("x"), BinaryOp("=/=", Id("y"), FloatLiteral(1.69e+33))),
                Assign(Id("y"), BinaryOp("<.", Id("x"), FloatLiteral(1.5e-51))),
                Assign(Id("z"), BinaryOp(">.", Id("y"), FloatLiteral(90000000000.0))),
                Assign(Id("t"), BinaryOp("<=.", Id("z"), FloatLiteral(987.3456))),
                Assign(Id("w"), BinaryOp(">=.", Id("t"), FloatLiteral(0.7)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))

    # 23
    def test_index_expression_ast(self):
        """Test index expression"""
        input = """
        Var: a,b;
        Function: zoo
        Body:
            a[7] = b[2] + 4;
        EndBody.
        """
        expect = Program([VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None), FuncDecl(Id("zoo"), [], ([], [
            Assign(ArrayCell(Id("a"), [IntLiteral(7)]),
                   BinaryOp("+", ArrayCell(Id("b"), [IntLiteral(2)]), IntLiteral(4)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 322))

    # 24
    def test_index_expression_with_function_ast(self):
        """Test index expression with function inside"""
        input = """
        Var: a,b;
        Function: coo
        Body:
            x = y[10*func(15)];
        EndBody.
        """
        expect = Program([VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None), FuncDecl(Id("coo"), [], ([], [
            Assign(Id("x"),
                   ArrayCell(Id("y"), [BinaryOp("*", IntLiteral(10), CallExpr(Id("func"), [IntLiteral(15)]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 323))

    # 25
    def test_index_nested_expression_ast(self):
        """Test index nested expression"""
        input = """
        Var: g,h,tree;
        Function: doo
        Body:
            a[3 + foo(2)] = a[b[2][3]] + 4;
        EndBody.
        """
        expect = Program([VarDecl(Id("g"), [], None), VarDecl(Id("h"), [], None), VarDecl(Id("tree"), [], None),
                          FuncDecl(Id("doo"), [], ([], [Assign(
                              ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(3), CallExpr(Id("foo"), [IntLiteral(2)]))]),
                              BinaryOp("+", ArrayCell(Id("a"), [ArrayCell(Id("b"), [IntLiteral(2), IntLiteral(3)])]),
                                       IntLiteral(4)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 324))

    # 26
    def test_function_call_expression_no_para_ast(self):
        """Test function call expression with no parameter"""
        input = """
        Var: j,k,l;
        Function: eoo
        Body:
            j = hoo();
        EndBody.
        """
        expect = Program([VarDecl(Id("j"), [], None), VarDecl(Id("k"), [], None), VarDecl(Id("l"), [], None),
                          FuncDecl(Id("eoo"), [], ([], [Assign(Id("j"), CallExpr(Id("hoo"), []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    # 27
    def test_function_call_expression_with_para_ast(self):
        """Test function call expression with with parameter"""
        input = """
        Var: q,w,e,r;
        Function: goo
        Body:
            q = foo(w - 5, e *  0xFF, r + 0o567);
        EndBody.
        """
        expect = Program([VarDecl(Id("q"), [], None), VarDecl(Id("w"), [], None),
                          VarDecl(Id("e"), [], None), VarDecl(Id("r"), [], None), FuncDecl(Id("goo"), [], ([], [
                Assign(Id("q"), CallExpr(Id("foo"), [BinaryOp("-", Id("w"), IntLiteral(5)),
                                                     BinaryOp("*", Id("e"), IntLiteral(255)),
                                                     BinaryOp("+", Id("r"), IntLiteral(375))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    # 28
    def test_multiple_expression_ast(self):
        """Test multiple expression"""
        input = """
        Var: a,b,c,d,e,f,g,h,t,res = 1;
        Function: joo
        Parameter: x, y
        Body:
            x = foo(30.5);
            y = x[a[15][3]] - 9.7;
            b = -.79;
            d = !y;
            f = 1235 \\ 5;
            g = t && True;
            h = x <=. y;
        EndBody.
        """
        expect = Program([VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None), VarDecl(Id("c"), [], None),
                          VarDecl(Id("d"), [], None), VarDecl(Id("e"), [], None), VarDecl(Id("f"), [], None),
                          VarDecl(Id("g"), [], None), VarDecl(Id("h"), [], None), VarDecl(Id("t"), [], None),
                          VarDecl(Id("res"), [], IntLiteral(1)),
                          FuncDecl(Id("joo"), [VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None)], ([], [
                              Assign(Id("x"), CallExpr(Id("foo"), [FloatLiteral(30.5)])), Assign(Id("y"), BinaryOp("-",
                                                                                                                   ArrayCell(
                                                                                                                       Id(
                                                                                                                           "x"),
                                                                                                                       [
                                                                                                                           ArrayCell(
                                                                                                                               Id(
                                                                                                                                   "a"),
                                                                                                                               [
                                                                                                                                   IntLiteral(
                                                                                                                                       15),
                                                                                                                                   IntLiteral(
                                                                                                                                       3)])]),
                                                                                                                   FloatLiteral(
                                                                                                                       9.7))),
                              Assign(Id("b"), UnaryOp("-.", IntLiteral(79))), Assign(Id("d"), UnaryOp("!", Id("y"))),
                              Assign(Id("f"), BinaryOp("\\", IntLiteral(1235), IntLiteral(5))),
                              Assign(Id("g"), BinaryOp("&&", Id("t"), BooleanLiteral(True))),
                              Assign(Id("h"), BinaryOp("<=.", Id("x"), Id("y")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 327))

    # 29
    def test_if_statement_ast(self):
        """Test if statement"""
        input = """
        Function: main
        Body:
            If a == b Then a = a + 1;
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"), [], ([], [
            If([(BinaryOp("==", Id("a"), Id("b")), [], [Assign(Id("a"), BinaryOp("+", Id("a"), IntLiteral(1)))])],
               ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 328))

    # 30
    def test_if_else_statement_ast(self):
        """Test if else statement"""
        input = """
        Function: main
        Body:
            If x =/= 78.92 Then 
                ans = ans * ans;
            Else
                ans = ans - 1;
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"), [], ([], [If([(BinaryOp("=/=", Id("x"), FloatLiteral(78.92)), [], [
            Assign(Id("ans"), BinaryOp("*", Id("ans"), Id("ans")))])], ([], [
            Assign(Id("ans"), BinaryOp("-", Id("ans"), IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))

    # 31
    def test_if_elseif_statement_ast(self):
        """Test if elseif statement"""
        input = """
        Function: main
        Body:
            If !a Then 
                b = a + c - d + 100;
            ElseIf b == True Then
                a = a % 10;
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"), [], ([], [If([(UnaryOp("!", Id("a")), [], [
            Assign(Id("b"), BinaryOp("+", BinaryOp("-", BinaryOp("+", Id("a"), Id("c")), Id("d")), IntLiteral(100)))]),
                                                             (BinaryOp("==", Id("b"), BooleanLiteral(True)), [], [
                                                                 Assign(Id("a"),
                                                                        BinaryOp("%", Id("a"), IntLiteral(10)))])],
                                                            ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 330))

    # 32
    def test_if_elseif_else_statement_ast(self):
        """Test if elseif else statement"""
        input = """
        Function: main
        Body:
            If !a Then 
                b = a + c - d + 100;
                e = b % 15;
                z = z * b;
            ElseIf b == True Then
                a = a % 10;
                c = c \\ 2;
                f = f \\. 15.97;
            Else
                a = b;
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"), [], ([], [If([(UnaryOp("!", Id("a")), [], [
            Assign(Id("b"), BinaryOp("+", BinaryOp("-", BinaryOp("+", Id("a"), Id("c")), Id("d")), IntLiteral(100))),
            Assign(Id("e"), BinaryOp("%", Id("b"), IntLiteral(15))), Assign(Id("z"), BinaryOp("*", Id("z"), Id("b")))]),
                                                             (BinaryOp("==", Id("b"), BooleanLiteral(True)), [],
                                                              [Assign(Id("a"), BinaryOp("%", Id("a"), IntLiteral(10))),
                                                               Assign(Id("c"), BinaryOp("\\", Id("c"), IntLiteral(2))),
                                                               Assign(Id("f"),
                                                                      BinaryOp("\\.", Id("f"), FloatLiteral(15.97)))])],
                                                            ([], [Assign(Id("a"), Id("b"))]))]))])

    # 33
    def test_if_empty_statement_ast(self):
        """Test if empty statement"""
        input = """
        Function: main
        Parameter: x, y
        Body:
            If y == True Then 

            ElseIf x > 12.e3 Then

            Else

            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"), [VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None)], ([], [If(
            [(BinaryOp("==", Id("y"), BooleanLiteral(True)), [], []),
             (BinaryOp(">", Id("x"), FloatLiteral(12000.0)), [], [])], ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))

    # 34
    def test_for_statement_ast(self):
        """Test for statement"""
        input = """
        Function: main
        Body:
            For(i = 1, i < 10, 1) Do
                x =  x + 1;
                y = z[p[2]];
            EndFor.
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"), [], ([], [
            For(Id("i"), IntLiteral(1), BinaryOp("<", Id("i"), IntLiteral(10)), IntLiteral(1), ([], [
                Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(1))),
                Assign(Id("y"), ArrayCell(Id("z"), [ArrayCell(Id("p"), [IntLiteral(2)])]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 333))

    # 35
    def test_while_statement_ast(self):
        """Test while statement"""
        input = """
        Function: main
        Body:
            While x < 5 Do
                 a = b - c;
            EndWhile.
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"), [], (
            [],
            [While(BinaryOp("<", Id("x"), IntLiteral(5)), ([], [Assign(Id("a"), BinaryOp("-", Id("b"), Id("c")))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))

    # 36
    def test_do_while_statement_ast(self):
        """Test do while statement"""
        input = """
        Function: loo
        Body:
            Do 
                num = num + 1;
            While num <= 100 EndDo.
        EndBody.
        """
        expect = Program([FuncDecl(Id("loo"), [], ([], [
            Dowhile(([], [Assign(Id("num"), BinaryOp("+", Id("num"), IntLiteral(1)))]),
                    BinaryOp("<=", Id("num"), IntLiteral(100)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))

    # 37
    def test_break_statement_ast(self):
        """Test break statement"""
        input = """
        Function: qoo
        Body:
            Break;
        EndBody.
        """
        expect = Program([FuncDecl(Id("qoo"), [], ([], [Break()]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 336))

    # 38
    def test_continue_statement_ast(self):
        """Test continue statement"""
        input = """
        Function: woo
        Body:
            Continue;
        EndBody.
        """
        expect = Program([FuncDecl(Id("woo"), [], ([], [Continue()]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 337))

    # 39
    def test_call_statement_ast(self):
        """Test call statement"""
        input = """
        Function: main
        Body:
            foo(2 + x, 4. \\. y);
            goo();
            func(x + y);
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"), [], ([], [
            CallStmt(Id("foo"), [BinaryOp("+", IntLiteral(2), Id("x")), BinaryOp("\\.", FloatLiteral(4.0), Id("y"))]),
            CallStmt(Id("goo"), []), CallStmt(Id("func"), [BinaryOp("+", Id("x"), Id("y"))])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 338))

    # 40
    def test_return_statement_ast(self):
        """Test return statement"""
        input = """
        Function: eoo
        Body:
            Return;
        EndBody.
        """
        expect = Program([FuncDecl(Id("eoo"), [], ([], [Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 339))

    # 41
    def test_if_nested_statement_ast(self):
        """Test if nested statement"""
        input = """
        Function: main
        Parameter: score
        Body:
            If age > 18 Then 
                If height < 20 Then
                    print("Congratulation");
                EndIf.
            ElseIf age > 13 Then
                writeln("Good luck");
            Else
                writeln("Adios");
                If score > 100 Then
                    writeln("Secret unlocked");
                EndIf.
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"),
                                   [VarDecl(Id("score"), [], None)],
                                   ([], [If([(BinaryOp(">", Id("age"), IntLiteral(18)), [],
                                              [If([(BinaryOp("<", Id("height"), IntLiteral(20)),
                                                    [], [CallStmt(Id("print"), [StringLiteral("Congratulation")])])],
                                                  ([], []))]),
                                             (BinaryOp(">", Id("age"), IntLiteral(13)), [],
                                              [CallStmt(Id("writeln"), [StringLiteral("Good luck")])])],
                                            ([], [CallStmt(Id("writeln"), [StringLiteral("Adios")]),
                                                  If([(BinaryOp(">", Id("score"), IntLiteral(100)), [],
                                                       [CallStmt(Id("writeln"), [StringLiteral("Secret unlocked")])])],
                                                     ([], []))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 340))

    # 42
    def test_if_with_var_decl_statement_ast(self):
        """Test if statement with variable declaration"""
        input = """
        Function: poo
        Parameter: x, y
        Body:
            Var: r = 10., v;
            v = (4. \\. 3.) *. 3.14 *. r *. r *. r;
            If y == True Then 
                v = v + 1;
            ElseIf x > 12.e3 Then
                v = 0O77;
            Else
                v = 120000e-1;
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("poo"),
                                   [VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None)],
                                   ([VarDecl(Id("r"), [], FloatLiteral(10.0)), VarDecl(Id("v"), [], None)],
                                    [Assign(Id("v"), BinaryOp("*.", BinaryOp("*.",
                                                                             BinaryOp("*.", BinaryOp("*.",
                                                                                                     BinaryOp("\\.",
                                                                                                              FloatLiteral(
                                                                                                                  4.0),
                                                                                                              FloatLiteral(
                                                                                                                  3.0)),
                                                                                                     FloatLiteral(
                                                                                                         3.14)),
                                                                                      Id("r")), Id("r")), Id("r"))),
                                     If([(BinaryOp("==", Id("y"), BooleanLiteral(True)), [],
                                          [Assign(Id("v"), BinaryOp("+", Id("v"),
                                                                    IntLiteral(1)))]),
                                         (BinaryOp(">", Id("x"), FloatLiteral(12000.0)),
                                          [], [Assign(Id("v"), IntLiteral(63))])],
                                        ([], [Assign(Id("v"), FloatLiteral(12000.0))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 341))

    # 43
    def test_if_with_var_decl_inside_statement_ast(self):
        """Test if statement with variable declaration inside body"""
        input = """
        Function: ioo
        Parameter: x, y
        Body:
            Var: r = 10., v, arr[2][5][6];
            If y == True Then 
                Var: isTrue = False;
                x = x - 1;
            ElseIf x > 12.e3 Then
                isTrue = !x;
            Else
                isTrue = True;
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("ioo"), [VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None)], (
            [VarDecl(Id("r"), [], FloatLiteral(10.0)), VarDecl(Id("v"), [], None), VarDecl(Id("arr"), [2, 5, 6], None)],
            [
                If([(BinaryOp("==", Id("y"), BooleanLiteral(True)), [VarDecl(Id("isTrue"), [], BooleanLiteral(False))],
                     [Assign(Id("x"), BinaryOp("-", Id("x"), IntLiteral(1)))]),
                    (BinaryOp(">", Id("x"), FloatLiteral(12000.0)), [], [Assign(Id("isTrue"), UnaryOp("!", Id("x")))])],
                   ([], [Assign(Id("isTrue"), BooleanLiteral(True))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 342))

    # 44
    def test_for_statement_null_ast(self):
        """Test for statement with no body  """
        input = """
        Function: uoo
        Body:
            For(k = 1, k < 10, -1) Do EndFor. 
        EndBody.
        """
        expect = Program([FuncDecl(Id("uoo"), [], ([], [
            For(Id("k"), IntLiteral(1), BinaryOp("<", Id("k"), IntLiteral(10)), UnaryOp("-", IntLiteral(1)),
                ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 343))

    # 45
    def test_for_statement_with_call_stmt_ast(self):
        """Test for statement with call statement  """
        input = """
        Function: yoo
        Parameter: a, b[1]
        Body:
            Var: x, y, arr[3] = {2, 3, 4}, res[10];
            For(k = 0, k < 10, 1) Do
                 res[k] = x + y;
                 x = x - y;
            EndFor. 
        EndBody.
        """
        expect = Program([FuncDecl(Id("yoo"), [VarDecl(Id("a"), [], None), VarDecl(Id("b"), [1], None)], (
            [VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None),
             VarDecl(Id("arr"), [3], ArrayLiteral([IntLiteral(2), IntLiteral(3), IntLiteral(4)])),
             VarDecl(Id("res"), [10], None)], [
                For(Id("k"), IntLiteral(0), BinaryOp("<", Id("k"), IntLiteral(10)), IntLiteral(1), ([], [
                    Assign(ArrayCell(Id("res"), [Id("k")]), BinaryOp("+", Id("x"), Id("y"))),
                    Assign(Id("x"), BinaryOp("-", Id("x"), Id("y")))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 344))

    # 46
    def test_for_nested_statement_ast(self):
        """Test nested for statement"""
        input = """
        Function: xoo
            Body:
                For(i = 1, i < 10, -2) Do 
                    For(j = 0, j < 15, 1) Do
                        goo(arr[i][j]);
                    EndFor.
                    noo();
                    i = -i;
                    x = i + i;
                EndFor. 
            EndBody.
        """
        expect = Program([FuncDecl(Id("xoo"), [], ([], [
            For(Id("i"), IntLiteral(1), BinaryOp("<", Id("i"), IntLiteral(10)), UnaryOp("-", IntLiteral(2)), ([], [
                For(Id("j"), IntLiteral(0), BinaryOp("<", Id("j"), IntLiteral(15)), IntLiteral(1),
                    ([], [CallStmt(Id("goo"), [ArrayCell(Id("arr"), [Id("i"), Id("j")])])])), CallStmt(Id("noo"), []),
                Assign(Id("i"), UnaryOp("-", Id("i"))), Assign(Id("x"), BinaryOp("+", Id("i"), Id("i")))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 345))

    # 47
    def test_while_statement_with_var_decl_ast(self):
        """Test while statement with var declaration"""
        input = """
        Var: m, n[10];
        Function: coo
        Parameter: x[1], y[2]
        Body:
            Var: res = 0, arr[2] = {1.3, 4.5};
            While x >= 100 Do
                 Var: isTrue = True;
                 moo(x);
                 m = -r;
            EndWhile.
        EndBody.
        """
        expect = Program([VarDecl(Id("m"), [], None), VarDecl(Id("n"), [10], None),
                          FuncDecl(Id("coo"), [VarDecl(Id("x"), [1], None), VarDecl(Id("y"), [2], None)], (
                              [VarDecl(Id("res"), [], IntLiteral(0)),
                               VarDecl(Id("arr"), [2], ArrayLiteral([FloatLiteral(1.3), FloatLiteral(4.5)]))], [
                                  While(BinaryOp(">=", Id("x"), IntLiteral(100)), (
                                      [VarDecl(Id("isTrue"), [], BooleanLiteral(True))],
                                      [CallStmt(Id("moo"), [Id("x")]), Assign(Id("m"), UnaryOp("-", Id("r")))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 346))

    # 48
    def test_while_nested_statement_ast(self):
        """Test while nested statement"""
        input = """
        Function: doo
        Body:
            Var: x, y[2][3] = {{1,2,3},{4,5,6}};
            While num >= 79 Do
                While j != False Do
                    If a == b Then
                        c = a + b;
                    EndIf.
                EndWhile.
                hoo("Hello World");
            EndWhile.
        EndBody.
        """
        expect = Program([FuncDecl(Id("doo"), [], ([VarDecl(Id("x"), [], None), VarDecl(Id("y"), [2, 3], ArrayLiteral(
            [ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)]),
             ArrayLiteral([IntLiteral(4), IntLiteral(5), IntLiteral(6)])]))], [
                                                       While(BinaryOp(">=", Id("num"), IntLiteral(79)), ([], [
                                                           While(BinaryOp("!=", Id("j"), BooleanLiteral(False)), ([], [
                                                               If([(BinaryOp("==", Id("a"), Id("b")), [], [
                                                                   Assign(Id("c"), BinaryOp("+", Id("a"), Id("b")))])],
                                                                  ([], []))])),
                                                           CallStmt(Id("hoo"), [StringLiteral("Hello World")])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 347))

    # 49
    def test_do_while_nested_statement_ast(self):
        """Test do while nested statement"""
        input = """
        Function: joo
        Body:
            Do 
                Do
                    calculate(x);
                    ans = x + y - z * 5;
                While i >= 100 EndDo.
                process(x);
            While num <= 1000 EndDo.
        EndBody.
        """
        expect = Program([FuncDecl(Id("joo"), [], (
            [], [Dowhile(([], [Dowhile(([],
                                        [CallStmt(Id("calculate"), [Id("x")]),
                                         Assign(Id("ans"), BinaryOp("-", BinaryOp("+", Id("x"), Id("y")),
                                                                    BinaryOp("*", Id("z"), IntLiteral(5))))]),
                                       BinaryOp(">=", Id("i"), IntLiteral(100))), CallStmt(Id("process"), [Id("x")])]),
                         BinaryOp("<=", Id("num"), IntLiteral(1000)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 348))

    # 50
    def test_return_literal_statement_ast(self):
        """Test do while nested statement"""
        input = """
        Function: roo
        Body:
            Return 100;
        EndBody.
        """
        expect = Program([FuncDecl(Id("roo"), [], ([], [Return(IntLiteral(100))]))])

        self.assertTrue(TestAST.checkASTGen(input, expect, 349))

    # 51
    def test_return_function_statement_ast(self):
        """Test return function statement"""
        input = """
        Function: shoo
        Body:
            Return foo(x);
        EndBody.
        """
        expect = Program([FuncDecl(Id("shoo"), [], ([], [Return(CallExpr(Id("foo"), [Id("x")]))]))])

        self.assertTrue(TestAST.checkASTGen(input, expect, 350))

    # 52
    def test_multiple_function_decl_ast(self):
        """Test multiple function declaration statement"""
        input = """
        Var: x;
        Function: fact
        Parameter: n
        Body:
            If n == 0 Then
                Return 1;
            Else
                Return n * fact (n - 1);
            EndIf.
        EndBody.
        Function: main
        Body:
            x = 10;
            fact(x);
        EndBody.
        """
        expect = Program([VarDecl(Id("x"), [], None), FuncDecl(Id("fact"), [VarDecl(Id("n"), [], None)], ([], [
            If([(BinaryOp("==", Id("n"), IntLiteral(0)), [], [Return(IntLiteral(1))])], (
                [],
                [Return(BinaryOp("*", Id("n"), CallExpr(Id("fact"), [BinaryOp("-", Id("n"), IntLiteral(1))])))]))])),
                          FuncDecl(Id("main"), [],
                                   ([], [Assign(Id("x"), IntLiteral(10)), CallStmt(Id("fact"), [Id("x")])]))])

        self.assertTrue(TestAST.checkASTGen(input, expect, 351))

    # 53
    def test_if_for_stmt_ast(self):
        """Test if for statement"""
        input = """
        Var: x, y[3] = {12., 45e5, 98.e-8};
        Function: qoo
        Parameter: a, b
        Body:
            For(k = 0, k < 3, 1) Do
                y[k] = b *. a;
                If x == 0 Then
                    Return 1;
                ElseIf x =/= 100.1234 Then
                    Return n * fact (n - 1);
                EndIf.
            EndFor.
        EndBody.
        Function: woo
        Body:
            y[3] = 10.45;
            eoo(x);
        EndBody.
        """
        expect = Program([VarDecl(Id("x"), [], None), VarDecl(Id("y"), [3], ArrayLiteral(
            [FloatLiteral(12.0), FloatLiteral(4500000.0), FloatLiteral(9.8e-07)])),
                          FuncDecl(Id("qoo"), [VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None)], ([], [
                              For(Id("k"), IntLiteral(0), BinaryOp("<", Id("k"), IntLiteral(3)), IntLiteral(1), ([], [
                                  Assign(ArrayCell(Id("y"), [Id("k")]), BinaryOp("*.", Id("b"), Id("a"))), If(
                                      [(BinaryOp("==", Id("x"), IntLiteral(0)), [], [Return(IntLiteral(1))]), (
                                          BinaryOp("=/=", Id("x"), FloatLiteral(100.1234)), [], [Return(
                                              BinaryOp("*", Id("n"),
                                                       CallExpr(Id("fact"),
                                                                [BinaryOp("-", Id("n"), IntLiteral(1))])))])],
                                      ([], []))]))])), FuncDecl(Id("woo"), [], (
                [],
                [Assign(ArrayCell(Id("y"), [IntLiteral(3)]), FloatLiteral(10.45)), CallStmt(Id("eoo"), [Id("x")])]))])

        self.assertTrue(TestAST.checkASTGen(input, expect, 352))

    # 54
    def test_if_while_stmt_ast(self):
        """Test if with while statement"""
        input = """
           Var: x, z[3] = {21., 46e5, 100.e-8};
           Function: roo
           Parameter: c, d
           Body:
                Var: a = 0;
                While x <=. 9.2 Do
                    a = b - c;
                    If x != 0 Then
                       Break;
                    ElseIf x =/= 100.1234 Then
                       Continue;
                    EndIf.
                EndWhile.
           EndBody.
           Function: woo
           Body:
               z[3] = 10.45;
               eto(x);
           EndBody.
           """
        expect = Program([VarDecl(Id("x"), [], None), VarDecl(Id("z"), [3], ArrayLiteral(
            [FloatLiteral(21.0), FloatLiteral(4600000.0), FloatLiteral(1e-06)])),
                          FuncDecl(Id("roo"), [VarDecl(Id("c"), [], None), VarDecl(Id("d"), [], None)], (
                              [VarDecl(Id("a"), [], IntLiteral(0))],
                              [While(BinaryOp("<=.", Id("x"), FloatLiteral(9.2)), (
                                  [], [Assign(Id("a"), BinaryOp("-", Id("b"), Id("c"))), If(
                                      [(BinaryOp("!=", Id("x"), IntLiteral(0)), [], [Break()]),
                                       (BinaryOp("=/=", Id("x"), FloatLiteral(100.1234)), [], [Continue()])],
                                      ([], []))]))])),
                          FuncDecl(Id("woo"), [], ([],
                                                   [Assign(ArrayCell(Id("z"), [IntLiteral(3)]), FloatLiteral(10.45)),
                                                    CallStmt(Id("eto"), [Id("x")])]))])

        self.assertTrue(TestAST.checkASTGen(input, expect, 353))

    # 55
    def test_if_do_while_stmt_ast(self):
        """Test if with do while statement"""
        input = """
            ** This is a single-line comment. **
           Var: a[5] = {1,4,3,2,0};
           Function: yoo
           Parameter: c, d
           Body:
                Var: a = 0;
                Do 
                    num = num + 1;
                    If x != 0 Then
                       Break;
                    ElseIf x =/= 100.1234 Then
                       Continue;
                    EndIf.
                While num <= 100 EndDo.
           EndBody.
           Function: uoo
           Body:
                Var: isCorrect = True;
                z[3] = 10.45;
                torress(x);
           EndBody.
           """
        expect = Program([VarDecl(Id("a"), [5], ArrayLiteral(
            [IntLiteral(1), IntLiteral(4), IntLiteral(3), IntLiteral(2), IntLiteral(0)])),
                          FuncDecl(Id("yoo"), [VarDecl(Id("c"), [], None), VarDecl(Id("d"), [], None)], (
                              [VarDecl(Id("a"), [], IntLiteral(0))], [Dowhile(([], [
                                  Assign(Id("num"), BinaryOp("+", Id("num"), IntLiteral(1))), If(
                                      [(BinaryOp("!=", Id("x"), IntLiteral(0)), [], [Break()]),
                                       (BinaryOp("=/=", Id("x"), FloatLiteral(100.1234)), [], [Continue()])],
                                      ([], []))]),
                                                                              BinaryOp("<=", Id("num"),
                                                                                       IntLiteral(100)))])),
                          FuncDecl(Id("uoo"), [], ([VarDecl(Id("isCorrect"), [], BooleanLiteral(True))],
                                                   [Assign(ArrayCell(Id("z"), [IntLiteral(3)]), FloatLiteral(10.45)),
                                                    CallStmt(Id("torress"), [Id("x")])]))])

        self.assertTrue(TestAST.checkASTGen(input, expect, 354))

    # 56
    def test_for_while_stmt_ast(self):
        """Test for while statement"""
        input = """
            ** This is a single-line comment. **
           Var: a[5] = {1,4,3,2,0};
           Function: yoo
           Parameter: e, f
           Body:
                Var: app = 0, isCorrect = False;
                For(k = 0, k < 5, 1) Do
                    a[k] = b % a;
                    While x >=. 78e4 Do
                        app = f * e - 100;
                    EndWhile.
                    suarez(x);
                EndFor.
           EndBody.
           """
        expect = Program([VarDecl(Id("a"), [5], ArrayLiteral(
            [IntLiteral(1), IntLiteral(4), IntLiteral(3), IntLiteral(2), IntLiteral(0)])),
                          FuncDecl(Id("yoo"), [VarDecl(Id("e"), [], None), VarDecl(Id("f"), [], None)], (
                              [VarDecl(Id("app"), [], IntLiteral(0)),
                               VarDecl(Id("isCorrect"), [], BooleanLiteral(False))],
                              [For(Id("k"), IntLiteral(0), BinaryOp("<", Id("k"), IntLiteral(5)), IntLiteral(1), ([], [
                                  Assign(ArrayCell(Id("a"), [Id("k")]), BinaryOp("%", Id("b"), Id("a"))),
                                  While(BinaryOp(">=.", Id("x"), FloatLiteral(780000.0)), ([], [
                                      Assign(Id("app"),
                                             BinaryOp("-", BinaryOp("*", Id("f"), Id("e")), IntLiteral(100)))])),
                                  CallStmt(Id("suarez"), [Id("x")])]))]))])

        self.assertTrue(TestAST.checkASTGen(input, expect, 355))

    # 57
    def test_for_do_while_stmt_ast(self):
        """Test for with do while statement"""
        input = """
            ** This is a single-line comment. **
           Var: a[5] = {1,4,3,2,0};
           Function: yoo
           Parameter: e, f
           Body:
                Var: app = 0, isCorrect = False;
                For(k = 0, k < 5, 1) Do
                    a[k] = b % a;
                    Do 
                        num = num + 3;
                    While num <= 100 EndDo.
                    a[3 + foo(2)] = a[b[2][3]] + 4;
                    liv(x);
                EndFor.
           EndBody.
           """
        expect = Program([VarDecl(Id("a"), [5],
                                  ArrayLiteral(
                                      [IntLiteral(1), IntLiteral(4), IntLiteral(3), IntLiteral(2), IntLiteral(0)])),
                          FuncDecl(Id("yoo"), [VarDecl(Id("e"), [], None), VarDecl(Id("f"), [], None)],
                                   ([VarDecl(Id("app"), [], IntLiteral(0)),
                                     VarDecl(Id("isCorrect"), [], BooleanLiteral(False))],
                                    [For(Id("k"), IntLiteral(0), BinaryOp("<", Id("k"), IntLiteral(5)), IntLiteral(1), (
                                        [], [Assign(ArrayCell(Id("a"), [Id("k")]), BinaryOp("%", Id("b"), Id("a"))),
                                             Dowhile(([], [Assign(Id("num"), BinaryOp("+", Id("num"), IntLiteral(3)))]),
                                                     BinaryOp("<=", Id("num"), IntLiteral(100))), Assign(
                                                ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(3),
                                                                             CallExpr(Id("foo"), [IntLiteral(2)]))]),
                                                BinaryOp("+", ArrayCell(Id("a"), [
                                                    ArrayCell(Id("b"), [IntLiteral(2), IntLiteral(3)])]),
                                                         IntLiteral(4))), CallStmt(Id("liv"), [Id("x")])]))]))])

        self.assertTrue(TestAST.checkASTGen(input, expect, 356))

    # 58
    def test_for_return_stmt_ast(self):
        """Test for with do while statement"""
        input = """
            ** This is a single-line comment. **
           Var: b[2][3]= {{1,2,3},{4,5,6}};
           Function: noo
           Parameter: j, k, l[5]
           Body:
                Var: food = "Chicken", isCorrect = True;
                For(i = 0, i < 5, 1) Do
                    a[i] = b - a;
                    If a[i] == 100 Then
                        Return func();
                    EndIf.                    
                EndFor.
                a[3 + foo(2)] = a[b[2][3]] + 4;
                manu(x);
           EndBody.
           """
        expect = Program([VarDecl(Id("b"), [2, 3],
                                  ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)]),
                                                ArrayLiteral([IntLiteral(4), IntLiteral(5), IntLiteral(6)])])),
                          FuncDecl(Id("noo"), [VarDecl(Id("j"), [], None),
                                               VarDecl(Id("k"), [], None), VarDecl(Id("l"), [5], None)],
                                   ([VarDecl(Id("food"), [], StringLiteral("Chicken")),
                                     VarDecl(Id("isCorrect"), [], BooleanLiteral(True))], [
                                        For(Id("i"), IntLiteral(0), BinaryOp("<", Id("i"), IntLiteral(5)),
                                            IntLiteral(1), ([], [
                                                Assign(ArrayCell(Id("a"), [Id("i")]), BinaryOp("-", Id("b"), Id("a"))),
                                                If([(BinaryOp("==", ArrayCell(Id("a"), [Id("i")]), IntLiteral(100)), [],
                                                     [Return(CallExpr(Id("func"), []))])], ([], []))])), Assign(
                                           ArrayCell(Id("a"), [
                                               BinaryOp("+", IntLiteral(3), CallExpr(Id("foo"), [IntLiteral(2)]))]),
                                           BinaryOp("+", ArrayCell(Id("a"), [
                                               ArrayCell(Id("b"), [IntLiteral(2), IntLiteral(3)])]), IntLiteral(4))),
                                        CallStmt(Id("manu"), [Id("x")])]))])

        self.assertTrue(TestAST.checkASTGen(input, expect, 357))

    # 59
    def test_while_do_while_stmt_ast(self):
        """Test while with do while statement"""
        input = """
            ** This is a single-line comment. **
           Var: b[2][3]= {{1,2,3},{4,5,6}};
           Function: moo
           Parameter: a, b, c
           Body:
                Var: food = "Ham";
                While x >=. 78e4 Do
                        app = goo(food);
                        Do 
                            i = i + 10;
                        While i >= 100 EndDo.
                EndWhile.
                a[3 + foo(2)] = a[b[2][3]] + b[d[2][3]];
                ars(x);
           EndBody.
           """
        expect = Program([VarDecl(Id("b"), [2, 3],
                                  ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)]),
                                                ArrayLiteral([IntLiteral(4), IntLiteral(5), IntLiteral(6)])])),
                          FuncDecl(Id("moo"), [VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None),
                                               VarDecl(Id("c"), [], None)],
                                   ([VarDecl(Id("food"), [], StringLiteral("Ham"))],
                                    [While(BinaryOp(">=.", Id("x"), FloatLiteral(780000.0)),
                                           ([], [Assign(Id("app"), CallExpr(Id("goo"), [Id("food")])),
                                                 Dowhile(
                                                     ([], [Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(10)))]),
                                                     BinaryOp(">=", Id("i"), IntLiteral(100)))])), Assign(
                                        ArrayCell(Id("a"),
                                                  [BinaryOp("+", IntLiteral(3), CallExpr(Id("foo"), [IntLiteral(2)]))]),
                                        BinaryOp("+", ArrayCell(Id("a"),
                                                                [ArrayCell(Id("b"), [IntLiteral(2), IntLiteral(3)])]),
                                                 ArrayCell(Id("b"),
                                                           [ArrayCell(Id("d"), [IntLiteral(2), IntLiteral(3)])]))),
                                     CallStmt(Id("ars"), [Id("x")])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))

    # 60
    def test_decimal_literal_ast(self):
        """Test decimal literal"""
        input = """
           Var: b[3]= {1,2,3};
           Function: moo
           Parameter: a, b, c
           Body:
                Var: x = 10, y = 20, res;
                a = 10 - 5 + 7 * 20;
                res = a + y \\ x - 102364;
                Return res;
           EndBody.
           """
        expect = Program([VarDecl(Id("b"), [3],
                                  ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)])),
                          FuncDecl(Id("moo"), [VarDecl(Id("a"), [], None),
                                               VarDecl(Id("b"), [], None), VarDecl(Id("c"), [], None)],
                                   ([VarDecl(Id("x"), [], IntLiteral(10)), VarDecl(Id("y"), [], IntLiteral(20)),
                                     VarDecl(Id("res"), [], None)],
                                    [Assign(Id("a"), BinaryOp("+", BinaryOp("-", IntLiteral(10), IntLiteral(5)),
                                                              BinaryOp("*", IntLiteral(7), IntLiteral(20)))),
                                     Assign(Id("res"),
                                            BinaryOp("-", BinaryOp("+", Id("a"), BinaryOp("\\", Id("y"), Id("x"))),
                                                     IntLiteral(102364))), Return(Id("res"))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))

    # 61
    def test_hex_literal_ast(self):
        """Test hexadecimal literal"""
        input = """
           Var: b[3]= {0x123, 0XADE, 0x12AB};
           Function: hoo
           Parameter: q, w, e
           Body:
                Var: a = 0xFFFF, y = 0XABCD, res;
                a = 0xABC + 0X1A2C;
                res = a - y * x + 0x1A2B;
                Return res;
           EndBody.
           """
        expect = Program([VarDecl(Id("b"), [3], ArrayLiteral([IntLiteral(291), IntLiteral(2782), IntLiteral(4779)])),
                          FuncDecl(Id("hoo"),
                                   [VarDecl(Id("q"), [], None), VarDecl(Id("w"), [], None), VarDecl(Id("e"), [], None)],
                                   ([VarDecl(Id("a"), [], IntLiteral(65535)), VarDecl(Id("y"), [], IntLiteral(43981)),
                                     VarDecl(Id("res"), [], None)],
                                    [Assign(Id("a"), BinaryOp("+", IntLiteral(2748), IntLiteral(6700))),
                                     Assign(Id("res"),
                                            BinaryOp("+", BinaryOp("-", Id("a"), BinaryOp("*", Id("y"), Id("x"))),
                                                     IntLiteral(6699))), Return(Id("res"))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))

    # 62
    def test_octal_literal_ast(self):
        """Test octal literal"""
        input = """
           Var: b[3]= {0o456, 0O123, 0o711};
           Function: joo
           Parameter: a, c, d
           Body:
                Var: a = 0o753, y = 0o651,res;
                a = 0o567 * 0O77;
                res = a - y * x + 0o742;
                Return res;
           EndBody.
           """
        expect = Program([VarDecl(Id("b"), [3],
                                  ArrayLiteral([IntLiteral(302), IntLiteral(83), IntLiteral(457)])),
                          FuncDecl(Id("joo"), [VarDecl(Id("a"), [], None), VarDecl(Id("c"), [], None),
                                               VarDecl(Id("d"), [], None)],
                                   ([VarDecl(Id("a"), [], IntLiteral(491)), VarDecl(Id("y"),
                                                                                    [], IntLiteral(425)),
                                     VarDecl(Id("res"), [], None)],
                                    [Assign(Id("a"), BinaryOp("*", IntLiteral(375), IntLiteral(63))),
                                     Assign(Id("res"),
                                            BinaryOp("+", BinaryOp("-", Id("a"), BinaryOp("*", Id("y"), Id("x"))),
                                                     IntLiteral(482))), Return(Id("res"))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 361))

    # 63
    def test_boolean_literal_ast(self):
        """Test boolean literal"""
        input = """
           Var: isGone = False;
           Function: joo
           Body:
                Var: a = 1, y = 2, res;
                a = 7 * 9;
                res = a - y * x;
                Return True;
           EndBody.
           """
        expect = Program([VarDecl(Id("isGone"), [], BooleanLiteral(False)), FuncDecl(Id("joo"), [], (
            [VarDecl(Id("a"), [], IntLiteral(1)), VarDecl(Id("y"), [], IntLiteral(2)), VarDecl(Id("res"), [], None)],
            [Assign(Id("a"), BinaryOp("*", IntLiteral(7), IntLiteral(9))),
             Assign(Id("res"), BinaryOp("-", Id("a"), BinaryOp("*", Id("y"), Id("x")))),
             Return(BooleanLiteral(True))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 362))

    # 64
    def test_string_literal_ast(self):
        """Test string literal"""
        input = """
           Var: name = "khanh";
           Function: koo
           Parameter: ara
           Body:
                Var: laptop = "Asus";
                a = laptop + "Tuf";
                res = "He asked me: '"Where is John?'"";
                Return res + a;
           EndBody.
           """
        expect = Program([VarDecl(Id("name"), [], StringLiteral("khanh")),
                          FuncDecl(Id("koo"), [VarDecl(Id("ara"), [], None)], (
                              [VarDecl(Id("laptop"), [], StringLiteral("Asus"))],
                              [Assign(Id("a"), BinaryOp("+", Id("laptop"), StringLiteral("Tuf"))),
                               Assign(Id("res"), StringLiteral("He asked me: \'\"Where is John?\'\"")),
                               Return(BinaryOp("+", Id("res"), Id("a")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))

        # 65

    def test_array_literal_ast(self):
        """Test array literal"""
        input = """
           Var: arr[4] = {1,5,7,12};
           Function: loo
           Parameter: chel
           Body:
                Var: a[5] = {1,4,3,2,0};
                Var: b[2][3]={{1,2,3},{4,5,6}};
                a[3 + foo(2)] = a[b[2][3]] + 4;
                Return a[2];
           EndBody.
           """
        expect = Program([VarDecl(Id("arr"), [4],
                                  ArrayLiteral([IntLiteral(1), IntLiteral(5), IntLiteral(7), IntLiteral(12)])),
                          FuncDecl(Id("loo"), [VarDecl(Id("chel"), [], None)],
                                   ([VarDecl(Id("a"), [5],
                                             ArrayLiteral([IntLiteral(1), IntLiteral(4), IntLiteral(3), IntLiteral(2),
                                                           IntLiteral(0)])), VarDecl(Id("b"), [2, 3], ArrayLiteral(
                                       [ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)]),
                                        ArrayLiteral([IntLiteral(4), IntLiteral(5), IntLiteral(6)])]))], [Assign(
                                       ArrayCell(Id("a"),
                                                 [BinaryOp("+", IntLiteral(3), CallExpr(Id("foo"), [IntLiteral(2)]))]),
                                       BinaryOp("+", ArrayCell(Id("a"),
                                                               [ArrayCell(Id("b"), [IntLiteral(2), IntLiteral(3)])]),
                                                IntLiteral(4))), Return(ArrayCell(Id("a"), [IntLiteral(2)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 364))

    # 66
    def test_empty_while_stmt_ast(self):
        """Test empty while statement"""
        input = """
           Var: t = 0;
           Function: zoo
           Parameter: bar
           Body:
                Var: a[2] = {9,10};
                While x >= 100 Do  EndWhile.
                Return a[2];
           EndBody.
           """
        expect = Program([VarDecl(Id("t"), [], IntLiteral(0)), FuncDecl(Id("zoo"), [VarDecl(Id("bar"), [], None)], (
            [VarDecl(Id("a"), [2], ArrayLiteral([IntLiteral(9), IntLiteral(10)]))],
            [While(BinaryOp(">=", Id("x"), IntLiteral(100)), ([], [])), Return(ArrayCell(Id("a"), [IntLiteral(2)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 365))

    # 67
    def test_empty_do_while_stmt_ast(self):
        """Test empty do while statement"""
        input = """
           Var: w = 0;
           Function: xoo
           Parameter: real
           Body:
                Var: b[2] = {9,10};
                Do While i >= 100 EndDo.
                Return !a;
           EndBody.
           """
        expect = Program([VarDecl(Id("w"), [], IntLiteral(0)), FuncDecl(Id("xoo"), [VarDecl(Id("real"), [], None)], (
            [VarDecl(Id("b"), [2], ArrayLiteral([IntLiteral(9), IntLiteral(10)]))],
            [Dowhile(([], []), BinaryOp(">=", Id("i"), IntLiteral(100))), Return(UnaryOp("!", Id("a")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))

    # 68
    def test_do_while_with_var_decl_stmt_ast(self):
        """Test do while with variable declaration statement"""
        input = """
           Var: w = 0;
           Function: xoo
           Parameter: real
           Body:
                Var: b[2] = {9,10};
                Do 
                    Var: game = "Witcher";
                    book = "Lotr";
                    i = i + 1;
                While i >= 100 EndDo.
                Return !b;
           EndBody.
           """
        expect = Program([VarDecl(Id("w"), [], IntLiteral(0)), FuncDecl(Id("xoo"),
                                                                        [VarDecl(Id("real"), [], None)],
                                                                        ([VarDecl(Id("b"), [2],
                                                                                  ArrayLiteral([IntLiteral(9),
                                                                                                IntLiteral(10)]))],
                                                                         [Dowhile(([VarDecl(Id("game"), [],
                                                                                            StringLiteral("Witcher"))],
                                                                                   [Assign(Id("book"),
                                                                                           StringLiteral("Lotr")),
                                                                                    Assign(Id("i"),
                                                                                           BinaryOp("+", Id("i"),
                                                                                                    IntLiteral(1)))]),
                                                                                  BinaryOp(">=", Id("i"),
                                                                                           IntLiteral(100))),
                                                                          Return(UnaryOp("!", Id("b")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))

    # 69
    def test_global_local_var_decl_ast(self):
        """Test global and local statement"""
        input = """
           Var: w = 0, school = "BK";
           Function: coo
           Parameter: inter
           Body:
                Var: a = 5;
                Var: b[2][3] = {{2,3,4},{4,5,6}};
                Var: c, d = 6, e, f;
                Var: m, n[10];
                Return True;
           EndBody.
           """
        expect = Program([VarDecl(Id("w"), [], IntLiteral(0)), VarDecl(Id("school"), [], StringLiteral("BK")),
                          FuncDecl(Id("coo"), [VarDecl(Id("inter"), [], None)], ([VarDecl(Id("a"), [], IntLiteral(5)),
                                                                                  VarDecl(Id("b"), [2, 3], ArrayLiteral(
                                                                                      [ArrayLiteral(
                                                                                          [IntLiteral(2), IntLiteral(3),
                                                                                           IntLiteral(4)]),
                                                                                          ArrayLiteral([IntLiteral(4),
                                                                                                        IntLiteral(5),
                                                                                                        IntLiteral(
                                                                                                            6)])])),
                                                                                  VarDecl(Id("c"), [], None),
                                                                                  VarDecl(Id("d"), [], IntLiteral(6)),
                                                                                  VarDecl(Id("e"), [], None),
                                                                                  VarDecl(Id("f"), [], None),
                                                                                  VarDecl(Id("m"), [], None),
                                                                                  VarDecl(Id("n"), [10], None)],
                                                                                 [Return(BooleanLiteral(True))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))

    # 70
    def test_if_stmt_with_relational_expression_ast(self):
        """Test if statement with relational expression"""
        input = """
           Function: voo
           Parameter: milan
           Body:
                If a == b Then
                    b = a != c;
                    e = f > 15;
                    z = g >= f;
                ElseIf b =/= 95.6 Then
                    a = a >. 15;
                    c = c <=. 6532e12;
                Else
                    a = b;
                EndIf.
           EndBody.
           """
        expect = Program([FuncDecl(Id("voo"), [VarDecl(Id("milan"), [], None)],
                                   ([], [If([(BinaryOp("==", Id("a"), Id("b")), [],
                                              [Assign(Id("b"), BinaryOp("!=", Id("a"), Id("c"))),
                                               Assign(Id("e"), BinaryOp(">", Id("f"), IntLiteral(15))),
                                               Assign(Id("z"), BinaryOp(">=", Id("g"), Id("f")))]),
                                             (BinaryOp("=/=", Id("b"), FloatLiteral(95.6)), [],
                                              [Assign(Id("a"), BinaryOp(">.", Id("a"), IntLiteral(15))),
                                               Assign(Id("c"), BinaryOp("<=.", Id("c"), FloatLiteral(6532e12)))])],
                                            ([], [Assign(Id("a"), Id("b"))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))

    # 71
    def test_function_call_assign_ast(self):
        """Test function call assign statement"""
        input = """
           Function: boo
           Parameter: juve
           Body:
                Var: a[1];
                foo()[1] = 2 ;
           EndBody.
           """
        expect = Program([FuncDecl(Id("boo"), [VarDecl(Id("juve"), [], None)], (
            [VarDecl(Id("a"), [1], None)],
            [Assign(ArrayCell(CallExpr(Id("foo"), []), [IntLiteral(1)]), IntLiteral(2))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))

    # 72
    def test_function_call_assign_with_para_ast(self):
        """Test function call assign statement with parameter"""
        input = """
           Function: roo
           Parameter: par
           Body:
                Var: b[1][2];
                foo(a)[1] = 15 ;
           EndBody.
           """
        expect = Program([FuncDecl(Id("roo"), [VarDecl(Id("par"), [], None)], ([VarDecl(Id("b"), [1, 2], None)], [
            Assign(ArrayCell(CallExpr(Id("foo"), [Id("a")]), [IntLiteral(1)]), IntLiteral(15))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))

    # 73
    def test_function_call_assign_complex_ast(self):
        """Test function call assign statement complex"""
        input = """
           Function: too
           Parameter: ata
           Body:
                Var: c[1][2][3];
                foo(3 + goo(2))[2] = 15 ;
           EndBody.
           """
        expect = Program([FuncDecl(Id("too"), [VarDecl(Id("ata"), [], None)], ([VarDecl(Id("c"), [1, 2, 3], None)], [
            Assign(ArrayCell(CallExpr(Id("foo"), [BinaryOp("+", IntLiteral(3), CallExpr(Id("goo"), [IntLiteral(2)]))]),
                             [IntLiteral(2)]), IntLiteral(15))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))

    # 74
    def test_if_with_logical_not_expression_ast(self):
        """Test function call assign statement complex"""
        input = """
           Function: qoo
           Parameter: witch
           Body:
                If a == b Then
                    b = !c;
                    e = !(a > d);
                    z = !foo(a + goo(5));
                ElseIf b =/= 79.6 Then
                    a = !game(x)[2];
                Else
                    a = b;
                EndIf.
           EndBody.
           """
        expect = Program([FuncDecl(Id("qoo"),
                                   [VarDecl(Id("witch"), [], None)],
                                   ([],
                                    [If([(BinaryOp("==", Id("a"), Id("b")),
                                          [], [Assign(Id("b"), UnaryOp("!", Id("c"))), Assign(Id("e"),
                                                                                              UnaryOp("!", BinaryOp(">",
                                                                                                                    Id(
                                                                                                                        "a"),
                                                                                                                    Id(
                                                                                                                        "d")))),
                                               Assign(Id("z"), UnaryOp("!", CallExpr(Id("foo"),
                                                                                     [BinaryOp("+", Id("a"),
                                                                                               CallExpr(Id("goo"),
                                                                                                        [IntLiteral(
                                                                                                            5)]))])))]),
                                         (BinaryOp("=/=", Id("b"), FloatLiteral(79.6)),
                                          [], [Assign(Id("a"), UnaryOp("!", ArrayCell(CallExpr(Id("game"), [Id("x")]),
                                                                                      [IntLiteral(2)])))])],
                                        ([], [Assign(Id("a"), Id("b"))]))]))])

        self.assertTrue(TestAST.checkASTGen(input, expect, 373))

    # 75
    def test_if_with_logical_expression_ast(self):
        """Test function call assign statement complex"""
        input = """
           Function: yoo
           Parameter: geralt
           Body:
                If a == p Then
                    a = func(a, b)[79 + func(30)] - (3 + 20) * -10 && True == 4 + 5 || False;
                ElseIf hoo(a[2][3] + foo(1, 3.5, 0xFF)) && (a =/= b) Then
                    a = !game(x)[2];
                Else
                    a = b;
                EndIf.
           EndBody.
           """
        expect = Program([FuncDecl(Id("yoo"), [VarDecl(Id("geralt"), [], None)],
                                   ([], [If([(BinaryOp("==", Id("a"), Id("p")), [],
                                              [Assign(Id("a"), BinaryOp("==", BinaryOp("&&", BinaryOp("-", ArrayCell(
                                                  CallExpr(Id("func"), [Id("a"), Id("b")]),
                                                  [BinaryOp("+", IntLiteral(79),
                                                            CallExpr(Id("func"), [IntLiteral(30)]))]),
                                                                                                      BinaryOp("*",
                                                                                                               BinaryOp(
                                                                                                                   "+",
                                                                                                                   IntLiteral(
                                                                                                                       3),
                                                                                                                   IntLiteral(
                                                                                                                       20)),
                                                                                                               UnaryOp(
                                                                                                                   "-",
                                                                                                                   IntLiteral(
                                                                                                                       10)))),
                                                                                       BooleanLiteral(True)),
                                                                        BinaryOp("||", BinaryOp("+", IntLiteral(4),
                                                                                                IntLiteral(5)),
                                                                                 BooleanLiteral(False))))]), (
                                                 BinaryOp("&&", CallExpr(Id("hoo"), [
                                                     BinaryOp("+", ArrayCell(Id("a"), [IntLiteral(2), IntLiteral(3)]),
                                                              CallExpr(Id("foo"), [IntLiteral(1), FloatLiteral(3.5),
                                                                                   IntLiteral(255)]))]),
                                                          BinaryOp("=/=", Id("a"), Id("b"))), [], [Assign(Id("a"),
                                                                                                          UnaryOp("!",
                                                                                                                  ArrayCell(
                                                                                                                      CallExpr(
                                                                                                                          Id(
                                                                                                                              "game"),
                                                                                                                          [
                                                                                                                              Id(
                                                                                                                                  "x")]),
                                                                                                                      [
                                                                                                                          IntLiteral(
                                                                                                                              2)])))])],
                                            ([], [Assign(Id("a"), Id("b"))]))]))])

        self.assertTrue(TestAST.checkASTGen(input, expect, 374))

    # 76
    def test_if_with_index_ast(self):
        """Test if with index statement"""
        input = """
           Function: uoo
           Parameter: yennefer
           Body:
                If a == p Then
                    a = b[a[c[2]]];
                    b[2][3] = 1;
                ElseIf too(a[2][3] + hoo(1, 9.5)) || (a =/= b) Then
                    a = !game(x)[2];
                Else
                    a = b;
                EndIf.
           EndBody.
           """
        expect = Program([FuncDecl(Id("uoo"), [VarDecl(Id("yennefer"), [], None)],
                                   ([], [If([(BinaryOp("==", Id("a"), Id("p")), [],
                                              [Assign(Id("a"), ArrayCell(Id("b"), [
                                                  ArrayCell(Id("a"), [ArrayCell(Id("c"), [IntLiteral(2)])])])),
                                               Assign(ArrayCell(Id("b"), [IntLiteral(2), IntLiteral(3)]),
                                                      IntLiteral(1))]), (BinaryOp("||", CallExpr(Id("too"), [
                                       BinaryOp("+", ArrayCell(Id("a"), [IntLiteral(2), IntLiteral(3)]),
                                                CallExpr(Id("hoo"), [IntLiteral(1), FloatLiteral(9.5)]))]),
                                                                                  BinaryOp("=/=", Id("a"), Id("b"))),
                                                                         [], [Assign(Id("a"), UnaryOp("!", ArrayCell(
                                       CallExpr(Id("game"), [Id("x")]), [IntLiteral(2)])))])],
                                            ([], [Assign(Id("a"), Id("b"))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))

    # 77
    def test_if_with_multiplying_statement_ast(self):
        """Test if with multiplying statement"""
        input = """
           Function: poo
           Parameter: ciri
           Body:
                If c >=. a Then
                    a = b * a *. c \\ d \\. e % f;
                    b[2][3] = 1;
                ElseIf too(a[2][3] + hoo(1, 9.5)) || (a =/= b) Then
                    game();
                Else
                    a = b;
                EndIf.
           EndBody.
           """
        expect = Program([FuncDecl(Id("poo"), [VarDecl(Id("ciri"), [], None)],
                                   ([], [If([(BinaryOp(">=.", Id("c"), Id("a")),
                                              [], [Assign(Id("a"),
                                                          BinaryOp("%", BinaryOp("\\.",
                                                                                 BinaryOp("\\",
                                                                                          BinaryOp("*.",
                                                                                                   BinaryOp("*",
                                                                                                            Id("b"),
                                                                                                            Id("a")),
                                                                                                   Id("c")), Id("d")),
                                                                                 Id("e")), Id("f"))),
                                                   Assign(ArrayCell(Id("b"), [IntLiteral(2), IntLiteral(3)]),
                                                          IntLiteral(1))]), (BinaryOp("||", CallExpr(Id("too"), [
                                       BinaryOp("+", ArrayCell(Id("a"), [IntLiteral(2), IntLiteral(3)]),
                                                CallExpr(Id("hoo"), [IntLiteral(1), FloatLiteral(9.5)]))]),
                                                                                      BinaryOp("=/=", Id("a"),
                                                                                               Id("b"))), [],
                                                                             [CallStmt(Id("game"), [])])],
                                            ([], [Assign(Id("a"), Id("b"))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))

    # 78
    def test_if_with_adding_statement_ast(self):
        """Test if with adding statement"""
        input = """
           Function: dandelion
           Parameter: x
           Body:
                If a != True Then
                    a = a + b +. c - e -. f;
                    f[5][6] = 10;
                ElseIf a =/= b Then
                    Continue;
                Else
                    a = b;
                EndIf.
           EndBody.
           """
        expect = Program([FuncDecl(Id("dandelion"), [VarDecl(Id("x"), [], None)],
                                   ([], [If([(BinaryOp("!=", Id("a"), BooleanLiteral(True)),
                                              [], [Assign(Id("a"), BinaryOp("-.",
                                                                            BinaryOp("-", BinaryOp("+.",
                                                                                                   BinaryOp("+",
                                                                                                            Id("a"),
                                                                                                            Id("b")),
                                                                                                   Id("c")), Id("e")),
                                                                            Id("f"))),
                                                   Assign(ArrayCell(Id("f"), [IntLiteral(5), IntLiteral(6)]),
                                                          IntLiteral(10))]),
                                             (BinaryOp("=/=", Id("a"), Id("b")), [], [Continue()])],
                                            ([], [Assign(Id("a"), Id("b"))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))

    # 79
    def test_if_with_function_statement_ast(self):
        """Test if with function statement"""
        input = """
           Function: zoltan
           Parameter: x
           Body:
                If a == 10 Then
                    a = foo(b + goo(1, 2) * hoo(r));
                    y[7][9] = 10;
                ElseIf a =/= b Then
                    Continue;
                Else
                    Break;
                EndIf.
           EndBody.
           """
        expect = Program([FuncDecl(Id("zoltan"), [VarDecl(Id("x"), [], None)],
                                   ([], [If([(BinaryOp("==", Id("a"), IntLiteral(10)),
                                              [], [Assign(Id("a"), CallExpr(Id("foo"),
                                                                            [BinaryOp("+", Id("b"),
                                                                                      BinaryOp("*",
                                                                                               CallExpr(Id("goo"),
                                                                                                        [IntLiteral(1),
                                                                                                         IntLiteral(
                                                                                                             2)]),
                                                                                               CallExpr(Id("hoo"),
                                                                                                        [Id("r")])))])),
                                                   Assign(ArrayCell(Id("y"), [IntLiteral(7), IntLiteral(9)]),
                                                          IntLiteral(10))]),
                                             (BinaryOp("=/=", Id("a"), Id("b")), [], [Continue()])],
                                            ([], [Break()]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))

    # 80
    def test_empty_for_statement_ast(self):
        """Test empty for statement"""
        input = """
           Function: regis
           Parameter: x
           Body:
                Var: story = "What lies unseen";
                For(i = 0, i < 5, 1) Do

                EndFor.
           EndBody.
           """
        expect = Program([FuncDecl(Id("regis"), [VarDecl(Id("x"), [], None)], (
            [VarDecl(Id("story"), [], StringLiteral("What lies unseen"))],
            [For(Id("i"), IntLiteral(0), BinaryOp("<", Id("i"), IntLiteral(5)), IntLiteral(1), ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))

    # 81
    def test_for_statement_with_relational_ast(self):
        """Test for statement with logical expression"""
        input = """
           Function: avallach
           Parameter: x
           Body:
                Var: story = "Lilac and Gooseberries";
                For(i = 100, i > 0, -1) Do
                    x = a == b;
                    y = x != d;
                    z = y >= q;
                    func(a)[1] = (a > b) == (c < d);  
                EndFor.
           EndBody.
           """
        expect = Program([FuncDecl(Id("avallach"), [VarDecl(Id("x"), [], None)], (
            [VarDecl(Id("story"), [], StringLiteral("Lilac and Gooseberries"))], [
                For(Id("i"), IntLiteral(100), BinaryOp(">", Id("i"), IntLiteral(0)), UnaryOp("-", IntLiteral(1)), ([], [
                    Assign(Id("x"), BinaryOp("==", Id("a"), Id("b"))),
                    Assign(Id("y"), BinaryOp("!=", Id("x"), Id("d"))),
                    Assign(Id("z"), BinaryOp(">=", Id("y"), Id("q"))),
                    Assign(ArrayCell(CallExpr(Id("func"), [Id("a")]), [IntLiteral(1)]),
                           BinaryOp("==", BinaryOp(">", Id("a"), Id("b")), BinaryOp("<", Id("c"), Id("d"))))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 380))

    # 82
    def test_for_statement_with_logical_ast(self):
        """Test for statement with logical expression"""
        input = """
           Function: avallach
           Parameter: x
           Body:
                Var: story = "Lilac and Gooseberries";
                For(i = 100, i > 0, -1) Do
                    x = a == b;
                    y = x != d;
                    z = y >= q;
                    func(a)[1] = (a > b) == (c < d);  
                EndFor.
           EndBody.
           """
        expect = Program([FuncDecl(Id("avallach"), [VarDecl(Id("x"), [], None)], (
            [VarDecl(Id("story"), [], StringLiteral("Lilac and Gooseberries"))], [
                For(Id("i"), IntLiteral(100), BinaryOp(">", Id("i"), IntLiteral(0)), UnaryOp("-", IntLiteral(1)), ([], [
                    Assign(Id("x"), BinaryOp("==", Id("a"), Id("b"))),
                    Assign(Id("y"), BinaryOp("!=", Id("x"), Id("d"))),
                    Assign(Id("z"), BinaryOp(">=", Id("y"), Id("q"))),
                    Assign(ArrayCell(CallExpr(Id("func"), [Id("a")]), [IntLiteral(1)]),
                           BinaryOp("==", BinaryOp(">", Id("a"), Id("b")), BinaryOp("<", Id("c"), Id("d"))))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))

    # 83
    def test_for_statement_with_adding_ast(self):
        """Test for statement with logical expression"""
        input = """
           Function: triss
           Parameter: x
           Body:
                Var: story = "Kaer Morhen";
                For(i = 100, i > 0, -1) Do
                    a = a + b + e + f;
                    x = y +. 100. +. 12.24;
                    f = t - x - a;
                    ans = f -. 12e2;
                EndFor.
           EndBody.
           """
        expect = Program([FuncDecl(Id("triss"), [VarDecl(Id("x"), [], None)], (
            [VarDecl(Id("story"), [], StringLiteral("Kaer Morhen"))], [
                For(Id("i"), IntLiteral(100), BinaryOp(">", Id("i"), IntLiteral(0)), UnaryOp("-", IntLiteral(1)), ([], [
                    Assign(Id("a"), BinaryOp("+", BinaryOp("+", BinaryOp("+", Id("a"), Id("b")), Id("e")), Id("f"))),
                    Assign(Id("x"), BinaryOp("+.", BinaryOp("+.", Id("y"), FloatLiteral(100.0)), FloatLiteral(12.24))),
                    Assign(Id("f"), BinaryOp("-", BinaryOp("-", Id("t"), Id("x")), Id("a"))),
                    Assign(Id("ans"), BinaryOp("-.", Id("f"), FloatLiteral(1200.0)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))

    # 84
    def test_for_statement_with_sign_ast(self):
        """Test for statement with sign expression"""
        input = """
           Function: gaunter
           Parameter: x
           Body:
                Var: story = "Ladies of the Wood";
                For(i = 100, i > 0, -1) Do
                    a[2][3] = -y;
                    res = -.100.45;
                EndFor.
                Return;
           EndBody.
           """
        expect = Program([FuncDecl(Id("gaunter"), [VarDecl(Id("x"), [], None)], (
            [VarDecl(Id("story"), [], StringLiteral("Ladies of the Wood"))], [
                For(Id("i"), IntLiteral(100), BinaryOp(">", Id("i"), IntLiteral(0)), UnaryOp("-", IntLiteral(1)), ([], [
                    Assign(ArrayCell(Id("a"), [IntLiteral(2), IntLiteral(3)]), UnaryOp("-", Id("y"))),
                    Assign(Id("res"), UnaryOp("-.", FloatLiteral(100.45)))])), Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 383))

    # 85
    def test_for_statement_with_function_ast(self):
        """Test for statement with function expression"""
        input = """
           Function: anna
           Parameter: x
           Body:
                Var: story = "Echoes of the Past";
                For(i = 100, i > 0, -1) Do
                    a[2][3] = func(1, 2, 3) + goo(x);
                    func(a + b - c)[3] = 100;
                    res = foo()[2];
                EndFor.
                Return True;
           EndBody.
           """
        expect = Program([FuncDecl(Id("anna"), [VarDecl(Id("x"), [], None)], (
            [VarDecl(Id("story"), [], StringLiteral("Echoes of the Past"))], [
                For(Id("i"), IntLiteral(100), BinaryOp(">", Id("i"), IntLiteral(0)), UnaryOp("-", IntLiteral(1)), ([], [
                    Assign(ArrayCell(Id("a"), [IntLiteral(2), IntLiteral(3)]),
                           BinaryOp("+", CallExpr(Id("func"), [IntLiteral(1), IntLiteral(2), IntLiteral(3)]),
                                    CallExpr(Id("goo"), [Id("x")]))), Assign(
                        ArrayCell(CallExpr(Id("func"), [BinaryOp("-", BinaryOp("+", Id("a"), Id("b")), Id("c"))]),
                                  [IntLiteral(3)]), IntLiteral(100)),
                    Assign(Id("res"), ArrayCell(CallExpr(Id("foo"), []), [IntLiteral(2)]))])),
                Return(BooleanLiteral(True))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 384))

    # 86
    def test_while_statement_with_relational_ast(self):
        """Test while statement with relational expression"""
        input = """
           Function: detlaff
           Parameter: x
           Body:
                Var: story = "Va Fail, Elaine";
                While x >=. 78e4 Do
                    app = t <. 10.5;
                    re = a >=. 789.64;
                    tr = u =/= 8562.9985;
                EndWhile.
           EndBody.
           """
        expect = Program([FuncDecl(Id("detlaff"), [VarDecl(Id("x"), [], None)], (
            [VarDecl(Id("story"), [], StringLiteral("Va Fail, Elaine"))], [
                While(BinaryOp(">=.", Id("x"), FloatLiteral(780000.0)), ([], [
                    Assign(Id("app"), BinaryOp("<.", Id("t"), FloatLiteral(10.5))),
                    Assign(Id("re"), BinaryOp(">=.", Id("a"), FloatLiteral(789.64))),
                    Assign(Id("tr"), BinaryOp("=/=", Id("u"), FloatLiteral(8562.9985)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))

    # 87
    def test_while_statement_with_logical_ast(self):
        """Test while statement with logical expression"""
        input = """
           Function: syanna
           Parameter: x
           Body:
                Var: story = "The Isle of Mists";
                While x >=. 98e4 Do
                    b = !c;
                    e = !(a > d);
                    z = !foo(a + goo(5));
                EndWhile.
                Return func(n + goo());
           EndBody.
           """
        expect = Program([FuncDecl(Id("syanna"), [VarDecl(Id("x"), [], None)],
                                   ([VarDecl(Id("story"), [], StringLiteral("The Isle of Mists"))],
                                    [While(BinaryOp(">=.", Id("x"), FloatLiteral(980000.0)), (
                                        [], [Assign(Id("b"), UnaryOp("!", Id("c"))),
                                             Assign(Id("e"), UnaryOp("!", BinaryOp(">", Id("a"), Id("d")))),
                                             Assign(Id("z"), UnaryOp("!", CallExpr(Id("foo"), [
                                                 BinaryOp("+", Id("a"), CallExpr(Id("goo"), [IntLiteral(5)]))])))])),
                                     Return(
                                         CallExpr(Id("func"), [BinaryOp("+", Id("n"), CallExpr(Id("goo"), []))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))

    # 88
    def test_while_statement_with_index_ast(self):
        """Test while statement with index expression"""
        input = """
           Function: dijkstra
           Parameter: x
           Body:
                Var: story = "Through Time and Space";
                While x >=. 98e4 Do
                    a = b[a[c[2]]];
                    b[2][3] = 1;
                    a[3 + foo(2)] = a[b[2][3]] + 4;
                EndWhile.
                Return func(n + goo());
           EndBody.
           """
        expect = Program([FuncDecl(Id("dijkstra"), [VarDecl(Id("x"), [], None)], (
            [VarDecl(Id("story"), [], StringLiteral("Through Time and Space"))], [
                While(BinaryOp(">=.", Id("x"), FloatLiteral(980000.0)), ([], [
                    Assign(Id("a"), ArrayCell(Id("b"), [ArrayCell(Id("a"), [ArrayCell(Id("c"), [IntLiteral(2)])])])),
                    Assign(ArrayCell(Id("b"), [IntLiteral(2), IntLiteral(3)]), IntLiteral(1)),
                    Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(3), CallExpr(Id("foo"), [IntLiteral(2)]))]),
                           BinaryOp("+", ArrayCell(Id("a"), [ArrayCell(Id("b"), [IntLiteral(2), IntLiteral(3)])]),
                                    IntLiteral(4)))])),
                Return(CallExpr(Id("func"), [BinaryOp("+", Id("n"), CallExpr(Id("goo"), []))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))

    # 89
    def test_while_statement_with_function_ast(self):
        """Test while statement with function expression"""
        input = """
           Function: eihart
           Parameter: x
           Body:
                Var: story = "Veni Vidi Vigo";
                While x >=. 98e4 Do
                    a[2][3] = func(1, 2, 3) + goo(x);
                    func(a + b - c)[3] = 100;
                    res = foo()[2];
                    arr[a[2][3]-b[2][5]] = 95.69;
                EndWhile.
                Return func(n + goo());
           EndBody.
           """
        expect = Program([FuncDecl(Id("eihart"), [VarDecl(Id("x"), [], None)], (
            [VarDecl(Id("story"), [], StringLiteral("Veni Vidi Vigo"))], [
                While(BinaryOp(">=.", Id("x"), FloatLiteral(980000.0)), ([], [
                    Assign(ArrayCell(Id("a"), [IntLiteral(2), IntLiteral(3)]),
                           BinaryOp("+", CallExpr(Id("func"), [IntLiteral(1), IntLiteral(2), IntLiteral(3)]),
                                    CallExpr(Id("goo"), [Id("x")]))), Assign(
                        ArrayCell(CallExpr(Id("func"), [BinaryOp("-", BinaryOp("+", Id("a"), Id("b")), Id("c"))]),
                                  [IntLiteral(3)]), IntLiteral(100)),
                    Assign(Id("res"), ArrayCell(CallExpr(Id("foo"), []), [IntLiteral(2)])),
                    Assign(ArrayCell(Id("arr"), [
                        BinaryOp("-", ArrayCell(Id("a"), [IntLiteral(2), IntLiteral(3)]),
                                 ArrayCell(Id("b"), [IntLiteral(2), IntLiteral(5)]))]), FloatLiteral(95.69))])),
                Return(CallExpr(Id("func"), [BinaryOp("+", Id("n"), CallExpr(Id("goo"), []))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 388))

    # 90
    def test_do_while_statement_with_logical_ast(self):
        """Test do while statement with logical expression"""
        input = """
           Function: roche
           Parameter: x
           Body:
                Var: story = "Child of the Elder Blood";
                Do 
                    b = !c;
                    e = !(a > d);
                    z = !foo(a + goo(5));
                    r = y || x;
                    f = r && (a > b + c);
                While i >= 100 EndDo.
                Return func(n + goo());
           EndBody.
           """
        expect = Program([FuncDecl(Id("roche"), [VarDecl(Id("x"), [], None)], (
            [VarDecl(Id("story"), [], StringLiteral("Child of the Elder Blood"))], [Dowhile(([], [
                Assign(Id("b"), UnaryOp("!", Id("c"))), Assign(Id("e"), UnaryOp("!", BinaryOp(">", Id("a"), Id("d")))),
                Assign(Id("z"),
                       UnaryOp("!",
                               CallExpr(Id("foo"), [BinaryOp("+", Id("a"), CallExpr(Id("goo"), [IntLiteral(5)]))]))),
                Assign(Id("r"), BinaryOp("||", Id("y"), Id("x"))),
                Assign(Id("f"), BinaryOp("&&", Id("r"), BinaryOp(">", Id("a"), BinaryOp("+", Id("b"), Id("c")))))]),
                                                                                            BinaryOp(">=", Id("i"),
                                                                                                     IntLiteral(100))),
                                                                                    Return(CallExpr(Id("func"), [
                                                                                        BinaryOp("+", Id("n"),
                                                                                                 CallExpr(Id("goo"),
                                                                                                          []))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 389))

    # 91
    def test_do_while_statement_with_adding_ast(self):
        """Test do while statement with adding expression"""
        input = """
           Function: ves
           Parameter: x
           Body:
                Var: story = "Defender of the Faith";
                Do 
                    a = a + b +. c - e;
                    e = f -. 151.2;
                    f[5][6] = 10;
                While i >= 100 EndDo.
                Return func(n + goo());
           EndBody.
           """
        expect = Program([FuncDecl(Id("ves"), [VarDecl(Id("x"), [], None)], (
            [VarDecl(Id("story"), [], StringLiteral("Defender of the Faith"))], [Dowhile(([], [
                Assign(Id("a"), BinaryOp("-", BinaryOp("+.", BinaryOp("+", Id("a"), Id("b")), Id("c")), Id("e"))),
                Assign(Id("e"), BinaryOp("-.", Id("f"), FloatLiteral(151.2))),
                Assign(ArrayCell(Id("f"), [IntLiteral(5), IntLiteral(6)]), IntLiteral(10))]), BinaryOp(">=", Id("i"),
                                                                                                       IntLiteral(
                                                                                                           100))),
                                                                                 Return(CallExpr(Id("func"), [
                                                                                     BinaryOp("+", Id("n"),
                                                                                              CallExpr(Id("goo"),
                                                                                                       []))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 390))

    # 92
    def test_do_while_statement_with_function_ast(self):
        """Test do while statement with function expression"""
        input = """
           Function: vesemir
           Parameter: x
           Body:
                Var: story = "Carnal Sins";
                Do 
                    arr[5][9] = func(1, 2, 3) + hoo(y);
                    func(a * b + c)[5] = 0;
                    ans = foo()[2];
                    arr[a[2][3]-b[2][5]+c[4][5]] = 95.69;
                While i >= 100 EndDo.
                Return func(n + goo());
           EndBody.
           """
        expect = Program([FuncDecl(Id("vesemir"), [VarDecl(Id("x"), [], None)], (
            [VarDecl(Id("story"), [], StringLiteral("Carnal Sins"))], [Dowhile(([], [
                Assign(ArrayCell(Id("arr"), [IntLiteral(5), IntLiteral(9)]),
                       BinaryOp("+", CallExpr(Id("func"), [IntLiteral(1), IntLiteral(2), IntLiteral(3)]),
                                CallExpr(Id("hoo"), [Id("y")]))), Assign(
                    ArrayCell(CallExpr(Id("func"), [BinaryOp("+", BinaryOp("*", Id("a"), Id("b")), Id("c"))]),
                              [IntLiteral(5)]), IntLiteral(0)),
                Assign(Id("ans"), ArrayCell(CallExpr(Id("foo"), []), [IntLiteral(2)])), Assign(ArrayCell(Id("arr"), [
                    BinaryOp("+", BinaryOp("-", ArrayCell(Id("a"), [IntLiteral(2), IntLiteral(3)]),
                                           ArrayCell(Id("b"), [IntLiteral(2), IntLiteral(5)])),
                             ArrayCell(Id("c"), [IntLiteral(4), IntLiteral(5)]))]), FloatLiteral(95.69))]),
                                                                               BinaryOp(">=", Id("i"),
                                                                                        IntLiteral(100))),
                                                                       Return(
                                                                           CallExpr(Id("func"), [BinaryOp("+", Id("n"),
                                                                                                          CallExpr(
                                                                                                              Id("goo"),
                                                                                                              []))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 391))

    # 93
    def test_nested_if_with_nested_for_ast(self):
        """Test nested if with nested for statement"""
        input = """
           Function: lambert
           Parameter: x
           Body:
                Var: story = "Of Dairy and Darkness";
                If age > 18 Then 
                    If height < 20 Then
                        print("Congratulation");
                    EndIf.
                ElseIf age > 13 Then
                    writeln("Good luck");
                    For(i = 1, i < 10, -2) Do 
                        For(j = 0, j < 15, 1) Do
                            goo(arr[i][j]);
                        EndFor.
                        noo();
                        i = -i;
                        x = i + i;
                    EndFor. 
                Else
                    writeln("Hola");
                    If score > 100 Then
                        writeln("Achievement unlocked");
                    EndIf.
                EndIf.
           EndBody.
           """
        expect = Program([FuncDecl(Id("lambert"), [VarDecl(Id("x"), [], None)],
                                   ([VarDecl(Id("story"), [], StringLiteral("Of Dairy and Darkness"))],
                                    [If([(BinaryOp(">", Id("age"), IntLiteral(18)),
                                          [], [If([(BinaryOp("<", Id("height"), IntLiteral(20)), [],
                                                    [CallStmt(Id("print"), [StringLiteral("Congratulation")])])],
                                                  ([], []))]), (BinaryOp(">", Id("age"), IntLiteral(13)), [],
                                                                [CallStmt(Id("writeln"), [StringLiteral("Good luck")]),
                                                                 For(Id("i"), IntLiteral(1),
                                                                     BinaryOp("<", Id("i"), IntLiteral(10)),
                                                                     UnaryOp("-", IntLiteral(2)), ([], [
                                                                         For(Id("j"), IntLiteral(0),
                                                                             BinaryOp("<", Id("j"), IntLiteral(15)),
                                                                             IntLiteral(1), ([], [CallStmt(Id("goo"), [
                                                                                 ArrayCell(Id("arr"),
                                                                                           [Id("i"), Id("j")])])])),
                                                                         CallStmt(Id("noo"), []),
                                                                         Assign(Id("i"), UnaryOp("-", Id("i"))),
                                                                         Assign(Id("x"),
                                                                                BinaryOp("+", Id("i"), Id("i")))]))])],
                                        ([], [CallStmt(Id("writeln"), [StringLiteral("Hola")]), If([(BinaryOp(">", Id(
                                            "score"), IntLiteral(100)), [], [CallStmt(Id("writeln"), [
                                            StringLiteral("Achievement unlocked")])])], ([], []))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 392))

    # 94
    def test_nested_if_with_nested_while_ast(self):
        """Test nested if with nested while statement"""
        input = """
           Function: eskiel
           Parameter: x
           Body:
                Var: story = "Rose on a Red Field";
                If age > 18 Then 
                    If height < 45 Then
                        print("Proceed");
                    EndIf.
                ElseIf age > 13 Then
                    While num >= 79 Do
                        While j != False Do
                            If a == b Then
                                c = a + b;
                            EndIf.
                        EndWhile.
                        hoo("Hello World");
                    EndWhile.
                EndIf.
           EndBody.
           """
        expect = Program([FuncDecl(Id("eskiel"), [VarDecl(Id("x"), [], None)],
                                   ([VarDecl(Id("story"), [], StringLiteral("Rose on a Red Field"))],
                                    [If([(BinaryOp(">", Id("age"), IntLiteral(18)),
                                          [], [If([(BinaryOp("<", Id("height"), IntLiteral(45)),
                                                    [], [CallStmt(Id("print"), [StringLiteral("Proceed")])])],
                                                  ([], []))]), (BinaryOp(">", Id("age"), IntLiteral(13)), [], [
                                        While(BinaryOp(">=", Id("num"), IntLiteral(79)), ([], [
                                            While(BinaryOp("!=", Id("j"), BooleanLiteral(False)), ([], [If([(BinaryOp(
                                                "==", Id("a"), Id("b")), [], [Assign(Id("c"), BinaryOp("+", Id("a"),
                                                                                                       Id("b")))])],
                                                ([], []))])),
                                            CallStmt(Id("hoo"), [StringLiteral("Hello World")])]))])], ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 393))

    # 95
    def test_nested_if_with_nested_do_while_ast(self):
        """Test nested if with nested do while statement"""
        input = """
           Function: shani
           Parameter: x
           Body:
                Var: story = "Whatsoever a Man Soweth";
                If age > 18 Then 
                    If height < 45 Then
                        print("Proceed");
                    EndIf.
                ElseIf age > 13 Then
                    Do 
                        Do
                            calculate(x);
                            ans = x + y - z * 5;
                        While i >= 100 EndDo.
                        process(x);
                    While num <= 1000 EndDo.
                EndIf.
           EndBody.
           """
        expect = Program([FuncDecl(Id("shani"), [VarDecl(Id("x"), [], None)], (
            [VarDecl(Id("story"), [], StringLiteral("Whatsoever a Man Soweth"))], [If([(BinaryOp(">", Id("age"),
                                                                                                 IntLiteral(18)), [],
                                                                                        [If(
                                                                                            [(
                                                                                                BinaryOp("<",
                                                                                                         Id("height"),
                                                                                                         IntLiteral(
                                                                                                             45)),
                                                                                                [],
                                                                                                [CallStmt(Id("print"),
                                                                                                          [
                                                                                                              StringLiteral(
                                                                                                                  "Proceed")])])],
                                                                                            ([], []))]), (
                                                                                           BinaryOp(">", Id("age"),
                                                                                                    IntLiteral(13)), [],
                                                                                           [Dowhile(([], [Dowhile(([], [
                                                                                               CallStmt(Id("calculate"),
                                                                                                        [Id("x")]),
                                                                                               Assign(Id("ans"),
                                                                                                      BinaryOp("-",
                                                                                                               BinaryOp(
                                                                                                                   "+",
                                                                                                                   Id(
                                                                                                                       "x"),
                                                                                                                   Id(
                                                                                                                       "y")),
                                                                                                               BinaryOp(
                                                                                                                   "*",
                                                                                                                   Id(
                                                                                                                       "z"),
                                                                                                                   IntLiteral(
                                                                                                                       5))))]),
                                                                                                                  BinaryOp(
                                                                                                                      ">=",
                                                                                                                      Id(
                                                                                                                          "i"),
                                                                                                                      IntLiteral(
                                                                                                                          100))),
                                                                                                          CallStmt(
                                                                                                              Id(
                                                                                                                  "process"),
                                                                                                              [Id(
                                                                                                                  "x")])]),
                                                                                                    BinaryOp("<=",
                                                                                                             Id("num"),
                                                                                                             IntLiteral(
                                                                                                                 1000)))])],
                                                                                      ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 394))

    # 96
    def test_nested_for_with_nested_while_ast(self):
        """Test nested for with nested while statement"""
        input = """
           Function: neneke
           Parameter: x
           Body:
                Var: story = "La Cage au Fou";
                For(i = 2, i < 100, 1) Do 
                    For(j = 0, j < 15, 1) Do
                        roo(arr[i][j][k]);
                        While ans == 9 Do
                            While j <=. 13.9 Do
                                If c =/= d Then
                                    c = ans * b - a;
                                EndIf.
                            EndWhile.
                            foo("meth");
                        EndWhile.
                    EndFor.
                    noo();
                    i = -i;
                    x = i + i;
                EndFor. 
           EndBody.
           """
        expect = Program([FuncDecl(Id("neneke"), [VarDecl(Id("x"), [], None)],
                                   ([VarDecl(Id("story"), [], StringLiteral("La Cage au Fou"))],
                                    [For(Id("i"), IntLiteral(2), BinaryOp("<", Id("i"), IntLiteral(100)), IntLiteral(1),
                                         ([], [For(Id("j"), IntLiteral(0), BinaryOp("<", Id("j"), IntLiteral(15)),
                                                   IntLiteral(1),
                                                   ([], [CallStmt(Id("roo"),
                                                                  [ArrayCell(Id("arr"), [Id("i"), Id("j"), Id("k")])]),
                                                         While(BinaryOp("==", Id("ans"), IntLiteral(9)), ([], [
                                                             While(BinaryOp("<=.", Id("j"), FloatLiteral(13.9)), ([], [
                                                                 If([(BinaryOp("=/=", Id("c"), Id("d")), [], [
                                                                     Assign(Id("c"), BinaryOp("-",
                                                                                              BinaryOp("*", Id("ans"),
                                                                                                       Id("b")),
                                                                                              Id("a")))])],
                                                                    ([], []))])),
                                                             CallStmt(Id("foo"), [StringLiteral("meth")])]))])),
                                               CallStmt(Id("noo"), []), Assign(Id("i"), UnaryOp("-", Id("i"))),
                                               Assign(Id("x"), BinaryOp("+", Id("i"), Id("i")))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 395))

    # 97
    def test_nested_for_with_nested_do_while_ast(self):
        """Test nested for with nested do while statement"""
        input = """
           Function: neneke
           Parameter: x
           Body:
                Var: story = "La Cage au Fou";
                For(i = 2, i < 100, 1) Do 
                    For(j = 0, j < 15, 1) Do
                        roo(arr[i][j][k]);
                    Do 
                        Do
                            calculate(x);
                            ans = x + y - z * 5;
                        While i >= 100 EndDo.
                        process(x);
                    While num <= 1000 EndDo.
                    EndFor.
                EndFor. 
           EndBody.
           """
        expect = Program([FuncDecl(Id("neneke"), [VarDecl(Id("x"), [], None)],
                                   ([VarDecl(Id("story"), [], StringLiteral("La Cage au Fou"))],
                                    [For(Id("i"), IntLiteral(2), BinaryOp("<", Id("i"), IntLiteral(100)), IntLiteral(1),
                                         ([], [For(Id("j"), IntLiteral(0), BinaryOp("<", Id("j"), IntLiteral(15)),
                                                   IntLiteral(1),
                                                   ([], [CallStmt(Id("roo"),
                                                                  [ArrayCell(Id("arr"), [Id("i"), Id("j"), Id("k")])]),
                                                         Dowhile(
                                                             ([], [Dowhile(([], [CallStmt(Id("calculate"), [Id("x")]),
                                                                                 Assign(Id("ans"),
                                                                                        BinaryOp("-",
                                                                                                 BinaryOp(
                                                                                                     "+",
                                                                                                     Id("x"),
                                                                                                     Id(
                                                                                                         "y")),
                                                                                                 BinaryOp(
                                                                                                     "*",
                                                                                                     Id("z"),
                                                                                                     IntLiteral(
                                                                                                         5))))]),
                                                                           BinaryOp(">=", Id("i"), IntLiteral(100))),
                                                                   CallStmt(Id("process"), [Id("x")])]),
                                                             BinaryOp("<=", Id("num"), IntLiteral(1000)))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 396))

    # 98
    def test_nested_while_with_nested_do_while_ast(self):
        """Test nested while with nested do while statement"""
        input = """
           Function: foltest
           Parameter: x
           Body:
                Var: story = "Tesham Mutna";
                Do 
                    Do
                        calculate(x);
                        ans = x + y - z * 5;
                    While i >= 100 EndDo.
                    While ans == 9 Do
                        While j <=. 13.9 Do
                            If c =/= d Then
                                c = ans * b - a;
                            EndIf.
                        EndWhile.
                        foo("meth");
                    EndWhile.
                While num <= 1000 EndDo.
           EndBody.
           """
        expect = Program([FuncDecl(Id("foltest"), [VarDecl(Id("x"), [], None)],
                                   ([VarDecl(Id("story"), [], StringLiteral("Tesham Mutna"))],
                                    [Dowhile(([], [Dowhile(([], [CallStmt(Id("calculate"), [Id("x")]),
                                                                 Assign(Id("ans"),
                                                                        BinaryOp("-", BinaryOp("+", Id("x"), Id("y")),
                                                                                 BinaryOp("*", Id("z"),
                                                                                          IntLiteral(5))))]),
                                                           BinaryOp(">=", Id("i"), IntLiteral(100))),
                                                   While(BinaryOp("==", Id("ans"), IntLiteral(9)), (
                                                       [], [While(BinaryOp("<=.", Id("j"), FloatLiteral(13.9)), (
                                                           [], [If([(BinaryOp("=/=", Id("c"), Id("d")), [], [
                                                               Assign(Id("c"),
                                                                      BinaryOp("-", BinaryOp("*", Id("ans"), Id("b")),
                                                                               Id("a")))])], ([], []))])),
                                                            CallStmt(Id("foo"), [StringLiteral("meth")])]))]),
                                             BinaryOp("<=", Id("num"), IntLiteral(1000)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 397))

    # 99
    def test_general_program_ast(self):
        """Test general program"""
        input = """
            Var: x = "The Night of Long Fangs";
            Var: a = 5;
            Var: b[2][3] = {{2,3,4},{4,5,6}};
            Var: c, d = 6, e, f;
            Var: m, n[10];
            Function: fact
            Parameter: n
            Body:
                If n == 0 Then
                    Return 1;
                Else
                    Return n * fact (n - 1);
                EndIf.
                EndBody.
            Function: main
            Body:
                x = 10;
                fact (x);
            EndBody.
           """
        expect = Program(
            [VarDecl(Id("x"), [], StringLiteral("The Night of Long Fangs")), VarDecl(Id("a"), [], IntLiteral(5)),
             VarDecl(Id("b"), [2, 3], ArrayLiteral([ArrayLiteral([IntLiteral(2), IntLiteral(3), IntLiteral(4)]),
                                                    ArrayLiteral([IntLiteral(4), IntLiteral(5), IntLiteral(6)])])),
             VarDecl(Id("c"), [], None), VarDecl(Id("d"), [], IntLiteral(6)), VarDecl(Id("e"), [], None),
             VarDecl(Id("f"), [], None), VarDecl(Id("m"), [], None), VarDecl(Id("n"), [10], None),
             FuncDecl(Id("fact"), [VarDecl(Id("n"), [], None)], ([], [
                 If([(BinaryOp("==", Id("n"), IntLiteral(0)), [], [Return(IntLiteral(1))])], ([], [Return(
                     BinaryOp("*", Id("n"), CallExpr(Id("fact"), [BinaryOp("-", Id("n"), IntLiteral(1))])))]))])),
             FuncDecl(Id("main"), [], ([], [Assign(Id("x"), IntLiteral(10)), CallStmt(Id("fact"), [Id("x")])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 398))

    # 100
    def test_complex_program_ast(self):
        """Test complex program"""
        input = """
            Var: x = "Land of a Thousand Fables";
            Var: a = 5;
            Var: b[2][3] = {{2,3,4},{4,5,6}};
            Var: c, d = 6, e, f;
            Var: m, n[10];
            Function: fact
            Parameter: n
            Body:
                If n == 0 Then
                    Return 1;
                Else
                    Return n * fact (n - 1);
                EndIf.
                EndBody.
            Function: foo
            Parameter: a[5], b
            Body:
                Var: i = 0;
                While (i < 5) Do
                a[i] = b +. 1.0;
                i = i + 1;
                EndWhile.
            EndBody.
            Function: too
            Body:
                Var: a[5] = {1,4,3,2,0};
                Var: b[2][3]={{1,2,3},{4,5,6}};
                If bool_of_string ("True") Then
                    a = int_of_string(read());
                    b = float_of_int (a) +. 2.0;
                EndIf.
            EndBody.
           """
        expect = Program([VarDecl(Id("x"), [], StringLiteral("Land of a Thousand Fables")),
                          VarDecl(Id("a"),
                                  [], IntLiteral(5)), VarDecl(Id("b"), [2, 3],
                                                              ArrayLiteral([ArrayLiteral(
                                                                  [IntLiteral(2), IntLiteral(3), IntLiteral(4)]),
                                                                  ArrayLiteral([IntLiteral(4), IntLiteral(5),
                                                                                IntLiteral(6)])])),
                          VarDecl(Id("c"), [], None),
                          VarDecl(Id("d"), [], IntLiteral(6)), VarDecl(Id("e"), [], None), VarDecl(Id("f"), [], None),
                          VarDecl(Id("m"), [], None), VarDecl(Id("n"), [10], None),
                          FuncDecl(Id("fact"), [VarDecl(Id("n"), [], None)], (
                              [], [If([(BinaryOp("==", Id("n"), IntLiteral(0)),
                                        [], [Return(IntLiteral(1))])], (
                                          [], [Return(BinaryOp("*", Id("n"),
                                                               CallExpr(Id("fact"), [
                                                                   BinaryOp("-", Id("n"), IntLiteral(1))])))]))])),
                          FuncDecl(Id("foo"), [VarDecl(Id("a"), [5], None), VarDecl(Id("b"), [], None)],
                                   ([VarDecl(Id("i"), [], IntLiteral(0))],
                                    [While(BinaryOp("<", Id("i"), IntLiteral(5)), (
                                        [], [Assign(ArrayCell(Id("a"), [Id("i")]),
                                                    BinaryOp("+.", Id("b"), FloatLiteral(1.0))),
                                             Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))]))])),
                          FuncDecl(Id("too"), [],
                                   ([VarDecl(Id("a"), [5],
                                             ArrayLiteral([IntLiteral(1), IntLiteral(4), IntLiteral(3), IntLiteral(2),
                                                           IntLiteral(0)])),
                                     VarDecl(Id("b"), [2, 3],
                                             ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)]),
                                                           ArrayLiteral(
                                                               [IntLiteral(4), IntLiteral(5), IntLiteral(6)])]))],
                                    [If([(CallExpr(Id("bool_of_string"), [StringLiteral("True")]), [],
                                          [Assign(Id("a"), CallExpr(Id("int_of_string"), [CallExpr(Id("read"), [])])),
                                           Assign(Id("b"), BinaryOp("+.", CallExpr(Id("float_of_int"), [Id("a")]),
                                                                    FloatLiteral(2.0)))])], ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 399))


    def test_shit(self):
        """Simple program: int main() {} """
        input = """
        Var: a = 1;
        Function: main
            Body:
                a = 1;
                a[1] = 1;
                print(string_of_int(fact(5)));
            EndBody.
        Function: fact
            Parameter: n
            Body:
                If n == 0 Then
                    Return 1;
                ElseIf n < 0 Then
                    Return 0;
            EndBody.
        """

        expect = Program([VarDecl(Id("x"), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 400))

