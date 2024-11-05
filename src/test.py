from cpu import Cpu
from disk import Disk
import json
from dataclass_wizard import fromdict, fromlist
from eyes import Eyes

vector = """
{"fields":{"usage_idle":89.99999999999773,"usage_iowait":0,"usage_nice":0,"usage_system":0.2500000000000391,"usage_user":9.249999999999936},"name":"cpu","tags":{"cpu":"cpu-total","host":"hilbert"},"timestamp":1730802899}
"""

cpu = fromdict(Cpu, json.loads(vector))

print(
    f"time: {cpu.timestamp}\ncpu usage_idle: {cpu.fields.usage_idle}\ncpu usage_iowait: {cpu.fields.usage_iowait}"
)

with open("./telegraf.json", "r") as f:
    eyes = Eyes(f.readlines())
    eyes.print_stats()
