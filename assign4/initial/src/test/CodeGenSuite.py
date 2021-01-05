import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_0(self):
        """Global Var"""
        input = 'Var: a=9, b=15.7; Function: main Body: print(string_of_int(a)); EndBody.'

        expect = '9'
        self.assertTrue(TestCodeGen.test(input, expect, 500))

    def test_1(self):
        input = 'Var: a=10, b=0x12; Function: main Body: print(string_of_int(a+b)); EndBody.'

        expect = '28'
        self.assertTrue(TestCodeGen.test(input, expect, 501))

    def test_2(self):
        input = 'Var: a=10, x=97.2; Function: main Body: print(string_of_float(x)); EndBody.'

        expect = '97.2'
        self.assertTrue(TestCodeGen.test(input, expect, 502))

    def test_3(self):
        input = """Var: a=5;
        Function: main
        Body:
            Var: b= "game";
            print(b);
        EndBody."""

        expect = 'game'
        self.assertTrue(TestCodeGen.test(input, expect, 503))

    def test_4(self):
        input = 'Var: a=5,b="string";  Function: main Body: Var: b= "throne"; print(b); EndBody.'

        expect = 'throne'
        self.assertTrue(TestCodeGen.test(input, expect, 504))

    def test_5(self):
        input = """Var: a = 10,b = "string";
        Function: main
        Body:
            Var: b= "last of us";
            print(f(b));
        EndBody.
        Function: f
        Parameter: x
            Body:
                Return x;
        EndBody."""

        expect = 'last of us'
        self.assertTrue(TestCodeGen.test(input, expect, 505))

    def test_6(self):
        input = """Var: a=5,b="string";
        Function: main
        Body:
            Var: b= "deathstroke";
            print(f(a));
        EndBody.
        Function: f
        Parameter: x
        Body:
            Return string_of_int(x);
        EndBody."""

        expect = '5'
        self.assertTrue(TestCodeGen.test(input, expect, 506))

    def test_7(self):
        input = """Var: a=5,b="string";
        Function: main
        Body:
            Var: x=7,y="x",z=1.5;
            print(f(z));
        EndBody.
        Function: f
        Parameter: x
        Body:
            Return "unlock";
        EndBody."""

        expect = 'unlock'
        self.assertTrue(TestCodeGen.test(input, expect, 507))

    def test_8(self):
        input = """Var: a=5,b="string";
        Function: main
        Body:
            Var: x=7,y="x",z=1.5;
            print(f(z));
            EndBody.
        Function: f
        Parameter: x
        Body:
            Return string_of_float(x);
        EndBody."""

        expect = '1.5'
        self.assertTrue(TestCodeGen.test(input, expect, 508))

    def test_9(self):
        input = """Var: a=5,b="string";
        Function: main
        Body:
            Var: x=15,y="new",z=8.5;
            print(string_of_int(f(x)));
        EndBody.

        Function: f
        Parameter: x
        Body:
            Return -x;
        EndBody."""

        expect = '-15'
        self.assertTrue(TestCodeGen.test(input, expect, 509))

    def test_10(self):
        input = """Var: a=5,b="string";
        Function: main
        Body:
            Var: x=7,y="x",z=1.5;
            print(string_of_int(f1(a,x)));
        EndBody.
        Function: f1
        Parameter: x,y
        Body:
            Return x+y;
        EndBody."""

        expect = '12'
        self.assertTrue(TestCodeGen.test(input, expect, 510))

    def test_11(self):
        input = """Var: a=5,b="string";
        Function: main
        Body:
            Var: x=7,y="x",z=1.5;
            print(string_of_int(f(x)));
        EndBody.
        Function: f
        Parameter: x
        Body:
            Return x+5--x;
        EndBody."""

        expect = '19'
        self.assertTrue(TestCodeGen.test(input, expect, 511))

    def test_12(self):
        input = """Var: a=5,b="string",c=5.6;
        Function: main
        Body:
            Var: x=7,y="x",z=2,k = 1.5; 
            z = x + z -- z -- z\\2 +x*2;
            print(string_of_int(z));
        EndBody."""

        expect = '26'
        self.assertTrue(TestCodeGen.test(input, expect, 512))

    def test_13(self):
        input = """Var: a=5,b="string",c=5.6;
        Function: main
        Body:
            Var: x=7,y="x",z=2,k = 1.5; k = c +. k *.k -. float_to_int(z);
            print(string_of_float(k));
        EndBody."""

        expect = '5.85'
        self.assertTrue(TestCodeGen.test(input, expect, 513))

    def test_14(self):
        input = """Var: a=5,b="string",c=5.6;
        Function: main
        Body:
            Var: x=7,y="x",z=2,k = 1.5; z = x -1 + f1(k);
            print(string_of_int(z)); EndBody.
        Function: f1
        Parameter: x
        Body: Return int_of_float(x);
        EndBody."""

        expect = '7'
        self.assertTrue(TestCodeGen.test(input, expect, 514))

    def test_15(self):
        input = """Var: a=5,b="string",c=5.6;
        Function: main
        Body:
            Var: x=7,y="x",z=2,k = 1.5; b = "undo";
            print(b);
        EndBody. """

        expect = 'undo'
        self.assertTrue(TestCodeGen.test(input, expect, 515))

    def test_16(self):
        input = """Var: a=5,b="lmao",c=5.6;
        Function: main
        Body:
            Var: x=7,y="x",z=2,k = 1.5;
            Var: temp = "";
            temp = b;
            b=y;
            y= temp;
            print(b);
            print(y);
        EndBody. """

        expect = 'xlmao'
        self.assertTrue(TestCodeGen.test(input, expect, 516))

    def test_17(self):
        input = """Var: a=1.6, b= 0.4;
        Function: main
        Body:
            Var: t= True;
            f(a>.b);
            f(a<.b);
            f(a=/=b);
            f(a>=.b);
            f(a<=.b);
        EndBody.
        Function: f
        Parameter: x
        Body:
            print(string_of_bool(x));
            Return;
        EndBody."""

        expect = 'truefalsetruetruefalse'
        self.assertTrue(TestCodeGen.test(input, expect, 517))

    def test_18(self):
        input = """Var: a=4, b= 5;
        Function: main
        Body:
            Var: t= True;
            f(a>b);
            f(a<b);
            f(a==b);
            f(a!=b);
            f(a>=b);
            f(a<=b);
        EndBody.

        Function: f
        Parameter: x
        Body:
            print(string_of_bool(x));
            Return;
        EndBody."""

        expect = 'falsetruefalsetruefalsetrue'
        self.assertTrue(TestCodeGen.test(input, expect, 518))

    def test_19(self):
        input = """Var: a=5,b="string",c=5.6;
        Function: main
        Body:
            Var: x=7,y="x",z=2,k = 1.5;
            print(f1(1,1.5,"2"));
        EndBody.
        Function: f1
        Parameter: a,b,c
        Body:
            Return string_of_int(a + int_of_float(b) + int_of_string(c));
        EndBody."""

        expect = '4'
        self.assertTrue(TestCodeGen.test(input, expect, 519))

    def test_20(self):
        input = 'Var: a=5,b="hey",c=5.6;  Function: main Body: print(b);  EndBody.'

        expect = 'hey'
        self.assertTrue(TestCodeGen.test(input, expect, 520))

    def test_21(self):
        input = """Var: a=10,b="string",c=7.8;
        Function: main
        Body:
            f1("random");
        EndBody.
        Function: f1
        Parameter: x
        Body:
            print("yeah");
            Return;
        EndBody."""

        expect = 'yeah'
        self.assertTrue(TestCodeGen.test(input, expect, 521))

    def test_22(self):
        input = """Var: a=5,b="string",c=5.6;
        Function: main
        Body:
            If a == 5
            Then print("yes");
        EndIf.
        EndBody."""

        expect = 'yes'
        self.assertTrue(TestCodeGen.test(input, expect, 522))

    def test_23(self):
        input = """Var: a=5,b="string",c=5.6;
        Function: main
        Body:
            If c =/= 6.0 Then
                print("no");
            EndIf.
        EndBody."""

        expect = 'no'
        self.assertTrue(TestCodeGen.test(input, expect, 523))

    def test_24(self):
        input = """Var: a=5,b="string",c=5.6;
        Function: main
        Body:
            If True Then
                print("True");
            Else
                print("false");
            EndIf.
        EndBody."""

        expect = 'True'
        self.assertTrue(TestCodeGen.test(input, expect, 524))

    def test_25(self):
        input = """Var: a=5,b="string",c=5.6;
        Function: main
        Body:
            If a==5 Then
                print("wow");
            Else print("nan");
        EndIf.
        EndBody."""

        expect = 'wow'
        self.assertTrue(TestCodeGen.test(input, expect, 525))

    def test_26(self):
        """Ifs"""
        input = """Var: a=5,b="string",c=5.6;
        Function: main
        Body:
            If (a >= 5) && (a <= 10 )Then
                a = 6;
            ElseIf a == 7 Then
                a = 7;
            Else
                a=10;
            EndIf.
            print(string_of_int(a));
        EndBody."""

        expect = '6'
        self.assertTrue(TestCodeGen.test(input, expect, 526))

    def test_27(self):
        """Ifs"""
        input = """Var: a=5,b="string",c=5.6;
        Function: main
        Body:
            If c >. 5.6 Then
                c = c +. 1.0;
            EndIf.
            print(string_of_float(c));
            If c <. 6e0 Then
                print("yes");
            Else print("No");
            EndIf.
        EndBody."""

        expect = '5.6yes'
        self.assertTrue(TestCodeGen.test(input, expect, 527))

    def test_28(self):
        input = """Function: main
        Body:
            Var: i = 7;
            If i == 1 Then
                print("1");
            ElseIf i==2 Then
                print("2");
            ElseIf i==3 Then
                print("3");
            ElseIf i==4 Then
                print("4");
            ElseIf i==7 Then
                print("7");
            Else
                print("greater");
            EndIf.
        EndBody."""

        expect = '7'
        self.assertTrue(TestCodeGen.test(input, expect, 528))

    def test_29(self):
        input = """Function: main
        Body:
            Var: i = 15;
            If i == 1 Then
                print("1");
            ElseIf i==2 Then
                print("2");
            ElseIf i == 3 Then
                print("3");
            ElseIf i==4 Then
                print("4");
            ElseIf i == 7 Then
                print("7");
            Else
                print("greater");
            EndIf.
        EndBody."""

        expect = 'greater'
        self.assertTrue(TestCodeGen.test(input, expect, 529))

    def test_30(self):
        input = """Function: main
        Body:
            Var: i = 1;
            If i == 1 Then
                print("1");
            ElseIf i==2 Then
                print("2");
            ElseIf i==3 Then
                print("3");
            ElseIf i==4 Then
                print("4");
            ElseIf i==7 Then
                print("7");
            Else
                print("greater");
            EndIf.
        EndBody."""

        expect = '1'
        self.assertTrue(TestCodeGen.test(input, expect, 530))

    def test_31(self):
        input = """Function: main
        Body:
            Var: a=1,b=2,c=3;
            If a +b +c > 3 Then
                If a+b>2 Then
                    If a>1 Then
                        print("a");
                    ElseIf b>1 Then
                        print("b");
                    Else
                        print("nei");
                    EndIf.
                EndIf.
            EndIf.
        EndBody."""

        expect = 'b'
        self.assertTrue(TestCodeGen.test(input, expect, 531))

    def test_32(self):
        """Ifs"""
        input = """Var:a=1,b=2,c=3;
        Function: main
        Body:
            f1(b);
        EndBody.
        Function: f1
        Parameter: a
        Body:
            If a>1 Then
                print("yes");
            EndIf.
                Return;
        EndBody."""

        expect = 'yes'
        self.assertTrue(TestCodeGen.test(input, expect, 532))

    def test_33(self):
        """Ifs"""
        input = """Var:a=1,b=2,c=3;
        Function: main
        Body:
            f1(a,b);
        EndBody.
        Function: f1
        Parameter: a,b
        Body:
            If a>b Then
                print("a");
            Else
                print("b");
            EndIf.
            Return;
        EndBody."""

        expect = 'b'
        self.assertTrue(TestCodeGen.test(input, expect, 533))

    def test_34(self):
        """Ifs"""
        input = """Var:a=1,b=2,c=3;
        Function: main
        Body:
            f1(1,1);
        EndBody.
        Function: f1
        Parameter: a,b
        Body:
            If a>b Then
                print("a");
            Else
                print("b");
            EndIf.
            Return;
        EndBody."""

        expect = 'b'
        self.assertTrue(TestCodeGen.test(input, expect, 534))

    def test_35(self):
        """Ifs"""
        input = """Var:a=1,b=2,c=3;
        Function: main
        Body:
            f1(4,5);
        EndBody.
        Function: f1
        Parameter: a,b
        Body:
            If a>b Then
                print(string_of_int(a));
            Else
                print(string_of_int(b));
            EndIf.
            Return;
        EndBody."""

        expect = '5'
        self.assertTrue(TestCodeGen.test(input, expect, 535))

    def test_36(self):
        """Fors"""
        input = """Var:a=1;
        Function: main
        Body:
            For(a=1, a <5, 1) Do
                Var: x = 100;
                print(string_of_int(x));
            EndFor.
        EndBody."""

        expect = '100100100100'
        self.assertTrue(TestCodeGen.test(input, expect, 536))

    def test_37(self):
        """Fors"""
        input = """Var:a=1,b=2,c=3;
        Function: main
        Body:
            Var: a = 15;
            For(a=1, a <5, 1) Do
                print(string_of_int(a));
            EndFor.
        EndBody."""

        expect = '1234'
        self.assertTrue(TestCodeGen.test(input, expect, 537))

    def test_38(self):
        """Fors"""
        input = """Var:a=1,b=2,c=3;
        Function: main
        Body:
            Var: a = 15;
            For(c=10,c>=0, -2) Do
                print(string_of_int(c));
            EndFor.
        EndBody."""

        expect = '1086420'
        self.assertTrue(TestCodeGen.test(input, expect, 538))

    def test_39(self):
        """Fors"""
        input = """Var:a=1,b=2,c=3;
        Function: main
        Body:
            Var: a = 15;
            For(c=1,c<=5, 1) Do
                print("start:");
                print(string_of_int( c));
                For(b=c-1,b>=-1,-1) Do
                    print(string_of_int(b));
                EndFor.
            EndFor.
        EndBody."""

        expect = 'start:10-1start:210-1start:3210-1start:43210-1start:543210-1'
        self.assertTrue(TestCodeGen.test(input, expect, 539))

    def test_40(self):
        """Fors"""
        input = """Var:a=1,b=2,c=3;
        Function:  main
        Body:
            Var: a = 15;
            For (a=b, a<c, 1) Do
                print(string_of_int(a));
            EndFor.
        EndBody."""

        expect = '2'
        self.assertTrue(TestCodeGen.test(input, expect, 540))

    def test_41(self):
        """Fors"""
        input = """Var:a=1,b=2,c=3;
        Function:  main
        Body:
            Var: a = 15,b=10,c=15;
            For(a=0,a<b,1) Do
                print(string_of_int(a));
            EndFor.
            For(b=0,b<c,1) Do
                print(string_of_int(b));
            EndFor.
        EndBody."""

        expect = '012345678901234567891011121314'
        self.assertTrue(TestCodeGen.test(input, expect, 541))

    def test_42(self):
        """Fors"""
        input = """Var:a=1,b=2,c=3;
        Function:main
        Body:
            Var: a = 15,b=10,c=15;
            For(a=0,a<10,1)  Do EndFor.
            print(string_of_int(a)); EndBody.
        """

        expect = '10'
        self.assertTrue(TestCodeGen.test(input, expect, 542))

    def test_43(self):
        """Fors"""
        input = """Var:a=1,b=2,c=3;
        Function:main
        Body:
            Var: a = 15;
            For(a=0,a<5,1) Do
                Var: i=0,j=0;
                i=b+a;
                j=c+a;
                print(string_of_int(i+j));
                EndFor.
        EndBody. """

        expect = '5791113'
        self.assertTrue(TestCodeGen.test(input, expect, 543))

    def test_44(self):
        """Fors"""
        input = """Var:a=1,b=2,c=3;
        Function:main
        Body:
            Var: a = 5,b=5,c=15;
            Var: i=0,j=0;
            For(i=a-5, j<b, c-14) Do
                print(string_of_int(i));
                j=j+2;
            EndFor.
        EndBody."""

        expect = '012'
        self.assertTrue(TestCodeGen.test(input, expect, 544))

    def test_45(self):
        """While"""
        input = """Var: a=1,b=2,c=3;
        Function: main
        Body:
            Var: x=5,y=6,z=7;
            While (z<0) Do
                print("yeas");
            EndWhile.
            print("?");
        EndBody."""

        expect = '?'
        self.assertTrue(TestCodeGen.test(input, expect, 545))

    def test_46(self):
        """While"""
        input = """Var: a=1,b=2,c=3;
        Function: main
        Body:
            Var: x=5,y=6,z=7;
            While (x>0) Do
                print("x");
                x=x-b;
            EndWhile.
            print("?");
        EndBody."""

        expect = 'xxx?'
        self.assertTrue(TestCodeGen.test(input, expect, 546))

    def test_47(self):
        """While"""
        input = """Var: a=1,b=2,c=3;
        Function: main
        Body:
            Var: x=5,y=6,z=7;
            While (y+z > x) Do
                print(string_of_int(y+z));
                y=y-a;
                z=z-a;
            EndWhile.
            print("?");
        EndBody."""

        expect = '131197?'
        self.assertTrue(TestCodeGen.test(input, expect, 547))

    def test_48(self):
        """While"""
        input = """Var: a=1,b=2,c=3;
        Function: main
        Body:
            Var: x=5,y=6,z=7;
            While (z>a) Do
                c= z;
                While (c>a) Do
                    print(string_of_int(c));
                    c=c-1;
                EndWhile.
                z=z-1;
            EndWhile.
            print("?");
        EndBody."""

        expect = '765432654325432432322?'
        self.assertTrue(TestCodeGen.test(input, expect, 548))

    def test_49(self):
        """While"""
        input = """Var: a=1,b=2,c=3;
        Function: main
        Body:
            Var: x=5,y=6,z=7;
            While (z>a) Do
                c= a;
                While (c<z) Do
                    print(string_of_int(c));
                    c=c+1;
                EndWhile.
                z=z-1;
            EndWhile.
            print("?");
        EndBody."""

        expect = '123456123451234123121?'
        self.assertTrue(TestCodeGen.test(input, expect, 549))

    def test_50(self):
        """While"""
        input = """Var: a=1,b=2,c=3;
        Function: main
        Body:
            Var: x=5,y=6,z=7;
            While (x>0) Do
                print(string_of_int(x));
                x=x-b;
            EndWhile.
            While(x<5) Do
                print(string_of_int(x));
                x=x+a;
            EndWhile.
            print(string_of_int(x));
        EndBody."""

        expect = '531-1012345'
        self.assertTrue(TestCodeGen.test(input, expect, 550))

    def test_51(self):
        """While"""
        input = """Var: a=1,b=2,c=3;
        Function: main
        Body:
            Var: x=5,y=6,z=7;
            While (x>0) Do
                print(string_of_int(x));
                x=x-b;
            EndWhile.
            While(x>0) Do
                print(string_of_int(x));
                x=x+a;
            EndWhile.
            print(string_of_int(x));
        EndBody."""

        expect = '531-1'
        self.assertTrue(TestCodeGen.test(input, expect, 551))

    def test_52(self):
        """While"""
        input = """Var: a=1,b=2,c=3;
        Function: main
        Body:
            Var: x=5,y=6,z=7;
            While (x>5) Do
                print(string_of_int(x));
                x=x-1;
            EndWhile.
        EndBody."""

        expect = ''
        self.assertTrue(TestCodeGen.test(input, expect, 552))

    def test_53(self):
        """DoWhile"""
        input = """Var: a=1,b=2,c=3; 
        Function: main 
        Body: 
            Var: x=5,y=6,z=7; 
            Do 
                print(string_of_int(x)); 
                x=x-1; 
            While x>5 EndDo.  
        EndBody."""

        expect = '5'
        self.assertTrue(TestCodeGen.test(input, expect, 553))

    def test_54(self):
        """DoWhile"""
        input = """Var: a=1,b=2,c=3; 
        Function: main 
        Body: 
            Var: x=5,y=6,z=7; 
            Do 
                print(string_of_int(z)); 
                z=z-b; 
            While z>a EndDo.  
        EndBody."""

        expect = '753'
        self.assertTrue(TestCodeGen.test(input, expect, 554))

    def test_55(self):
        """DoWhile"""
        input = """Var: a=1,b=2,c=3; 
        Function: main 
        Body: 
            Var: x=5,y=6,z=7; 
            Do 
                print("x"); 
                x=x-b; 
            While (x>0) EndDo.
            print("?"); 
        EndBody."""

        expect = 'xxx?'
        self.assertTrue(TestCodeGen.test(input, expect, 555))

    def test_int(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body:
                        print(string_of_int(120));
                   EndBody."""
        expect = "120"
        self.assertTrue(TestCodeGen.test(input, expect, 556))

    def test_int_ast(self):
        input = Program([
            FuncDecl(Id("main"), [], ([], [
                CallStmt(Id("print"), [
                    CallExpr(Id("string_of_int"), [IntLiteral(120)])])]))])
        expect = "120"
        self.assertTrue(TestCodeGen.test(input, expect, 557))
    #

    def test_shit(self):
        """Ifs"""
        input = """Var: a=5,b="string",c=5.6;
        Function: main
        Body:
            If a == 5 Then
                Var: x = "yes";
                print(x);
            EndIf.
        EndBody."""

        expect = 'yes'
        self.assertTrue(TestCodeGen.test(input, expect, 558))
