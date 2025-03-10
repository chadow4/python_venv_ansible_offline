# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import Task

from pyVmomi.vim.cns import QueryFilter
from pyVmomi.vim.cns import QueryResult
from pyVmomi.vim.cns import QuerySelection
from pyVmomi.vim.cns import SnapshotCreateSpec
from pyVmomi.vim.cns import SnapshotDeleteSpec
from pyVmomi.vim.cns import VolumeACLConfigureSpec
from pyVmomi.vim.cns import VolumeAttachDetachSpec
from pyVmomi.vim.cns import VolumeCreateSpec
from pyVmomi.vim.cns import VolumeExtendSpec
from pyVmomi.vim.cns import VolumeId
from pyVmomi.vim.cns import VolumeMetadataUpdateSpec
from pyVmomi.vim.cns import VolumePolicyReconfigSpec
from pyVmomi.vim.cns import VolumeRelocateSpec

class VolumeManager(ManagedObject):
   def Create(self, createSpecs: list[VolumeCreateSpec]) -> Task: ...
   def UpdateVolumeMetadata(self, updateSpecs: list[VolumeMetadataUpdateSpec]) -> Task: ...
   def Delete(self, volumeIds: list[VolumeId], deleteDisk: bool) -> Task: ...
   def Attach(self, attachSpecs: list[VolumeAttachDetachSpec]) -> Task: ...
   def Detach(self, detachSpecs: list[VolumeAttachDetachSpec]) -> Task: ...
   def QueryAsync(self, filter: QueryFilter, selection: Optional[QuerySelection]) -> Task: ...
   def Query(self, filter: QueryFilter, selection: Optional[QuerySelection]) -> QueryResult: ...
   def ConfigureVolumeACLs(self, ACLConfigSpecs: list[VolumeACLConfigureSpec]) -> Task: ...
   def Extend(self, extendSpecs: list[VolumeExtendSpec]) -> Task: ...
   def CreateSnapshots(self, snapshotSpecs: list[SnapshotCreateSpec]) -> Task: ...
   def DeleteSnapshots(self, snapshotDeleteSpecs: list[SnapshotDeleteSpec]) -> Task: ...
   def Relocate(self, relocateSpecs: list[VolumeRelocateSpec]) -> Task: ...
   def ReconfigPolicy(self, volumePolicyReconfigSpecs: list[VolumePolicyReconfigSpec]) -> Task: ...
