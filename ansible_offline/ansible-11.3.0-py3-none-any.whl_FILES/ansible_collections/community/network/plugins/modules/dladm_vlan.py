#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2016, Adam Števko <adam.stevko@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = '''
---
module: dladm_vlan
deprecated:
  removed_in: 6.0.0
  why: This collection and all content in it is unmaintained and deprecated.
  alternative: Unknown.
short_description: Manage VLAN interfaces on Solaris/illumos systems.
description:
    - Create or delete VLAN interfaces on Solaris/illumos systems.
author: Adam Števko (@xen0l)
options:
    name:
        description:
            - VLAN interface name.
        required: true
    link:
        description:
            - VLAN underlying link name.
        required: true
    temporary:
        description:
            - Specifies that the VLAN interface is temporary. Temporary VLANs
              do not persist across reboots.
        required: false
        default: false
        type: bool
    vlan_id:
        description:
            - VLAN ID value for VLAN interface.
        required: false
        default: false
        aliases: [ "vid" ]
    state:
        description:
            - Create or delete Solaris/illumos VNIC.
        required: false
        default: "present"
        choices: [ "present", "absent" ]
'''

EXAMPLES = '''
- name: Create 'vlan42' VLAN over 'bnx0' link
  community.network.dladm_vlan: name=vlan42 link=bnx0 vlan_id=42 state=present

- name: Remove 'vlan1337' VLAN interface
  community.network.dladm_vlan: name=vlan1337 state=absent
'''

RETURN = '''
name:
    description: VLAN name
    returned: always
    type: str
    sample: vlan42
state:
    description: state of the target
    returned: always
    type: str
    sample: present
temporary:
    description: specifies if operation will persist across reboots
    returned: always
    type: bool
    sample: true
link:
    description: VLAN's underlying link name
    returned: always
    type: str
    sample: e100g0
vlan_id:
    description: VLAN ID
    returned: always
    type: str
    sample: 42
'''

from ansible.module_utils.basic import AnsibleModule


class VLAN(object):

    def __init__(self, module):
        self.module = module

        self.name = module.params['name']
        self.link = module.params['link']
        self.vlan_id = module.params['vlan_id']
        self.temporary = module.params['temporary']
        self.state = module.params['state']

    def vlan_exists(self):
        cmd = [self.module.get_bin_path('dladm', True)]

        cmd.append('show-vlan')
        cmd.append(self.name)

        (rc, dummy, dummy) = self.module.run_command(cmd)

        if rc == 0:
            return True
        else:
            return False

    def create_vlan(self):
        cmd = [self.module.get_bin_path('dladm', True)]

        cmd.append('create-vlan')

        if self.temporary:
            cmd.append('-t')

        cmd.append('-l')
        cmd.append(self.link)
        cmd.append('-v')
        cmd.append(self.vlan_id)
        cmd.append(self.name)

        return self.module.run_command(cmd)

    def delete_vlan(self):
        cmd = [self.module.get_bin_path('dladm', True)]

        cmd.append('delete-vlan')

        if self.temporary:
            cmd.append('-t')
        cmd.append(self.name)

        return self.module.run_command(cmd)

    def is_valid_vlan_id(self):

        return 0 <= int(self.vlan_id) <= 4095


def main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True, type='str'),
            link=dict(default=None, type='str'),
            vlan_id=dict(default=0, aliases=['vid']),
            temporary=dict(default=False, type='bool'),
            state=dict(default='present', choices=['absent', 'present']),
        ),
        required_if=[
            ['state', 'present', ['vlan_id', 'link', 'name']],
        ],
        supports_check_mode=True
    )

    vlan = VLAN(module)

    rc = None
    out = ''
    err = ''
    result = {}
    result['name'] = vlan.name
    result['link'] = vlan.link
    result['state'] = vlan.state
    result['temporary'] = vlan.temporary

    if int(vlan.vlan_id) != 0:
        if not vlan.is_valid_vlan_id():
            module.fail_json(msg='Invalid VLAN id value',
                             name=vlan.name,
                             state=vlan.state,
                             link=vlan.link,
                             vlan_id=vlan.vlan_id)
        result['vlan_id'] = vlan.vlan_id

    if vlan.state == 'absent':
        if vlan.vlan_exists():
            if module.check_mode:
                module.exit_json(changed=True)
            (rc, out, err) = vlan.delete_vlan()
            if rc != 0:
                module.fail_json(name=vlan.name, msg=err, rc=rc)
    elif vlan.state == 'present':
        if not vlan.vlan_exists():
            if module.check_mode:
                module.exit_json(changed=True)
            (rc, out, err) = vlan.create_vlan()

        if rc is not None and rc != 0:
            module.fail_json(name=vlan.name, msg=err, rc=rc)

    if rc is None:
        result['changed'] = False
    else:
        result['changed'] = True

    if out:
        result['stdout'] = out
    if err:
        result['stderr'] = err

    module.exit_json(**result)


if __name__ == '__main__':
    main()
