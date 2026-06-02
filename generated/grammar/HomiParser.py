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
        4,1,31,111,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,5,0,34,8,0,10,0,12,0,37,9,0,1,0,4,0,40,8,
        0,11,0,12,0,41,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,3,1,
        3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,3,4,64,8,4,1,5,1,5,1,5,1,5,1,6,1,6,
        1,6,1,6,1,6,1,7,1,7,1,7,5,7,78,8,7,10,7,12,7,81,9,7,1,7,1,7,1,8,
        1,8,1,8,1,8,1,8,1,8,3,8,91,8,8,1,9,1,9,1,9,1,10,1,10,1,11,1,11,1,
        11,1,12,1,12,1,12,1,12,1,13,1,13,1,14,1,14,1,15,1,15,1,15,0,0,16,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,0,5,1,0,11,14,1,0,7,8,
        1,0,15,18,1,0,27,28,3,0,19,20,26,26,29,29,99,0,35,1,0,0,0,2,45,1,
        0,0,0,4,52,1,0,0,0,6,54,1,0,0,0,8,60,1,0,0,0,10,65,1,0,0,0,12,69,
        1,0,0,0,14,74,1,0,0,0,16,90,1,0,0,0,18,92,1,0,0,0,20,95,1,0,0,0,
        22,97,1,0,0,0,24,100,1,0,0,0,26,104,1,0,0,0,28,106,1,0,0,0,30,108,
        1,0,0,0,32,34,3,2,1,0,33,32,1,0,0,0,34,37,1,0,0,0,35,33,1,0,0,0,
        35,36,1,0,0,0,36,39,1,0,0,0,37,35,1,0,0,0,38,40,3,6,3,0,39,38,1,
        0,0,0,40,41,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,43,1,0,0,0,43,
        44,5,0,0,1,44,1,1,0,0,0,45,46,5,1,0,0,46,47,3,4,2,0,47,48,5,28,0,
        0,48,49,5,21,0,0,49,50,5,27,0,0,50,51,5,24,0,0,51,3,1,0,0,0,52,53,
        7,0,0,0,53,5,1,0,0,0,54,55,5,2,0,0,55,56,5,29,0,0,56,57,5,22,0,0,
        57,58,3,8,4,0,58,59,5,23,0,0,59,7,1,0,0,0,60,61,3,10,5,0,61,63,3,
        14,7,0,62,64,3,24,12,0,63,62,1,0,0,0,63,64,1,0,0,0,64,9,1,0,0,0,
        65,66,5,3,0,0,66,67,3,12,6,0,67,68,5,24,0,0,68,11,1,0,0,0,69,70,
        5,4,0,0,70,71,3,28,14,0,71,72,5,5,0,0,72,73,3,30,15,0,73,13,1,0,
        0,0,74,75,5,6,0,0,75,79,5,22,0,0,76,78,3,16,8,0,77,76,1,0,0,0,78,
        81,1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,82,1,0,0,0,81,79,1,0,0,
        0,82,83,5,23,0,0,83,15,1,0,0,0,84,85,3,18,9,0,85,86,5,24,0,0,86,
        91,1,0,0,0,87,88,3,22,11,0,88,89,5,24,0,0,89,91,1,0,0,0,90,84,1,
        0,0,0,90,87,1,0,0,0,91,17,1,0,0,0,92,93,3,20,10,0,93,94,3,28,14,
        0,94,19,1,0,0,0,95,96,7,1,0,0,96,21,1,0,0,0,97,98,5,9,0,0,98,99,
        5,25,0,0,99,23,1,0,0,0,100,101,5,10,0,0,101,102,3,26,13,0,102,103,
        5,24,0,0,103,25,1,0,0,0,104,105,7,2,0,0,105,27,1,0,0,0,106,107,7,
        3,0,0,107,29,1,0,0,0,108,109,7,4,0,0,109,31,1,0,0,0,5,35,41,63,79,
        90
    ]

class HomiParser ( Parser ):

    grammarFileName = "Homi.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'entidade'", "'automacao'", "'quando'", 
                     "'estado'", "'ficar'", "'faca'", "'ligar'", "'desligar'", 
                     "'esperar'", "'modo'", "'luz'", "'sensor'", "'interruptor'", 
                     "'alarme'", "'single'", "'restart'", "'queued'", "'parallel'", 
                     "<INVALID>", "<INVALID>", "'='", "'{'", "'}'", "';'" ]

    symbolicNames = [ "<INVALID>", "ENTIDADE", "AUTOMACAO", "QUANDO", "ESTADO", 
                      "FICAR", "FACA", "LIGAR", "DESLIGAR", "ESPERAR", "MODO", 
                      "LUZ", "SENSOR", "INTERRUPTOR", "ALARME", "SINGLE", 
                      "RESTART", "QUEUED", "PARALLEL", "STATE", "BOOLEAN", 
                      "IGUAL", "ABRE_CHAVE", "FECHA_CHAVE", "PONTO_VIRGULA", 
                      "DURATION", "NUMBER", "ENTITY_ID", "IDENT", "STRING", 
                      "COMMENT", "WS" ]

    RULE_programa = 0
    RULE_declaracao = 1
    RULE_dominio = 2
    RULE_automacao = 3
    RULE_corpoAutomacao = 4
    RULE_blocoGatilho = 5
    RULE_gatilho = 6
    RULE_blocoAcoes = 7
    RULE_comando = 8
    RULE_acaoSimples = 9
    RULE_verboAcao = 10
    RULE_espera = 11
    RULE_modo = 12
    RULE_modoValor = 13
    RULE_referencia = 14
    RULE_valor = 15

    ruleNames =  [ "programa", "declaracao", "dominio", "automacao", "corpoAutomacao", 
                   "blocoGatilho", "gatilho", "blocoAcoes", "comando", "acaoSimples", 
                   "verboAcao", "espera", "modo", "modoValor", "referencia", 
                   "valor" ]

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
    LUZ=11
    SENSOR=12
    INTERRUPTOR=13
    ALARME=14
    SINGLE=15
    RESTART=16
    QUEUED=17
    PARALLEL=18
    STATE=19
    BOOLEAN=20
    IGUAL=21
    ABRE_CHAVE=22
    FECHA_CHAVE=23
    PONTO_VIRGULA=24
    DURATION=25
    NUMBER=26
    ENTITY_ID=27
    IDENT=28
    STRING=29
    COMMENT=30
    WS=31

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
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 32
                self.declaracao()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 39 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 38
                self.automacao()
                self.state = 41 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2):
                    break

            self.state = 43
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
            self.state = 45
            self.match(HomiParser.ENTIDADE)
            self.state = 46
            self.dominio()
            self.state = 47
            self.match(HomiParser.IDENT)
            self.state = 48
            self.match(HomiParser.IGUAL)
            self.state = 49
            self.match(HomiParser.ENTITY_ID)
            self.state = 50
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
            self.state = 52
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30720) != 0)):
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
            self.state = 54
            self.match(HomiParser.AUTOMACAO)
            self.state = 55
            self.match(HomiParser.STRING)
            self.state = 56
            self.match(HomiParser.ABRE_CHAVE)
            self.state = 57
            self.corpoAutomacao()
            self.state = 58
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
            self.state = 60
            self.blocoGatilho()
            self.state = 61
            self.blocoAcoes()
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 62
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
            self.state = 65
            self.match(HomiParser.QUANDO)
            self.state = 66
            self.gatilho()
            self.state = 67
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
            self.state = 69
            self.match(HomiParser.ESTADO)
            self.state = 70
            self.referencia()
            self.state = 71
            self.match(HomiParser.FICAR)
            self.state = 72
            self.valor()
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
        self.enterRule(localctx, 14, self.RULE_blocoAcoes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(HomiParser.FACA)
            self.state = 75
            self.match(HomiParser.ABRE_CHAVE)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 896) != 0):
                self.state = 76
                self.comando()
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 82
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
        self.enterRule(localctx, 16, self.RULE_comando)
        try:
            self.state = 90
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.acaoSimples()
                self.state = 85
                self.match(HomiParser.PONTO_VIRGULA)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.espera()
                self.state = 88
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
        self.enterRule(localctx, 18, self.RULE_acaoSimples)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.verboAcao()
            self.state = 93
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
        self.enterRule(localctx, 20, self.RULE_verboAcao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
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
        self.enterRule(localctx, 22, self.RULE_espera)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(HomiParser.ESPERAR)
            self.state = 98
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
        self.enterRule(localctx, 24, self.RULE_modo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(HomiParser.MODO)
            self.state = 101
            self.modoValor()
            self.state = 102
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
        self.enterRule(localctx, 26, self.RULE_modoValor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
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
        self.enterRule(localctx, 28, self.RULE_referencia)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            _la = self._input.LA(1)
            if not(_la==27 or _la==28):
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
        self.enterRule(localctx, 30, self.RULE_valor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 605552640) != 0)):
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





