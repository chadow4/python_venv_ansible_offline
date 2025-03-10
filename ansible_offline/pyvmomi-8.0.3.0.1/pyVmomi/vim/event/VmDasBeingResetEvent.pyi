# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.event import VmEvent

class VmDasBeingResetEvent(VmEvent):
   class ReasonCode(Enum):
      vmtoolsHeartbeatFailure: ClassVar['ReasonCode'] = 'vmtoolsHeartbeatFailure'
      appHeartbeatFailure: ClassVar['ReasonCode'] = 'appHeartbeatFailure'
      appImmediateResetRequest: ClassVar['ReasonCode'] = 'appImmediateResetRequest'
      vmcpResetApdCleared: ClassVar['ReasonCode'] = 'vmcpResetApdCleared'
      guestOsCrashFailure: ClassVar['ReasonCode'] = 'guestOsCrashFailure'

   reason: Optional[str] = None
