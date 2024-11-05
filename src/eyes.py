import json
from dataclass_wizard import fromdict
from cpu import *
from mem import *
from disk import *
from nginx import *
from netflow import *
from enum import Enum


class StreamId(Enum):
    CPU = ('cpu', Cpu)
    MEM = ('mem', Mem)
    DISK = ('disk', Disk)
    NGINX = ('nginx', Nginx)
    NETFLOW = ('netflow', Netflow)

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
        streams = {}
        for log in logs:
            raw_obj = json.loads(log)
            id = StreamId.parse(raw_obj['name'])
            stream = streams.get(id.name, [])
            stream.append(fromdict(id.value[1], raw_obj))
            streams[id.name] = stream
        self.streams = streams

    def print_stats(self):
        print('\n::: log streams parsed from file :::')
        for k, v in self.streams.items():
            print(f'{k}: {len(v)} log events')
