grammar Homi;

/*
 * Parser Rules
 */

programa
    : automacao+ EOF
    ;

automacao
    : AUTOMACAO ID
      QUANDO evento
      condicaoOpcional
      ENTAO acoes
      FIM
    ;

condicaoOpcional
    : SE condicao
    |
    ;

evento
    : ENTITY_ID LIGAR
    | ENTITY_ID DESLIGAR
    | ENTITY_ID MUDAR
    ;

condicao
    : ENTITY_ID operador NUMBER
    ;

operador
    : GT
    | LT
    | GE
    | LE
    | EQ
    | NE
    ;

acoes
    : acao+
    ;

acao
    : LIGAR ENTITY_ID
    | DESLIGAR ENTITY_ID
    | ESPERAR TIME
    ;

/*
 * Lexer Rules
 */

AUTOMACAO : 'automacao';
QUANDO    : 'quando';
SE        : 'se';
ENTAO     : 'entao';
FIM       : 'fim';

LIGAR     : 'ligar';
DESLIGAR  : 'desligar';
MUDAR     : 'mudar';

ESPERAR   : 'esperar';

GT : '>';
LT : '<';
GE : '>=';
LE : '<=';
EQ : '==';
NE : '!=';

TIME
    : [0-9]+ ('s' | 'min')
    ;

NUMBER
    : [0-9]+
    ;

ENTITY_ID
    : [a-zA-Z]+ '.' [a-zA-Z_][a-zA-Z0-9_]*
    ;

ID
    : [A-Z][a-zA-Z0-9_]*
    ;

COMMENT
    : '#' ~[\r\n]* -> skip
    ;

WS
    : [ \t\r\n]+ -> skip
    ;