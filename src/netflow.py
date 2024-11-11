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

    def __getitem__(self, key):
        match key:
            case 'src':
                return self.fields.src
            case 'dst':
                return self.fields.dst
            case 'flow_start_ms':
                return self.fields.flow_start_ms
            case 'flow_end_ms':
                return self.fields.flow_end_ms
            case k:
                raise Exception(f'getter for {k} field needs implementing')
