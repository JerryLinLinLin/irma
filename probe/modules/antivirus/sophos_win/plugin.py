#
# Copyright (c) 2013-2018 Quarkslab.
# This file is part of IRMA project.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the top-level directory
# of this distribution and at:
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# No part of the project, including this file, may be copied,
# modified, propagated, or distributed except according to the
# terms contained in the LICENSE file.

from .sophos_win import SophosWin
from ..interface import AntivirusPluginInterface

from irma.common.plugins import PluginMetaClass, PlatformDependency
from irma.common.base.utils import IrmaProbeType


class SophosWinPlugin(AntivirusPluginInterface, metaclass=PluginMetaClass):

    # =================
    #  plugin metadata
    # =================

    _plugin_name_ = "SophosWin"
    _plugin_display_name_ = SophosWin.name
    _plugin_author_ = "IRMA (c) Quarkslab"
    _plugin_version_ = "1.0.0"
    _plugin_category_ = IrmaProbeType.antivirus
    _plugin_description_ = "Plugin for Sophos on Windows"
    _plugin_dependencies_ = [
        PlatformDependency('win32')
    ]

    # ================
    #  interface data
    # ================

    module_cls = SophosWin
