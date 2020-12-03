// ID: 1852037
grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options{
	language=Python3;
}

program  :  (global_decl)? func_decl_part EOF;

global_decl : var_decl+;

var_decl: VAR COLON var_list SEMI;

var_list: var (COMMA var)* ;

var: scalar (ASSIGN scalar_value)?
   | composite (ASSIGN composite_value)?
   ;

scalar: ID;

scalar_value: INTLIT|FLOATLIT|booleanlit|STRINGLIT;

composite: ID dimension+;

composite_value: arraylit;

literal: INTLIT|FLOATLIT|booleanlit|STRINGLIT|arraylit;

arraylit: LB literal (COMMA literal)* RB;

func_decl_part: func_decl*;

func_decl: FUNCTION COLON ID (para_decl)? body;

para_decl: PARAMETER COLON para_list;

para_list: para (COMMA para)*;

para: scalar|composite;

body: BODY COLON stmt_list ENDBODY DOT;

dimension: LS INTLIT RS;

// Expression

expr: expr1 relational_operator expr1|expr1;

expr1: expr1 logical_operator expr2|expr2;

expr2: expr2 adding_operator expr3|expr3;

expr3: expr3 multiplying_operator expr4|expr4;

expr4: NEGATE expr4|expr5;

expr5: sign_operator expr5|expr6;

expr6: expr6 index_operator|expr7;

expr7: LP expr RP | function_call| ID | literal;

relational_operator:EQ|NOTEQ|LT|GT|LTE|GTE|NOTEQF|LTF|GTF|LTEF|GTEF;

logical_operator:AND|OR;

adding_operator:ADD|ADDF|SUB|SUBF;

multiplying_operator:MUL|MULF|DIV|DIVF|MOD;

sign_operator:SUB|SUBF;

index_operator:(LS expr RS)+;

function_call:ID LP expr_list? RP;

expr_list: expr (COMMA expr)*;

//--------------------------------------------//

// Statement

stmt_list: var_decl* stmt*;

stmt
    :
    assign_stmt
    |if_stmt
    |for_stmt
    |while_stmt
    |do_while_stmt
    |break_stmt
    |continue_stmt
    |call_stmt
    |return_stmt
    ;

index_expr: expr7 index_operator;

assign_stmt: (scalar|index_expr) ASSIGN expr SEMI;

if_stmt: if_then_stmt else_stmt;

if_then_stmt: IF expr THEN stmt_list (ELSEIF expr THEN stmt_list)*;

else_stmt: (ELSE stmt_list)? ENDIF DOT;

for_stmt: FOR LP scalar ASSIGN expr COMMA expr COMMA expr RP DO stmt_list ENDFOR DOT;

while_stmt: WHILE expr DO stmt_list ENDWHILE DOT;

do_while_stmt: DO stmt_list WHILE expr ENDDO DOT;

break_stmt: BREAK SEMI;

continue_stmt: CONTINUE SEMI;

call_stmt: function_call SEMI;

return_stmt: RETURN expr? SEMI;

//--------------------------------------------//

//identifier
ID: [a-z][a-zA-Z_0-9]* ;

// Assign operator
ASSIGN: '=';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

// Comment part
COMMENT: '**' .*? '**' -> skip;


// Keywords allowed in BKIT
BODY     : 'Body';
BREAK    : 'Break';
CONTINUE : 'Continue';
DO       : 'Do';
ELSE     : 'Else';
ELSEIF   : 'ElseIf';
ENDBODY  : 'EndBody';
ENDIF    : 'EndIf';
ENDFOR   : 'EndFor';
ENDWHILE : 'EndWhile';
FOR      : 'For';
FUNCTION : 'Function';
IF       : 'If';
PARAMETER: 'Parameter';
RETURN   : 'Return';
THEN     : 'Then';
VAR      : 'Var' ;
WHILE    : 'While';
ENDDO    : 'EndDo';
TRUE     : 'True';
FALSE    : 'False';

// Arithmetic operators
ADD     : '+';
ADDF    : '+.';
SUB     : '-';
SUBF    : '-.';
MUL     : '*';
MULF    : '*.';
DIV     : '\\';
DIVF    : '\\.';
MOD     : '%';

// Boolean operators
NEGATE  : '!';
AND     : '&&';
OR      : '||';

// Realtional operators
EQ      : '==';
NOTEQ   : '!=';
LT      : '<';
GT      : '>';
LTE     : '<=';
GTE     : '>=';
NOTEQF  : '=/=';
LTF     : '<.';
GTF     : '>.';
LTEF    : '<=.';
GTEF    : '>=.';


// Separators
LP      : '(';
RP      : ')';
LS      : '[';
RS      : ']';
COLON   : ':' ;
DOT     : '.';
COMMA   : ',';
SEMI    : ';' ;
LB      : '{';
RB      : '}';

// Literal

fragment DECIMAL: '0'|[1-9][0-9]*;
fragment HEXIMAL: '0' [xX] [1-9A-F][0-9A-F]*;
fragment OCTAL  : '0' [oO] [1-7][0-7]*;
INTLIT : DECIMAL|HEXIMAL|OCTAL;

fragment INT_PART: [0-9]+;
fragment DEC_PART: '.' [0-9]*;
fragment EXPONENT: [eE] [+-]? [0-9]+;
FLOATLIT: INT_PART DEC_PART EXPONENT
        | INT_PART (DEC_PART|EXPONENT)
        ;

booleanlit : TRUE|FALSE;

fragment ESC_SEQ: '\\' [bfnrt'\\];
fragment STRING_ESC_SEQUENCE: ~[\f\n\r"'\\] | ESC_SEQ | '\'"';
STRINGLIT: '"' STRING_ESC_SEQUENCE*'"'
	{
		self.text = (self.text)[1:-1]
	}
	;

fragment ESC_ILLEGAL: '\\' ~[bfnrt'\\] | ~'\\' | '\'' ~'"';

// Error handling

ERROR_CHAR: .;
UNCLOSE_STRING: '"' STRING_ESC_SEQUENCE* ( [\n\r\f]| EOF )
    {
        self.text = (self.text)[1:]
    };
ILLEGAL_ESCAPE: '"' STRING_ESC_SEQUENCE* ESC_ILLEGAL
    {
        self.text = (self.text)[1:]
    } ;
UNTERMINATED_COMMENT: '**' .*? ;

