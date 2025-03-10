# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

from pyVmomi.pbm.placement import PlacementHub

from pyVmomi.pbm.profile import Profile

class DefaultProfileInfo(DynamicData):
   datastores: list[PlacementHub] = []
   defaultProfile: Optional[Profile] = None
   methodFault: Optional[MethodFault] = None
