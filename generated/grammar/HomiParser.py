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
        4,1,21,65,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,4,0,18,8,0,11,0,12,0,19,1,0,1,0,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,3,2,36,8,2,1,3,1,3,1,3,1,3,1,3,1,3,
        3,3,44,8,3,1,4,1,4,1,4,1,4,1,5,1,5,1,6,4,6,53,8,6,11,6,12,6,54,1,
        7,1,7,1,7,1,7,1,7,1,7,3,7,63,8,7,1,7,0,0,8,0,2,4,6,8,10,12,14,0,
        1,1,0,10,15,63,0,17,1,0,0,0,2,23,1,0,0,0,4,35,1,0,0,0,6,43,1,0,0,
        0,8,45,1,0,0,0,10,49,1,0,0,0,12,52,1,0,0,0,14,62,1,0,0,0,16,18,3,
        2,1,0,17,16,1,0,0,0,18,19,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,
        21,1,0,0,0,21,22,5,0,0,1,22,1,1,0,0,0,23,24,5,1,0,0,24,25,5,19,0,
        0,25,26,5,2,0,0,26,27,3,6,3,0,27,28,3,4,2,0,28,29,5,4,0,0,29,30,
        3,12,6,0,30,31,5,5,0,0,31,3,1,0,0,0,32,33,5,3,0,0,33,36,3,8,4,0,
        34,36,1,0,0,0,35,32,1,0,0,0,35,34,1,0,0,0,36,5,1,0,0,0,37,38,5,18,
        0,0,38,44,5,6,0,0,39,40,5,18,0,0,40,44,5,7,0,0,41,42,5,18,0,0,42,
        44,5,8,0,0,43,37,1,0,0,0,43,39,1,0,0,0,43,41,1,0,0,0,44,7,1,0,0,
        0,45,46,5,18,0,0,46,47,3,10,5,0,47,48,5,17,0,0,48,9,1,0,0,0,49,50,
        7,0,0,0,50,11,1,0,0,0,51,53,3,14,7,0,52,51,1,0,0,0,53,54,1,0,0,0,
        54,52,1,0,0,0,54,55,1,0,0,0,55,13,1,0,0,0,56,57,5,6,0,0,57,63,5,
        18,0,0,58,59,5,7,0,0,59,63,5,18,0,0,60,61,5,9,0,0,61,63,5,16,0,0,
        62,56,1,0,0,0,62,58,1,0,0,0,62,60,1,0,0,0,63,15,1,0,0,0,5,19,35,
        43,54,62
    ]

class HomiParser ( Parser ):

    grammarFileName = "Homi.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'automacao'", "'quando'", "'se'", "'entao'", 
                     "'fim'", "'ligar'", "'desligar'", "'mudar'", "'esperar'", 
                     "'>'", "'<'", "'>='", "'<='", "'=='", "'!='" ]

    symbolicNames = [ "<INVALID>", "AUTOMACAO", "QUANDO", "SE", "ENTAO", 
                      "FIM", "LIGAR", "DESLIGAR", "MUDAR", "ESPERAR", "GT", 
                      "LT", "GE", "LE", "EQ", "NE", "TIME", "NUMBER", "ENTITY_ID", 
                      "ID", "COMMENT", "WS" ]

    RULE_programa = 0
    RULE_automacao = 1
    RULE_condicaoOpcional = 2
    RULE_evento = 3
    RULE_condicao = 4
    RULE_operador = 5
    RULE_acoes = 6
    RULE_acao = 7

    ruleNames =  [ "programa", "automacao", "condicaoOpcional", "evento", 
                   "condicao", "operador", "acoes", "acao" ]

    EOF = Token.EOF
    AUTOMACAO=1
    QUANDO=2
    SE=3
    ENTAO=4
    FIM=5
    LIGAR=6
    DESLIGAR=7
    MUDAR=8
    ESPERAR=9
    GT=10
    LT=11
    GE=12
    LE=13
    EQ=14
    NE=15
    TIME=16
    NUMBER=17
    ENTITY_ID=18
    ID=19
    COMMENT=20
    WS=21

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
            self.state = 17 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.automacao()
                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

            self.state = 21
            self.match(HomiParser.EOF)
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

        def ID(self):
            return self.getToken(HomiParser.ID, 0)

        def QUANDO(self):
            return self.getToken(HomiParser.QUANDO, 0)

        def evento(self):
            return self.getTypedRuleContext(HomiParser.EventoContext,0)


        def condicaoOpcional(self):
            return self.getTypedRuleContext(HomiParser.CondicaoOpcionalContext,0)


        def ENTAO(self):
            return self.getToken(HomiParser.ENTAO, 0)

        def acoes(self):
            return self.getTypedRuleContext(HomiParser.AcoesContext,0)


        def FIM(self):
            return self.getToken(HomiParser.FIM, 0)

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
        self.enterRule(localctx, 2, self.RULE_automacao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(HomiParser.AUTOMACAO)
            self.state = 24
            self.match(HomiParser.ID)
            self.state = 25
            self.match(HomiParser.QUANDO)
            self.state = 26
            self.evento()
            self.state = 27
            self.condicaoOpcional()
            self.state = 28
            self.match(HomiParser.ENTAO)
            self.state = 29
            self.acoes()
            self.state = 30
            self.match(HomiParser.FIM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicaoOpcionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SE(self):
            return self.getToken(HomiParser.SE, 0)

        def condicao(self):
            return self.getTypedRuleContext(HomiParser.CondicaoContext,0)


        def getRuleIndex(self):
            return HomiParser.RULE_condicaoOpcional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicaoOpcional" ):
                listener.enterCondicaoOpcional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicaoOpcional" ):
                listener.exitCondicaoOpcional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicaoOpcional" ):
                return visitor.visitCondicaoOpcional(self)
            else:
                return visitor.visitChildren(self)




    def condicaoOpcional(self):

        localctx = HomiParser.CondicaoOpcionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_condicaoOpcional)
        try:
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.match(HomiParser.SE)
                self.state = 33
                self.condicao()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)

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


    class EventoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENTITY_ID(self):
            return self.getToken(HomiParser.ENTITY_ID, 0)

        def LIGAR(self):
            return self.getToken(HomiParser.LIGAR, 0)

        def DESLIGAR(self):
            return self.getToken(HomiParser.DESLIGAR, 0)

        def MUDAR(self):
            return self.getToken(HomiParser.MUDAR, 0)

        def getRuleIndex(self):
            return HomiParser.RULE_evento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEvento" ):
                listener.enterEvento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEvento" ):
                listener.exitEvento(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEvento" ):
                return visitor.visitEvento(self)
            else:
                return visitor.visitChildren(self)




    def evento(self):

        localctx = HomiParser.EventoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_evento)
        try:
            self.state = 43
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.match(HomiParser.ENTITY_ID)
                self.state = 38
                self.match(HomiParser.LIGAR)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.match(HomiParser.ENTITY_ID)
                self.state = 40
                self.match(HomiParser.DESLIGAR)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 41
                self.match(HomiParser.ENTITY_ID)
                self.state = 42
                self.match(HomiParser.MUDAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENTITY_ID(self):
            return self.getToken(HomiParser.ENTITY_ID, 0)

        def operador(self):
            return self.getTypedRuleContext(HomiParser.OperadorContext,0)


        def NUMBER(self):
            return self.getToken(HomiParser.NUMBER, 0)

        def getRuleIndex(self):
            return HomiParser.RULE_condicao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicao" ):
                listener.enterCondicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicao" ):
                listener.exitCondicao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicao" ):
                return visitor.visitCondicao(self)
            else:
                return visitor.visitChildren(self)




    def condicao(self):

        localctx = HomiParser.CondicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_condicao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(HomiParser.ENTITY_ID)
            self.state = 46
            self.operador()
            self.state = 47
            self.match(HomiParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperadorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GT(self):
            return self.getToken(HomiParser.GT, 0)

        def LT(self):
            return self.getToken(HomiParser.LT, 0)

        def GE(self):
            return self.getToken(HomiParser.GE, 0)

        def LE(self):
            return self.getToken(HomiParser.LE, 0)

        def EQ(self):
            return self.getToken(HomiParser.EQ, 0)

        def NE(self):
            return self.getToken(HomiParser.NE, 0)

        def getRuleIndex(self):
            return HomiParser.RULE_operador

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperador" ):
                listener.enterOperador(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperador" ):
                listener.exitOperador(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperador" ):
                return visitor.visitOperador(self)
            else:
                return visitor.visitChildren(self)




    def operador(self):

        localctx = HomiParser.OperadorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_operador)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 64512) != 0)):
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


    class AcoesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def acao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HomiParser.AcaoContext)
            else:
                return self.getTypedRuleContext(HomiParser.AcaoContext,i)


        def getRuleIndex(self):
            return HomiParser.RULE_acoes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAcoes" ):
                listener.enterAcoes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAcoes" ):
                listener.exitAcoes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAcoes" ):
                return visitor.visitAcoes(self)
            else:
                return visitor.visitChildren(self)




    def acoes(self):

        localctx = HomiParser.AcoesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_acoes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 51
                self.acao()
                self.state = 54 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 704) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AcaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LIGAR(self):
            return self.getToken(HomiParser.LIGAR, 0)

        def ENTITY_ID(self):
            return self.getToken(HomiParser.ENTITY_ID, 0)

        def DESLIGAR(self):
            return self.getToken(HomiParser.DESLIGAR, 0)

        def ESPERAR(self):
            return self.getToken(HomiParser.ESPERAR, 0)

        def TIME(self):
            return self.getToken(HomiParser.TIME, 0)

        def getRuleIndex(self):
            return HomiParser.RULE_acao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAcao" ):
                listener.enterAcao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAcao" ):
                listener.exitAcao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAcao" ):
                return visitor.visitAcao(self)
            else:
                return visitor.visitChildren(self)




    def acao(self):

        localctx = HomiParser.AcaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_acao)
        try:
            self.state = 62
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.match(HomiParser.LIGAR)
                self.state = 57
                self.match(HomiParser.ENTITY_ID)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                self.match(HomiParser.DESLIGAR)
                self.state = 59
                self.match(HomiParser.ENTITY_ID)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 60
                self.match(HomiParser.ESPERAR)
                self.state = 61
                self.match(HomiParser.TIME)
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





