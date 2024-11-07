import json
from dataclass_wizard import fromdict
from cpu import *
from mem import *
from disk import *
from nginx import *
from netflow import *
from enum import Enum


class StreamId(Enum):
    CPU = 'cpu'
    MEM = 'mem'
    DISK = 'disk'
    NGINX = 'nginx'
    NETFLOW = 'netflow'

    @staticmethod
    def parse(val):
        match val.upper():
            case StreamId.CPU.name:
                return StreamId.CPU
            case StreamId.MEM.name:
                return StreamId.MEM
            case StreamId.DISK.name:
                return StreamId.DISK
            case StreamId.NGINX.name:
                return StreamId.NGINX
            case StreamId.NETFLOW.name:
                return StreamId.NETFLOW
            case _:
                raise Exception(f'Stream: {val} is unimplemented')


class Eyes:
    def __init__(self, logs: list[str]):
        self.cpu: list[Cpu] = []
        self.mem: list[Mem] = []
        self.disk: list[Disk] = []
        self.nginx: list[Nginx] = []
        self.netflow: list[Netflow] = []

        for log in logs:
            raw_obj = json.loads(log)
            id = StreamId.parse(raw_obj['name'])
            match id:
                case StreamId.CPU:
                    self.cpu.append(fromdict(Cpu, raw_obj))
                case StreamId.MEM:
                    self.mem.append(fromdict(Mem, raw_obj))
                case StreamId.DISK:
                    self.disk.append(fromdict(Disk, raw_obj))
                case StreamId.NGINX:
                    self.nginx.append(fromdict(Nginx, raw_obj))
                case StreamId.NETFLOW:
                    self.netflow.append(fromdict(Netflow, raw_obj))

    def __getitem__(self, key):
        match key:
            case 'cpu':
                return self.cpu
            case 'disk':
                return self.disk
            case 'mem':
                return self.mem
            case 'nginx':
                return self.nginx
            case 'netflow':
                return self.netflow

    def print_stats(self):
        print('\n::: log streams parsed from file :::')
        print(f'cpu: {len(self.cpu)} log events')
        print(f'disk: {len(self.disk)} log events')
        print(f'mem: {len(self.mem)} log events')
        print(f'nginx: {len(self.nginx)} log events')
        print(f'netflow: {len(self.netflow)} log events')
