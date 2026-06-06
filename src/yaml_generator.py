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

        # Actions
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

        # Mode
        if automation.mode:
            lines.append(f"mode: {automation.mode}")

        return "\n".join(lines)

    def resolve_entity(self, reference: str):
        if reference in self.symbol_table:
            return self.symbol_table[reference]
        return self.entity_id_table[reference]
