# Generated from grammar/Homi.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,35,149,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,1,0,5,0,44,8,0,10,0,12,0,47,9,0,1,0,4,0,50,8,0,11,0,12,0,51,
        1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,3,1,3,1,3,1,3,1,3,
        1,3,1,4,1,4,3,4,73,8,4,1,4,1,4,3,4,77,8,4,1,5,1,5,1,5,1,5,1,6,1,
        6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,5,8,96,8,8,10,8,12,
        8,99,9,8,1,9,3,9,102,8,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,11,1,
        11,1,12,1,12,1,12,5,12,116,8,12,10,12,12,12,119,9,12,1,12,1,12,1,
        13,1,13,1,13,1,13,1,13,1,13,3,13,129,8,13,1,14,1,14,1,14,1,15,1,
        15,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,18,1,18,1,19,1,19,1,20,1,
        20,1,20,0,0,21,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,0,6,1,0,15,18,1,0,12,13,1,0,7,8,1,0,19,22,1,0,31,32,3,0,
        23,24,30,30,33,33,135,0,45,1,0,0,0,2,55,1,0,0,0,4,62,1,0,0,0,6,64,
        1,0,0,0,8,70,1,0,0,0,10,78,1,0,0,0,12,82,1,0,0,0,14,87,1,0,0,0,16,
        91,1,0,0,0,18,101,1,0,0,0,20,105,1,0,0,0,22,110,1,0,0,0,24,112,1,
        0,0,0,26,128,1,0,0,0,28,130,1,0,0,0,30,133,1,0,0,0,32,135,1,0,0,
        0,34,138,1,0,0,0,36,142,1,0,0,0,38,144,1,0,0,0,40,146,1,0,0,0,42,
        44,3,2,1,0,43,42,1,0,0,0,44,47,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,
        0,46,49,1,0,0,0,47,45,1,0,0,0,48,50,3,6,3,0,49,48,1,0,0,0,50,51,
        1,0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,52,53,1,0,0,0,53,54,5,0,0,1,
        54,1,1,0,0,0,55,56,5,1,0,0,56,57,3,4,2,0,57,58,5,32,0,0,58,59,5,
        25,0,0,59,60,5,31,0,0,60,61,5,28,0,0,61,3,1,0,0,0,62,63,7,0,0,0,
        63,5,1,0,0,0,64,65,5,2,0,0,65,66,5,33,0,0,66,67,5,26,0,0,67,68,3,
        8,4,0,68,69,5,27,0,0,69,7,1,0,0,0,70,72,3,10,5,0,71,73,3,14,7,0,
        72,71,1,0,0,0,72,73,1,0,0,0,73,74,1,0,0,0,74,76,3,24,12,0,75,77,
        3,34,17,0,76,75,1,0,0,0,76,77,1,0,0,0,77,9,1,0,0,0,78,79,5,3,0,0,
        79,80,3,12,6,0,80,81,5,28,0,0,81,11,1,0,0,0,82,83,5,4,0,0,83,84,
        3,38,19,0,84,85,5,5,0,0,85,86,3,40,20,0,86,13,1,0,0,0,87,88,5,11,
        0,0,88,89,3,16,8,0,89,90,5,28,0,0,90,15,1,0,0,0,91,97,3,18,9,0,92,
        93,3,22,11,0,93,94,3,18,9,0,94,96,1,0,0,0,95,92,1,0,0,0,96,99,1,
        0,0,0,97,95,1,0,0,0,97,98,1,0,0,0,98,17,1,0,0,0,99,97,1,0,0,0,100,
        102,5,14,0,0,101,100,1,0,0,0,101,102,1,0,0,0,102,103,1,0,0,0,103,
        104,3,20,10,0,104,19,1,0,0,0,105,106,5,4,0,0,106,107,3,38,19,0,107,
        108,5,5,0,0,108,109,3,40,20,0,109,21,1,0,0,0,110,111,7,1,0,0,111,
        23,1,0,0,0,112,113,5,6,0,0,113,117,5,26,0,0,114,116,3,26,13,0,115,
        114,1,0,0,0,116,119,1,0,0,0,117,115,1,0,0,0,117,118,1,0,0,0,118,
        120,1,0,0,0,119,117,1,0,0,0,120,121,5,27,0,0,121,25,1,0,0,0,122,
        123,3,28,14,0,123,124,5,28,0,0,124,129,1,0,0,0,125,126,3,32,16,0,
        126,127,5,28,0,0,127,129,1,0,0,0,128,122,1,0,0,0,128,125,1,0,0,0,
        129,27,1,0,0,0,130,131,3,30,15,0,131,132,3,38,19,0,132,29,1,0,0,
        0,133,134,7,2,0,0,134,31,1,0,0,0,135,136,5,9,0,0,136,137,5,29,0,
        0,137,33,1,0,0,0,138,139,5,10,0,0,139,140,3,36,18,0,140,141,5,28,
        0,0,141,35,1,0,0,0,142,143,7,3,0,0,143,37,1,0,0,0,144,145,7,4,0,
        0,145,39,1,0,0,0,146,147,7,5,0,0,147,41,1,0,0,0,8,45,51,72,76,97,
        101,117,128
    ]

class HomiParser ( Parser ):

    grammarFileName = "Homi.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'entidade'", "'automacao'", "'quando'", 
                     "'estado'", "'ficar'", "'faca'", "'ligar'", "'desligar'", 
                     "'esperar'", "'modo'", "'se'", "'e'", "'ou'", "'nao'", 
                     "'luz'", "'sensor'", "'interruptor'", "'alarme'", "'single'", 
                     "'restart'", "'queued'", "'parallel'", "<INVALID>", 
                     "<INVALID>", "'='", "'{'", "'}'", "';'" ]

    symbolicNames = [ "<INVALID>", "ENTIDADE", "AUTOMACAO", "QUANDO", "ESTADO", 
                      "FICAR", "FACA", "LIGAR", "DESLIGAR", "ESPERAR", "MODO", 
                      "SE", "E", "OU", "NAO", "LUZ", "SENSOR", "INTERRUPTOR", 
                      "ALARME", "SINGLE", "RESTART", "QUEUED", "PARALLEL", 
                      "STATE", "BOOLEAN", "IGUAL", "ABRE_CHAVE", "FECHA_CHAVE", 
                      "PONTO_VIRGULA", "DURATION", "NUMBER", "ENTITY_ID", 
                      "IDENT", "STRING", "COMMENT", "WS" ]

    RULE_programa = 0
    RULE_declaracao = 1
    RULE_dominio = 2
    RULE_automacao = 3
    RULE_corpoAutomacao = 4
    RULE_blocoGatilho = 5
    RULE_gatilho = 6
    RULE_blocoCondicoes = 7
    RULE_expressaoCondicao = 8
    RULE_termoCondicao = 9
    RULE_condicaoEstado = 10
    RULE_operadorLogico = 11
    RULE_blocoAcoes = 12
    RULE_comando = 13
    RULE_acaoSimples = 14
    RULE_verboAcao = 15
    RULE_espera = 16
    RULE_modo = 17
    RULE_modoValor = 18
    RULE_referencia = 19
    RULE_valor = 20

    ruleNames =  [ "programa", "declaracao", "dominio", "automacao", "corpoAutomacao", 
                   "blocoGatilho", "gatilho", "blocoCondicoes", "expressaoCondicao", 
                   "termoCondicao", "condicaoEstado", "operadorLogico", 
                   "blocoAcoes", "comando", "acaoSimples", "verboAcao", 
                   "espera", "modo", "modoValor", "referencia", "valor" ]

    EOF = Token.EOF
    ENTIDADE=1
    AUTOMACAO=2
    QUANDO=3
    ESTADO=4
    FICAR=5
    FACA=6
    LIGAR=7
    DESLIGAR=8
    ESPERAR=9
    MODO=10
    SE=11
    E=12
    OU=13
    NAO=14
    LUZ=15
    SENSOR=16
    INTERRUPTOR=17
    ALARME=18
    SINGLE=19
    RESTART=20
    QUEUED=21
    PARALLEL=22
    STATE=23
    BOOLEAN=24
    IGUAL=25
    ABRE_CHAVE=26
    FECHA_CHAVE=27
    PONTO_VIRGULA=28
    DURATION=29
    NUMBER=30
    ENTITY_ID=31
    IDENT=32
    STRING=33
    COMMENT=34
    WS=35

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(HomiParser.EOF, 0)

        def declaracao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HomiParser.DeclaracaoContext)
            else:
                return self.getTypedRuleContext(HomiParser.DeclaracaoContext,i)


        def automacao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HomiParser.AutomacaoContext)
            else:
                return self.getTypedRuleContext(HomiParser.AutomacaoContext,i)


        def getRuleIndex(self):
            return HomiParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = HomiParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 42
                self.declaracao()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 49 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 48
                self.automacao()
                self.state = 51 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2):
                    break

            self.state = 53
            self.match(HomiParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENTIDADE(self):
            return self.getToken(HomiParser.ENTIDADE, 0)

        def dominio(self):
            return self.getTypedRuleContext(HomiParser.DominioContext,0)


        def IDENT(self):
            return self.getToken(HomiParser.IDENT, 0)

        def IGUAL(self):
            return self.getToken(HomiParser.IGUAL, 0)

        def ENTITY_ID(self):
            return self.getToken(HomiParser.ENTITY_ID, 0)

        def PONTO_VIRGULA(self):
            return self.getToken(HomiParser.PONTO_VIRGULA, 0)

        def getRuleIndex(self):
            return HomiParser.RULE_declaracao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracao" ):
                listener.enterDeclaracao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracao" ):
                listener.exitDeclaracao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracao" ):
                return visitor.visitDeclaracao(self)
            else:
                return visitor.visitChildren(self)




    def declaracao(self):

        localctx = HomiParser.DeclaracaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaracao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(HomiParser.ENTIDADE)
            self.state = 56
            self.dominio()
            self.state = 57
            self.match(HomiParser.IDENT)
            self.state = 58
            self.match(HomiParser.IGUAL)
            self.state = 59
            self.match(HomiParser.ENTITY_ID)
            self.state = 60
            self.match(HomiParser.PONTO_VIRGULA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DominioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LUZ(self):
            return self.getToken(HomiParser.LUZ, 0)

        def SENSOR(self):
            return self.getToken(HomiParser.SENSOR, 0)

        def INTERRUPTOR(self):
            return self.getToken(HomiParser.INTERRUPTOR, 0)

        def ALARME(self):
            return self.getToken(HomiParser.ALARME, 0)

        def getRuleIndex(self):
            return HomiParser.RULE_dominio

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDominio" ):
                listener.enterDominio(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDominio" ):
                listener.exitDominio(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDominio" ):
                return visitor.visitDominio(self)
            else:
                return visitor.visitChildren(self)




    def dominio(self):

        localctx = HomiParser.DominioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_dominio)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 491520) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AutomacaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AUTOMACAO(self):
            return self.getToken(HomiParser.AUTOMACAO, 0)

        def STRING(self):
            return self.getToken(HomiParser.STRING, 0)

        def ABRE_CHAVE(self):
            return self.getToken(HomiParser.ABRE_CHAVE, 0)

        def corpoAutomacao(self):
            return self.getTypedRuleContext(HomiParser.CorpoAutomacaoContext,0)


        def FECHA_CHAVE(self):
            return self.getToken(HomiParser.FECHA_CHAVE, 0)

        def getRuleIndex(self):
            return HomiParser.RULE_automacao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAutomacao" ):
                listener.enterAutomacao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAutomacao" ):
                listener.exitAutomacao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAutomacao" ):
                return visitor.visitAutomacao(self)
            else:
                return visitor.visitChildren(self)




    def automacao(self):

        localctx = HomiParser.AutomacaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_automacao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(HomiParser.AUTOMACAO)
            self.state = 65
            self.match(HomiParser.STRING)
            self.state = 66
            self.match(HomiParser.ABRE_CHAVE)
            self.state = 67
            self.corpoAutomacao()
            self.state = 68
            self.match(HomiParser.FECHA_CHAVE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CorpoAutomacaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blocoGatilho(self):
            return self.getTypedRuleContext(HomiParser.BlocoGatilhoContext,0)


        def blocoAcoes(self):
            return self.getTypedRuleContext(HomiParser.BlocoAcoesContext,0)


        def blocoCondicoes(self):
            return self.getTypedRuleContext(HomiParser.BlocoCondicoesContext,0)


        def modo(self):
            return self.getTypedRuleContext(HomiParser.ModoContext,0)


        def getRuleIndex(self):
            return HomiParser.RULE_corpoAutomacao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCorpoAutomacao" ):
                listener.enterCorpoAutomacao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCorpoAutomacao" ):
                listener.exitCorpoAutomacao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCorpoAutomacao" ):
                return visitor.visitCorpoAutomacao(self)
            else:
                return visitor.visitChildren(self)




    def corpoAutomacao(self):

        localctx = HomiParser.CorpoAutomacaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_corpoAutomacao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.blocoGatilho()
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 71
                self.blocoCondicoes()


            self.state = 74
            self.blocoAcoes()
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 75
                self.modo()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlocoGatilhoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUANDO(self):
            return self.getToken(HomiParser.QUANDO, 0)

        def gatilho(self):
            return self.getTypedRuleContext(HomiParser.GatilhoContext,0)


        def PONTO_VIRGULA(self):
            return self.getToken(HomiParser.PONTO_VIRGULA, 0)

        def getRuleIndex(self):
            return HomiParser.RULE_blocoGatilho

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlocoGatilho" ):
                listener.enterBlocoGatilho(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlocoGatilho" ):
                listener.exitBlocoGatilho(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlocoGatilho" ):
                return visitor.visitBlocoGatilho(self)
            else:
                return visitor.visitChildren(self)




    def blocoGatilho(self):

        localctx = HomiParser.BlocoGatilhoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_blocoGatilho)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(HomiParser.QUANDO)
            self.state = 79
            self.gatilho()
            self.state = 80
            self.match(HomiParser.PONTO_VIRGULA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GatilhoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ESTADO(self):
            return self.getToken(HomiParser.ESTADO, 0)

        def referencia(self):
            return self.getTypedRuleContext(HomiParser.ReferenciaContext,0)


        def FICAR(self):
            return self.getToken(HomiParser.FICAR, 0)

        def valor(self):
            return self.getTypedRuleContext(HomiParser.ValorContext,0)


        def getRuleIndex(self):
            return HomiParser.RULE_gatilho

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGatilho" ):
                listener.enterGatilho(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGatilho" ):
                listener.exitGatilho(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGatilho" ):
                return visitor.visitGatilho(self)
            else:
                return visitor.visitChildren(self)




    def gatilho(self):

        localctx = HomiParser.GatilhoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_gatilho)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(HomiParser.ESTADO)
            self.state = 83
            self.referencia()
            self.state = 84
            self.match(HomiParser.FICAR)
            self.state = 85
            self.valor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlocoCondicoesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SE(self):
            return self.getToken(HomiParser.SE, 0)

        def expressaoCondicao(self):
            return self.getTypedRuleContext(HomiParser.ExpressaoCondicaoContext,0)


        def PONTO_VIRGULA(self):
            return self.getToken(HomiParser.PONTO_VIRGULA, 0)

        def getRuleIndex(self):
            return HomiParser.RULE_blocoCondicoes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlocoCondicoes" ):
                listener.enterBlocoCondicoes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlocoCondicoes" ):
                listener.exitBlocoCondicoes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlocoCondicoes" ):
                return visitor.visitBlocoCondicoes(self)
            else:
                return visitor.visitChildren(self)




    def blocoCondicoes(self):

        localctx = HomiParser.BlocoCondicoesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_blocoCondicoes)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(HomiParser.SE)
            self.state = 88
            self.expressaoCondicao()
            self.state = 89
            self.match(HomiParser.PONTO_VIRGULA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressaoCondicaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termoCondicao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HomiParser.TermoCondicaoContext)
            else:
                return self.getTypedRuleContext(HomiParser.TermoCondicaoContext,i)


        def operadorLogico(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HomiParser.OperadorLogicoContext)
            else:
                return self.getTypedRuleContext(HomiParser.OperadorLogicoContext,i)


        def getRuleIndex(self):
            return HomiParser.RULE_expressaoCondicao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressaoCondicao" ):
                listener.enterExpressaoCondicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressaoCondicao" ):
                listener.exitExpressaoCondicao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressaoCondicao" ):
                return visitor.visitExpressaoCondicao(self)
            else:
                return visitor.visitChildren(self)




    def expressaoCondicao(self):

        localctx = HomiParser.ExpressaoCondicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_expressaoCondicao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.termoCondicao()
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12 or _la==13:
                self.state = 92
                self.operadorLogico()
                self.state = 93
                self.termoCondicao()
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermoCondicaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condicaoEstado(self):
            return self.getTypedRuleContext(HomiParser.CondicaoEstadoContext,0)


        def NAO(self):
            return self.getToken(HomiParser.NAO, 0)

        def getRuleIndex(self):
            return HomiParser.RULE_termoCondicao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermoCondicao" ):
                listener.enterTermoCondicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermoCondicao" ):
                listener.exitTermoCondicao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermoCondicao" ):
                return visitor.visitTermoCondicao(self)
            else:
                return visitor.visitChildren(self)




    def termoCondicao(self):

        localctx = HomiParser.TermoCondicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_termoCondicao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 100
                self.match(HomiParser.NAO)


            self.state = 103
            self.condicaoEstado()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicaoEstadoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ESTADO(self):
            return self.getToken(HomiParser.ESTADO, 0)

        def referencia(self):
            return self.getTypedRuleContext(HomiParser.ReferenciaContext,0)


        def FICAR(self):
            return self.getToken(HomiParser.FICAR, 0)

        def valor(self):
            return self.getTypedRuleContext(HomiParser.ValorContext,0)


        def getRuleIndex(self):
            return HomiParser.RULE_condicaoEstado

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicaoEstado" ):
                listener.enterCondicaoEstado(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicaoEstado" ):
                listener.exitCondicaoEstado(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicaoEstado" ):
                return visitor.visitCondicaoEstado(self)
            else:
                return visitor.visitChildren(self)




    def condicaoEstado(self):

        localctx = HomiParser.CondicaoEstadoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_condicaoEstado)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(HomiParser.ESTADO)
            self.state = 106
            self.referencia()
            self.state = 107
            self.match(HomiParser.FICAR)
            self.state = 108
            self.valor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperadorLogicoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def E(self):
            return self.getToken(HomiParser.E, 0)

        def OU(self):
            return self.getToken(HomiParser.OU, 0)

        def getRuleIndex(self):
            return HomiParser.RULE_operadorLogico

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperadorLogico" ):
                listener.enterOperadorLogico(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperadorLogico" ):
                listener.exitOperadorLogico(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperadorLogico" ):
                return visitor.visitOperadorLogico(self)
            else:
                return visitor.visitChildren(self)




    def operadorLogico(self):

        localctx = HomiParser.OperadorLogicoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_operadorLogico)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            _la = self._input.LA(1)
            if not(_la==12 or _la==13):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlocoAcoesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FACA(self):
            return self.getToken(HomiParser.FACA, 0)

        def ABRE_CHAVE(self):
            return self.getToken(HomiParser.ABRE_CHAVE, 0)

        def FECHA_CHAVE(self):
            return self.getToken(HomiParser.FECHA_CHAVE, 0)

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HomiParser.ComandoContext)
            else:
                return self.getTypedRuleContext(HomiParser.ComandoContext,i)


        def getRuleIndex(self):
            return HomiParser.RULE_blocoAcoes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlocoAcoes" ):
                listener.enterBlocoAcoes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlocoAcoes" ):
                listener.exitBlocoAcoes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlocoAcoes" ):
                return visitor.visitBlocoAcoes(self)
            else:
                return visitor.visitChildren(self)




    def blocoAcoes(self):

        localctx = HomiParser.BlocoAcoesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_blocoAcoes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(HomiParser.FACA)
            self.state = 113
            self.match(HomiParser.ABRE_CHAVE)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 896) != 0):
                self.state = 114
                self.comando()
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 120
            self.match(HomiParser.FECHA_CHAVE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def acaoSimples(self):
            return self.getTypedRuleContext(HomiParser.AcaoSimplesContext,0)


        def PONTO_VIRGULA(self):
            return self.getToken(HomiParser.PONTO_VIRGULA, 0)

        def espera(self):
            return self.getTypedRuleContext(HomiParser.EsperaContext,0)


        def getRuleIndex(self):
            return HomiParser.RULE_comando

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando" ):
                listener.enterComando(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando" ):
                listener.exitComando(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComando" ):
                return visitor.visitComando(self)
            else:
                return visitor.visitChildren(self)




    def comando(self):

        localctx = HomiParser.ComandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_comando)
        try:
            self.state = 128
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                self.acaoSimples()
                self.state = 123
                self.match(HomiParser.PONTO_VIRGULA)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.espera()
                self.state = 126
                self.match(HomiParser.PONTO_VIRGULA)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AcaoSimplesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def verboAcao(self):
            return self.getTypedRuleContext(HomiParser.VerboAcaoContext,0)


        def referencia(self):
            return self.getTypedRuleContext(HomiParser.ReferenciaContext,0)


        def getRuleIndex(self):
            return HomiParser.RULE_acaoSimples

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAcaoSimples" ):
                listener.enterAcaoSimples(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAcaoSimples" ):
                listener.exitAcaoSimples(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAcaoSimples" ):
                return visitor.visitAcaoSimples(self)
            else:
                return visitor.visitChildren(self)




    def acaoSimples(self):

        localctx = HomiParser.AcaoSimplesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_acaoSimples)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.verboAcao()
            self.state = 131
            self.referencia()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VerboAcaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LIGAR(self):
            return self.getToken(HomiParser.LIGAR, 0)

        def DESLIGAR(self):
            return self.getToken(HomiParser.DESLIGAR, 0)

        def getRuleIndex(self):
            return HomiParser.RULE_verboAcao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVerboAcao" ):
                listener.enterVerboAcao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVerboAcao" ):
                listener.exitVerboAcao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVerboAcao" ):
                return visitor.visitVerboAcao(self)
            else:
                return visitor.visitChildren(self)




    def verboAcao(self):

        localctx = HomiParser.VerboAcaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_verboAcao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            _la = self._input.LA(1)
            if not(_la==7 or _la==8):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EsperaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ESPERAR(self):
            return self.getToken(HomiParser.ESPERAR, 0)

        def DURATION(self):
            return self.getToken(HomiParser.DURATION, 0)

        def getRuleIndex(self):
            return HomiParser.RULE_espera

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEspera" ):
                listener.enterEspera(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEspera" ):
                listener.exitEspera(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEspera" ):
                return visitor.visitEspera(self)
            else:
                return visitor.visitChildren(self)




    def espera(self):

        localctx = HomiParser.EsperaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_espera)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(HomiParser.ESPERAR)
            self.state = 136
            self.match(HomiParser.DURATION)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MODO(self):
            return self.getToken(HomiParser.MODO, 0)

        def modoValor(self):
            return self.getTypedRuleContext(HomiParser.ModoValorContext,0)


        def PONTO_VIRGULA(self):
            return self.getToken(HomiParser.PONTO_VIRGULA, 0)

        def getRuleIndex(self):
            return HomiParser.RULE_modo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModo" ):
                listener.enterModo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModo" ):
                listener.exitModo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModo" ):
                return visitor.visitModo(self)
            else:
                return visitor.visitChildren(self)




    def modo(self):

        localctx = HomiParser.ModoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_modo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(HomiParser.MODO)
            self.state = 139
            self.modoValor()
            self.state = 140
            self.match(HomiParser.PONTO_VIRGULA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModoValorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINGLE(self):
            return self.getToken(HomiParser.SINGLE, 0)

        def RESTART(self):
            return self.getToken(HomiParser.RESTART, 0)

        def QUEUED(self):
            return self.getToken(HomiParser.QUEUED, 0)

        def PARALLEL(self):
            return self.getToken(HomiParser.PARALLEL, 0)

        def getRuleIndex(self):
            return HomiParser.RULE_modoValor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModoValor" ):
                listener.enterModoValor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModoValor" ):
                listener.exitModoValor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModoValor" ):
                return visitor.visitModoValor(self)
            else:
                return visitor.visitChildren(self)




    def modoValor(self):

        localctx = HomiParser.ModoValorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_modoValor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7864320) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReferenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(HomiParser.IDENT, 0)

        def ENTITY_ID(self):
            return self.getToken(HomiParser.ENTITY_ID, 0)

        def getRuleIndex(self):
            return HomiParser.RULE_referencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReferencia" ):
                listener.enterReferencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReferencia" ):
                listener.exitReferencia(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReferencia" ):
                return visitor.visitReferencia(self)
            else:
                return visitor.visitChildren(self)




    def referencia(self):

        localctx = HomiParser.ReferenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_referencia)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            _la = self._input.LA(1)
            if not(_la==31 or _la==32):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATE(self):
            return self.getToken(HomiParser.STATE, 0)

        def STRING(self):
            return self.getToken(HomiParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(HomiParser.NUMBER, 0)

        def BOOLEAN(self):
            return self.getToken(HomiParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return HomiParser.RULE_valor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValor" ):
                listener.enterValor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValor" ):
                listener.exitValor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValor" ):
                return visitor.visitValor(self)
            else:
                return visitor.visitChildren(self)




    def valor(self):

        localctx = HomiParser.ValorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_valor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 9688842240) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





