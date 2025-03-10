# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import VsanFailedRepairObjectResult

class VsanRepairObjectsResult(DynamicData):
   inQueueObjects: list[str] = []
   failedRepairObjects: list[VsanFailedRepairObjectResult] = []
   notInQueueObjects: list[str] = []
