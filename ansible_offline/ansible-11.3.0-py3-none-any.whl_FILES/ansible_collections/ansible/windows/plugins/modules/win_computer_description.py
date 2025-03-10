#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2019, RusoSova
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r'''
---
module: win_computer_description
short_description: Set windows description, owner and organization
description:
 - This module sets Windows description that is shown under My Computer properties. Module also sets
   Windows license owner and organization. License information can be viewed by running winver commad.
version_added: 2.7.0
options:
 description:
   description:
     - String value to apply to Windows descripton. Specify value of "" to clear the value.
   required: false
   type: str
 organization:
   description:
     - String value of organization that the Windows is licensed to. Specify value of "" to clear the value.
   required: false
   type: str
 owner:
   description:
     - String value of the persona that the Windows is licensed to. Specify value of "" to clear the value.
   required: false
   type: str
author:
 - RusoSova (@RusoSova)
'''

EXAMPLES = r'''
- name: Set Windows description, owner and organization
  ansible.windows.win_computer_description:
   description: Best Box
   owner: RusoSova
   organization: MyOrg
  register: result

- name: Set Windows description only
  ansible.windows.win_computer_description:
   description: This is my Windows machine
  register: result

- name: Set organization and clear owner field
  ansible.windows.win_computer_description:
   owner: ''
   organization: Black Mesa

- name: Clear organization, description and owner
  ansible.windows.win_computer_description:
   organization: ""
   owner: ""
   description: ""
  register: result
'''

RETURN = r'''
#
'''
