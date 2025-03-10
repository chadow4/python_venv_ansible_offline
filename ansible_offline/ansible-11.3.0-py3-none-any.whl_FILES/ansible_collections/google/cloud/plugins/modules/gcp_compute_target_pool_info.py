#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Google
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# ----------------------------------------------------------------------------
#
#     ***     AUTO GENERATED CODE    ***    Type: MMv1     ***
#
# ----------------------------------------------------------------------------
#
#     This file is automatically generated by Magic Modules and manual
#     changes will be clobbered when the file is regenerated.
#
#     Please read more about how to change this file at
#     https://www.github.com/GoogleCloudPlatform/magic-modules
#
# ----------------------------------------------------------------------------

from __future__ import absolute_import, division, print_function

__metaclass__ = type

################################################################################
# Documentation
################################################################################

ANSIBLE_METADATA = {'metadata_version': '1.1', 'status': ["preview"], 'supported_by': 'community'}

DOCUMENTATION = '''
---
module: gcp_compute_target_pool_info
description:
- Gather info for GCP TargetPool
short_description: Gather info for GCP TargetPool
author: Google Inc. (@googlecloudplatform)
requirements:
- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0
options:
  filters:
    description:
    - A list of filter value pairs. Available filters are listed here U(https://cloud.google.com/sdk/gcloud/reference/topic/filters).
    - Each additional filter in the list will act be added as an AND condition (filter1
      and filter2) .
    type: list
    elements: str
  region:
    description:
    - The region where the target pool resides.
    required: true
    type: str
  project:
    description:
    - The Google Cloud Platform project to use.
    type: str
  auth_kind:
    description:
    - The type of credential used.
    type: str
    required: true
    choices:
    - application
    - machineaccount
    - serviceaccount
    - accesstoken
  service_account_contents:
    description:
    - The contents of a Service Account JSON file, either in a dictionary or as a
      JSON string that represents it.
    type: jsonarg
  service_account_file:
    description:
    - The path of a Service Account JSON file if serviceaccount is selected as type.
    type: path
  service_account_email:
    description:
    - An optional service account email address if machineaccount is selected and
      the user does not wish to use the default email.
    type: str
  access_token:
    description:
    - An OAuth2 access token if credential type is accesstoken.
    type: str
  scopes:
    description:
    - Array of scopes to be used
    type: list
    elements: str
  env_type:
    description:
    - Specifies which Ansible environment you're running this module within.
    - This should not be set unless you know what you're doing.
    - This only alters the User Agent string for any API requests.
    type: str
notes:
- for authentication, you can set service_account_file using the C(GCP_SERVICE_ACCOUNT_FILE)
  env variable.
- for authentication, you can set service_account_contents using the C(GCP_SERVICE_ACCOUNT_CONTENTS)
  env variable.
- For authentication, you can set service_account_email using the C(GCP_SERVICE_ACCOUNT_EMAIL)
  env variable.
- For authentication, you can set access_token using the C(GCP_ACCESS_TOKEN)
  env variable.
- For authentication, you can set auth_kind using the C(GCP_AUTH_KIND) env variable.
- For authentication, you can set scopes using the C(GCP_SCOPES) env variable.
- Environment variables values will only be used if the playbook values are not set.
- The I(service_account_email) and I(service_account_file) options are mutually exclusive.
'''

EXAMPLES = '''
- name: get info on a target pool
  gcp_compute_target_pool_info:
    region: us-west1
    filters:
    - name = test_object
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
'''

RETURN = '''
resources:
  description: List of resources
  returned: always
  type: complex
  contains:
    backupPool:
      description:
      - This field is applicable only when the containing target pool is serving a
        forwarding rule as the primary pool, and its failoverRatio field is properly
        set to a value between [0, 1].
      - 'backupPool and failoverRatio together define the fallback behavior of the
        primary target pool: if the ratio of the healthy instances in the primary
        pool is at or below failoverRatio, traffic arriving at the load-balanced IP
        will be directed to the backup pool.'
      - In case where failoverRatio and backupPool are not set, or all the instances
        in the backup pool are unhealthy, the traffic will be directed back to the
        primary pool in the "force" mode, where traffic will be spread to the healthy
        instances with the best effort, or to all instances when no instance is healthy.
      returned: success
      type: dict
    creationTimestamp:
      description:
      - Creation timestamp in RFC3339 text format.
      returned: success
      type: str
    description:
      description:
      - An optional description of this resource.
      returned: success
      type: str
    failoverRatio:
      description:
      - This field is applicable only when the containing target pool is serving a
        forwarding rule as the primary pool (i.e., not as a backup pool to some other
        target pool). The value of the field must be in [0, 1].
      - 'If set, backupPool must also be set. They together define the fallback behavior
        of the primary target pool: if the ratio of the healthy instances in the primary
        pool is at or below this number, traffic arriving at the load-balanced IP
        will be directed to the backup pool.'
      - In case where failoverRatio is not set or all the instances in the backup
        pool are unhealthy, the traffic will be directed back to the primary pool
        in the "force" mode, where traffic will be spread to the healthy instances
        with the best effort, or to all instances when no instance is healthy.
      returned: success
      type: str
    healthCheck:
      description:
      - A reference to a HttpHealthCheck resource.
      - A member instance in this pool is considered healthy if and only if the health
        checks pass. If not specified it means all member instances will be considered
        healthy at all times.
      returned: success
      type: dict
    id:
      description:
      - The unique identifier for the resource.
      returned: success
      type: int
    instances:
      description:
      - A list of virtual machine instances serving this pool.
      - They must live in zones contained in the same region as this pool.
      returned: success
      type: list
    name:
      description:
      - Name of the resource. Provided by the client when the resource is created.
        The name must be 1-63 characters long, and comply with RFC1035. Specifically,
        the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`
        which means the first character must be a lowercase letter, and all following
        characters must be a dash, lowercase letter, or digit, except the last character,
        which cannot be a dash.
      returned: success
      type: str
    sessionAffinity:
      description:
      - 'Session affinity option. Must be one of these values: * NONE: Connections
        from the same client IP may go to any instance in the pool.'
      - "* CLIENT_IP: Connections from the same client IP will go to the same instance
        in the pool while that instance remains healthy."
      - "* CLIENT_IP_PROTO: Connections from the same client IP with the same IP protocol
        will go to the same instance in the pool while that instance remains healthy."
      returned: success
      type: str
    region:
      description:
      - The region where the target pool resides.
      returned: success
      type: str
'''

################################################################################
# Imports
################################################################################
from ansible_collections.google.cloud.plugins.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule
import json

################################################################################
# Main
################################################################################


def main():
    module = GcpModule(argument_spec=dict(filters=dict(type='list', elements='str'), region=dict(required=True, type='str')), supports_check_mode=True)

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/compute']

    return_value = {'resources': fetch_list(module, collection(module), query_options(module.params['filters']))}
    module.exit_json(**return_value)


def collection(module):
    return "https://compute.googleapis.com/compute/v1/projects/{project}/regions/{region}/targetPools".format(**module.params)


def fetch_list(module, link, query):
    auth = GcpSession(module, 'compute')
    return auth.list(link, return_if_object, array_name='items', params={'filter': query})


def query_options(filters):
    if not filters:
        return ''

    if len(filters) == 1:
        return filters[0]
    else:
        queries = []
        for f in filters:
            # For multiple queries, all queries should have ()
            if f[0] != '(' and f[-1] != ')':
                queries.append("(%s)" % ''.join(f))
            else:
                queries.append(f)

        return ' '.join(queries)


def return_if_object(module, response):
    # If not found, return nothing.
    if response.status_code == 404:
        return None

    # If no content, return nothing.
    if response.status_code == 204:
        return None

    try:
        module.raise_for_status(response)
        result = response.json()
    except getattr(json.decoder, 'JSONDecodeError', ValueError) as inst:
        module.fail_json(msg="Invalid JSON response with error: %s" % inst)

    if navigate_hash(result, ['error', 'errors']):
        module.fail_json(msg=navigate_hash(result, ['error', 'errors']))

    return result


if __name__ == "__main__":
    main()
