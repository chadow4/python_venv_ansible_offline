# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import HostSystem
from pyVmomi.vim import VsanUpgradeSystem

class DisallowEvacuateDataIssue(VsanUpgradeSystem.PreflightCheckIssue):
   hosts: list[HostSystem] = []
