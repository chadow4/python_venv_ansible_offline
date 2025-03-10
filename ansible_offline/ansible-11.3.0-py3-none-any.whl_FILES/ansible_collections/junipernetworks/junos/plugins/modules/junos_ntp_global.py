#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################
"""
The module file for junos_logging_global
"""

from __future__ import absolute_import, division, print_function


__metaclass__ = type

DOCUMENTATION = """
---
module: junos_ntp_global
version_added: 2.6.0
short_description: Manage NTP configuration on Junos devices.
description: This module manages NTP configuration on devices running Junos.
author: Rohit Thakur (@rohitthakur2590)
requirements:
  - ncclient (>=v0.6.4)
  - xmltodict (>=0.12.0)
notes:
  - This module requires the netconf system service be enabled on the device being managed.
  - This module works with connection C(netconf).
  - See L(the Junos OS Platform Options,https://docs.ansible.com/ansible/latest/network/user_guide/platform_junos.html).
  - Tested against JunOS v18.4R1
options:
  running_config:
    description:
    - This option is used only with state I(parsed).
    - The value of this option should be the output received from the Junos device
      by executing the command B(show system syslog).
    - The state I(parsed) reads the configuration from C(running_config) option and
      transforms it into Ansible structured data as per the resource module's argspec
      and the value is then returned in the I(parsed) key within the result.
    type: str
  config:
    description: A dictionary of NTP configuration.
    type: dict
    suboptions:
      authentication_keys:
        description: NTP authentication key.
        type: list
        elements: dict
        suboptions:
          id:
            description: Authentication key number.
            type: int
          algorithm:
            description: Authentication key type.
            type: str
            choices: ['md5', 'sha1', 'sha256']
          key:
            description: Authentication key value.
            type: str
      boot_server:
        description: Server to query during boot sequence.
        type: str
      broadcasts:
        description: Broadcast parameters.
        type: list
        elements: dict
        suboptions:
          address:
            description: Broadcast or multicast address to use.
            type: str
          key:
            description: Authentication key.
            type: str
          routing_instance_name:
            description: Routing intance name in which interface has address in broadcast subnet.
            type: str
          ttl:
            description: TTL value to transmit.
            type: int
          version:
            description: NTP version to use.
            type: int
      broadcast_client:
        description: Listen to broadcast NTP.
        type: bool
      interval_range:
        description: Set the minpoll and maxpoll interval range.
        type: int
      multicast_client:
        description: Listen to multicast NTP address.
        type: str
      peers:
        description: NTP Peers.
        type: list
        elements: dict
        suboptions: &peers
          peer:
            description: Hostname/IP address of the NTP Peer.
            type: str
          key_id:
            description: Key-id to be used while communicating.
            type: int
          prefer:
            description: Prefer this peer.
            type: bool
          version:
            description: NTP version to use.
            type: int
      servers:
        description: NTP Servers.
        type: list
        elements: dict
        suboptions:
          server:
            description: IP address or hostname of the server.
            type: str
          key_id:
            description: Key-id to be used while communicating.
            type: int
          prefer:
            description: Prefer this peer_serv.
            type: bool
          version:
            description: NTP version to use.
            type: int
          routing_instance:
            description: Routing instance through which server is reachable.
            type: str
      source_addresses:
        description: Source-Address parameters.
        type: list
        elements: dict
        suboptions:
          source_address:
            description: Use specified address as source address.
            type: str
          routing_instance:
            description: Routing intance name in which source address is defined.
            type: str
      threshold:
        description: Set the maximum threshold(sec) allowed for NTP adjustment.
        type: dict
        suboptions:
          value:
            description: The maximum value(sec) allowed for NTP adjustment.
            type: int
          action:
            description: Select actions for NTP abnormal adjustment.
            type: str
            choices: ['accept', 'reject']
      trusted_keys:
        description: List of trusted authentication keys.
        type: list
        elements: dict
        suboptions:
          key_id:
            description: Trusted-Key number.
            type: int
  state:
    description:
    - The state the configuration should be left in.
    - The states I(replaced) and I(overridden) have identical
      behaviour for this module.
    - Refer to examples for more details.
    type: str
    choices:
    - merged
    - replaced
    - deleted
    - overridden
    - parsed
    - gathered
    - rendered
    default: merged
"""
EXAMPLES = """
# Using merged
#
# Before state
# ------------
#
# vagrant@vsrx# show system ntp
#
# [edit]
# vagrant@vsrx# show routing-instances
# rt1 {
#     description rt1;
# }
# rt2 {
- name: Merge provided NTP configuration into running configuration.
  junipernetworks.junos.junos_ntp_global:
    config:
      boot_server: '78.46.194.186'
      broadcasts:
        - address: '172.16.255.255'
          key: '50'
          ttl: 200
          version: 3
          routing_instance_name: 'rt1'
        - address: '192.16.255.255'
          key: '50'
          ttl: 200
          version: 3
          routing_instance_name: 'rt2'
      broadcast_client: true
      interval_range: 2
      multicast_client: "224.0.0.1"
      peers:
        - peer: "78.44.194.186"
        - peer: "172.44.194.186"
          key_id: 10000
          prefer: true
          version: 3
      servers:
        - server: "48.46.194.186"
          key_id: 34
          prefer: true
          version: 2
          routing_instance: 'rt1'
        - server: "48.45.194.186"
          key_id: 34
          prefer: true
          version: 2
      source_addresses:
        - source_address: "172.45.194.186"
          routing_instance: 'rt1'
        - source_address: "171.45.194.186"
          routing_instance: 'rt2'
      threshold:
        value: 300
        action: "accept"
      trusted_keys:
        - key_id: 3000
        - key_id: 2000
    state: merged
#
# -------------------------
# Module Execution Result
# -------------------------
#     "after": {
#         "boot_server": "78.46.194.186",
#         "broadcast_client": true,
#         "broadcasts": [
#             {
#                 "address": "172.16.255.255",
#                 "key": "50",
#                 "routing_instance_name": "rt1",
#                 "ttl": 200,
#                 "version": 3
#             },
#             {
#                 "address": "192.16.255.255",
#                 "key": "50",
#                 "routing_instance_name": "rt2",
#                 "ttl": 200,
#                 "version": 3
#             }
#         ],
#         "interval_range": 2,
#         "multicast_client": "224.0.0.1",
#         "peers": [
#             {
#                 "peer": "78.44.194.186"
#             },
#             {
#                 "key_id": 10000,
#                 "peer": "172.44.194.186",
#                 "prefer": true,
#                 "version": 3
#             }
#         ],
#         "servers": [
#             {
#                 "key_id": 34,
#                 "prefer": true,
#                 "routing_instance": "rt1",
#                 "server": "48.46.194.186",
#                 "version": 2
#             },
#             {
#                 "key_id": 34,
#                 "prefer": true,
#                 "server": "48.45.194.186",
#                 "version": 2
#             }
#         ],
#         "source_addresses": [
#             {
#                 "routing_instance": "rt1",
#                 "source_address": "172.45.194.186"
#             },
#             {
#                 "routing_instance": "rt2",
#                 "source_address": "171.45.194.186"
#             }
#         ],
#         "threshold": {
#             "action": "accept",
#             "value": 300
#         },
#         "trusted_keys": [
#             {"key_id": 2000},
#             {"key_id": 3000}
#         ]
#     },
#     "before": {},
#     "changed": true,
#     "commands": [
#           "<nc:system xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\">"
#           "<nc:ntp><nc:boot-server>78.46.194.186</nc:boot-server><nc:broadcast>"
#           "<nc:name>172.16.255.255</nc:name><nc:key>50</nc:key><nc:routing-instance-name>rt1</nc:routing-instance-name>"
#           "<nc:ttl>200</nc:ttl><nc:version>3</nc:version></nc:broadcast><nc:broadcast><nc:name>192.16.255.255</nc:name>"
#           "<nc:key>50</nc:key><nc:routing-instance-name>rt2</nc:routing-instance-name><nc:ttl>200</nc:ttl>"
#           "<nc:version>3</nc:version></nc:broadcast><nc:broadcast-client/><nc:interval-range>2</nc:interval-range>"
#           "<nc:multicast-client>224.0.0.1</nc:multicast-client><nc:peer><nc:name>78.44.194.186</nc:name></nc:peer>"
#           "<nc:peer><nc:name>172.44.194.186</nc:name><nc:key>10000</nc:key><nc:prefer/><nc:version>3</nc:version>"
#           "</nc:peer><nc:server><nc:name>48.46.194.186</nc:name><nc:key>34</nc:key><nc:routing-instance>rt1</nc:routing-instance>"
#           "<nc:prefer/><nc:version>2</nc:version></nc:server><nc:server><nc:name>48.45.194.186</nc:name><nc:key>34</nc:key>"
#           "<nc:prefer/><nc:version>2</nc:version></nc:server><nc:source-address><nc:name>172.45.194.186</nc:name>"
#           "<nc:routing-instance>rt1</nc:routing-instance></nc:source-address><nc:source-address>"
#           "<nc:name>171.45.194.186</nc:name><nc:routing-instance>rt2</nc:routing-instance></nc:source-address>"
#           "<nc:threshold><nc:value>300</nc:value><nc:action>accept</nc:action></nc:threshold>"
#           "<nc:trusted-key>3000</nc:trusted-key><nc:trusted-key>2000</nc:trusted-key></nc:ntp></nc:system>"
#     ]
# After state
# -----------
#
# vagrant@vsrx# show system ntp
# boot-server 78.46.194.186;
# interval-range 2;
# peer 78.44.194.186;
# peer 172.44.194.186 key 10000 version 3 prefer; ## SECRET-DATA
# server 48.46.194.186 key 34 version 2 prefer routing-instance rt1; ## SECRET-DATA
# server 48.45.194.186 key 34 version 2 prefer; ## SECRET-DATA
# broadcast 172.16.255.255 routing-instance-name rt1 key 50 version 3 ttl 200;
# broadcast 192.16.255.255 routing-instance-name rt2 key 50 version 3 ttl 200;
# broadcast-client;
# multicast-client 224.0.0.1;
# trusted-key [ 3000 2000 ];
# threshold 300 action accept;
# source-address 172.45.194.186 routing-instance rt1;
# source-address 171.45.194.186 routing-instance rt2;
#
#
# Using Replaced
# Before state
# ------------
#
# vagrant@vsrx# show system ntp
# boot-server 78.46.194.186;
# interval-range 2;
# peer 78.44.194.186;
# peer 172.44.194.186 key 10000 version 3 prefer; ## SECRET-DATA
# server 48.46.194.186 key 34 version 2 prefer routing-instance rt1; ## SECRET-DATA
# server 48.45.194.186 key 34 version 2 prefer; ## SECRET-DATA
# broadcast 172.16.255.255 routing-instance-name rt1 key 50 version 3 ttl 200;
# broadcast 192.16.255.255 routing-instance-name rt2 key 50 version 3 ttl 200;
# broadcast-client;
# multicast-client 224.0.0.1;
# trusted-key [ 3000 2000 ];
# threshold 300 action accept;
# source-address 172.45.194.186 routing-instance rt1;
# source-address 171.45.194.186 routing-instance rt2;

- name: Replaced running ntp global configuration with provided configuration
  junipernetworks.junos.junos_ntp_global:
    config:
      authentication_keys:
        - id: 2
          algorithm: 'md5'
          key: 'asdfghd'
        - id: 5
          algorithm: 'sha1'
          key: 'aasdad'
      servers:
        - server: "48.46.194.186"
          key_id: 34
          prefer: true
          version: 2
          routing_instance: 'rt1'
        - server: "48.45.194.186"
          key_id: 34
          prefer: true
          version: 2
    state: replaced
#
# -------------------------
# Module Execution Result
# -------------------------
#     "after": {
#         "authentication_keys": [
#             {
#                 "algorithm": "md5",
#                 "id": 2,
#                 "key": "$9$03aAB1hreW7NbO1rvMLVbgoJ"
#             },
#             {
#                 "algorithm": "sha1",
#                 "id": 5,
#                 "key": "$9$DXiHmf5F/A0ZUjq.P3n"
#             }
#         ],
#         "servers": [
#             {
#                 "key_id": 34,
#                 "prefer": true,
#                 "routing_instance": "rt1",
#                 "server": "48.46.194.186",
#                 "version": 2
#             },
#             {
#                 "key_id": 34,
#                 "prefer": true,
#                 "server": "48.45.194.186",
#                 "version": 2
#             }
#         ]
#     },
#     "before": {
#         "boot_server": "78.46.194.186",
#         "broadcast_client": true,
#         "broadcasts": [
#             {
#                 "address": "172.16.255.255",
#                 "key": "50",
#                 "routing_instance_name": "rt1",
#                 "ttl": 200,
#                 "version": 3
#             },
#             {
#                 "address": "192.16.255.255",
#                 "key": "50",
#                 "routing_instance_name": "rt2",
#                 "ttl": 200,
#                 "version": 3
#             }
#         ],
#         "interval_range": 2,
#         "multicast_client": "224.0.0.1",
#         "peers": [
#             {
#                 "peer": "78.44.194.186"
#             },
#             {
#                 "key_id": 10000,
#                 "peer": "172.44.194.186",
#                 "prefer": true,
#                 "version": 3
#             }
#         ],
#         "servers": [
#             {
#                 "key_id": 34,
#                 "prefer": true,
#                 "routing_instance": "rt1",
#                 "server": "48.46.194.186",
#                 "version": 2
#             },
#             {
#                 "key_id": 34,
#                 "prefer": true,
#                 "server": "48.45.194.186",
#                 "version": 2
#             }
#         ],
#         "source_addresses": [
#             {
#                 "routing_instance": "rt1",
#                 "source_address": "172.45.194.186"
#             },
#             {
#                 "routing_instance": "rt2",
#                 "source_address": "171.45.194.186"
#             }
#         ],
#         "threshold": {
#             "action": "accept",
#             "value": 300
#         },
#         "trusted_keys": [
#             {"key_id": 2000},
#             {"key_id": 3000}
#         ]
#     },
#     "changed": true,
#     "commands": [
#             "<nc:system xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\">
#             "<nc:ntp delete=\"delete\"/><nc:ntp><nc:authentication-key><nc:name>2</nc:name><nc:type>md5</nc:type>
#             "<nc:value>asdfghd</nc:value></nc:authentication-key><nc:authentication-key><nc:name>5</nc:name>
#             "<nc:type>sha1</nc:type><nc:value>aasdad</nc:value></nc:authentication-key><nc:server>
#             "<nc:name>48.46.194.186</nc:name><nc:key>34</nc:key><nc:routing-instance>rt1</nc:routing-instance>
#             "<nc:prefer/><nc:version>2</nc:version></nc:server><nc:server><nc:name>48.45.194.186</nc:name>
#             "<nc:key>34</nc:key><nc:prefer/><nc:version>2</nc:version></nc:server></nc:ntp></nc:system>"
#     ]
# After state
# -----------
#
# vagrant@vsrx# show system ntp
# authentication-key 2 type md5 value "$9$03aAB1hreW7NbO1rvMLVbgoJ"; ## SECRET-DATA
# authentication-key 5 type sha1 value "$9$DXiHmf5F/A0ZUjq.P3n"; ## SECRET-DATA
# server 48.46.194.186 key 34 version 2 prefer routing-instance rt1; ## SECRET-DATA
# server 48.45.194.186 key 34 version 2 prefer; ## SECRET-DATA

# Using overridden
#
# Before state
# ------------
#
# vagrant@vsrx# show system ntp
# boot-server 78.46.194.186;
# interval-range 2;
# peer 78.44.194.186;
# peer 172.44.194.186 key 10000 version 3 prefer; ## SECRET-DATA
# server 48.46.194.186 key 34 version 2 prefer routing-instance rt1; ## SECRET-DATA
# server 48.45.194.186 key 34 version 2 prefer; ## SECRET-DATA
# broadcast 172.16.255.255 routing-instance-name rt1 key 50 version 3 ttl 200;
# broadcast 192.16.255.255 routing-instance-name rt2 key 50 version 3 ttl 200;
# broadcast-client;
# multicast-client 224.0.0.1;
# trusted-key [ 3000 2000 ];
# threshold 300 action accept;
# source-address 172.45.194.186 routing-instance rt1;
# source-address 171.45.194.186 routing-instance rt2;

- name: Override running ntp global configuration with provided configuration
  junipernetworks.junos.junos_ntp_global:
    config:
      authentication_keys:
        - id: 2
          algorithm: 'md5'
          key: 'asdfghd'
        - id: 5
          algorithm: 'sha1'
          key: 'aasdad'
      servers:
        - server: "48.46.194.186"
          key_id: 34
          prefer: true
          version: 2
          routing_instance: 'rt1'
        - server: "48.45.194.186"
          key_id: 34
          prefer: true
          version: 2
    state: overridden
#
# -------------------------
# Module Execution Result
# -------------------------
#     "after": {
#         "authentication_keys": [
#             {
#                 "algorithm": "md5",
#                 "id": 2,
#                 "key": "$9$03aAB1hreW7NbO1rvMLVbgoJ"
#             },
#             {
#                 "algorithm": "sha1",
#                 "id": 5,
#                 "key": "$9$DXiHmf5F/A0ZUjq.P3n"
#             }
#         ],
#         "servers": [
#             {
#                 "key_id": 34,
#                 "prefer": true,
#                 "routing_instance": "rt1",
#                 "server": "48.46.194.186",
#                 "version": 2
#             },
#             {
#                 "key_id": 34,
#                 "prefer": true,
#                 "server": "48.45.194.186",
#                 "version": 2
#             }
#         ]
#     },
#     "before": {
#         "boot_server": "78.46.194.186",
#         "broadcast_client": true,
#         "broadcasts": [
#             {
#                 "address": "172.16.255.255",
#                 "key": "50",
#                 "routing_instance_name": "rt1",
#                 "ttl": 200,
#                 "version": 3
#             },
#             {
#                 "address": "192.16.255.255",
#                 "key": "50",
#                 "routing_instance_name": "rt2",
#                 "ttl": 200,
#                 "version": 3
#             }
#         ],
#         "interval_range": 2,
#         "multicast_client": "224.0.0.1",
#         "peers": [
#             {
#                 "peer": "78.44.194.186"
#             },
#             {
#                 "key_id": 10000,
#                 "peer": "172.44.194.186",
#                 "prefer": true,
#                 "version": 3
#             }
#         ],
#         "servers": [
#             {
#                 "key_id": 34,
#                 "prefer": true,
#                 "routing_instance": "rt1",
#                 "server": "48.46.194.186",
#                 "version": 2
#             },
#             {
#                 "key_id": 34,
#                 "prefer": true,
#                 "server": "48.45.194.186",
#                 "version": 2
#             }
#         ],
#         "source_addresses": [
#             {
#                 "routing_instance": "rt1",
#                 "source_address": "172.45.194.186"
#             },
#             {
#                 "routing_instance": "rt2",
#                 "source_address": "171.45.194.186"
#             }
#         ],
#         "threshold": {
#             "action": "accept",
#             "value": 300
#         },
#         "trusted_keys": [
#             {"key_id": 2000},
#             {"key_id": 3000}
#         ]
#     },
#     "changed": true,
#     "commands": [
#             "<nc:system xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\">
#             "<nc:ntp delete=\"delete\"/><nc:ntp><nc:authentication-key><nc:name>2</nc:name><nc:type>md5</nc:type>
#             "<nc:value>asdfghd</nc:value></nc:authentication-key><nc:authentication-key><nc:name>5</nc:name>
#             "<nc:type>sha1</nc:type><nc:value>aasdad</nc:value></nc:authentication-key><nc:server>
#             "<nc:name>48.46.194.186</nc:name><nc:key>34</nc:key><nc:routing-instance>rt1</nc:routing-instance>
#             "<nc:prefer/><nc:version>2</nc:version></nc:server><nc:server><nc:name>48.45.194.186</nc:name>
#             "<nc:key>34</nc:key><nc:prefer/><nc:version>2</nc:version></nc:server></nc:ntp></nc:system>"
#     ]
# After state
# -----------
#
# vagrant@vsrx# show system ntp
# authentication-key 2 type md5 value "$9$03aAB1hreW7NbO1rvMLVbgoJ"; ## SECRET-DATA
# authentication-key 5 type sha1 value "$9$DXiHmf5F/A0ZUjq.P3n"; ## SECRET-DATA
# server 48.46.194.186 key 34 version 2 prefer routing-instance rt1; ## SECRET-DATA
# server 48.45.194.186 key 34 version 2 prefer; ## SECRET-DATA
#
# Using deleted
#
# Before state
# ------------
#
# vagrant@vsrx# show system ntp
# authentication-key 2 type md5 value "$9$03aAB1hreW7NbO1rvMLVbgoJ"; ## SECRET-DATA
# authentication-key 5 type sha1 value "$9$DXiHmf5F/A0ZUjq.P3n"; ## SECRET-DATA
# server 48.46.194.186 key 34 version 2 prefer routing-instance rt1; ## SECRET-DATA
# server 48.45.194.186 key 34 version 2 prefer; ## SECRET-DATA
#
- name: Delete running NTP global configuration
  junipernetworks.junos.junos_ntp_global:
    config:
    state: deleted
#
# -------------------------
# Module Execution Result
# -------------------------
#     "after": {},
#     "before": {
#         "authentication_keys": [
#             {
#                 "algorithm": "md5",
#                 "id": 2,
#                 "key": "$9$03aAB1hreW7NbO1rvMLVbgoJ"
#             },
#             {
#                 "algorithm": "sha1",
#                 "id": 5,
#                 "key": "$9$DXiHmf5F/A0ZUjq.P3n"
#             }
#         ],
#         "servers": [
#             {
#                 "key_id": 34,
#                 "prefer": true,
#                 "routing_instance": "rt1",
#                 "server": "48.46.194.186",
#                 "version": 2
#             },
#             {
#                 "key_id": 34,
#                 "prefer": true,
#                 "server": "48.45.194.186",
#                 "version": 2
#             }
#         ]
#     },
#     "changed": true,
#     "commands": [
#               "<nc:system xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\">"
#               "<nc:ntp delete=\"delete\"/></nc:system>"
#     ]
# After state
# -----------
#
# vagrant@vsrx# show system ntp
#
# [edit]
# Using gathered
#
# Before state
# ------------
#
# vagrant@vsrx# show system ntp
# boot-server 78.46.194.186;
# interval-range 2;
# peer 78.44.194.186;
# peer 172.44.194.186 key 10000 version 3 prefer; ## SECRET-DATA
# server 48.46.194.186 key 34 version 2 prefer routing-instance rt1; ## SECRET-DATA
# server 48.45.194.186 key 34 version 2 prefer; ## SECRET-DATA
# broadcast 172.16.255.255 routing-instance-name rt1 key 50 version 3 ttl 200;
# broadcast 192.16.255.255 routing-instance-name rt2 key 50 version 3 ttl 200;
# broadcast-client;
# multicast-client 224.0.0.1;
# trusted-key [ 3000 2000 ];
# threshold 300 action accept;
# source-address 172.45.194.186 routing-instance rt1;
# source-address 171.45.194.186 routing-instance rt2;
- name: Gather running NTP global configuration
  junipernetworks.junos.junos_ntp_global:
    state: gathered
#
# -------------------------
# Module Execution Result
# -------------------------
#     "gathered": {
#         "boot_server": "78.46.194.186",
#         "broadcast_client": true,
#         "broadcasts": [
#             {
#                 "address": "172.16.255.255",
#                 "key": "50",
#                 "routing_instance_name": "rt1",
#                 "ttl": 200,
#                 "version": 3
#             },
#             {
#                 "address": "192.16.255.255",
#                 "key": "50",
#                 "routing_instance_name": "rt2",
#                 "ttl": 200,
#                 "version": 3
#             }
#         ],
#         "interval_range": 2,
#         "multicast_client": "224.0.0.1",
#         "peers": [
#             {
#                 "peer": "78.44.194.186"
#             },
#             {
#                 "key_id": 10000,
#                 "peer": "172.44.194.186",
#                 "prefer": true,
#                 "version": 3
#             }
#         ],
#         "servers": [
#             {
#                 "key_id": 34,
#                 "prefer": true,
#                 "routing_instance": "rt1",
#                 "server": "48.46.194.186",
#                 "version": 2
#             },
#             {
#                 "key_id": 34,
#                 "prefer": true,
#                 "server": "48.45.194.186",
#                 "version": 2
#             }
#         ],
#         "source_addresses": [
#             {
#                 "routing_instance": "rt1",
#                 "source_address": "172.45.194.186"
#             },
#             {
#                 "routing_instance": "rt2",
#                 "source_address": "171.45.194.186"
#             }
#         ],
#         "threshold": {
#             "action": "accept",
#             "value": 300
#         },
#         "trusted_keys": [
#             {"key_id": 2000},
#             {"key_id": 3000}
#         ]
#     },
#     "changed": false,
# Using rendered
#
# Before state
# ------------
#
- name: Render xml for provided facts.
  junipernetworks.junos.junos_ntp_global:
    config:
      boot_server: '78.46.194.186'
      broadcasts:
        - address: '172.16.255.255'
          key: '50'
          ttl: 200
          version: 3
          routing_instance_name: 'rt1'
        - address: '192.16.255.255'
          key: '50'
          ttl: 200
          version: 3
          routing_instance_name: 'rt2'
      broadcast_client: true
      interval_range: 2
      multicast_client: "224.0.0.1"
      peers:
        - peer: "78.44.194.186"
        - peer: "172.44.194.186"
          key_id: 10000
          prefer: true
          version: 3
      servers:
        - server: "48.46.194.186"
          key_id: 34
          prefer: true
          version: 2
          routing_instance: 'rt1'
        - server: "48.45.194.186"
          key_id: 34
          prefer: true
          version: 2
      source_addresses:
        - source_address: "172.45.194.186"
          routing_instance: 'rt1'
        - source_address: "171.45.194.186"
          routing_instance: 'rt2'
      threshold:
        value: 300
        action: "accept"
      trusted_keys:
        - 3000
        - 2000
    state: rendered
#
# -------------------------
# Module Execution Result
# -------------------------
#     "rendered": [
#           "<nc:system xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\">"
#           "<nc:ntp><nc:boot-server>78.46.194.186</nc:boot-server><nc:broadcast><nc:name>172.16.255.255</nc:name>"
#           "<nc:key>50</nc:key><nc:routing-instance-name>rt1</nc:routing-instance-name><nc:ttl>200</nc:ttl>"
#           "<nc:version>3</nc:version></nc:broadcast><nc:broadcast><nc:name>192.16.255.255</nc:name>"
#           "<nc:key>50</nc:key><nc:routing-instance-name>rt2</nc:routing-instance-name>"
#           "<nc:ttl>200</nc:ttl><nc:version>3</nc:version></nc:broadcast><nc:broadcast-client/>"
#           "<nc:interval-range>2</nc:interval-range><nc:multicast-client>224.0.0.1</nc:multicast-client><nc:peer>"
#           "<nc:name>78.44.194.186</nc:name></nc:peer><nc:peer><nc:name>172.44.194.186</nc:name>"
#           "<nc:key>10000</nc:key><nc:prefer/><nc:version>3</nc:version></nc:peer><nc:server>"
#           "<nc:name>48.46.194.186</nc:name><nc:key>34</nc:key><nc:routing-instance>rt1</nc:routing-instance>"
#           "<nc:prefer/><nc:version>2</nc:version></nc:server><nc:server><nc:name>48.45.194.186</nc:name>"
#           "<nc:key>34</nc:key><nc:prefer/><nc:version>2</nc:version></nc:server><nc:source-address>"
#           "<nc:name>172.45.194.186</nc:name><nc:routing-instance>rt1</nc:routing-instance></nc:source-address>"
#           "<nc:source-address><nc:name>171.45.194.186</nc:name><nc:routing-instance>rt2</nc:routing-instance>"
#           "</nc:source-address><nc:threshold><nc:value>300</nc:value><nc:action>accept</nc:action></nc:threshold>"
#           "<nc:trusted-key>3000</nc:trusted-key><nc:trusted-key>2000</nc:trusted-key></nc:ntp></nc:system>"
#     ]
#
# Using parsed
# parsed.cfg
# ------------
# <?xml version="1.0" encoding="UTF-8"?>
# <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
#     <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
#         <version>18.4R1-S2.4</version>
#         <system xmlns="http://yang.juniper.net/junos-es/conf/system">
#            <ntp>
#               <authentication-key>
#                  <name>2</name>
#                  <type>md5</type>
#                  <value>$9$GxDjqfT3CA0UjfzF6u0RhS</value>
#               </authentication-key>
#               <authentication-key>
#                  <name>5</name>
#                  <type>sha1</type>
#                  <value>$9$ZsUDk.mT3/toJGiHqQz</value>
#               </authentication-key>
#           </ntp>
#     </system>
#     </configuration>
# </rpc-reply>
#
- name: Parse NTP global running config
  junipernetworks.junos.junos_ntp_global:
    running_config: "{{ lookup('file', './parsed.cfg') }}"
    state: parsed
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "parsed":  {
#         "authentication_keys": [
#             {
#                 "algorithm": "md5",
#                 "id": 2,
#                 "key": "$9$GxDjqfT3CA0UjfzF6u0RhS"
#             },
#             {
#                 "algorithm": "sha1",
#                 "id": 5,
#                 "key": "$9$ZsUDk.mT3/toJGiHqQz"
#             }
#         ]
#     }
#
#
"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
  type: dict
after:
  description: The resulting configuration model invocation.
  returned: when changed
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
  type: dict
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ["<nc:name>78.44.194.186</nc:name></nc:peer><nc:peer><nc:name>172.44.194.186</nc:name>",
           'xml 2', 'xml 3']
"""


from ansible.module_utils.basic import AnsibleModule

from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.argspec.ntp_global.ntp_global import (
    Ntp_globalArgs,
)
from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.config.ntp_global.ntp_global import (
    Ntp_global,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    required_if = [
        ("state", "merged", ("config",)),
        ("state", "replaced", ("config",)),
        ("state", "overridden", ("config",)),
        ("state", "rendered", ("config",)),
        ("state", "parsed", ("running_config",)),
    ]
    module = AnsibleModule(
        argument_spec=Ntp_globalArgs.argument_spec,
        required_if=required_if,
        supports_check_mode=True,
    )

    result = Ntp_global(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
