# =============================================================================
#
# Copyright (c) 2017, Cisco Systems
# All rights reserved.
#
# # Author: Klaudiusz Staniek
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
# Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
# THE POSSIBILITY OF SUCH DAMAGE.
# =============================================================================

from csmpe.plugins import CSMPlugin


class Plugin(CSMPlugin):
    """This plugin configures the device."""
    name = "Custom Configuration"
    platforms = {'ASR9K', 'CRS', 'NCS1K', 'NCS4K', 'NCS5K', 'NCS5500', 'NCS6K', 'ASR900', 'N6K', 'IOSXRv-9K', 'IOSXRv-X64'}
    phases = {'Pre-Check', 'Post-Check'}

    def _run(self):
        configlet = self.ctx.plugin_data.get('configlet', None)
        plane = self.ctx.plugin_data.get('plane', 'sdr')
        if configlet:
            description = self.ctx.plugin_data.get('description')
            if description:
                description = ': ' + description
            self.ctx.config(configlet=configlet, plane=plane)
            self.ctx.info("Configuration applied{}.".format(description))

        return True
