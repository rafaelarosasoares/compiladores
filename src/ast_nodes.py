from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Program:
    declarations: List["EntityDecl"]
    automations: List["Automation"]


@dataclass
class EntityDecl:
    domain: str
    name: str
    entity_id: str
    line: int = 0


@dataclass
class Automation:
    name: str
    trigger: "StateTrigger"
    condition: Optional["ConditionExpression"]
    actions: List["Action"]
    mode: Optional[str]
    line: int = 0


@dataclass
class StateTrigger:
    entity: str
    value: str
    line: int = 0


@dataclass
class ConditionExpression:
    terms: List["ConditionTerm"]
    operators: List[str]
    line: int = 0


@dataclass
class ConditionTerm:
    entity: str
    value: str
    negated: bool = False
    line: int = 0


class Action:
    pass


@dataclass
class SimpleAction(Action):
    verb: str
    entity: str
    line: int = 0


@dataclass
class DelayAction(Action):
    duration: str
    line: int = 0
