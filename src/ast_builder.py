import sys

sys.path.append("generated/grammar")

from HomiVisitor import HomiVisitor
from HomiParser import HomiParser

from ast_nodes import (
    Program,
    EntityDecl,
    Automation,
    StateTrigger,
    ConditionExpression,
    ConditionTerm,
    SimpleAction,
    DelayAction,
)


def clean_string(text: str) -> str:
    if text.startswith('"') and text.endswith('"'):
        return text[1:-1]
    return text


def line_of(ctx) -> int:
    return ctx.start.line if ctx.start is not None else 0


class AstBuilder(HomiVisitor):
    def visitPrograma(self, ctx: HomiParser.ProgramaContext):
        declarations = []
        automations = []

        for child in ctx.children:
            if isinstance(child, HomiParser.DeclaracaoContext):
                declarations.append(self.visit(child))
            elif isinstance(child, HomiParser.AutomacaoContext):
                automations.append(self.visit(child))

        return Program(declarations, automations)

    def visitDeclaracao(self, ctx: HomiParser.DeclaracaoContext):
        domain = ctx.dominio().getText()
        name = ctx.IDENT().getText()
        entity_id = ctx.ENTITY_ID().getText()

        return EntityDecl(domain, name, entity_id, line_of(ctx))

    def visitAutomacao(self, ctx: HomiParser.AutomacaoContext):
        name = clean_string(ctx.STRING().getText())
        body = ctx.corpoAutomacao()

        trigger = self.visit(body.blocoGatilho())
        condition = None
        if body.blocoCondicoes() is not None:
            condition = self.visit(body.blocoCondicoes())
        actions = self.visit(body.blocoAcoes())

        mode = None
        if body.modo() is not None:
            mode = body.modo().modoValor().getText()

        return Automation(name, trigger, condition, actions, mode, line_of(ctx))

    def visitBlocoGatilho(self, ctx: HomiParser.BlocoGatilhoContext):
        return self.visit(ctx.gatilho())

    def visitGatilho(self, ctx: HomiParser.GatilhoContext):
        entity = ctx.referencia().getText()
        value = ctx.valor().getText()
        return StateTrigger(entity, value, line_of(ctx))

    def visitBlocoCondicoes(self, ctx: HomiParser.BlocoCondicoesContext):
        return self.visit(ctx.expressaoCondicao())

    def visitExpressaoCondicao(self, ctx: HomiParser.ExpressaoCondicaoContext):
        terms = [self.visit(term_ctx) for term_ctx in ctx.termoCondicao()]
        operators = [op_ctx.getText() for op_ctx in ctx.operadorLogico()]
        return ConditionExpression(terms, operators, line_of(ctx))

    def visitTermoCondicao(self, ctx: HomiParser.TermoCondicaoContext):
        condition = ctx.condicaoEstado()
        entity = condition.referencia().getText()
        value = condition.valor().getText()
        negated = ctx.NAO() is not None
        return ConditionTerm(entity, value, negated, line_of(ctx))

    def visitBlocoAcoes(self, ctx: HomiParser.BlocoAcoesContext):
        actions = []

        for command_ctx in ctx.comando():
            actions.append(self.visit(command_ctx))

        return actions

    def visitComando(self, ctx: HomiParser.ComandoContext):
        if ctx.acaoSimples() is not None:
            return self.visit(ctx.acaoSimples())

        if ctx.espera() is not None:
            return self.visit(ctx.espera())

        raise Exception("Comando desconhecido")

    def visitAcaoSimples(self, ctx: HomiParser.AcaoSimplesContext):
        verb = ctx.verboAcao().getText()
        entity = ctx.referencia().getText()

        return SimpleAction(verb, entity, line_of(ctx))

    def visitEspera(self, ctx: HomiParser.EsperaContext):
        duration = ctx.DURATION().getText()
        return DelayAction(duration, line_of(ctx))
