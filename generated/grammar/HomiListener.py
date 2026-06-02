# Generated from grammar/Homi.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .HomiParser import HomiParser
else:
    from HomiParser import HomiParser

# This class defines a complete listener for a parse tree produced by HomiParser.
class HomiListener(ParseTreeListener):

    # Enter a parse tree produced by HomiParser#programa.
    def enterPrograma(self, ctx:HomiParser.ProgramaContext):
        pass

    # Exit a parse tree produced by HomiParser#programa.
    def exitPrograma(self, ctx:HomiParser.ProgramaContext):
        pass


    # Enter a parse tree produced by HomiParser#automacao.
    def enterAutomacao(self, ctx:HomiParser.AutomacaoContext):
        pass

    # Exit a parse tree produced by HomiParser#automacao.
    def exitAutomacao(self, ctx:HomiParser.AutomacaoContext):
        pass


    # Enter a parse tree produced by HomiParser#condicaoOpcional.
    def enterCondicaoOpcional(self, ctx:HomiParser.CondicaoOpcionalContext):
        pass

    # Exit a parse tree produced by HomiParser#condicaoOpcional.
    def exitCondicaoOpcional(self, ctx:HomiParser.CondicaoOpcionalContext):
        pass


    # Enter a parse tree produced by HomiParser#evento.
    def enterEvento(self, ctx:HomiParser.EventoContext):
        pass

    # Exit a parse tree produced by HomiParser#evento.
    def exitEvento(self, ctx:HomiParser.EventoContext):
        pass


    # Enter a parse tree produced by HomiParser#condicao.
    def enterCondicao(self, ctx:HomiParser.CondicaoContext):
        pass

    # Exit a parse tree produced by HomiParser#condicao.
    def exitCondicao(self, ctx:HomiParser.CondicaoContext):
        pass


    # Enter a parse tree produced by HomiParser#operador.
    def enterOperador(self, ctx:HomiParser.OperadorContext):
        pass

    # Exit a parse tree produced by HomiParser#operador.
    def exitOperador(self, ctx:HomiParser.OperadorContext):
        pass


    # Enter a parse tree produced by HomiParser#acoes.
    def enterAcoes(self, ctx:HomiParser.AcoesContext):
        pass

    # Exit a parse tree produced by HomiParser#acoes.
    def exitAcoes(self, ctx:HomiParser.AcoesContext):
        pass


    # Enter a parse tree produced by HomiParser#acao.
    def enterAcao(self, ctx:HomiParser.AcaoContext):
        pass

    # Exit a parse tree produced by HomiParser#acao.
    def exitAcao(self, ctx:HomiParser.AcaoContext):
        pass



del HomiParser