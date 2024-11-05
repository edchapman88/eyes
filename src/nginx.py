from dataclasses import dataclass
from typing import Any


@dataclass
class NginxFields:
    accepts: int
    active: int
    handled: int
    reading: int
    requests: int
    waiting: int
    writing: int


@dataclass
class Nginx:
    name: str
    fields: NginxFields
    timestamp: int
    tags: dict[str, Any]
