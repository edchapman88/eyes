from dataclasses import dataclass
from typing import Any


@dataclass
class DiskFields:
    used_percent: float


@dataclass
class Disk:
    name: str
    fields: DiskFields
    timestamp: int
    tags: dict[str, Any]

    def __getitem__(self, key):
        match key:
            case 'used_percent':
                return self.fields.used_percent
