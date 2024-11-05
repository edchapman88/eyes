## Input Streams
### CPU
#### Fields
**usage_user**: Percentage of CPU utilization that occurred while executing at the user level (application).
**usage_nice**: Percentage of CPU utilization that occurred while executing at the user level with nice priority.
**usage_system**: Percentage of CPU utilization that occurred while executing at the system level (kernel).
**usage_iowait**: Percentage of time that the CPU or CPUs were idle during which the system had an outstanding disk I/O request.
**usage_idle**: Percentage of time that the CPU or CPUs were idle and the system did not have an outstanding disk I/O request.

### Memory
#### Fields
**buffered**:
**cached**:
**swap_cached**:
**swap_free**:
**used_percent**:
**vmalloc_used**:


### Disk
#### Fields
**used_percent**: Calculated by doing used / (used + free), not used / total, which is how the unix df command does it.

### Nginx
#### Fields
**active**: The current number of active client connections including Waiting connections.
**accepts**: The total number of accepted client connections.
**handled**: The total number of handled connections. Generally, the parameter value is the same as accepts unless some resource limits have been reached (for example, the worker_connections limit).
**requests**: The total number of client requests.
**reading**: The current number of connections where nginx is reading the request header.
**writing**: The current number of connections where nginx is writing the response back to the client.
**waiting**: The current number of idle client connections waiting for a request.

### Netflow
#### Tags
**source**: IP of the exporter sending the data.
**version**: Flow protocol version.

#### Fields
**src**: IP address, address of the source of the packets.
**src_port**: `uint64`, source port.
**src_tos**:
**dst**: IP address, address of the destination of the packets.
**dst_port**: `uint64`, destination port.
**flow_start_ms**:
**flow_end_ms**:
**protocol**: `string`, Layer 4 protocol name.
**ip_version**:
**in_bytes**: `uint64`, number of incoming bytes.
**in_packets**: `uint64`, number of incoming packets.
**in_snmp**:
**out_snmp**:
**tcp_flags**: `string`, TCP flags for the flow.
