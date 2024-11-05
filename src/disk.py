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
