#
# Copyright (C) 2011 Dominik Oepen
# 
# This file is part of virtualsmartcard.
# 
# virtualsmartcard is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
# 
# virtualsmartcard is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
# 
# You should have received a copy of the GNU General Public License along with
# virtualsmartcard.  If not, see <http://www.gnu.org/licenses/>.

from virtualsmartcard.SmartcardSAM import SAM
from virtualsmartcard.SEutils import ControlReferenceTemplate
from virtualsmartcard.SWutils import SwError, SW
from virtualsmartcard.ConstantDefinitions import CRT_TEMPLATE
from virtualsmartcard.TLVutils import unpack, bertlv_pack

import hashlib, struct
from os import urandom

class nPA__AT_CRT(ControlReferenceTemplate):
    def __init__(self):
        ControlReferenceTemplate(CRT_TEMPLATE["AT"])

    def parse_SE_config(self, config)
        try:
            ControlReferenceTemplate.parse_SE_config(self, config)
        except SwError, e:
            structure = unpack(config)
            for tlv in structure:
                tag, length, value = structure
                if tag == 0x7f4c:
                    chat = CHAT(bertlv_pack([tlv])
                    print chat
                elif tag == 0x67:
                    auxiliary_data = value
                else:
                    raise SwError(SW["ERR_REFNOTUSABLE"])

class nPA_SAM(SAM):       
    """
    SAM for ICAO ePassport. Implements Basic access control and key derivation
    for Secure Messaging. 
    """
    def __init__(self, mf):
        SAM.__init__(self, None, None, mf)
        self.current_SE.at = nPA_AT_CRT() 