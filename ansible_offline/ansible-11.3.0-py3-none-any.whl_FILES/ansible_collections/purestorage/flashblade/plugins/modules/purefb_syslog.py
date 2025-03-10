#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2020, Simon Dodsley (simon@purestorage.com)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: purefb_syslog
version_added: '1.4.0'
short_description: Configure Pure Storage FlashBlade syslog settings
description:
- Configure syslog configuration for Pure Storage FlashBlades.
- Add or delete an individual syslog server to the existing
  list of serves.
author:
- Pure Storage Ansible Team (@sdodsley) <pure-ansible-team@purestorage.com>
options:
  name:
    description:
    - Unique identifier for the syslog server address
    type: str
    required: true
  state:
    description:
    - Create or delete syslog servers configuration
    default: present
    type: str
    choices: [ absent, present ]
  protocol:
    description:
    - Protocol which server uses
    type: str
    choices: [ tcp, tls, udp ]
  port:
    description:
    - Port at which the server is listening. If no port is specified
      the system will use 514
    type: str
  address:
    description:
    - Syslog server address.
      This field supports IPv4 or FQDN.
      An invalid IP addresses will cause the module to fail.
      No validation is performed for FQDNs.
    type: str
  services:
    description:
    - Syslog service type(s)
    type: list
    elements: str
    choices: [ management, data-audit ]
    default: management
extends_documentation_fragment:
- purestorage.flashblade.purestorage.fb
"""

EXAMPLES = r"""
- name: Delete exisitng syslog server entries
  purestorage.flashblade.purefb_syslog:
    name: syslog1
    state: absent
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

- name: Set array syslog servers
  purestorage.flashblade.purefb_syslog:
    state: present
    name: syslog1
    services:
    - data-audit
    address: syslog1.com
    protocol: udp
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641
"""

RETURN = r"""
"""


HAS_PURITY_FB = True
try:
    from purity_fb import SyslogServerPostOrPatch
except ImportError:
    HAS_PURITY_FB = False

HAS_PURESTORAGE = True
try:
    from pypureclient.flashblade import SyslogServerPost, SyslogServerPatch
except ImportError:
    HAS_PURESTORAGE = False


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.purestorage.flashblade.plugins.module_utils.purefb import (
    get_blade,
    get_system,
    purefb_argument_spec,
)


MIN_REQUIRED_API_VERSION = "1.10"
SYSLOG_SERVICES_API = "2.14"


def delete_syslog(module, blade):
    """Delete Syslog Server"""
    changed = False
    try:
        server = blade.syslog.list_syslog_servers(names=[module.params["name"]])
    except Exception:
        server = None

    if server:
        changed = True
        if not module.check_mode:
            try:
                blade.syslog.delete_syslog_servers(names=[module.params["name"]])
                changed = True
            except Exception:
                module.fail_json(
                    msg="Failed to remove syslog server: {0}".format(
                        module.params["name"]
                    )
                )

    module.exit_json(changed=changed)


def add_syslog(module, blade):
    """Add Syslog Server"""
    changed = False
    noport_address = module.params["protocol"] + "://" + module.params["address"]

    if module.params["port"]:
        full_address = noport_address + ":" + module.params["port"]
    else:
        full_address = noport_address
    api_version = blade.api_version.list_versions().versions

    changed = True
    if not module.check_mode:
        if SYSLOG_SERVICES_API in api_version:
            bladev2 = get_system(module)
            res = bladev2.post_syslog_servers(
                names=[module.params["name"]],
                syslog_server=SyslogServerPost(
                    uri=full_address, services=module.params["services"]
                ),
            )
            if res.status_code != 200:
                module.fail_json(
                    msg="Failed to add syslog server. Error: {0}".format(
                        res.errors[0].message
                    )
                )
        else:
            try:
                attr = SyslogServerPostOrPatch(uri=full_address)
                blade.syslog.create_syslog_servers(
                    syslog=attr, names=[module.params["name"]]
                )
            except Exception:
                module.fail_json(
                    msg="Failed to add syslog server {0} - {1}".format(
                        module.params["name"], full_address
                    )
                )

    module.exit_json(changed=changed)


def update_syslog(module, blade):
    """Update Syslog Server"""
    changed = False
    api_version = blade.api_version.list_versions().versions
    if SYSLOG_SERVICES_API not in api_version:
        module.exit_json(changed=changed)
    else:
        bladev2 = get_system(module)
    syslog_config = list(
        bladev2.get_syslog_servers(names=[module.params["name"]]).items
    )[0]
    noport_address = module.params["protocol"] + "://" + module.params["address"]

    if module.params["port"]:
        full_address = noport_address + ":" + module.params["port"]
    else:
        full_address = noport_address
    new_uri = syslog_config.uri
    if full_address != new_uri:
        changed = True
        new_uri = full_address
    new_services = syslog_config.services
    if module.params["services"] != new_services:
        changed = True
        new_services = module.params["services"]
    if changed and not module.check_mode:
        res = bladev2.patch_syslog_servers(
            names=[module.params["name"]],
            syslog_server=SyslogServerPatch(uri=new_uri, services=new_services),
        )
        if res.status_code != 200:
            module.fail_json(
                msg="Updating syslog server {0} failed. Error: {1}".format(
                    module.params["name"], res.errors[0].message
                )
            )
    module.exit_json(changed=changed)


def main():
    argument_spec = purefb_argument_spec()
    argument_spec.update(
        dict(
            address=dict(type="str"),
            protocol=dict(type="str", choices=["tcp", "tls", "udp"]),
            port=dict(type="str"),
            name=dict(type="str", required=True),
            services=dict(
                type="list",
                elements="str",
                choices=["management", "data-audit"],
                default=["management"],
            ),
            state=dict(type="str", default="present", choices=["absent", "present"]),
        )
    )

    required_if = [["state", "present", ["address", "protocol"]]]

    module = AnsibleModule(
        argument_spec, required_if=required_if, supports_check_mode=True
    )

    if not HAS_PURITY_FB:
        module.fail_json(msg="purity_fb sdk is required for this module")

    blade = get_blade(module)
    api_version = blade.api_version.list_versions().versions
    if MIN_REQUIRED_API_VERSION not in api_version:
        module.fail_json(msg="Purity//FB must be upgraded to support this module.")

    address_list = blade.syslog.list_syslog_servers()
    if len(address_list.items) == 3:
        module.fail_json(msg="Maximum number of syslog servers (3) already configured.")
    exists = False

    if not HAS_PURESTORAGE and SYSLOG_SERVICES_API in api_version:
        module.fail_json(msg="py-pure-client sdk is required for to set quotas")

    if address_list:
        for address in range(0, len(address_list.items)):
            if address_list.items[address].name == module.params["name"]:
                exists = True
                break
    if module.params["state"] == "absent":
        delete_syslog(module, blade)
    elif not exists:
        add_syslog(module, blade)
    else:
        update_syslog(module, blade)

    module.exit_json(changed=False)


if __name__ == "__main__":
    main()
