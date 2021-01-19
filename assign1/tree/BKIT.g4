//ID = 1852118
grammar BKIT;

program : STRING EOF;
// exp :  term ASSIGN exp | term;
// term : term EXPONENT fact | fact;
// fact : factor RELOP fact | factor ADDOP fact | factor;
// factor: LB exp RB | ID;
// exp: LB exp RB | INTLIT | exp MULOP exp | exp ADDOP exp;
// array [1 .. 3, -2 .. 4, 15 .. 20] of array [-13 .. 15] of int
// ASSIGN: '=';
// EXPONENT: '^';
// RELOP: '>';
// ADDOP: '+';
// MULOP: '*';
// LB: '(';
// RB: ')';
// INTLIT: [0-9]+;
// fragment DIGIT: [0-9];
// fragment LOWCASE: [a-z];
// ID: LOWCASE(LOWCASE|DIGIT)*;


// 1/
//INTLIT: '0'|[1-9][0-9]*;

// 2/
STRING: '""' ('"'~["]|~[\n\f\r"])*  '""';


// 3/
// exp -> exp ? exp1 | exp1
// exp1 -> exp2 ^ exp2 | exp2
// exp2 -> exp3 @ exp2 | exp3
// exp3 -> INT | (exp) 

// 4/
// type: INT | FLOAT | array;
// INT: 'int';
// FLOAT: 'float';
// ARRAY: 'array';
// OF: 'of';
// array: ARRAY LSB range_list RSB OF type;
// range_list: range (',' range)*;
// range: num '..' num;
// num:  SIGN? DIGIT;
// SIGN: '-';
// LSB: '[';
// RSB: ']';
// DIGIT: [0-9]+;