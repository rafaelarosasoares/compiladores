# Generated from grammar/Homi.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .HomiParser import HomiParser
else:
    from HomiParser import HomiParser

# This class defines a complete generic visitor for a parse tree produced by HomiParser.

class HomiVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by HomiParser#programa.
    def visitPrograma(self, ctx:HomiParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HomiParser#automacao.
    def visitAutomacao(self, ctx:HomiParser.AutomacaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HomiParser#condicaoOpcional.
    def visitCondicaoOpcional(self, ctx:HomiParser.CondicaoOpcionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HomiParser#evento.
    def visitEvento(self, ctx:HomiParser.EventoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HomiParser#condicao.
    def visitCondicao(self, ctx:HomiParser.CondicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HomiParser#operador.
    def visitOperador(self, ctx:HomiParser.OperadorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HomiParser#acoes.
    def visitAcoes(self, ctx:HomiParser.AcoesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HomiParser#acao.
    def visitAcao(self, ctx:HomiParser.AcaoContext):
        return self.visitChildren(ctx)



del HomiParser