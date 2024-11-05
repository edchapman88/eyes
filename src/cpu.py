from dataclasses import dataclass
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
