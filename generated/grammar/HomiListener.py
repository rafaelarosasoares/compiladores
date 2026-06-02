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


    # Enter a parse tree produced by HomiParser#declaracao.
    def enterDeclaracao(self, ctx:HomiParser.DeclaracaoContext):
        pass

    # Exit a parse tree produced by HomiParser#declaracao.
    def exitDeclaracao(self, ctx:HomiParser.DeclaracaoContext):
        pass


    # Enter a parse tree produced by HomiParser#dominio.
    def enterDominio(self, ctx:HomiParser.DominioContext):
        pass

    # Exit a parse tree produced by HomiParser#dominio.
    def exitDominio(self, ctx:HomiParser.DominioContext):
        pass


    # Enter a parse tree produced by HomiParser#automacao.
    def enterAutomacao(self, ctx:HomiParser.AutomacaoContext):
        pass

    # Exit a parse tree produced by HomiParser#automacao.
    def exitAutomacao(self, ctx:HomiParser.AutomacaoContext):
        pass


    # Enter a parse tree produced by HomiParser#corpoAutomacao.
    def enterCorpoAutomacao(self, ctx:HomiParser.CorpoAutomacaoContext):
        pass

    # Exit a parse tree produced by HomiParser#corpoAutomacao.
    def exitCorpoAutomacao(self, ctx:HomiParser.CorpoAutomacaoContext):
        pass


    # Enter a parse tree produced by HomiParser#blocoGatilho.
    def enterBlocoGatilho(self, ctx:HomiParser.BlocoGatilhoContext):
        pass

    # Exit a parse tree produced by HomiParser#blocoGatilho.
    def exitBlocoGatilho(self, ctx:HomiParser.BlocoGatilhoContext):
        pass


    # Enter a parse tree produced by HomiParser#gatilho.
    def enterGatilho(self, ctx:HomiParser.GatilhoContext):
        pass

    # Exit a parse tree produced by HomiParser#gatilho.
    def exitGatilho(self, ctx:HomiParser.GatilhoContext):
        pass


    # Enter a parse tree produced by HomiParser#blocoAcoes.
    def enterBlocoAcoes(self, ctx:HomiParser.BlocoAcoesContext):
        pass

    # Exit a parse tree produced by HomiParser#blocoAcoes.
    def exitBlocoAcoes(self, ctx:HomiParser.BlocoAcoesContext):
        pass


    # Enter a parse tree produced by HomiParser#comando.
    def enterComando(self, ctx:HomiParser.ComandoContext):
        pass

    # Exit a parse tree produced by HomiParser#comando.
    def exitComando(self, ctx:HomiParser.ComandoContext):
        pass


    # Enter a parse tree produced by HomiParser#acaoSimples.
    def enterAcaoSimples(self, ctx:HomiParser.AcaoSimplesContext):
        pass

    # Exit a parse tree produced by HomiParser#acaoSimples.
    def exitAcaoSimples(self, ctx:HomiParser.AcaoSimplesContext):
        pass


    # Enter a parse tree produced by HomiParser#verboAcao.
    def enterVerboAcao(self, ctx:HomiParser.VerboAcaoContext):
        pass

    # Exit a parse tree produced by HomiParser#verboAcao.
    def exitVerboAcao(self, ctx:HomiParser.VerboAcaoContext):
        pass


    # Enter a parse tree produced by HomiParser#espera.
    def enterEspera(self, ctx:HomiParser.EsperaContext):
        pass

    # Exit a parse tree produced by HomiParser#espera.
    def exitEspera(self, ctx:HomiParser.EsperaContext):
        pass


    # Enter a parse tree produced by HomiParser#modo.
    def enterModo(self, ctx:HomiParser.ModoContext):
        pass

    # Exit a parse tree produced by HomiParser#modo.
    def exitModo(self, ctx:HomiParser.ModoContext):
        pass


    # Enter a parse tree produced by HomiParser#modoValor.
    def enterModoValor(self, ctx:HomiParser.ModoValorContext):
        pass

    # Exit a parse tree produced by HomiParser#modoValor.
    def exitModoValor(self, ctx:HomiParser.ModoValorContext):
        pass


    # Enter a parse tree produced by HomiParser#referencia.
    def enterReferencia(self, ctx:HomiParser.ReferenciaContext):
        pass

    # Exit a parse tree produced by HomiParser#referencia.
    def exitReferencia(self, ctx:HomiParser.ReferenciaContext):
        pass


    # Enter a parse tree produced by HomiParser#valor.
    def enterValor(self, ctx:HomiParser.ValorContext):
        pass

    # Exit a parse tree produced by HomiParser#valor.
    def exitValor(self, ctx:HomiParser.ValorContext):
        pass



del HomiParser