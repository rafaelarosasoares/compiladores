from ast_nodes import Program, SimpleAction, DelayAction


class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = {}
        self.errors = []

    def analyze(self, program: Program):
        self.build_symbol_table(program)
        self.check_automations(program)

        return self.errors

    def build_symbol_table(self, program: Program):
        for decl in program.declarations:
            if decl.name in self.symbol_table:
                self.errors.append(
                    f"Erro semântico: entidade '{decl.name}' já foi declarada."
                )
            else:
                self.symbol_table[decl.name] = decl

    def check_automations(self, program: Program):
        for automation in program.automations:
            self.check_trigger(automation.trigger)

            for action in automation.actions:
                self.check_action(action)

    def check_trigger(self, trigger):
        entity_name = trigger.entity

        if not self.entity_exists(entity_name):
            self.errors.append(
                f"Erro semântico: entidade '{entity_name}' usada no gatilho não foi declarada."
            )

    def check_action(self, action):
        if isinstance(action, SimpleAction):
            self.check_simple_action(action)

        elif isinstance(action, DelayAction):
            self.check_delay(action)

    def check_simple_action(self, action: SimpleAction):
        entity_name = action.entity

        if not self.entity_exists(entity_name):
            self.errors.append(
                f"Erro semântico: entidade '{entity_name}' usada na ação '{action.verb}' não foi declarada."
            )
            return

        entity_decl = self.symbol_table[entity_name]
        entity_domain = entity_decl.domain

        allowed_domains = {
            "ligar": ["luz", "interruptor", "alarme"],
            "desligar": ["luz", "interruptor", "alarme"],
        }

        if action.verb not in allowed_domains:
            self.errors.append(
                f"Erro semântico: ação desconhecida '{action.verb}'."
            )
            return

        if entity_domain not in allowed_domains[action.verb]:
            self.errors.append(
                f"Erro semântico: ação '{action.verb}' não pode ser aplicada à entidade "
                f"'{entity_name}', pois ela foi declarada como '{entity_domain}'."
            )

    def check_delay(self, action: DelayAction):
        duration = action.duration

        if duration.endswith("s"):
            value = int(duration[:-1])
        elif duration.endswith("min"):
            value = int(duration[:-3])
        elif duration.endswith("h"):
            value = int(duration[:-1])
        else:
            self.errors.append(
                f"Erro semântico: duração inválida '{duration}'."
            )
            return

        if value <= 0:
            self.errors.append(
                f"Erro semântico: duração deve ser maior que zero, mas recebeu '{duration}'."
            )

    def entity_exists(self, entity_name: str):
        return entity_name in self.symbol_table