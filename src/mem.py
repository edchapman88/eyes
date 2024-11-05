from dataclasses import dataclass
from typing import Any


@dataclass
class MemFields:
    buffered: int
    cached: int
    swap_cached: int
    swap_free: int
    used_percent: float
    vmalloc_used: int


@dataclass
class Mem:
    name: str
    fields: MemFields
    timestamp: int
    tags: dict[str, Any]
