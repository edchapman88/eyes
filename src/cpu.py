from dataclasses import dataclass, fields
from typing import Any


@dataclass
class CpuFields:
    usage_idle: float
    usage_iowait: float
    usage_nice: float
    usage_system: float
    usage_user: float


@dataclass
class Cpu:
    name: str
    fields: CpuFields
    timestamp: int
    tags: dict[str, Any]

    def __getitem__(self, key):
        match key:
            case 'usage_idle':
                return self.fields.usage_idle
            case 'usage_iowait':
                return self.fields.usage_iowait
            case 'usage_nice':
                return self.fields.usage_nice
            case 'usage_system':
                return self.fields.usage_system
            case 'usage_user':
                return self.fields.usage_user
