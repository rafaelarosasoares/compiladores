from ast_nodes import SimpleAction, DelayAction


def clean_value(value: str) -> str:
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]
    return value


class YamlGenerator:

    DOMAIN_MAP = {
        "luz": "light",
        "interruptor": "switch",
        "alarme": "alarm_control_panel",
    }

    def __init__(self, symbol_table, entity_id_table=None):
        self.symbol_table = symbol_table
        self.entity_id_table = entity_id_table or {}

    def generate(self, automation):

        lines = []

        # Alias
        lines.append(f'alias: "{automation.name}"')
        lines.append("")

        # Trigger
        trigger_entity = self.resolve_entity(automation.trigger.entity)

        lines.append("trigger:")
        lines.append("  - platform: state")
        lines.append(f"    entity_id: {trigger_entity.entity_id}")
        lines.append(f'    to: "{clean_value(automation.trigger.value)}"')
        lines.append("")

        # Condições
        if automation.condition is not None:
            lines.append("condition:")
            self.add_condition_expression(lines, automation.condition, "  ")
            lines.append("")

        # Ações
        lines.append("action:")

        for action in automation.actions:

            if isinstance(action, SimpleAction):

                entity = self.resolve_entity(action.entity)

                domain = self.DOMAIN_MAP.get(
                    entity.domain,
                    entity.domain
                )

                if action.verb == "ligar":
                    service = f"{domain}.turn_on"

                elif action.verb == "desligar":
                    service = f"{domain}.turn_off"

                lines.append(f"  - service: {service}")
                lines.append("    target:")
                lines.append(
                    f"      entity_id: {entity.entity_id}"
                )

            elif isinstance(action, DelayAction):

                lines.append(
                    f'  - delay: "{action.duration}"'
                )

        lines.append("")

        if automation.mode:
            lines.append(f"mode: {automation.mode}")

        return "\n".join(lines)

    def resolve_entity(self, reference: str):
        if reference in self.symbol_table:
            return self.symbol_table[reference]
        return self.entity_id_table[reference]

    def add_condition_expression(self, lines, condition, indent: str):
        if not condition.operators or set(condition.operators) == {"e"}:
            for term in condition.terms:
                self.add_condition_term(lines, term, indent + "- ")
            return

        lines.append(f"{indent}- condition: or")
        lines.append(f"{indent}  conditions:")

        for term in condition.terms:
            self.add_condition_term(lines, term, indent + "    - ")

    def add_condition_term(self, lines, term, item_prefix: str):
        if term.negated:
            lines.append(f"{item_prefix}condition: not")
            nested_indent = " " * (len(item_prefix) - 2)
            lines.append(f"{nested_indent}  conditions:")
            self.add_state_condition(lines, term, nested_indent + "    - ")
            return

        self.add_state_condition(lines, term, item_prefix)

    def add_state_condition(self, lines, term, item_prefix: str):
        entity = self.resolve_entity(term.entity)
        nested_indent = " " * len(item_prefix)

        lines.append(f"{item_prefix}condition: state")
        lines.append(f"{nested_indent}entity_id: {entity.entity_id}")
        lines.append(f'{nested_indent}state: "{clean_value(term.value)}"')
