import re

from ast_nodes import Program, SimpleAction, DelayAction, EntityDecl


class SemanticAnalyzer:
    ACTION_DOMAIN_MAP = {
        "ligar": ["luz", "interruptor", "alarme"],
        "desligar": ["luz", "interruptor", "alarme"],
    }

    TRIGGER_STATE_MAP = {
        "luz": ["on", "off"],
        "interruptor": ["on", "off"],
        "alarme": ["armed", "disarmed", "on", "off"],
        "sensor": ["on", "off", "armed", "disarmed", "charging", "idle", "running"],
    }

    DURATION_PATTERN = re.compile(r"^([1-9][0-9]*)(s|min|h)$")

    def __init__(self):
        self.symbol_table = {}
        self.entity_id_table = {}
        self.automation_names = set()
        self.errors = []

    def analyze(self, program: Program):
        self.build_symbol_table(program)
        self.check_automations(program)

        return self.errors

    def build_symbol_table(self, program: Program):
        for decl in program.declarations:
            self.check_entity_declaration(decl)

        for automation in program.automations:
            if automation.name in self.automation_names:
                self.errors.append(
                    f"Erro semântico: automação '{automation.name}' já foi declarada."
                )
            else:
                self.automation_names.add(automation.name)

    def check_entity_declaration(self, decl: EntityDecl):
        if decl.name in self.symbol_table:
            self.errors.append(
                f"Erro semântico: entidade '{decl.name}' já foi declarada."
            )
        else:
            self.symbol_table[decl.name] = decl

        if decl.entity_id in self.entity_id_table:
            self.errors.append(
                f"Erro semântico: identificador de entidade '{decl.entity_id}' já foi usado."
            )
        else:
            self.entity_id_table[decl.entity_id] = decl

    def check_automations(self, program: Program):
        for automation in program.automations:
            self.check_trigger(automation.trigger)

            for action in automation.actions:
                self.check_action(action)

    def check_trigger(self, trigger):
        entity = self.resolve_entity(trigger.entity)

        if entity is None:
            self.errors.append(
                f"Erro semântico: entidade '{trigger.entity}' usada no gatilho não foi declarada."
            )
            return

        self.check_trigger_value(trigger.value, entity)

    def check_trigger_value(self, value: str, entity: EntityDecl):
        normalized_value = self.normalize_value(value)
        allowed_states = self.TRIGGER_STATE_MAP.get(entity.domain, [])

        if normalized_value not in allowed_states:
            self.errors.append(
                f"Erro semântico: valor '{normalized_value}' não é válido para o domínio "
                f"'{entity.domain}' no gatilho da entidade '{entity.name}'."
            )

    def normalize_value(self, value: str) -> str:
        if value.startswith('"') and value.endswith('"'):
            return value[1:-1]
        return value

    def check_action(self, action):
        if isinstance(action, SimpleAction):
            self.check_simple_action(action)
        elif isinstance(action, DelayAction):
            self.check_delay(action)

    def check_simple_action(self, action: SimpleAction):
        entity = self.resolve_entity(action.entity)

        if entity is None:
            self.errors.append(
                f"Erro semântico: entidade '{action.entity}' usada na ação '{action.verb}' não foi declarada."
            )
            return

        allowed_domains = self.ACTION_DOMAIN_MAP.get(action.verb)
        if allowed_domains is None:
            self.errors.append(
                f"Erro semântico: ação desconhecida '{action.verb}'."
            )
            return

        if entity.domain not in allowed_domains:
            self.errors.append(
                f"Erro semântico: ação '{action.verb}' não pode ser aplicada à entidade "
                f"'{action.entity}', pois ela foi declarada como '{entity.domain}'."
            )

    def check_delay(self, action: DelayAction):
        match = self.DURATION_PATTERN.match(action.duration)
        if not match:
            self.errors.append(
                f"Erro semântico: duração inválida '{action.duration}'."
            )
            return

        value = int(match.group(1))
        if value <= 0:
            self.errors.append(
                f"Erro semântico: duração deve ser maior que zero, mas recebeu '{action.duration}'."
            )

    def resolve_entity(self, reference: str):
        if reference in self.symbol_table:
            return self.symbol_table[reference]
        return self.entity_id_table.get(reference)
