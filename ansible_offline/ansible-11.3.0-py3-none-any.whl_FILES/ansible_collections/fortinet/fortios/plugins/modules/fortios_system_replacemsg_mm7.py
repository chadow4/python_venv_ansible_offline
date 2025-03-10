#!/usr/bin/python
from __future__ import absolute_import, division, print_function

# Copyright: (c) 2022 Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

__metaclass__ = type

ANSIBLE_METADATA = {
    "status": ["preview"],
    "supported_by": "community",
    "metadata_version": "1.1",
}

DOCUMENTATION = """
---
module: fortios_system_replacemsg_mm7
short_description: Replacement messages in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the
      user to set and modify system_replacemsg feature and mm7 category.
      Examples include all parameters and values need to be adjusted to datasources before usage.
      Tested with FOS v6.0.0
version_added: "2.0.0"
author:
    - Link Zheng (@chillancezen)
    - Jie Xue (@JieX19)
    - Hongbin Lu (@fgtdev-hblu)
    - Frank Shen (@frankshen01)
    - Miguel Angel Munoz (@mamunozgonzalez)
    - Nicolas Thomas (@thomnico)
notes:
    - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

    - The module supports check_mode.

requirements:
    - ansible>=2.15
options:
    access_token:
        description:
            - Token-based authentication.
              Generated from GUI of Fortigate.
        type: str
        required: false
    enable_log:
        description:
            - Enable/Disable logging for task.
        type: bool
        required: false
        default: false
    vdom:
        description:
            - Virtual domain, among those defined previously. A vdom is a
              virtual instance of the FortiGate that can be configured and
              used as a different unit.
        type: str
        default: root
    member_path:
        type: str
        description:
            - Member attribute path to operate on.
            - Delimited by a slash character if there are more than one attribute.
            - Parameter marked with member_path is legitimate for doing member operation.
    member_state:
        type: str
        description:
            - Add or delete a member under specified attribute path.
            - When member_state is specified, the state option is ignored.
        choices:
            - 'present'
            - 'absent'

    state:
        description:
            - Indicates whether to create or remove the object.
        type: str
        required: true
        choices:
            - 'present'
            - 'absent'
    system_replacemsg_mm7:
        description:
            - Replacement messages.
        default: null
        type: dict
        suboptions:
            add_smil:
                description:
                    - add message encapsulation
                type: str
                choices:
                    - 'enable'
                    - 'disable'
            addr_type:
                description:
                    - from address type
                type: str
                choices:
                    - 'rfc2822-addr'
                    - 'number'
                    - 'short-code'
            allow_content_adaptation:
                description:
                    - allow content adaptations
                type: str
                choices:
                    - 'enable'
                    - 'disable'
            charset:
                description:
                    - character encoding used for replacement message
                type: str
                choices:
                    - 'utf-8'
                    - 'us-ascii'
            class:
                description:
                    - message class
                type: str
                choices:
                    - 'not-included'
                    - 'personal'
                    - 'informational'
                    - 'advertisement'
                    - 'auto'
            format:
                description:
                    - Format flag.
                type: str
                choices:
                    - 'none'
                    - 'text'
                    - 'html'
                    - 'wml'
            fos_message:
                description:
                    - message text
                type: str
            from:
                description:
                    - from address
                type: str
            from_sender:
                description:
                    - notification message sent from recipient
                type: str
                choices:
                    - 'enable'
                    - 'disable'
            header:
                description:
                    - Header flag.
                type: str
                choices:
                    - 'none'
                    - 'http'
                    - '8bit'
            image:
                description:
                    - Message string. Source system.replacemsg-image.name.
                type: str
            msg_type:
                description:
                    - Message type.
                required: true
                type: str
            priority:
                description:
                    - message priority
                type: str
                choices:
                    - 'not-included'
                    - 'low'
                    - 'normal'
                    - 'high'
            rsp_status:
                description:
                    - response status
                type: str
                choices:
                    - 'success'
                    - 'partial-success'
                    - 'client-err'
                    - 'oper-restrict'
                    - 'addr-err'
                    - 'addr-not-found'
                    - 'content-refused'
                    - 'msg-id-not-found'
                    - 'link-id-not-found'
                    - 'msg-fmt-corrupt'
                    - 'app-id-not-found'
                    - 'repl-app-id-not-found'
                    - 'srv-err'
                    - 'not-possible'
                    - 'msg-rejected'
                    - 'multiple-addr-not-supp'
                    - 'app-addr-not-supp'
                    - 'gen-service-err'
                    - 'improper-ident'
                    - 'unsupp-ver'
                    - 'unsupp-oper'
                    - 'validation-err'
                    - 'service-err'
                    - 'service-unavail'
                    - 'service-denied'
                    - 'app-denied'
            smil_part:
                description:
                    - message encapsulation text
                type: str
            subject:
                description:
                    - subject text string
                type: str
"""

EXAMPLES = """
- name: Replacement messages.
  fortinet.fortios.fortios_system_replacemsg_mm7:
      vdom: "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      system_replacemsg_mm7:
          add_smil: "enable"
          addr_type: "rfc2822-addr"
          allow_content_adaptation: "enable"
          charset: "utf-8"
          class: "not-included"
          format: "none"
          fos_message: "<your_own_value>"
          from: "<your_own_value>"
          from_sender: "enable"
          header: "none"
          image: "<your_own_value> (source system.replacemsg-image.name)"
          msg_type: "<your_own_value>"
          priority: "not-included"
          rsp_status: "success"
          smil_part: "<your_own_value>"
          subject: "<your_own_value>"
"""

RETURN = """
build:
  description: Build number of the fortigate image
  returned: always
  type: str
  sample: '1547'
http_method:
  description: Last method used to provision the content into FortiGate
  returned: always
  type: str
  sample: 'PUT'
http_status:
  description: Last result given by FortiGate on last operation applied
  returned: always
  type: str
  sample: "200"
mkey:
  description: Master key (id) used in the last call to FortiGate
  returned: success
  type: str
  sample: "id"
name:
  description: Name of the table used to fulfill the request
  returned: always
  type: str
  sample: "urlfilter"
path:
  description: Path of the table used to fulfill the request
  returned: always
  type: str
  sample: "webfilter"
revision:
  description: Internal revision number
  returned: always
  type: str
  sample: "17.0.2.10658"
serial:
  description: Serial number of the unit
  returned: always
  type: str
  sample: "FGVMEVYYQT3AB5352"
status:
  description: Indication of the operation's result
  returned: always
  type: str
  sample: "success"
vdom:
  description: Virtual domain used
  returned: always
  type: str
  sample: "root"
version:
  description: Version of the FortiGate
  returned: always
  type: str
  sample: "v5.6.3"
"""
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.fortios import (
    FortiOSHandler,
)
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.fortios import (
    check_legacy_fortiosapi,
)
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.fortios import (
    schema_to_module_spec,
)
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.fortios import (
    check_schema_versioning,
)
from ansible_collections.fortinet.fortios.plugins.module_utils.fortimanager.common import (
    FAIL_SOCKET_MSG,
)
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.data_post_processor import (
    remove_invalid_fields,
)
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.comparison import (
    is_same_comparison,
)
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.comparison import (
    serialize,
)
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.comparison import (
    find_current_values,
)


def filter_system_replacemsg_mm7_data(json):
    option_list = [
        "add_smil",
        "addr_type",
        "allow_content_adaptation",
        "charset",
        "class",
        "format",
        "fos_message",
        "from",
        "from_sender",
        "header",
        "image",
        "msg_type",
        "priority",
        "rsp_status",
        "smil_part",
        "subject",
    ]

    json = remove_invalid_fields(json)
    dictionary = {}

    for attribute in option_list:
        if attribute in json and json[attribute] is not None:
            dictionary[attribute] = json[attribute]

    return dictionary


def underscore_to_hyphen(data):
    new_data = None
    if isinstance(data, list):
        new_data = []
        for i, elem in enumerate(data):
            new_data.append(underscore_to_hyphen(elem))
    elif isinstance(data, dict):
        new_data = {}
        for k, v in data.items():
            new_data[k.replace("_", "-")] = underscore_to_hyphen(v)
    else:
        return data
    return new_data


def valid_attr_to_invalid_attr(data):
    speciallist = {"message": "fos_message"}

    for k, v in speciallist.items():
        if v == data:
            return k

    return data


def valid_attr_to_invalid_attrs(data):
    if isinstance(data, list):
        new_data = []
        for elem in data:
            elem = valid_attr_to_invalid_attrs(elem)
            new_data.append(elem)
        data = new_data
    elif isinstance(data, dict):
        new_data = {}
        for k, v in data.items():
            new_data[valid_attr_to_invalid_attr(k)] = valid_attr_to_invalid_attrs(v)
        data = new_data

    return valid_attr_to_invalid_attr(data)


def system_replacemsg_mm7(data, fos, check_mode=False):

    state = None
    vdom = data["vdom"]
    state = data.get("state", None)
    system_replacemsg_mm7_data = data["system_replacemsg_mm7"]

    filtered_data = filter_system_replacemsg_mm7_data(system_replacemsg_mm7_data)
    converted_data = underscore_to_hyphen(valid_attr_to_invalid_attrs(filtered_data))

    # check_mode starts from here
    if check_mode:
        diff = {
            "before": "",
            "after": filtered_data,
        }
        mkeyname = fos.get_mkeyname(None, None)
        mkey = fos.get_mkey("system.replacemsg", "mm7", filtered_data, vdom=vdom)
        current_data = fos.get("system.replacemsg", "mm7", vdom=vdom, mkey=mkey)
        is_existed = (
            current_data
            and current_data.get("http_status") == 200
            and (
                mkeyname
                and isinstance(current_data.get("results"), list)
                and len(current_data["results"]) > 0
                or not mkeyname
                and current_data["results"]  # global object response
            )
        )

        # 2. if it exists and the state is 'present' then compare current settings with desired
        if state == "present" or state is True or state is None:
            # for non global modules, mkeyname must exist and it's a new module when mkey is None
            if mkeyname is not None and mkey is None:
                return False, True, filtered_data, diff

            # if mkey exists then compare each other
            # record exits and they're matched or not
            copied_filtered_data = filtered_data.copy()
            copied_filtered_data.pop(mkeyname, None)

            current_data_results = current_data.get("results", {})
            current_config = (
                current_data_results[0]
                if mkeyname
                and isinstance(current_data_results, list)
                and len(current_data_results) > 0
                else current_data_results
            )
            if is_existed:
                current_values = find_current_values(
                    copied_filtered_data, current_config
                )

                is_same = is_same_comparison(
                    serialize(current_values), serialize(copied_filtered_data)
                )

                return (
                    False,
                    not is_same,
                    filtered_data,
                    {"before": current_values, "after": copied_filtered_data},
                )

            # record does not exist
            return False, True, filtered_data, diff

        if state == "absent":
            if mkey is None:
                return (
                    False,
                    False,
                    filtered_data,
                    {"before": current_data["results"][0], "after": ""},
                )

            if is_existed:
                return (
                    False,
                    True,
                    filtered_data,
                    {"before": current_data["results"][0], "after": ""},
                )
            return False, False, filtered_data, {}

        return True, False, {"reason: ": "Must provide state parameter"}, {}
    # pass post processed data to member operations
    # no need to do underscore_to_hyphen since do_member_operation handles it by itself
    data_copy = data.copy()
    data_copy["system_replacemsg_mm7"] = filtered_data
    fos.do_member_operation(
        "system.replacemsg",
        "mm7",
        data_copy,
    )

    if state == "present" or state is True:
        return fos.set("system.replacemsg", "mm7", data=converted_data, vdom=vdom)

    elif state == "absent":
        return fos.delete(
            "system.replacemsg", "mm7", mkey=converted_data["msg-type"], vdom=vdom
        )
    else:
        fos._module.fail_json(msg="state must be present or absent!")


def is_successful_status(resp):
    return (
        "status" in resp
        and resp["status"] == "success"
        or "http_status" in resp
        and resp["http_status"] == 200
        or "http_method" in resp
        and resp["http_method"] == "DELETE"
        and resp["http_status"] == 404
    )


def fortios_system_replacemsg(data, fos, check_mode):

    if data["system_replacemsg_mm7"]:
        resp = system_replacemsg_mm7(data, fos, check_mode)
    else:
        fos._module.fail_json(msg="missing task body: %s" % ("system_replacemsg_mm7"))
    if isinstance(resp, tuple) and len(resp) == 4:
        return resp
    return (
        not is_successful_status(resp),
        is_successful_status(resp)
        and (resp["revision_changed"] if "revision_changed" in resp else True),
        resp,
        {},
    )


versioned_schema = {
    "type": "list",
    "elements": "dict",
    "children": {
        "msg_type": {
            "v_range": [["v6.0.0", "v6.2.7"]],
            "type": "string",
            "required": True,
        },
        "from_sender": {
            "v_range": [["v6.0.0", "v6.2.7"]],
            "type": "string",
            "options": [{"value": "enable"}, {"value": "disable"}],
        },
        "from": {"v_range": [["v6.0.0", "v6.2.7"]], "type": "string"},
        "addr_type": {
            "v_range": [["v6.0.0", "v6.2.7"]],
            "type": "string",
            "options": [
                {"value": "rfc2822-addr"},
                {"value": "number"},
                {"value": "short-code"},
            ],
        },
        "subject": {"v_range": [["v6.0.0", "v6.2.7"]], "type": "string"},
        "priority": {
            "v_range": [["v6.0.0", "v6.2.7"]],
            "type": "string",
            "options": [
                {"value": "not-included"},
                {"value": "low"},
                {"value": "normal"},
                {"value": "high"},
            ],
        },
        "class": {
            "v_range": [["v6.0.0", "v6.2.7"]],
            "type": "string",
            "options": [
                {"value": "not-included"},
                {"value": "personal"},
                {"value": "informational"},
                {"value": "advertisement"},
                {"value": "auto"},
            ],
        },
        "rsp_status": {
            "v_range": [["v6.0.0", "v6.2.7"]],
            "type": "string",
            "options": [
                {"value": "success"},
                {"value": "partial-success"},
                {"value": "client-err"},
                {"value": "oper-restrict"},
                {"value": "addr-err"},
                {"value": "addr-not-found"},
                {"value": "content-refused"},
                {"value": "msg-id-not-found"},
                {"value": "link-id-not-found"},
                {"value": "msg-fmt-corrupt"},
                {"value": "app-id-not-found"},
                {"value": "repl-app-id-not-found"},
                {"value": "srv-err"},
                {"value": "not-possible"},
                {"value": "msg-rejected"},
                {"value": "multiple-addr-not-supp"},
                {"value": "app-addr-not-supp"},
                {"value": "gen-service-err"},
                {"value": "improper-ident"},
                {"value": "unsupp-ver"},
                {"value": "unsupp-oper"},
                {"value": "validation-err"},
                {"value": "service-err"},
                {"value": "service-unavail"},
                {"value": "service-denied"},
                {"value": "app-denied"},
            ],
        },
        "allow_content_adaptation": {
            "v_range": [["v6.0.0", "v6.2.7"]],
            "type": "string",
            "options": [{"value": "enable"}, {"value": "disable"}],
        },
        "add_smil": {
            "v_range": [["v6.0.0", "v6.2.7"]],
            "type": "string",
            "options": [{"value": "enable"}, {"value": "disable"}],
        },
        "smil_part": {"v_range": [["v6.0.0", "v6.2.7"]], "type": "string"},
        "charset": {
            "v_range": [["v6.0.0", "v6.2.7"]],
            "type": "string",
            "options": [{"value": "utf-8"}, {"value": "us-ascii"}],
        },
        "image": {"v_range": [["v6.0.0", "v6.2.7"]], "type": "string"},
        "header": {
            "v_range": [["v6.0.0", "v6.2.7"]],
            "type": "string",
            "options": [{"value": "none"}, {"value": "http"}, {"value": "8bit"}],
        },
        "format": {
            "v_range": [["v6.0.0", "v6.2.7"]],
            "type": "string",
            "options": [
                {"value": "none"},
                {"value": "text"},
                {"value": "html"},
                {"value": "wml"},
            ],
        },
        "fos_message": {"v_range": [["v6.0.0", "v6.2.7"]], "type": "string"},
    },
    "v_range": [["v6.0.0", "v6.2.7"]],
}


def main():
    module_spec = schema_to_module_spec(versioned_schema)
    mkeyname = "msg-type"
    fields = {
        "access_token": {"required": False, "type": "str", "no_log": True},
        "enable_log": {"required": False, "type": "bool", "default": False},
        "vdom": {"required": False, "type": "str", "default": "root"},
        "member_path": {"required": False, "type": "str"},
        "member_state": {
            "type": "str",
            "required": False,
            "choices": ["present", "absent"],
        },
        "state": {"required": True, "type": "str", "choices": ["present", "absent"]},
        "system_replacemsg_mm7": {
            "required": False,
            "type": "dict",
            "default": None,
            "options": {},
        },
    }
    for attribute_name in module_spec["options"]:
        fields["system_replacemsg_mm7"]["options"][attribute_name] = module_spec[
            "options"
        ][attribute_name]
        if mkeyname and mkeyname == attribute_name:
            fields["system_replacemsg_mm7"]["options"][attribute_name][
                "required"
            ] = True

    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    check_legacy_fortiosapi(module)

    is_error = False
    has_changed = False
    result = None
    diff = None

    versions_check_result = None
    if module._socket_path:
        connection = Connection(module._socket_path)
        if "access_token" in module.params:
            connection.set_custom_option("access_token", module.params["access_token"])

        if "enable_log" in module.params:
            connection.set_custom_option("enable_log", module.params["enable_log"])
        else:
            connection.set_custom_option("enable_log", False)
        fos = FortiOSHandler(connection, module, mkeyname)
        versions_check_result = check_schema_versioning(
            fos, versioned_schema, "system_replacemsg_mm7"
        )

        is_error, has_changed, result, diff = fortios_system_replacemsg(
            module.params, fos, module.check_mode
        )

    else:
        module.fail_json(**FAIL_SOCKET_MSG)

    if versions_check_result and versions_check_result["matched"] is False:
        module.warn(
            "Ansible has detected version mismatch between FortOS system and your playbook, see more details by specifying option -vvv"
        )

    if not is_error:
        if versions_check_result and versions_check_result["matched"] is False:
            module.exit_json(
                changed=has_changed,
                version_check_warning=versions_check_result,
                meta=result,
                diff=diff,
            )
        else:
            module.exit_json(changed=has_changed, meta=result, diff=diff)
    else:
        if versions_check_result and versions_check_result["matched"] is False:
            module.fail_json(
                msg="Error in repo",
                version_check_warning=versions_check_result,
                meta=result,
            )
        else:
            module.fail_json(msg="Error in repo", meta=result)


if __name__ == "__main__":
    main()
