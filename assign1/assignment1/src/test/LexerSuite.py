import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    # Test identifier
    # 1
    def test_lower_identifier(self):
        """test lower identifiers"""
        self.assertTrue(TestLexer.checkLexeme("""abc""",
                                              """abc,<EOF>""", 101))

    # 2
    def test_wrong_token(self):
        """test wrong identifiers"""
        self.assertTrue(TestLexer.checkLexeme("""ab?svn""",
                                              """ab,Error Token ?""", 102))

    # 3
    def test_upper_identifier(self):
        """test upper identifiers"""
        self.assertTrue(TestLexer.checkLexeme("""APP""",
                                              """Error Token A""", 103))

    # 4
    def test_identifier_with_number(self):
        """test identifiers with number"""
        self.assertTrue(TestLexer.checkLexeme("""abcdef12345""",
                                              """abcdef12345,<EOF>""", 104))

    # 5
    def test_identifier_with_underscore(self):
        """test identifiers with underscore"""
        self.assertTrue(TestLexer.checkLexeme("""under_score_test""",
                                              """under_score_test,<EOF>""", 105))

    # 6
    def test_multiple_identifiers(self):
        """test multiple identifiers"""
        self.assertTrue(
            TestLexer.checkLexeme("""abc cAt chick_en123 fallO_u123t""",
                                  """abc,cAt,chick_en123,fallO_u123t,<EOF>""", 106))

    # 7
    def test_identifier_with_number_first(self):
        """test identifiers starting with number"""
        self.assertTrue(TestLexer.checkLexeme("""1abcdefgh""",
                                              """1,abcdefgh,<EOF>""", 107))

    # 8
    def test_identifier_with_valid_token(self):
        """test identifiers with tokens"""
        self.assertTrue(TestLexer.checkLexeme("""anc.def*ef01""", """anc,.,def,*,ef01,<EOF>""", 108))

    # Test keyword
    # 9
    def test_keyword(self):
        """test keyword"""
        self.assertTrue(TestLexer.checkLexeme("""Body""",
                                              """Body,<EOF>""", 109))

    # 10
    def test_keywords(self):
        """test many keyword"""
        self.assertTrue(TestLexer.checkLexeme("""Body Break Continue Do Else ElseIf""",
                                              """Body,Break,Continue,Do,Else,ElseIf,<EOF>""", 110))

    # 11
    def test_keyword_with_identifier(self):
        """test keyword with identifier"""
        self.assertTrue(TestLexer.checkLexeme("""If Else abcdef""",
                                              """If,Else,abcdef,<EOF>""", 111))

    # 12
    def test_keyword_with_number(self):
        """test keyword with number"""
        self.assertTrue(TestLexer.checkLexeme("""Parameter Return Then 123 456""",
                                              """Parameter,Return,Then,123,456,<EOF>""", 112))

    # 13
    def test_keyword_with_operator(self):
        """test keyword with operator"""
        self.assertTrue(TestLexer.checkLexeme("""EndFor EndWhile *For Function- If+""",
                                              """EndFor,EndWhile,*,For,Function,-,If,+,<EOF>""", 113))

    # 14
    def test_invalid_keyword(self):
        """test invalid keyword"""
        self.assertTrue(TestLexer.checkLexeme("""FunCtion""",
                                              """Error Token F""", 114))

    # 15
    def test_invalid_keyword_with_valid_keyword(self):
        """test invalid keyword with valid keyword"""
        self.assertTrue(TestLexer.checkLexeme("""ElseIf Endbody""",
                                              """ElseIf,Error Token E""", 115))

    # 16
    def test_keyword_variable_identifier(self):
        """test keyword with variable identifier"""
        self.assertTrue(TestLexer.checkLexeme("""Var x;""",
                                              """Var,x,;,<EOF>""", 116))

    # Test operator
    # 17
    def test_operator(self):
        """test operator"""
        self.assertTrue(TestLexer.checkLexeme("abc<=def>=dlc&&dmc",
                                              "abc,<=,def,>=,dlc,&&,dmc,<EOF>", 117))

    # 18
    def test_integer_operator(self):
        """test integer operator"""
        self.assertTrue(TestLexer.checkLexeme("""+ - * \\ % == != < > <= >=""",
                                              "+,-,*,\\,%,==,!=,<,>,<=,>=,<EOF>", 118))

    # 19
    def test_float_operator(self):
        """test float operator"""
        self.assertTrue(TestLexer.checkLexeme("""+. -. *. \\.  =/= <. >. <=. >=.""",
                                              """+.,-.,*.,\\.,=/=,<.,>.,<=.,>=.,<EOF>""", 119))

    # 20
    def test_boolean_operator(self):
        """test boolean operator"""
        self.assertTrue(TestLexer.checkLexeme("""! && ||""",
                                              """!,&&,||,<EOF>""", 120))

    # 21
    def test_invalid_operator(self):
        """test invalid operator"""
        self.assertTrue(TestLexer.checkLexeme("""ab&c""",
                                              """ab,Error Token &""", 121))

    # Test separator
    # 22
    def test_separator(self):
        """test separator"""
        self.assertTrue(TestLexer.checkLexeme("""() [] : . , ; {}""",
                                              """(,),[,],:,.,,,;,{,},<EOF>""", 122))

    # 23
    def test_separator_with_identifier(self):
        """test separator with identifier"""
        self.assertTrue(TestLexer.checkLexeme("""(name),{school};[gender,game]:yes""",
                                              """(,name,),,,{,school,},;,[,gender,,,game,],:,yes,<EOF>""", 123))

    # 24
    def test_separator_with_number(self):
        """test separator with number"""
        self.assertTrue(TestLexer.checkLexeme("""789,879;0123""",
                                              """789,,,879,;,0,123,<EOF>""", 124))

    # Test String literal
    # 25
    def test_normal_string(self):
        """test string literal"""
        self.assertTrue(TestLexer.checkLexeme(""" "A normal string" """,
                                              """A normal string,<EOF>""", 125))

    # 26
    def test_string_in_string(self):
        """test string contains string"""
        self.assertTrue(TestLexer.checkLexeme(""" "My favourite book is '"LOTR'"" """,
                                              """My favourite book is '"LOTR'",<EOF>""", 126))

    # 27
    def test_normal_string_with_escape(self):
        """test string literal with escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  """,
                                              """ab'"c\\n def,<EOF>""", 127))

    # 28
    def test_illegal_escape(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  """,
                                              """Illegal Escape In String: abc\\h""", 128))

    # 29
    def test_unterminated_string(self):
        """test unterminated string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc def  """,
                                              """Unclosed String: abc def  """, 129))

    # 30
    def test_normal_string_with_tab(self):
        """test normal string with tab"""
        self.assertTrue(TestLexer.checkLexeme(""" "This is a string\t containing tab \\t" """,
                                              """This is a string	 containing tab \\t,<EOF>""", 130))

    # 31
    def test_string_with_invalid_quote(self):
        """test string literal with illegal quote"""
        self.assertTrue(TestLexer.checkLexeme(""" "A simple sentence' in a paragraph" """,
                                              """Illegal Escape In String: A simple sentence' """, 131))

    # 32
    def test_string_invalid_newline(self):
        """test string literal with illegal newline"""
        self.assertTrue(TestLexer.checkLexeme(""" "\nA definite tutorial" """,
                                              """Unclosed String: \n""", 132))

    # 33
    def test_string_multiple_escape(self):
        """test string literal with many escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "Time \\b of \\f life \\t somewhere" """,
                                              """Time \\b of \\f life \\t somewhere,<EOF>""", 133))

    # 34
    def test_string_with_special_character(self):
        """test string literal with special character"""
        self.assertTrue(TestLexer.checkLexeme(""" "Sword of ?()*^ destiny@" """,
                                              """Sword of ?()*^ destiny@,<EOF>""", 134))

    # 35
    def test_multiple_string(self):
        """test string literal with strings inside"""
        self.assertTrue(TestLexer.checkLexeme(""" "Blood of ""Elves""Witch" """,
                                              """Blood of ,Elves,Witch,<EOF>""", 135))

    # 36
    def test_invalid_quote(self):
        """test string literal unescaped quote"""
        self.assertTrue(TestLexer.checkLexeme(""" "Hi It's Johnny" """,
                                              """Illegal Escape In String: Hi It's""", 136))

    # Test Integer literal
    # 37
    def test_normal_integer(self):
        """test integer literal"""
        self.assertTrue(TestLexer.checkLexeme(""" 12345 """,
                                              """12345,<EOF>""", 137))

    # 38
    def test_long_integer(self):
        """test long integer literal"""
        self.assertTrue(TestLexer.checkLexeme(""" 1234567891012131415161420 """,
                                              """1234567891012131415161420,<EOF>""", 138))

    # 39
    def test_invalid_integer(self):
        """test invalid integer literal"""
        self.assertTrue(TestLexer.checkLexeme(""" 123_456""",
                                              """123,Error Token _""", 139))

    # 40
    def test_invalid_integer_with_zero(self):
        """test invalid integer literal with initial zero"""
        self.assertTrue(TestLexer.checkLexeme(""" 097577 """,
                                              """0,97577,<EOF>""", 140))

    # 41
    def test_single_zero(self):
        """test integer literal with single zero"""
        self.assertTrue(TestLexer.checkLexeme(""" 0 """,
                                              """0,<EOF>""", 141))

    # 42
    def test_hexadecimal_lower(self):
        """test hexadecimal lowercase"""
        self.assertTrue(TestLexer.checkLexeme(""" 0x45FF """,
                                              """0x45FF,<EOF>""", 142))

    # 43
    def test_hexadecimal_upper(self):
        """test hexadecimal uppercase"""
        self.assertTrue(TestLexer.checkLexeme(""" 0XABC """,
                                              """0XABC,<EOF>""", 143))

    # 44
    def test_invalid_hexadecimal_lower(self):
        """test invalid hexadecimal lowercase"""
        self.assertTrue(TestLexer.checkLexeme(""" 0x12AH """,
                                              """0x12A,Error Token H""", 144))

    # 45
    def test_invalid_hexadecimal_upper(self):
        """test invalid hexadecimal uppercase"""
        self.assertTrue(TestLexer.checkLexeme(""" 0X789EK """,
                                              """0X789E,Error Token K""", 145))

    # 46
    def test_octal_lower(self):
        """test octal lowercase"""
        self.assertTrue(TestLexer.checkLexeme(""" 0o567 """,
                                              """0o567,<EOF>""", 146))

    # 47
    def test_octal_upper(self):
        """test octal uppercase"""
        self.assertTrue(TestLexer.checkLexeme(""" 0O77 """,
                                              """0O77,<EOF>""", 147))

    # 48
    def test_invalid_octal_number(self):
        """test invalid octal number"""
        self.assertTrue(TestLexer.checkLexeme(""" 0o4589 """,
                                              """0o45,89,<EOF>""", 148))

    # 49
    def test_invalid_octal_letter(self):
        """test invalid octal with wrong letter"""
        self.assertTrue(TestLexer.checkLexeme(""" 0O627A12 """,
                                              """0O627,Error Token A""", 149))

    # 50
    def test_all_integer(self):
        """test multiple integers"""
        self.assertTrue(TestLexer.checkLexeme(""" 0 199 0xFF 0XABC 0o567 0O77 """,
                                              """0,199,0xFF,0XABC,0o567,0O77,<EOF>""", 150))

    # 51
    def test_hexadecimal_zero_after_prefix_lower(self):
        """test hexadecimal with zero after prefix lowercase"""
        self.assertTrue(TestLexer.checkLexeme(""" 0x01234 """,
                                              """0,x01234,<EOF>""", 151))

    # 52
    def test_hexadecimal_zero_after_prefix_upper(self):
        """test hexadecimal with zero after prefix upper"""
        self.assertTrue(TestLexer.checkLexeme(""" 0X0ABC """,
                                              """0,Error Token X""", 152))

    # 53
    def test_octal_zero_after_prefix_lower(self):
        """test octal with zero after prefix lowercase"""
        self.assertTrue(TestLexer.checkLexeme(""" 0o01253 """,
                                              """0,o01253,<EOF>""", 153))

    # 54
    def test_octal_zero_after_prefix_upper(self):
        """test octal with zero after prefix upper"""
        self.assertTrue(TestLexer.checkLexeme(""" 0O0456132 """,
                                              """0,Error Token O""", 154))

    # 55
    def test_invalid_integer_lower(self):
        """test invalid integer lowercase"""
        self.assertTrue(TestLexer.checkLexeme(""" 0x12ABC 0X45def12 """,
                                              """0x12ABC,0X45,def12,<EOF>""", 155))

    # Test float literal
    # 56
    def test_float_with_decimal(self):
        """test float literal"""
        self.assertTrue(TestLexer.checkLexeme(""" 27.8589 """,
                                              """27.8589,<EOF>""", 156))

    # 57
    def test_float_with_exponent(self):
        """test float with exponent"""
        self.assertTrue(TestLexer.checkLexeme(""" 123e12 """,
                                              """123e12,<EOF>""", 157))

    # 58
    def test_float_with_exponent_minus(self):
        """test float exponent with minus sign"""
        self.assertTrue(TestLexer.checkLexeme(""" 987e-48 """,
                                              """987e-48,<EOF>""", 158))

    # 59
    def test_float_with_exponent_plus(self):
        """test float with exponent plus sign"""
        self.assertTrue(TestLexer.checkLexeme(""" 549e+798 """,
                                              """549e+798,<EOF>""", 159))

    # 60
    def test_float_with_exponent_uppercase(self):
        """test float exponent uppercase"""
        self.assertTrue(TestLexer.checkLexeme(""" 9456E75 """,
                                              """9456E75,<EOF>""", 160))

    # 61
    def test_float_with_exponent_decimal(self):
        """test float exponent and decimal part"""
        self.assertTrue(TestLexer.checkLexeme(""" 645.12e89 """,
                                              """645.12e89,<EOF>""", 161))

    # 62
    def test_float_with_exponent_dot(self):
        """test float with dot and exponent"""
        self.assertTrue(TestLexer.checkLexeme(""" 200.e-6 """,
                                              """200.e-6,<EOF>""", 162))

    # 63
    def test_float_with_dot(self):
        """test float with dot"""
        self.assertTrue(TestLexer.checkLexeme(""" 3450. """,
                                              """3450.,<EOF>""", 163))

    # 64
    def test_multiple_float(self):
        """test multiple floats"""
        self.assertTrue(TestLexer.checkLexeme(""" 12.0e3 12e3 12.e5 12.0e3 12000. 120000e-1 """,
                                              """12.0e3,12e3,12.e5,12.0e3,12000.,120000e-1,<EOF>""", 164))

    # 65
    def test_invalid_float_many_dot(self):
        """test float with more than one dot"""
        self.assertTrue(TestLexer.checkLexeme(""" 213.45.46 """,
                                              """213.45,.,46,<EOF>""", 165))

    # 66
    def test_invalid_float_exponent(self):
        """test float with invalid exponent expression"""
        self.assertTrue(TestLexer.checkLexeme(""" 346.e """,
                                              """346.,e,<EOF>""", 166))

    # 67
    def test_invalid_float_exponent_before_dot(self):
        """test invalid float with exponent before dot"""
        self.assertTrue(TestLexer.checkLexeme(""" 1000e.12""",
                                              """1000,e,.,12,<EOF>""", 167))

    # 68
    def test_invalid_float_missing_integer(self):
        """test invalid float missing initial decimal part"""
        self.assertTrue(TestLexer.checkLexeme(""" .798""",
                                              """.,798,<EOF>""", 168))

    # 69
    def test_invalid_float_exponent_sign(self):
        """test invalid float sign"""
        self.assertTrue(TestLexer.checkLexeme(""" 7895.12e+-34""",
                                              """7895.12,e,+,-,34,<EOF>""", 169))

    # 70
    def test_invalid_float_with_space(self):
        """test float with invalid space"""
        self.assertTrue(TestLexer.checkLexeme(""" 654. e4""",
                                              """654.,e4,<EOF>""", 170))

    # Test boolean literal
    # 71
    def test_normal_boolean(self):
        """test normal boolean literal"""
        self.assertTrue(TestLexer.checkLexeme(""" True False False True""",
                                              """True,False,False,True,<EOF>""", 171))

    # 72
    def test_boolean_tied(self):
        """test boolean literal tied together"""
        self.assertTrue(TestLexer.checkLexeme(""" TrueFalseFalseTrue""",
                                              """True,False,False,True,<EOF>""", 172))

    # 73
    def test_invalid_boolean(self):
        """test invalid boolean literal"""
        self.assertTrue(TestLexer.checkLexeme(""" TRUE """,
                                              """Error Token T""", 173))

    # Test comment
    # 74
    def test_single_line_comment(self):
        """test single-line comment"""
        self.assertTrue(TestLexer.checkLexeme(""" ** This is a single-line comment. ** """,
                                              """<EOF>""", 174))

    # 75
    def test_multi_line_comment(self):
        """test multi-line comment"""
        self.assertTrue(TestLexer.checkLexeme(""" ** This is a
                                                    * multi-line
                                                    * comment.
                                                    ** """,
                                              """<EOF>""", 175))

    # 76
    def test_multi_comment(self):
        """test multiple comment"""
        self.assertTrue(TestLexer.checkLexeme(""" ** A book ** ** Assassin** """,
                                              """<EOF>""", 176))

    # 77
    def test_invalid_comment(self):
        """test invalid comment"""
        self.assertTrue(TestLexer.checkLexeme(""" * a wrong sentence * """,
                                              """*,a,wrong,sentence,*,<EOF>""", 177))

    # 78
    def test_invalid_multi_line_comment(self):
        """test invalid multi-line comment"""
        self.assertTrue(TestLexer.checkLexeme(""" * this is a
                                                     multi-line
                                                     comment.
                                                    * """,
                                              """*,this,is,a,multi,-,line,comment,.,*,<EOF>""", 178))

    # 79
    def test_unterminated_comment(self):
        """test unterminated comment"""
        self.assertTrue(TestLexer.checkLexeme(""" ** The brotherhood of ac """,
                                              """Unterminated Comment""", 179))

    # 80
    def test_unterminated_multi_line_comment(self):
        """test unterminated multi-line comment"""
        self.assertTrue(TestLexer.checkLexeme(""" ** The 
                                                    wonder
                                                     of the 
                                                     world """,
                                              """Unterminated Comment""", 180))

    # Test error char
    # 81
    def test_error_char(self):
        """test error char"""
        self.assertTrue(TestLexer.checkLexeme(""" a + b = c*d#q-2 """,
                                              """a,+,b,=,c,*,d,Error Token #""", 181))

    # 82
    def test_error_char_boolean(self):
        """test error boolean char"""
        self.assertTrue(TestLexer.checkLexeme(""" trick ||| treat """,
                                              """trick,||,Error Token |""", 182))

    # 83
    def test_error_char_question(self):
        """test error char question"""
        self.assertTrue(TestLexer.checkLexeme(""" what is it? Nothing """,
                                              """what,is,it,Error Token ?""", 183))

    # Test unclosed string
    # 84
    def test_unclosed_normal_string(self):
        """test unclosed normal string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abcdexyz """,
                                              """Unclosed String: abcdexyz """, 184))

    # 85
    def test_unclosed_string_empty(self):
        """test unclosed empty string"""
        self.assertTrue(TestLexer.checkLexeme(""" " """,
                                              """Unclosed String:  """, 185))

    # 86
    def test_unclosed_string_escape(self):
        """test unclosed string with escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "Google Pixel \\n """,
                                              """Unclosed String: Google Pixel \\n """, 186))

    # 87
    def test_unclosed_nested_string(self):
        """test unclosed nested string"""
        self.assertTrue(TestLexer.checkLexeme(""" "University of "technology" """,
                                              """University of ,technology,Unclosed String:  """, 187))

    # 88
    def test_unclosed_string_number(self):
        """test unclosed string of number"""
        self.assertTrue(TestLexer.checkLexeme(""" "123456 """,
                                              """Unclosed String: 123456 """, 188))

    # 89
    def test_unclosed_string_operator(self):
        """test unclosed string of operators"""
        self.assertTrue(TestLexer.checkLexeme(""" "+-*/><== """,
                                              """Unclosed String: +-*/><== """, 189))

    # 90
    def test_unclosed_string_separator(self):
        """test unclosed string of separtors"""
        self.assertTrue(TestLexer.checkLexeme(""" "( ) [ ] : . , ; { } """,
                                              """Unclosed String: ( ) [ ] : . , ; { } """, 190))

    # Test illegal escape
    # 91
    def test_illegal_escape_string(self):
        """test illegal string escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "Mythology\\kof greek" """,
                                              """Illegal Escape In String: Mythology\\k""", 191))

    # 92
    def test_illegal_escape_newline(self):
        """test illegal escape newline character"""
        self.assertTrue(TestLexer.checkLexeme(""" "\nIt is raining" """,
                                              """Unclosed String: \n""", 192))

    # 93
    def test_illegal_escape_quote(self):
        """test illegal escape quote"""
        self.assertTrue(TestLexer.checkLexeme(""" "King under the ' mountain" """,
                                              """Illegal Escape In String: King under the ' """, 193))

    # 94
    def test_illegal_escape_newline_end(self):
        """test illegal escape newline at the end"""
        self.assertTrue(TestLexer.checkLexeme(""" "The forest\b of Fangorn\n" """,
                                              """Unclosed String: The forest\b of Fangorn\n""", 194))

    # 95
    def test_illegal_escape_backslash(self):
        """test illegal escape backslash character"""
        self.assertTrue(TestLexer.checkLexeme(""" "The planet \\bof \\nUranus\\ in the system" """,
                                              """Illegal Escape In String: The planet \\bof \\nUranus\\ """, 195))

    # 96
    def test_illegal_escape_backslash_quote(self):
        """test illegal escape backslash quote"""
        self.assertTrue(TestLexer.checkLexeme(""" "Something is \' ending" """,
                                              """Illegal Escape In String: Something is \' """, 196))

    # 97
    def test_string_single_quote(self):
        """test string with single quote"""
        self.assertTrue(TestLexer.checkLexeme(""" "Coffee is addictive \\'substance" """,
                                              """Coffee is addictive \\'substance,<EOF>""", 197))

    # 98
    def test_string_with_separator(self):
        """test string with separator"""
        self.assertTrue(TestLexer.checkLexeme(""" print("Hello World") """,
                                              """print,(,Hello World,),<EOF>""", 198))

    # 99
    def test_operator_with_number(self):
        """test operator with number """
        self.assertTrue(TestLexer.checkLexeme(""" 0xFF + 2.e106 = 70.e-5 """,
                                              """0xFF,+,2.e106,=,70.e-5,<EOF>""", 199))

    # 100
    def test_identifier_with_boolean(self):
        """test identifier with boolean """
        self.assertTrue(TestLexer.checkLexeme(""" two False != True """,
                                              """two,False,!=,True,<EOF>""", 200))

