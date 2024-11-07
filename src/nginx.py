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

    def __getitem__(self, key):
        match key:
            case 'accepts':
                return self.fields.accepts
            case 'active':
                return self.fields.active
            case 'handled':
                return self.fields.handled
            case 'reading':
                return self.fields.reading
            case 'requests':
                return self.fields.requests
            case 'waiting':
                return self.fields.waiting
            case 'writing':
                return self.fields.writing
