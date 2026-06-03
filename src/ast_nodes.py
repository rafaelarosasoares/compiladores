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


@dataclass
class Automation:
    name: str
    trigger: "StateTrigger"
    actions: List["Action"]
    mode: Optional[str]


@dataclass
class StateTrigger:
    entity: str
    value: str


class Action:
    pass


@dataclass
class SimpleAction(Action):
    verb: str
    entity: str


@dataclass
class DelayAction(Action):
    duration: str