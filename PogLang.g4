grammar PogLang;

// === Palavras-chave ===
START: 'start';
END: 'end';
VAL: 'val';
VAR: 'var';
IF: 'if';
ELSE: 'else';
WHILE: 'while';
PRINTLN: 'println';
READLINE: 'readLine';
POG: 'pog';
INT_TYPE: 'Int';
STRING_TYPE: 'String';

// === Operadores e símbolos ===
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';

EQUALS: '==';
NEQUALS: '!=';
LT: '<';
LTE: '<=';
GT: '>';
GTE: '>=';

AND: '&&';
OR: '||';
NOT: '!';

LBRACE: '{';
RBRACE: '}';
LPAREN: '(';
RPAREN: ')';
SEMI: ';';
COLON: ':';
ASSIGN: '=';

// === Tokens ===
ID: [a-zA-Z_][a-zA-Z_0-9]* ;
INT: [0-9]+ ;
STRING: '"' ( ~["\\\r\n] | '\\' . )* '"' ;

// === Espaços e comentários ===
WS: [ \t\r\n]+ -> skip ;
COMMENT: '//' ~[\r\n]* -> skip ;

// === Regras principais ===
program: START LBRACE statement* RBRACE END ;

statement
    : VAL ID COLON type ASSIGN expression SEMI
    | VAR ID COLON type ASSIGN expression SEMI
    | ID ASSIGN expression SEMI
    | PRINTLN LPAREN expression RPAREN SEMI
    | ID ASSIGN READLINE LPAREN RPAREN SEMI
    | IF LPAREN expression RPAREN LBRACE statement* RBRACE (ELSE LBRACE statement* RBRACE)?
    | WHILE LPAREN expression RPAREN LBRACE statement* RBRACE
    | POG SEMI
    ;

expression
    : expression op=(MULT | DIV) expression
    | expression op=(PLUS | MINUS) expression
    | expression op=(EQUALS | NEQUALS | LT | LTE | GT | GTE) expression
    | expression op=(AND | OR) expression
    | NOT expression
    | LPAREN expression RPAREN
    | ID
    | INT
    | STRING
    ;

type: INT_TYPE | STRING_TYPE ;
