# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import NoReturn

from pyVmomi.vim import ExtensibleManagedObject

from pyVmomi.vim.host import ServiceInfo

class ServiceSystem(ExtensibleManagedObject):
   @property
   def serviceInfo(self) -> ServiceInfo: ...

   def UpdatePolicy(self, id: str, policy: str) -> NoReturn: ...
   def Start(self, id: str) -> NoReturn: ...
   def Stop(self, id: str) -> NoReturn: ...
   def Restart(self, id: str) -> NoReturn: ...
   def Uninstall(self, id: str) -> NoReturn: ...
   def Refresh(self) -> NoReturn: ...
