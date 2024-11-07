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

    def __getitem__(self, key):
        match key:
            case 'buffered':
                return self.fields.buffered
            case 'cached':
                return self.fields.cached
            case 'swap_cached':
                return self.fields.swap_cached
            case 'swap_free':
                return self.fields.swap_free
            case 'used_percent':
                return self.fields.used_percent
            case 'vmalloc_used':
                return self.fields.vmalloc_used
