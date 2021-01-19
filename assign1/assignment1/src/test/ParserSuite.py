import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):

    # Test variable declaration
    # Test 1
    def test_variable_declaration_empty(self):
        """Variable declaration"""
        input = """Var: x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 201))

    # Test 2
    def test_wrong_miss_variable_declaration(self):
        """Miss variable"""
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 202))

    # Test 3
    def test_scalar_number_declaration(self):
        """Scalar number variable declaration"""
        input = """Var: a = 5;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 203))

    # Test 4
    def test_scalar_string_declaration(self):
        """Scalar string variable declaration"""
        input = """Var: name = "Charles";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 204))

    # Test 5
    def test_scalar_boolean_declaration(self):
        """Scalar boolean variable declaration"""
        input = """Var: isCorrect = True;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 205))

    # Test 6
    def test_scalar_float_declaration(self):
        """Scalar float variable declaration"""
        input = """Var: num = 8.9;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 206))

    # Test 7
    def test_multi_var_declaration(self):
        """Multiple variable declaration"""
        input = """Var: c, d = 6, e, f;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 207))

    # Test 8
    def test_composite_var_declaration_empty(self):
        """Uninitialized Composite variable declaration"""
        input = """Var: x[2];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 208))

    # Test 9
    def test_composite_var_declaration(self):
        """Composite variable declaration"""
        input = """Var: x[1] = {0};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 209))

    # Test 10
    def test_multi_dimension_var_declaration(self):
        """Multiple dimension variable declaration"""
        input = """Var: b[2][3]={{1,2,3},{4,5,6}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 210))

    # Test 11
    def test_multi_global_var_declaration(self):
        """Multi dimension variable declaration"""
        input = """ Var: a = 5;
                    Var: b[2][3] = {{2,3,4},{4,5,6}};
                    Var: c, d = 6, e, f;
                    Var: m, n[10];
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 211))

    # Test 12
    def test_invalid_var_initialization(self):
        """Empty variable initialization"""
        input = """Var: a = ;"""
        expect = "Error on line 1 col 9: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 212))

    # Test 13
    def test_wrong_declaration_miss_colon(self):
        """Empty variable initialization"""
        input = """Var: a = 3"""
        expect = "Error on line 1 col 10: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 213))

    # Test 14
    def test_empty_function_program(self):
        """A program with empty function"""
        input = """
        Function: main
            Body:
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 214))

    # Test 15
    def test_program_global_declaration(self):
        """A program with global declaration"""
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 215))

    # Parameter
    # Test 16
    def test_program_parameter(self):
        """Program with parameter"""
        input = """
        Function: main
        Parameter: a[5], b
        Body:
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 216))

    # Test 17
    def test_program_parameter_initialized(self):
        """Program with parameter"""
        input = """
        Function: main
        Parameter: x, b = 1
        Body:
        EndBody.
        """
        expect = "Error on line 3 col 24: ="
        self.assertTrue(TestParser.checkParser(input, expect, 217))

    # Expression
    # Test 18
    def test_arithmetic_integer_expression(self):
        """Program with simple expression with number arithmetic"""
        input = """
        Var: x,y,z,t;
        Function: main
        Body:
            x = 1 + 2 - 3 * 4;
            y = 0O45 \\ 0o12;
            z = 0xABFF;
            t = x % y;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 218))

    # Test 19
    def test_arithmetic_float_expression(self):
        """Program with simple expression with number arithmetic"""
        input = """
        Var: x,y,z;
        Function: main
        Body:
            x = 5.8 -. 1.2 +. 9.0;
            y = 100 *. x \\. 78.9e10;
            z = -.y; 
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 219))

    # Test 20
    def test_logical_not_expression(self):
        """Check boolean logical NOT expression"""
        input = """
        Var: x,y;
        Function: main
        Body:
            x = !y;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 220))

    # Test 21
    def test_logical_and_expression(self):
        """Check boolean logical AND expression"""
        input = """
        Var: x,y;
        Function: main
        Body:
            x = y && True;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 221))

    # Test 22
    def test_logical_or_expression(self):
        """Check boolean logical OR expression"""
        input = """
        Var: x,y;
        Function: main
        Body:
            x = y || False;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 222))

    # Test 23
    def test_relational_integer_expression(self):
        """Check relational integer expression"""
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 223))

    # Test 24
    def test_relational_float_expression(self):
        """Check boolean logical OR expression"""
        input = """
        Var: x,y,z,t,w;
        Function: main
        Body:
            x = y =/= 15.8e12;
            y = x <. 10.e-12;
            z = y >. 3e10;
            t = z <=. 789.3456;
            w = t >=. 0.1;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 224))

    # Test 25
    def test_index_expression(self):
        """Check index operator expression"""
        input = """
        Var: x,y,z;
        Function: main
        Body:
            x[3] = y[1] + 4;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 225))

    # Test 26
    def test_index_expression_with_function(self):
        """Check index operator expression with function"""
        input = """
        Var: x,y,z;
        Function: main
        Body:
            x = y[10*func(15)];
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 226))

    # Test 27
    def test_index_nested_expression(self):
        """Check nested index operator expression"""
        input = """
        Var: x,y,z;
        Function: main
        Body:
            a[3 + foo(2)] = a[b[2][3]] + 4;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 227))

    # Test 28
    def test_function_call_empty_expression(self):
        """Check function call expression with no parameter"""
        input = """
        Var: x,y,z;
        Function: main
        Body:
            x = foo(1);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 228))

    # Test 29
    def test_function_call_expression(self):
        """Check function call expression with parameter"""
        input = """
        Var: x,y,z;
        Function: main
        Body:
            x = foo(x - 5, y * 3, z + 20);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 229))

    # Test 30
    def test_multiple_expression(self):
        """Check multiple expressions"""
        input = """
        Var: x,y,z,t,w,g,h;
        Function: main
        Body:
            x = foo(12.5);
            y = x[a[10][2]] - 5.7;
            z = -.9;
            t = !y;
            w = 1235 \\ 5;
            g = t && True;
            h = x >=. y;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 230))

    # Test statement
    # Test 31
    def test_var_declaration_statement(self):
        """Check variable declaration statement"""
        input = """
        Function: main
        Body:
            Var: r = 10., v;
            v = (4. \\. 3.) *. 3.14 *. r *. r *. r;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 231))

    # Test 32
    def test_assign_statement(self):
        """Check assign statement"""
        input = """
        Function: main
        Body:
            Var: r = 10., v, t, ans;
            v = (4. \\. 3.) *. 3.14 *. r *. r *. r;
            t = (15.79 *. 79e13) \\. 89.3;
            ans = t =/= v;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 232))

    # Test 33
    def test_if_statement(self):
        """Check if statement"""
        input = """
        Function: main
        Body:
            If a == b Then a = a + 1;
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 233))

    # Test 34
    def test_if_statement_with_multi_stmt(self):
        """Check if statement with a list of statements"""
        input = """
        Function: main
        Body:
            If a != True Then 
                a = a + 1;
                b = b * 2;
                c = a \\. b;
                ans = (a + b) * c;
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 234))

    # Test 35
    def test_if_else_statement(self):
        """Check if else statement"""
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 235))

    # Test 36
    def test_if_elseif_statement(self):
        """Check if elseif else statement"""
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 236))

    # Test 37
    def test_call_statement(self):
        """Check call statement"""
        input = """
        Function: main
        Body:
            foo (2 + x, 4. \\. y);
            goo ();
            func(x + y);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 237))

    # Test 38
    def test_if_empty_statement(self):
        """Check if with no statement"""
        input = """
        Function: main
        Body:
            If y == False Then 
                
            ElseIf z == True Then
                
            Else
                
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 238))

    # Test 39
    def test_if_nested_statement(self):
        """Check nested if statement"""
        input = """
        Function: main
        Body:
            If age > 18 Then 
                If height < 20 Then
                    print("Congratulation");
                EndIf.
            ElseIf age > 13 Then
                writeln("Good luck");
            Else
                writeln("No");
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 239))

    # Test 40
    def test_for_statement(self):
        """Check for statement"""
        input = """
        Function: main
        Body:
            For(i = 1, i < 10, 1) Do
                x =  x + 1;
                y = z[p[2]];
            EndFor. 
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 240))

    # Test 41
    def test_for_statement_null_list(self):
        """Check for statement with null list"""
        input = """
        Function: main
        Body:
            For(i = 1, i < 10, -2) Do EndFor. 
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 241))

    # Test 42
    def test_nested_for_statement(self):
        """Check nested for statement"""
        input = """
        Function: main
            Body:
                For(i = 1, i < 10, -2) Do 
                    For(j = 0, j < 15, 1) Do
                        println(arr[i][j]);
                    EndFor.
                    writeln();
                EndFor. 
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 242))

    # Test 43
    def test_while_statement(self):
        """Check while statement"""
        input = """
        Function: main
        Body:
            While x < 5 Do
                 writeln(x);
            EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 243))

    # Test 44
    def test_while_statement_null_list(self):
        """Check while statement with null statement list"""
        input = """
        Function: main
            Body:
                While num >= 12 Do EndWhile.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 244))

    # Test 45
    def test_nested_while_statement(self):
        """Check nested while statement"""
        input = """
        Function: main
        Body:
            While num >= 12 Do
                While j != True Do
                    If(a == b) Then
                        c = a + b;
                    EndIf.
                EndWhile.
                writeln("Hello World");
            EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 245))

    # Test 46
    def test_do_while_statement(self):
        """Check do while statement"""
        input = """
        Function: main
        Body:
            Do 
                print(x);
                calculate(y);
                z = x + y;
            While num <= 100 EndDo.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 246))

    # Test 47
    def test_do_while_statement_null_list(self):
        """Check while statement with null statement list"""
        input = """
        Function: main
        Body:
            Do While num <= 100 EndDo.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 247))

    # Test 48
    def test_nested_do_while_statement(self):
        """Check do while statement"""
        input = """
        Function: main
        Body:
            Do 
                Do
                    calculate(y);
                    z = x + y;
                While i >= 10 EndDo.
                print(x);
            While num <= 100 EndDo.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 248))

    # Test 49
    def test_break_statement(self):
        """Check while statement with null statement list"""
        input = """
        Function: main
        Body:
            Break;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 249))

    # Test 50
    def test_continue_statement(self):
        """Check while statement with null statement list"""
        input = """
        Function: main
        Body:
            Continue;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 250))

    # Test 51
    def test_return_null_statement(self):
        """Check return null value statement"""
        input = """
        Function: main
        Body:
            Return;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 251))

    # Test 52
    def test_return_literal_statement(self):
        """Check return literal value statement"""
        input = """
        Function: main
        Body:
            Return 100;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 252))

    # Test 53
    def test_return_function_statement(self):
        """Check return literal value statement"""
        input = """
        Function: main
        Body:
            Return foo(x);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 253))

    # Test invalid expression
    # Test 54
    def test_invalid_relational_statement(self):
        """Check invalid relational statement"""
        input = """
        Function: main
        Parameter: x, y
           Body:
               x = 6 5 >=;
           EndBody.
           """
        expect = "Error on line 5 col 21: 5"
        self.assertTrue(TestParser.checkParser(input, expect, 254))

    # Test 55
    def test_invalid_logical_statement(self):
        """Check invalid logical statement"""
        input = """
        Function: main
        Parameter: x, y
           Body:
               x = &&y;
           EndBody.
           """
        expect = "Error on line 5 col 19: &&"
        self.assertTrue(TestParser.checkParser(input, expect, 255))

    # Test 56
    def test_invalid_adding_statement(self):
        """Check invalid adding statement"""
        input = """
        Function: main
        Parameter: x, y
           Body:
               x = y z +;
           EndBody.
           """
        expect = "Error on line 5 col 21: z"
        self.assertTrue(TestParser.checkParser(input, expect, 256))

    # Test 57
    def test_invalid_multiplying_statement(self):
        """Check invalid multiplying statement"""
        input = """
        Function: main
        Parameter: x, y
           Body:
               x = \\ y 5;
           EndBody.
           """
        expect = "Error on line 5 col 19: \\"
        self.assertTrue(TestParser.checkParser(input, expect, 257))

    # Test 58
    def test_invalid_logical_not_statement(self):
        """Check invalid logical not statement"""
        input = """
        Function: main
        Parameter: x, y
           Body:
               x = ans!;
           EndBody.
           """
        expect = "Error on line 5 col 22: !"
        self.assertTrue(TestParser.checkParser(input, expect, 258))

    # Test 59
    def test_invalid_index_statement(self):
        """Check invalid index statement"""
        input = """
        Function: main
        Parameter: x, y
           Body:
               x[1] = [0]arr;
           EndBody.
           """
        expect = "Error on line 5 col 22: ["
        self.assertTrue(TestParser.checkParser(input, expect, 259))

    # Invalid statement
    # Test 60
    def test_invalid_var_declaration(self):
        """Check invalid variable declaration statement(not at the top)"""
        input = """
        Function: main
        Body:
            v = (4. \\. 3.) *. 3.14 *. r *. r *. r;
            Var: r = 10., v;
        EndBody.
        """
        expect = "Error on line 5 col 12: Var"
        self.assertTrue(TestParser.checkParser(input, expect, 260))

    # Test 61
    def test_invalid_assign_null_statement(self):
        """Check invalid assign statement (empty)"""
        input = """
        Function: main
        Parameter: x, y
        Body:
            a = ;
        EndBody.
        """
        expect = "Error on line 5 col 16: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 261))

    # Test 62
    def test_invalid_assign_statement(self):
        """Check invalid assign statement (wrong assignment)"""
        input = """
        **Wrong assignment to statement**
        Function: main
            Parameter: x, y
            Body:
                a = Return True; 
            EndBody.
        """
        expect = "Error on line 6 col 20: Return"
        self.assertTrue(TestParser.checkParser(input, expect, 262))

    # Test 63
    def test_invalid_if_statement_miss_expression(self):
        """Check invalid if statement (missing conditional expression)"""
        input = """
        Function: main
        Parameter: x, y
            Body:
                 If Then 
                    foo(100);
                    hoo(1.5);
                    x = x - 1;
                EndIf.
            EndBody.
        """
        expect = "Error on line 5 col 20: Then"
        self.assertTrue(TestParser.checkParser(input, expect, 263))

    # Test 64
    def test_invalid_if_statement_wrong_expression(self):
        """Check invalid if statement (statement instead of expression)"""
        input = """
        Function: main
        Parameter: x, y
            Body:
                If a = 2 Then 
                    foo(100);
                    hoo(1.5);
                    x = x - 1;
                EndIf.
            EndBody.
        """
        expect = "Error on line 5 col 21: ="
        self.assertTrue(TestParser.checkParser(input, expect, 264))

    # Test 65
    def test_invalid_if_statement_miss_keyword(self):
        """Check invalid if statement (missing then keyword)"""
        input = """
        Function: main
        Parameter: x, y
            Body:
                If a > 10  
                    foo(100);
                    hoo(1.5);
                    x = x - 1;
                EndIf.
            EndBody.
        """
        expect = "Error on line 6 col 20: foo"
        self.assertTrue(TestParser.checkParser(input, expect, 265))

    # Test 66
    def test_invalid_if_statement_unclosed(self):
        """Check invalid if statement (unclosed if statement)"""
        input = """
        Function: main
        Parameter: x, y
            Body:
                If a > 10 Then
                    foo(100);
                    koo(300.6);
                    z = z * 10;
            EndBody.
        """
        expect = "Error on line 9 col 12: EndBody"
        self.assertTrue(TestParser.checkParser(input, expect, 266))

    # Test 67
    def test_invalid_if_elseif_statement(self):
        """Check invalid if else if statement"""
        input = """
        Function: main
        Parameter: x, y
            Body:
                If a > 10 Then
                    foo(100);
                    koo(300.6);
                    z = z * 10;
                ElseIf Then
                    cal(133);
                EndIf.    
            EndBody.
        """
        expect = "Error on line 9 col 23: Then"
        self.assertTrue(TestParser.checkParser(input, expect, 267))

    # Test 68
    def test_invalid_if_else_statement(self):
        """Check invalid if else statement"""
        input = """
        Function: main
        Parameter: x, y
            Body:
                If a > 10 Then
                    foo(100);
                    cal(300.6);
                    w = w \\ 10;
                Else b <= 10 Then
                    exe(123);
                EndIf.    
            EndBody.
        """
        expect = "Error on line 9 col 23: <="
        self.assertTrue(TestParser.checkParser(input, expect, 268))

    # Test 69
    def test_invalid_if_statement_wrong_order(self):
        """Check invalid if else statement(wrong order)"""
        input = """
        Function: main
        Parameter: x, y
            Body:
                If a > 10 Then
                    foo(100);
                    cal(300.6);
                    w = w \\ 10;
                Else
                    print(123);
                ElseIf b <= 988 Then
                    func(10);
                EndIf.    
            EndBody.
        """
        expect = "Error on line 11 col 16: ElseIf"
        self.assertTrue(TestParser.checkParser(input, expect, 269))

    # Test 70
    def test_invalid_for_statement_wrong_condition_format(self):
        """Check invalid for statement wrong conditional format"""
        input = """
        Function: main
        Parameter: x, y
            Body:
                For(i = 1, i < 10, i = i + 1) Do
                    print(arr[i]);
                EndFor.    
            EndBody.
        """
        expect = "Error on line 5 col 37: ="
        self.assertTrue(TestParser.checkParser(input, expect, 270))

    # Test 71
    def test_invalid_for_statement_wrong_condition_order(self):
        """Check invalid for statement with wrong order of conditional expression"""
        input = """
        Function: main
        Parameter: x, y
            Body:
                For(i < 10, 2, i = 1) Do
                    print(arr[i]);
                    foo(ans[i]);
                EndFor.    
            EndBody.
        """
        expect = "Error on line 5 col 22: <"
        self.assertTrue(TestParser.checkParser(input, expect, 271))

    # Test 72
    def test_invalid_for_statement_missing_condition(self):
        """Check invalid for statement missing condition"""
        input = """
        Var: i = 1;
        Function: main
        Parameter: x, y
            Body:
                For() Do
                    print(arr[i]);
                    foo(ans[i]);
                EndFor.    
            EndBody.
        """
        expect = "Error on line 6 col 20: )"
        self.assertTrue(TestParser.checkParser(input, expect, 272))

    # Test 73
    def test_invalid_for_statement_missing_keyword(self):
        """Check invalid for statement missing condition"""
        input = """
        Function: main
        Parameter: x, y
            Body:
                For(i = 1, i < 10, 2)
                    print(arr[i]);
                    foo(ans[i]);
                    soo(res[i]);
                EndFor.    
            EndBody.
        """
        expect = "Error on line 6 col 20: print"
        self.assertTrue(TestParser.checkParser(input, expect, 273))

    # Test 74
    def test_invalid_for_statement_unterminated(self):
        """Check invalid for statement unterminated"""
        input = """
        Function: main
        Parameter: x, y
            Body:
                For(i = 1, i < 10, 2) Do
                    print(arr[i]);
                    foo(ans[i]);
                    x = (x + 1);
                    a[3 + foo(2)] = a[b[2][3]] + 4;
                    soo(res[i]);
                  
            EndBody.
        """
        expect = "Error on line 12 col 12: EndBody"
        self.assertTrue(TestParser.checkParser(input, expect, 274))

    # Test 75
    def test_invalid_while_statement_wrong_condition(self):
        """Check invalid while statement wrong condition(expression)"""
        input = """
        Function: main
        Parameter: x, y
            Body:
                While x = 7 Do
                    exe(x);
                    print(x);
                EndWhile.
            EndBody.
        """
        expect = "Error on line 5 col 16: While"
        self.assertTrue(TestParser.checkParser(input, expect, 275))

    # Test 76
    def test_invalid_while_statement_missing_condition(self):
        """Check invalid while statement missing condition"""
        input = """
        Function: main
        Parameter: x, y
            Body:
                While Do
                    foo (2 + x, 4. \\. y);
                    exe(x);
                    print(x);
                EndWhile.
            EndBody.
        """
        expect = "Error on line 5 col 16: While"
        self.assertTrue(TestParser.checkParser(input, expect, 276))

    # Test 77
    def test_invalid_while_statement_missing_keyword(self):
        """Check invalid while statement missing keyword"""
        input = """
        Function: main
        Parameter: x, y
            Body:
                While Do
                    foo (2 + x, 4. \\. y);
                    func(9.5 *. 10.0);
                EndWhile.
            EndBody.
        """
        expect = "Error on line 5 col 16: While"
        self.assertTrue(TestParser.checkParser(input, expect, 277))

    # Test 78
    def test_invalid_while_statement_unterminated(self):
        """Check invalid while statement missing keyword"""
        input = """
        Function: main
        Parameter: x, y
            Body:
                Var: b[2][3] = {{2,3,4},{4,5,6}};
                While x > 15 Do
                    foo (2 + x, 4. \\. y);
                    func(9.5 *. 10.0);
                
            EndBody.
        """
        expect = "Error on line 10 col 12: EndBody"
        self.assertTrue(TestParser.checkParser(input, expect, 278))

    # Test 79
    def test_invalid_do_while_statement_wrong_condition(self):
        """Check invalid do while statement wrong condition"""
        input = """
        Function: main
        Parameter: x, y
            Body:
                Do 
                    cal(x);
                    process(y);
                    ans = x + y;
                While num = 100 EndDo.
            EndBody.
        """
        expect = "Error on line 9 col 26: ="
        self.assertTrue(TestParser.checkParser(input, expect, 279))

    # Test 80
    def test_invalid_do_while_statement_missing_condition(self):
        """Check invalid do while statement wrong condition"""
        input = """
        Function: main
        Parameter: x, y
            Body:
                Do 
                    cal(x);
                    process(y);
                    i = 0xFF;
                    y = 0O12;
                While EndDo.
            EndBody.
        """
        expect = "Error on line 10 col 22: EndDo"
        self.assertTrue(TestParser.checkParser(input, expect, 280))

    # Test 81
    def test_invalid_do_while_statement_missing_keyword(self):
        """Check invalid do while statement missing keyword"""
        input = """
        Function: main
        Parameter: x, y
            Body:
                 Do
                    cal(x);
                    z = 19.5;
                    i = 10.e10;
                    y = 98e-10;
                 i <= 100 EndDo.
            EndBody.
        """
        expect = "Error on line 10 col 19: <="
        self.assertTrue(TestParser.checkParser(input, expect, 281))

    # Test 82
    def test_invalid_do_while_statement_unterminated(self):
        """Check invalid do while statement unterminated"""
        input = """
        Function: main
        Parameter: x, y
            Body:
                 Do
                    foo(x);
                    z = 19.5;
                    i = 10.e10;
                    y = 98e-10;
                    t = 10.7e-98;
                 While i <= 100 
            EndBody.
        """
        expect = "Error on line 12 col 12: EndBody"
        self.assertTrue(TestParser.checkParser(input, expect, 282))

    # Test 83
    def test_invalid_continue_statement_nonempty(self):
        """Check invalid continue statement nonempty"""
        input = """
        Function: main
        Parameter: x, y
            Body:
                For(i=1, i < 10, 1) Do
                    x = x + 1;
                    y = z[p[x]];
                    If y == 10 Then
                        Continue foo(x);
                    EndIf.
                EndFor. 
            EndBody.
            """
        expect = "Error on line 9 col 33: foo"
        self.assertTrue(TestParser.checkParser(input, expect, 283))

    # Test 84
    def test_invalid_continue_statement_wrong_format(self):
        """Check invalid continue statement wrong format"""
        input = """
        Function: main
        Parameter: x, y
            Body:
                For(i=1, i < 10, 1) Do
                    x = x + 1;
                    y = z[p[x]];
                    If y == 10 Then
                        Continue
                    EndIf.
                EndFor. 
            EndBody.
            """
        expect = "Error on line 10 col 20: EndIf"
        self.assertTrue(TestParser.checkParser(input, expect, 284))

    # Test 85
    def test_invalid_call_statement_wrong_format(self):
        """Check invalid call statement wrong format"""
        input = """
        ** This is a comment **
        Function: main
        Parameter: x, y
            Body:
                foo();
                aoo(x);
                calculate;
            EndBody.
            """
        expect = "Error on line 8 col 25: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 285))

    # Test 86
    def test_invalid_call_statement_wrong_initialization(self):
        """Check invalid call statement variable initialized"""
        input = """
        ** This is a comment **
        Function: main
        Parameter: x, y
            Body:
                foo();
                aoo(x);
                calculate(x, y, z);
                foo(2 + x, 4. \\. y);
                roo(x = 9, y = 10);
            EndBody.
            """
        expect = "Error on line 10 col 22: ="
        self.assertTrue(TestParser.checkParser(input, expect, 286))

    # Test 87
    def test_invalid_return_statement_wrong_format(self):
        """Check invalid return statement wrong format(statement)"""
        input = """
        ** This 
        is 
        a multi-line
        comment **
        Function: main
        Parameter: x, y
            Body:
                Return x = 1;
            EndBody.
            """
        expect = "Error on line 9 col 25: ="
        self.assertTrue(TestParser.checkParser(input, expect, 287))

    # Test 88
    def test_invalid_return_statement_missing_format(self):
        """Check invalid call statement missing termination"""
        input = """
        ** This 
        is 
        a multi-line
        comment **
        Function: main
        Parameter: x, y
            Body:
                Return True
            EndBody.
            """
        expect = "Error on line 10 col 12: EndBody"
        self.assertTrue(TestParser.checkParser(input, expect, 288))

    # Test parameter
    # Test 89
    def test_parameter_uninitialized(self):
        """Check parameter uninitialized"""
        input = """
        Function: main
        Parameter: x, y
            Body:
                x = x + y;
                Return x;
            EndBody.
            
        Function: foo
        Parameter: a, b
            Body:
                b =  b - a;
                Return b;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 289))

    # Test 90
    def test_invalid_parameter_empty(self):
        """Check invalid parameter empty"""
        input = """
        Function: main
        Parameter: x, y
            Body:
                x = x + y;
                Return x;
            EndBody.

        Function: foo
        Parameter:
            Body:
                b =  b - a;
                Return b;
            EndBody.
        """
        expect = "Error on line 11 col 12: Body"
        self.assertTrue(TestParser.checkParser(input, expect, 290))

    # Test 91
    def test_invalid_parameter_initialized(self):
        """Check invalid parameter variable initialized"""
        input = """
        Function: main
        Parameter: x, y
            Body:
                x = x + y;
                Return x;
            EndBody.

        Function: foo
        Parameter: a = 1
            Body:
                b =  b - a;
                Return b;
            EndBody.
        """
        expect = "Error on line 10 col 21: ="
        self.assertTrue(TestParser.checkParser(input, expect, 291))

    # Test 92
    def test_invalid_parameter_wrong_order(self):
        """Check invalid parameter rong order"""
        input = """
        ** A simple program **
        Function: foo
            Body:
                b =  b - a;
                Return b;
            EndBody.
        Parameter: a, b
        """
        expect = "Error on line 8 col 8: Parameter"
        self.assertTrue(TestParser.checkParser(input, expect, 292))

    # Test invalid program structure
    # Test 93
    def test_invalid_program_unnamed_function(self):
        """Check program with statement"""
        input = """
        ** A simple program **
        Var: x;
        Function:
        Parameter: n
            Body:
                func("yeah");
            EndBody.
        Function: main
            Body:
                print(ans);
            EndBody.
        """
        expect = "Error on line 5 col 8: Parameter"
        self.assertTrue(TestParser.checkParser(input, expect, 293))

    # Test 94
    def test_invalid_program_no_body(self):
        """Check program with statement"""
        input = """
        ** A simple program **
        Var: x;
        Function: foo
        Parameter: n

        Function: main
            Body:
                print(ans);
            EndBody.
        """
        expect = "Error on line 7 col 8: Function"
        self.assertTrue(TestParser.checkParser(input, expect, 294))

    # Test 95
    def test_invalid_program_wrong_format(self):
        """Check program with statement"""
        input = """
        ** A simple program **
        Var: x;
        Function: x = y
            Body:
                print(ans);
            EndBody.
        """
        expect = "Error on line 4 col 20: ="
        self.assertTrue(TestParser.checkParser(input, expect, 295))

    # Test mixed program
    # Test 96
    def test_simple_program(self):
        """Check a simple program"""
        input = """
        ** A simple program **
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
                fact (x);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 296))

    # Test 97
    def test_program_global_local_declaration(self):
        """Check program with global and local declaration"""
        input = """
        ** A simple program **
        Var: x;
        Function: fact
        Parameter: n
            Body:
                Var: r = 10., v, t, ans;
                x = foo(x - 5, y * 3, z + 20);
            EndBody.
        Function: main
            Body:
                x = 10;
                fact (x);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 297))

    # Test 98
    def test_program_loops(self):
        """Check program with loops"""
        input = """
        ** A simple program **
        Var: x;
        Function: fact
        Parameter: n
            Body:
                For(i = 1, i < 10, -2) Do 
                    For(j = 0, j < 15, 1) Do
                        println(arr[i][j]);
                    EndFor.
                    writeln();
                    While x < 5 Do
                        writeln(x);
                    EndWhile.
                EndFor.
            EndBody.
        Function: main
            Body:
                Do 
                    cal(x);
                    process(y);
                    ans = x + y;
                While num == 100 EndDo.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 298))

    # Test 99
    def test_program_expression(self):
        """Check program with expression"""
        input = """
        ** A simple program **
        Var: x;
        Function: fact
        Parameter: n
            Body:
                y = x[a[10][2]] + b[c[2][9]];
                x = (func(12.5) + foo(79.10e-12)) * 10; 
                isValid = x && y;
                isGood = x > y;
                z = !y || exe(89465.654);
                w = -.z;
            EndBody.
        Function: main
            Body:
                print(ans);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 299))

    # Test 100
    def test_program_statement(self):
        """Check program with statement"""
        input = """
        ** A simple program **
        Var: x;
        Function: fact
        Parameter: n
            Body:
                Var: ans = 10.12, x, y, z;
                x = (4. \\. 3.) *. 3.14 *. r *. r *. r;
                If x =/= 78.92 Then 
                    ans = ans * ans;
                Else
                    ans = ans - 1;
                EndIf.
                For(i = 1, i < 10, -2) Do print(i); EndFor.
                While num >= 12 Do foo(num); EndWhile. 
                Do goo(2); While num <= 100 EndDo.
            EndBody.
        Function: main
            Body:
                print(ans);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 300))

    def test(self):
        """Check program with statement"""
        input = """
        ** A simple program **
        Var: x;
        Function: fact
            Body:
            x[2][3] = 1;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 301))

