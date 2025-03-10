# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim import HostSystem

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import VsanIoInsightInfo

class VsanHostIoInsightInfo(DynamicData):
   host: HostSystem
   ioinsightWorldId: Optional[long] = None
   faultMessage: Optional[str] = None
   ioinsightInfo: Optional[VsanIoInsightInfo] = None
