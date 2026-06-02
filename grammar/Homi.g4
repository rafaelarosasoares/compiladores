grammar Homi;

// Parser rules

programa
    : declaracao* automacao+ EOF
    ;

declaracao
    : ENTIDADE dominio IDENT IGUAL ENTITY_ID PONTO_VIRGULA
    ;

dominio
    : LUZ
    | SENSOR
    | INTERRUPTOR
    | ALARME
    ;

automacao
    : AUTOMACAO STRING ABRE_CHAVE corpoAutomacao FECHA_CHAVE
    ;

corpoAutomacao
    : blocoGatilho blocoAcoes modo?
    ;

blocoGatilho
    : QUANDO gatilho PONTO_VIRGULA
    ;

gatilho
    : ESTADO referencia FICAR valor
    ;

blocoAcoes
    : FACA ABRE_CHAVE comando* FECHA_CHAVE
    ;

comando
    : acaoSimples PONTO_VIRGULA
    | espera PONTO_VIRGULA
    ;

acaoSimples
    : verboAcao referencia
    ;

verboAcao
    : LIGAR
    | DESLIGAR
    ;

espera
    : ESPERAR DURATION
    ;

modo
    : MODO modoValor PONTO_VIRGULA
    ;

modoValor
    : SINGLE
    | RESTART
    | QUEUED
    | PARALLEL
    ;

referencia
    : IDENT
    | ENTITY_ID
    ;

valor
    : STATE
    | STRING
    | NUMBER
    | BOOLEAN
    ;

// Lexer rules

ENTIDADE: 'entidade';
AUTOMACAO: 'automacao';
QUANDO: 'quando';
ESTADO: 'estado';
FICAR: 'ficar';
FACA: 'faca';
LIGAR: 'ligar';
DESLIGAR: 'desligar';
ESPERAR: 'esperar';
MODO: 'modo';

LUZ: 'luz';
SENSOR: 'sensor';
INTERRUPTOR: 'interruptor';
ALARME: 'alarme';

SINGLE: 'single';
RESTART: 'restart';
QUEUED: 'queued';
PARALLEL: 'parallel';

STATE
    : 'on'
    | 'off'
    | 'disarmed'
    | 'armed'
    | 'charging'
    | 'idle'
    | 'running'
    ;

BOOLEAN
    : 'true'
    | 'false'
    ;

IGUAL: '=';
ABRE_CHAVE: '{';
FECHA_CHAVE: '}';
PONTO_VIRGULA: ';';

DURATION
    : [0-9]+ ('s' | 'min' | 'h')
    ;

NUMBER
    : [0-9]+ ('.' [0-9]+)?
    ;

ENTITY_ID
    : [a-z_][a-z0-9_]* '.' [a-zA-Z0-9_]+
    ;

IDENT
    : [a-zA-Z_][a-zA-Z0-9_]*
    ;

STRING
    : '"' (~["\r\n])* '"'
    ;

COMMENT
    : ('//' ~[\r\n]* | '#' ~[\r\n]*) -> skip
    ;

WS
    : [ \t\r\n]+ -> skip
    ;