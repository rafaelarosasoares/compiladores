from antlr4 import Token

from HomiLexer import HomiLexer
from ast_nodes import (
    Program,
    EntityDecl,
    Automation,
    StateTrigger,
    SimpleAction,
    DelayAction,
)


EOF = Token.EOF
EPSILON = ()


def clean_string(text: str) -> str:
    if text.startswith('"') and text.endswith('"'):
        return text[1:-1]
    return text


class TableParser:
    TERMINAL_NAMES = {
        EOF: "EOF",
        HomiLexer.ENTIDADE: "entidade",
        HomiLexer.AUTOMACAO: "automacao",
        HomiLexer.QUANDO: "quando",
        HomiLexer.ESTADO: "estado",
        HomiLexer.FICAR: "ficar",
        HomiLexer.FACA: "faca",
        HomiLexer.LIGAR: "ligar",
        HomiLexer.DESLIGAR: "desligar",
        HomiLexer.ESPERAR: "esperar",
        HomiLexer.MODO: "modo",
        HomiLexer.LUZ: "luz",
        HomiLexer.SENSOR: "sensor",
        HomiLexer.INTERRUPTOR: "interruptor",
        HomiLexer.ALARME: "alarme",
        HomiLexer.SINGLE: "single",
        HomiLexer.RESTART: "restart",
        HomiLexer.QUEUED: "queued",
        HomiLexer.PARALLEL: "parallel",
        HomiLexer.STATE: "STATE",
        HomiLexer.BOOLEAN: "BOOLEAN",
        HomiLexer.IGUAL: "=",
        HomiLexer.ABRE_CHAVE: "{",
        HomiLexer.FECHA_CHAVE: "}",
        HomiLexer.PONTO_VIRGULA: ";",
        HomiLexer.DURATION: "DURATION",
        HomiLexer.NUMBER: "NUMBER",
        HomiLexer.ENTITY_ID: "ENTITY_ID",
        HomiLexer.IDENT: "IDENT",
        HomiLexer.STRING: "STRING",
    }

    PARSE_TABLE = {
        ("programa", HomiLexer.ENTIDADE): ("declaracao_lista", "automacao_lista", EOF),
        ("programa", HomiLexer.AUTOMACAO): ("declaracao_lista", "automacao_lista", EOF),

        ("declaracao_lista", HomiLexer.ENTIDADE): ("declaracao", "declaracao_lista"),
        ("declaracao_lista", HomiLexer.AUTOMACAO): EPSILON,

        (
            "declaracao",
            HomiLexer.ENTIDADE,
        ): (
            HomiLexer.ENTIDADE,
            "dominio",
            HomiLexer.IDENT,
            HomiLexer.IGUAL,
            HomiLexer.ENTITY_ID,
            HomiLexer.PONTO_VIRGULA,
        ),

        ("dominio", HomiLexer.LUZ): (HomiLexer.LUZ,),
        ("dominio", HomiLexer.SENSOR): (HomiLexer.SENSOR,),
        ("dominio", HomiLexer.INTERRUPTOR): (HomiLexer.INTERRUPTOR,),
        ("dominio", HomiLexer.ALARME): (HomiLexer.ALARME,),

        ("automacao_lista", HomiLexer.AUTOMACAO): ("automacao", "automacao_cauda"),

        ("automacao_cauda", HomiLexer.AUTOMACAO): ("automacao", "automacao_cauda"),
        ("automacao_cauda", EOF): EPSILON,

        (
            "automacao",
            HomiLexer.AUTOMACAO,
        ): (
            HomiLexer.AUTOMACAO,
            HomiLexer.STRING,
            HomiLexer.ABRE_CHAVE,
            "corpo_automacao",
            HomiLexer.FECHA_CHAVE,
        ),

        ("corpo_automacao", HomiLexer.QUANDO): (
            "bloco_gatilho",
            "bloco_acoes",
            "modo_opcional",
        ),

        ("bloco_gatilho", HomiLexer.QUANDO): (
            HomiLexer.QUANDO,
            "gatilho",
            HomiLexer.PONTO_VIRGULA,
        ),

        ("gatilho", HomiLexer.ESTADO): (
            HomiLexer.ESTADO,
            "referencia",
            HomiLexer.FICAR,
            "valor",
        ),

        ("bloco_acoes", HomiLexer.FACA): (
            HomiLexer.FACA,
            HomiLexer.ABRE_CHAVE,
            "comando_lista",
            HomiLexer.FECHA_CHAVE,
        ),

        ("comando_lista", HomiLexer.LIGAR): ("comando", "comando_lista"),
        ("comando_lista", HomiLexer.DESLIGAR): ("comando", "comando_lista"),
        ("comando_lista", HomiLexer.ESPERAR): ("comando", "comando_lista"),
        ("comando_lista", HomiLexer.FECHA_CHAVE): EPSILON,

        ("comando", HomiLexer.LIGAR): ("acao_simples", HomiLexer.PONTO_VIRGULA),
        ("comando", HomiLexer.DESLIGAR): ("acao_simples", HomiLexer.PONTO_VIRGULA),
        ("comando", HomiLexer.ESPERAR): ("espera", HomiLexer.PONTO_VIRGULA),

        ("acao_simples", HomiLexer.LIGAR): ("verbo_acao", "referencia"),
        ("acao_simples", HomiLexer.DESLIGAR): ("verbo_acao", "referencia"),

        ("verbo_acao", HomiLexer.LIGAR): (HomiLexer.LIGAR,),
        ("verbo_acao", HomiLexer.DESLIGAR): (HomiLexer.DESLIGAR,),

        ("espera", HomiLexer.ESPERAR): (HomiLexer.ESPERAR, HomiLexer.DURATION),

        ("modo_opcional", HomiLexer.MODO): ("modo",),
        ("modo_opcional", HomiLexer.FECHA_CHAVE): EPSILON,

        ("modo", HomiLexer.MODO): (
            HomiLexer.MODO,
            "modo_valor",
            HomiLexer.PONTO_VIRGULA,
        ),

        ("modo_valor", HomiLexer.SINGLE): (HomiLexer.SINGLE,),
        ("modo_valor", HomiLexer.RESTART): (HomiLexer.RESTART,),
        ("modo_valor", HomiLexer.QUEUED): (HomiLexer.QUEUED,),
        ("modo_valor", HomiLexer.PARALLEL): (HomiLexer.PARALLEL,),

        ("referencia", HomiLexer.IDENT): (HomiLexer.IDENT,),
        ("referencia", HomiLexer.ENTITY_ID): (HomiLexer.ENTITY_ID,),

        ("valor", HomiLexer.STATE): (HomiLexer.STATE,),
        ("valor", HomiLexer.STRING): (HomiLexer.STRING,),
        ("valor", HomiLexer.NUMBER): (HomiLexer.NUMBER,),
        ("valor", HomiLexer.BOOLEAN): (HomiLexer.BOOLEAN,),
    }

    FOLLOW = {
        "programa": {EOF},
        "declaracao_lista": {HomiLexer.AUTOMACAO},
        "declaracao": {HomiLexer.ENTIDADE, HomiLexer.AUTOMACAO},
        "dominio": {HomiLexer.IDENT},
        "automacao_lista": {EOF},
        "automacao_cauda": {EOF},
        "automacao": {HomiLexer.AUTOMACAO, EOF},
        "corpo_automacao": {HomiLexer.FECHA_CHAVE},
        "bloco_gatilho": {HomiLexer.FACA},
        "gatilho": {HomiLexer.PONTO_VIRGULA},
        "bloco_acoes": {HomiLexer.MODO, HomiLexer.FECHA_CHAVE},
        "comando_lista": {HomiLexer.FECHA_CHAVE},
        "comando": {
            HomiLexer.LIGAR,
            HomiLexer.DESLIGAR,
            HomiLexer.ESPERAR,
            HomiLexer.FECHA_CHAVE,
        },
        "acao_simples": {HomiLexer.PONTO_VIRGULA},
        "verbo_acao": {HomiLexer.IDENT, HomiLexer.ENTITY_ID},
        "espera": {HomiLexer.PONTO_VIRGULA},
        "modo_opcional": {HomiLexer.FECHA_CHAVE},
        "modo": {HomiLexer.FECHA_CHAVE},
        "modo_valor": {HomiLexer.PONTO_VIRGULA},
        "referencia": {HomiLexer.FICAR, HomiLexer.PONTO_VIRGULA},
        "valor": {HomiLexer.PONTO_VIRGULA},
    }

    def __init__(self, tokens):
        self.tokens = [
            token
            for token in tokens
            if token.channel == Token.DEFAULT_CHANNEL or token.type == EOF
        ]
        self.pos = 0
        self.ast_pos = 0
        self.errors = []
        self.first_sets = self.build_first_sets()

    def parse(self):
        self.validate_by_table()
        if self.errors:
            return None
        return self.build_ast()

    def build_first_sets(self):
        first_sets = {}
        for non_terminal, lookahead in self.PARSE_TABLE:
            first_sets.setdefault(non_terminal, set()).add(lookahead)
        return first_sets

    def validate_by_table(self):
        stack = [EOF, "programa"]

        while stack:
            top = stack.pop()
            lookahead = self.current().type

            if isinstance(top, int):
                self.match_terminal(top)
                continue

            production = self.PARSE_TABLE.get((top, lookahead))
            if production is None:
                self.recover_non_terminal(top, lookahead, stack)
                continue

            for symbol in reversed(production):
                stack.append(symbol)

            if top == "automacao_lista" and lookahead != HomiLexer.AUTOMACAO:
                self.report_current(
                    "era esperada pelo menos uma declaração de automação"
                )

    def match_terminal(self, expected_type: int):
        current = self.current()
        if current.type == expected_type:
            self.pos += 1
            return

        self.errors.append(
            f"Linha {current.line}, coluna {current.column}: esperado "
            f"'{self.token_name(expected_type)}', encontrado "
            f"'{self.token_text(current)}'"
        )

    def recover_non_terminal(self, non_terminal: str, lookahead: int, stack):
        expected = self.expected_tokens(non_terminal)
        self.report_current(
            f"token inesperado em {non_terminal}; esperado {expected}"
        )

        follow = self.FOLLOW.get(non_terminal, {EOF})
        first = self.first_sets.get(non_terminal, set())

        if lookahead in follow or lookahead == EOF:
            return

        while self.current().type not in first and self.current().type not in follow:
            if self.current().type == EOF:
                return
            self.pos += 1

        if self.current().type in first:
            stack.append(non_terminal)

    def report_current(self, message: str):
        current = self.current()
        self.errors.append(
            f"Linha {current.line}, coluna {current.column}: {message}"
        )

    def expected_tokens(self, non_terminal: str):
        tokens = sorted(self.first_sets.get(non_terminal, set()))
        return ", ".join(self.token_name(token_type) for token_type in tokens)

    def current(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return self.tokens[-1]

    def ast_current(self):
        if self.ast_pos < len(self.tokens):
            return self.tokens[self.ast_pos]
        return self.tokens[-1]

    def ast_consume(self, expected_type: int):
        token = self.ast_current()
        if token.type == expected_type:
            self.ast_pos += 1
            return token
        raise ValueError(
            f"AST esperava {self.token_name(expected_type)}, "
            f"encontrou {self.token_text(token)}"
        )

    def token_name(self, token_type: int) -> str:
        return self.TERMINAL_NAMES.get(token_type, str(token_type))

    def token_text(self, token) -> str:
        if token.type == EOF:
            return "EOF"
        return token.text

    def build_ast(self):
        declarations = []
        automations = []

        while self.ast_current().type == HomiLexer.ENTIDADE:
            declarations.append(self.parse_declaration())

        while self.ast_current().type == HomiLexer.AUTOMACAO:
            automations.append(self.parse_automation())

        self.ast_consume(EOF)

        return Program(declarations, automations)

    def parse_declaration(self):
        start = self.ast_consume(HomiLexer.ENTIDADE)
        domain = self.ast_consume(self.ast_current().type)
        name = self.ast_consume(HomiLexer.IDENT)
        self.ast_consume(HomiLexer.IGUAL)
        entity_id = self.ast_consume(HomiLexer.ENTITY_ID)
        self.ast_consume(HomiLexer.PONTO_VIRGULA)

        return EntityDecl(domain.text, name.text, entity_id.text, start.line)

    def parse_automation(self):
        start = self.ast_consume(HomiLexer.AUTOMACAO)
        name = self.ast_consume(HomiLexer.STRING)
        self.ast_consume(HomiLexer.ABRE_CHAVE)

        trigger = self.parse_trigger_block()
        actions = self.parse_actions_block()
        mode = self.parse_optional_mode()

        self.ast_consume(HomiLexer.FECHA_CHAVE)

        return Automation(clean_string(name.text), trigger, actions, mode, start.line)

    def parse_trigger_block(self):
        self.ast_consume(HomiLexer.QUANDO)
        trigger = self.parse_trigger()
        self.ast_consume(HomiLexer.PONTO_VIRGULA)
        return trigger

    def parse_trigger(self):
        start = self.ast_consume(HomiLexer.ESTADO)
        reference = self.ast_consume(self.ast_current().type)
        self.ast_consume(HomiLexer.FICAR)
        value = self.ast_consume(self.ast_current().type)
        return StateTrigger(reference.text, value.text, start.line)

    def parse_actions_block(self):
        actions = []

        self.ast_consume(HomiLexer.FACA)
        self.ast_consume(HomiLexer.ABRE_CHAVE)

        while self.ast_current().type in {
            HomiLexer.LIGAR,
            HomiLexer.DESLIGAR,
            HomiLexer.ESPERAR,
        }:
            actions.append(self.parse_command())

        self.ast_consume(HomiLexer.FECHA_CHAVE)

        return actions

    def parse_command(self):
        if self.ast_current().type in {HomiLexer.LIGAR, HomiLexer.DESLIGAR}:
            action = self.parse_simple_action()
        else:
            action = self.parse_delay()

        self.ast_consume(HomiLexer.PONTO_VIRGULA)
        return action

    def parse_simple_action(self):
        verb = self.ast_consume(self.ast_current().type)
        reference = self.ast_consume(self.ast_current().type)
        return SimpleAction(verb.text, reference.text, verb.line)

    def parse_delay(self):
        start = self.ast_consume(HomiLexer.ESPERAR)
        duration = self.ast_consume(HomiLexer.DURATION)
        return DelayAction(duration.text, start.line)

    def parse_optional_mode(self):
        if self.ast_current().type != HomiLexer.MODO:
            return None

        self.ast_consume(HomiLexer.MODO)
        mode = self.ast_consume(self.ast_current().type)
        self.ast_consume(HomiLexer.PONTO_VIRGULA)

        return mode.text
