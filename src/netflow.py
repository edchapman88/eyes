from dataclasses import dataclass
from typing import Any


@dataclass
class NetflowFields:
    direction: str
    src: str
    src_port: str
    src_tos: str
    dst: str
    dst_port: int
    flow_start_ms: int
    flow_end_ms: int
    in_bytes: int
    in_packets: int
    in_snmp: int
    out_snmp: int
    ip_version: str
    protocol: str
    tcp_flags: str


@dataclass
class Netflow:
    name: str
    fields: NetflowFields
    timestamp: int
    tags: dict[str, Any]
