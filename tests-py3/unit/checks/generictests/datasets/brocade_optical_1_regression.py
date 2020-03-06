#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# yapf: disable
# type: ignore

checkname = 'brocade_optical'

info = [[[u'1', u'10GigabitEthernet1/1/1', u'6',
          u'1'], [u'2', u'10GigabitEthernet1/1/2', u'6', u'2'],
         [u'3', u'10GigabitEthernet1/1/3', u'6',
          u'1'], [u'4', u'10GigabitEthernet1/1/4', u'6', u'2'],
         [u'5', u'10GigabitEthernet1/1/5', u'6',
          u'1'], [u'6', u'10GigabitEthernet1/1/6', u'6', u'2'],
         [u'7', u'10GigabitEthernet1/1/7', u'6',
          u'1'], [u'8', u'10GigabitEthernet1/1/8', u'6', u'2'],
         [u'9', u'10GigabitEthernet1/1/9', u'6', u'1'],
         [u'10', u'10GigabitEthernet1/1/10', u'6', u'2'],
         [u'11', u'10GigabitEthernet1/1/11', u'6', u'1'],
         [u'12', u'10GigabitEthernet1/1/12', u'6', u'2'],
         [u'13', u'10GigabitEthernet1/1/13', u'6', u'2'],
         [u'14', u'10GigabitEthernet1/1/14', u'6', u'2'],
         [u'15', u'10GigabitEthernet1/1/15', u'6', u'2'],
         [u'16', u'10GigabitEthernet1/1/16', u'6', u'2'],
         [u'17', u'10GigabitEthernet1/1/17', u'6', u'2'],
         [u'18', u'10GigabitEthernet1/1/18', u'6', u'2'],
         [u'19', u'10GigabitEthernet1/1/19', u'6', u'2'],
         [u'20', u'10GigabitEthernet1/1/20', u'6', u'2'],
         [u'21', u'10GigabitEthernet1/1/21', u'6', u'2'],
         [u'22', u'10GigabitEthernet1/1/22', u'6', u'2'],
         [u'23', u'10GigabitEthernet1/1/23', u'6', u'2'],
         [u'24', u'10GigabitEthernet1/1/24', u'6', u'2'],
         [u'25', u'10GigabitEthernet1/1/25', u'6', u'2'],
         [u'26', u'10GigabitEthernet1/1/26', u'6', u'2'],
         [u'27', u'10GigabitEthernet1/1/27', u'6', u'2'],
         [u'28', u'10GigabitEthernet1/1/28', u'6', u'2'],
         [u'29', u'10GigabitEthernet1/1/29', u'6', u'2'],
         [u'30', u'10GigabitEthernet1/1/30', u'6', u'2'],
         [u'31', u'10GigabitEthernet1/1/31', u'6', u'2'],
         [u'32', u'10GigabitEthernet1/1/32', u'6', u'2'],
         [u'33', u'10GigabitEthernet1/1/33', u'6', u'2'],
         [u'34', u'10GigabitEthernet1/1/34', u'6', u'2'],
         [u'35', u'10GigabitEthernet1/1/35', u'6', u'2'],
         [u'36', u'10GigabitEthernet1/1/36', u'6', u'2'],
         [u'37', u'10GigabitEthernet1/1/37', u'6', u'2'],
         [u'38', u'10GigabitEthernet1/1/38', u'6', u'2'],
         [u'39', u'10GigabitEthernet1/1/39', u'6', u'2'],
         [u'40', u'10GigabitEthernet1/1/40', u'6', u'2'],
         [u'41', u'10GigabitEthernet1/1/41', u'6', u'2'],
         [u'42', u'10GigabitEthernet1/1/42', u'6', u'2'],
         [u'43', u'10GigabitEthernet1/1/43', u'6', u'2'],
         [u'44', u'10GigabitEthernet1/1/44', u'6', u'2'],
         [u'45', u'10GigabitEthernet1/1/45', u'6', u'2'],
         [u'46', u'10GigabitEthernet1/1/46', u'6', u'2'],
         [u'47', u'10GigabitEthernet1/1/47', u'6', u'2'],
         [u'48', u'10GigabitEthernet1/1/48', u'6', u'2'], [u'49', u'Management', u'6', u'2'],
         [u'65', u'40GigabitEthernet1/2/1', u'6', u'1'],
         [u'69', u'40GigabitEthernet1/2/2', u'6', u'2'],
         [u'73', u'40GigabitEthernet1/2/3', u'6', u'2'],
         [u'77', u'40GigabitEthernet1/2/4', u'6', u'1'],
         [u'81', u'40GigabitEthernet1/2/5', u'6', u'2'],
         [u'85', u'40GigabitEthernet1/2/6', u'6', u'2'],
         [u'129', u'40GigabitEthernet1/3/1', u'6', u'1'],
         [u'133', u'40GigabitEthernet1/3/2', u'6', u'2'],
         [u'137', u'40GigabitEthernet1/3/3', u'6', u'2'],
         [u'141', u'40GigabitEthernet1/3/4', u'6', u'2'],
         [u'145', u'40GigabitEthernet1/3/5', u'6', u'2'],
         [u'149', u'40GigabitEthernet1/3/6', u'6', u'2'],
         [u'257', u'10GigabitEthernet2/1/1', u'6', u'1'],
         [u'258', u'10GigabitEthernet2/1/2', u'6', u'2'],
         [u'259', u'10GigabitEthernet2/1/3', u'6', u'1'],
         [u'260', u'10GigabitEthernet2/1/4', u'6', u'2'],
         [u'261', u'10GigabitEthernet2/1/5', u'6', u'1'],
         [u'262', u'10GigabitEthernet2/1/6', u'6', u'2'],
         [u'263', u'10GigabitEthernet2/1/7', u'6', u'1'],
         [u'264', u'10GigabitEthernet2/1/8', u'6', u'2'],
         [u'265', u'10GigabitEthernet2/1/9', u'6', u'1'],
         [u'266', u'10GigabitEthernet2/1/10', u'6', u'2'],
         [u'267', u'10GigabitEthernet2/1/11', u'6', u'1'],
         [u'268', u'10GigabitEthernet2/1/12', u'6', u'2'],
         [u'269', u'10GigabitEthernet2/1/13', u'6', u'2'],
         [u'270', u'10GigabitEthernet2/1/14', u'6', u'2'],
         [u'271', u'10GigabitEthernet2/1/15', u'6', u'2'],
         [u'272', u'10GigabitEthernet2/1/16', u'6', u'2'],
         [u'273', u'10GigabitEthernet2/1/17', u'6', u'2'],
         [u'274', u'10GigabitEthernet2/1/18', u'6', u'2'],
         [u'275', u'10GigabitEthernet2/1/19', u'6', u'2'],
         [u'276', u'10GigabitEthernet2/1/20', u'6', u'2'],
         [u'277', u'10GigabitEthernet2/1/21', u'6', u'2'],
         [u'278', u'10GigabitEthernet2/1/22', u'6', u'2'],
         [u'279', u'10GigabitEthernet2/1/23', u'6', u'2'],
         [u'280', u'10GigabitEthernet2/1/24', u'6', u'2'],
         [u'281', u'10GigabitEthernet2/1/25', u'6', u'2'],
         [u'282', u'10GigabitEthernet2/1/26', u'6', u'2'],
         [u'283', u'10GigabitEthernet2/1/27', u'6', u'2'],
         [u'284', u'10GigabitEthernet2/1/28', u'6', u'2'],
         [u'285', u'10GigabitEthernet2/1/29', u'6', u'2'],
         [u'286', u'10GigabitEthernet2/1/30', u'6', u'2'],
         [u'287', u'10GigabitEthernet2/1/31', u'6', u'2'],
         [u'288', u'10GigabitEthernet2/1/32', u'6', u'2'],
         [u'289', u'10GigabitEthernet2/1/33', u'6', u'2'],
         [u'290', u'10GigabitEthernet2/1/34', u'6', u'2'],
         [u'291', u'10GigabitEthernet2/1/35', u'6', u'2'],
         [u'292', u'10GigabitEthernet2/1/36', u'6', u'2'],
         [u'293', u'10GigabitEthernet2/1/37', u'6', u'2'],
         [u'294', u'10GigabitEthernet2/1/38', u'6', u'2'],
         [u'295', u'10GigabitEthernet2/1/39', u'6', u'2'],
         [u'296', u'10GigabitEthernet2/1/40', u'6', u'2'],
         [u'297', u'10GigabitEthernet2/1/41', u'6', u'2'],
         [u'298', u'10GigabitEthernet2/1/42', u'6', u'2'],
         [u'299', u'10GigabitEthernet2/1/43', u'6', u'2'],
         [u'300', u'10GigabitEthernet2/1/44', u'6', u'2'],
         [u'301', u'10GigabitEthernet2/1/45', u'6', u'2'],
         [u'302', u'10GigabitEthernet2/1/46', u'6', u'2'],
         [u'303', u'10GigabitEthernet2/1/47', u'6', u'2'],
         [u'304', u'10GigabitEthernet2/1/48', u'6', u'2'],
         [u'321', u'40GigabitEthernet2/2/1', u'6', u'1'],
         [u'325', u'40GigabitEthernet2/2/2', u'6', u'2'],
         [u'329', u'40GigabitEthernet2/2/3', u'6', u'2'],
         [u'333', u'40GigabitEthernet2/2/4', u'6', u'1'],
         [u'337', u'40GigabitEthernet2/2/5', u'6', u'2'],
         [u'341', u'40GigabitEthernet2/2/6', u'6', u'2'],
         [u'385', u'40GigabitEthernet2/3/1', u'6', u'1'],
         [u'389', u'40GigabitEthernet2/3/2', u'6', u'1'],
         [u'393', u'40GigabitEthernet2/3/3', u'6', u'2'],
         [u'397', u'40GigabitEthernet2/3/4', u'6', u'2'],
         [u'401', u'40GigabitEthernet2/3/5', u'6', u'2'],
         [u'405', u'40GigabitEthernet2/3/6', u'6', u'2'], [u'3073', u'lg1', u'6', u'1'],
         [u'3074', u'lg2', u'6', u'1'], [u'3075', u'lg3', u'6',
                                         u'1'], [u'3076', u'lg4', u'6', u'1'],
         [u'3077', u'lg5', u'6', u'1'], [u'3078', u'lg6', u'6', u'1'],
         [u'3079', u'lg7', u'6', u'1'], [u'16777217', u'v30', u'135', u'1']], [], [],
        [[u'28.5273 C Normal', u'-002.2373 dBm Normal', u'-002.4298 dBm Normal', u'3.1'],
         [u'28.8945 C Normal', u'-002.2848 dBm Normal', u'-002.3597 dBm Normal', u'5.1'],
         [u'29.3554 C Normal', u'-002.2944 dBm Normal', u'-002.8474 dBm Normal', u'7.1'],
         [u'28.2851 C Normal', u'-002.2789 dBm Normal', u'-002.7278 dBm Normal', u'9.1'],
         [u'26.0507 C Normal', u'-002.2848 dBm Normal', u'-004.1953 dBm Normal', u'11.1'],
         [u'25.5468 C Normal', u'-002.2723 dBm Normal', u'-002.3942 dBm Normal', u'259.1'],
         [u'26.5156 C Normal', u'-002.2635 dBm Normal', u'-002.4116 dBm Normal', u'261.1'],
         [u'27.7500 C Normal', u'-002.2672 dBm Normal', u'-002.2760 dBm Normal', u'263.1'],
         [u'25.4765 C Normal', u'-002.2519 dBm Normal', u'-002.1331 dBm Normal', u'265.1'],
         [u'26.9257 C Normal', u'-002.2716 dBm Normal', u'-002.5251 dBm Normal', u'267.1'],
         [u'', u'', u'', u'321.1'], [u'', u'', u'', u'321.2'], [u'', u'', u'', u'321.3'],
         [u'', u'', u'', u'321.4'], [u'', u'', u'', u'333.1'], [u'', u'', u'', u'333.2'],
         [u'', u'', u'', u'333.3'], [u'', u'', u'', u'333.4']]]

discovery = {'': []}
