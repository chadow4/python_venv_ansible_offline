# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import ClusterComputeResource

from pyVmomi.vmodl import DynamicData

class CryptoConfigInfo(DynamicData):
   class CryptoMode(Enum):
      onDemand: ClassVar['CryptoMode'] = 'onDemand'
      forceEnable: ClassVar['CryptoMode'] = 'forceEnable'

   cryptoMode: Optional[str] = None
   policy: Optional[ClusterComputeResource.CryptoModePolicy] = None
