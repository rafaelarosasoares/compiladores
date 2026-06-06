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


    # Visit a parse tree produced by HomiParser#declaracao.
    def visitDeclaracao(self, ctx:HomiParser.DeclaracaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HomiParser#dominio.
    def visitDominio(self, ctx:HomiParser.DominioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HomiParser#automacao.
    def visitAutomacao(self, ctx:HomiParser.AutomacaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HomiParser#corpoAutomacao.
    def visitCorpoAutomacao(self, ctx:HomiParser.CorpoAutomacaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HomiParser#blocoGatilho.
    def visitBlocoGatilho(self, ctx:HomiParser.BlocoGatilhoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HomiParser#gatilho.
    def visitGatilho(self, ctx:HomiParser.GatilhoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HomiParser#blocoCondicoes.
    def visitBlocoCondicoes(self, ctx:HomiParser.BlocoCondicoesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HomiParser#expressaoCondicao.
    def visitExpressaoCondicao(self, ctx:HomiParser.ExpressaoCondicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HomiParser#termoCondicao.
    def visitTermoCondicao(self, ctx:HomiParser.TermoCondicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HomiParser#condicaoEstado.
    def visitCondicaoEstado(self, ctx:HomiParser.CondicaoEstadoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HomiParser#operadorLogico.
    def visitOperadorLogico(self, ctx:HomiParser.OperadorLogicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HomiParser#blocoAcoes.
    def visitBlocoAcoes(self, ctx:HomiParser.BlocoAcoesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HomiParser#comando.
    def visitComando(self, ctx:HomiParser.ComandoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HomiParser#acaoSimples.
    def visitAcaoSimples(self, ctx:HomiParser.AcaoSimplesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HomiParser#verboAcao.
    def visitVerboAcao(self, ctx:HomiParser.VerboAcaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HomiParser#espera.
    def visitEspera(self, ctx:HomiParser.EsperaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HomiParser#modo.
    def visitModo(self, ctx:HomiParser.ModoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HomiParser#modoValor.
    def visitModoValor(self, ctx:HomiParser.ModoValorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HomiParser#referencia.
    def visitReferencia(self, ctx:HomiParser.ReferenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HomiParser#valor.
    def visitValor(self, ctx:HomiParser.ValorContext):
        return self.visitChildren(ctx)



del HomiParser