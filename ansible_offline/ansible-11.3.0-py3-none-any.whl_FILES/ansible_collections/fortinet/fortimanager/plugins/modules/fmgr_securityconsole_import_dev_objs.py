#!/usr/bin/python
from __future__ import absolute_import, division, print_function
# Copyright 2019-2024 Fortinet, Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

__metaclass__ = type

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.1'}

DOCUMENTATION = '''
---
module: fmgr_securityconsole_import_dev_objs
short_description: Import objects from device to ADOM, or from ADOM to Global.
description:
    - This module is able to configure a FortiManager device.
    - Examples include all parameters and values which need to be adjusted to data sources before usage.

version_added: "2.0.0"
author:
    - Xinwei Du (@dux-fortinet)
    - Xing Li (@lix-fortinet)
    - Jie Xue (@JieX19)
    - Link Zheng (@chillancezen)
    - Frank Shen (@fshen01)
    - Hongbin Lu (@fgtdev-hblu)
notes:
    - Starting in version 2.4.0, all input arguments are named using the underscore naming convention (snake_case).
      Please change the arguments such as "var-name" to "var_name".
      Old argument names are still available yet you will receive deprecation warnings.
      You can ignore this warning by setting deprecation_warnings=False in ansible.cfg.
    - Running in workspace locking mode is supported in this FortiManager module, the top
      level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
    - Normally, running one module can fail when a non-zero rc is returned. you can also override
      the conditions to fail or succeed with parameters rc_failed and rc_succeeded
options:
    access_token:
        description: The token to access FortiManager without using username and password.
        type: str
    bypass_validation:
        description: Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.
        type: bool
        default: false
    enable_log:
        description: Enable/Disable logging for task.
        type: bool
        default: false
    forticloud_access_token:
        description: Authenticate Ansible client with forticloud API access token.
        type: str
    rc_succeeded:
        description: The rc codes list with which the conditions to succeed will be overriden.
        type: list
        elements: int
    rc_failed:
        description: The rc codes list with which the conditions to fail will be overriden.
        type: list
        elements: int
    workspace_locking_adom:
        description: The adom to lock for FortiManager running in workspace mode, the value can be global and others including root.
        type: str
    workspace_locking_timeout:
        description: The maximum time in seconds to wait for other user to release the workspace lock.
        type: int
        default: 300
    securityconsole_import_dev_objs:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            add_mappings:
                type: str
                description: Automatically add required dynamic mappings for the device during the search stages.
                choices:
                    - 'disable'
                    - 'enable'
            adom:
                type: str
                description: Source ADOM name.
            dst_name:
                type: str
                description: Name of the policy package where the objects are to be imported.
            dst_parent:
                type: str
                description: Path to the folder for the target package.
            if_all_objs:
                type: str
                description: If all objs.
                choices:
                    - 'none'
                    - 'all'
                    - 'filter'
            if_all_policy:
                type: str
                description: If all policy.
                choices:
                    - 'disable'
                    - 'enable'
            import_action:
                type: str
                description:
                    - do - Perform the policy and object import.
                    - policy_search - Preprocess and scan through device database to gather information about policies that need to be imported.
                    - obj_search - Preprocess and scan through device database to collect objects that are required to be imported.
                choices:
                    - 'do'
                    - 'policy_search'
                    - 'obj_search'
            name:
                type: str
                description: Source device name.
            position:
                type: str
                description: Position.
                choices:
                    - 'bottom'
                    - 'top'
            vdom:
                type: str
                description: Vdom.
'''

EXAMPLES = '''
- name: Example playbook (generated based on argument schema)
  hosts: fortimanagers
  connection: httpapi
  vars:
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_httpapi_port: 443
  tasks:
    - name: Import objects from device to ADOM, or from ADOM to Global.
      fortinet.fortimanager.fmgr_securityconsole_import_dev_objs:
        # bypass_validation: false
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        # rc_succeeded: [0, -2, -3, ...]
        # rc_failed: [-2, -3, ...]
        securityconsole_import_dev_objs:
          add_mappings: <value in [disable, enable]>
          adom: <string>
          dst_name: <string>
          dst_parent: <string>
          if_all_objs: <value in [none, all, filter]>
          if_all_policy: <value in [disable, enable]>
          import_action: <value in [do, policy_search, obj_search]>
          name: <string>
          position: <value in [bottom, top]>
          vdom: <string>
'''

RETURN = '''
meta:
    description: The result of the request.
    type: dict
    returned: always
    contains:
        request_url:
            description: The full url requested.
            returned: always
            type: str
            sample: /sys/login/user
        response_code:
            description: The status of api request.
            returned: always
            type: int
            sample: 0
        response_data:
            description: The api response.
            type: list
            returned: always
        response_message:
            description: The descriptive message of the api response.
            type: str
            returned: always
            sample: OK.
        system_information:
            description: The information of the target system.
            type: dict
            returned: always
rc:
    description: The status the request.
    type: int
    returned: always
    sample: 0
version_check_warning:
    description: Warning if the parameters used in the playbook are not supported by the current FortiManager version.
    type: list
    returned: complex
'''
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible_collections.fortinet.fortimanager.plugins.module_utils.napi import NAPIManager, check_galaxy_version, check_parameter_bypass
from ansible_collections.fortinet.fortimanager.plugins.module_utils.common import get_module_arg_spec


def main():
    urls_list = [
        '/securityconsole/import/dev/objs'
    ]
    url_params = []
    module_primary_key = None
    module_arg_spec = {
        'securityconsole_import_dev_objs': {
            'type': 'dict',
            'v_range': [['6.0.0', '']],
            'options': {
                'add_mappings': {'choices': ['disable', 'enable'], 'type': 'str'},
                'adom': {'type': 'str'},
                'dst_name': {'type': 'str'},
                'dst_parent': {'type': 'str'},
                'if_all_objs': {'choices': ['none', 'all', 'filter'], 'type': 'str'},
                'if_all_policy': {'choices': ['disable', 'enable'], 'type': 'str'},
                'import_action': {'choices': ['do', 'policy_search', 'obj_search'], 'type': 'str'},
                'name': {'type': 'str'},
                'position': {'choices': ['bottom', 'top'], 'type': 'str'},
                'vdom': {'type': 'str'}
            }
        }
    }

    module_option_spec = get_module_arg_spec('exec')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'securityconsole_import_dev_objs'),
                           supports_check_mode=True)

    if not module._socket_path:
        module.fail_json(msg='MUST RUN IN HTTPAPI MODE')
    connection = Connection(module._socket_path)
    fmgr = NAPIManager('exec', module_arg_spec, urls_list, module_primary_key, url_params,
                       module, connection, top_level_schema_name='data')
    fmgr.validate_parameters(params_validation_blob)
    fmgr.process_exec()

    module.exit_json(meta=module.params)


if __name__ == '__main__':
    main()
