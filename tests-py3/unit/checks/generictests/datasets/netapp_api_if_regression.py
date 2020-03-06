#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# yapf: disable
# type: ignore



checkname = 'netapp_api_if'


info = [[u'interface GTB1020-2-CL_mgmt',
         u'comment -',
         u'use-failover-group unused',
         u'address 191.128.142.33',
         u'dns-domain-name none',
         u'is-auto-revert false',
         u'lif-uuid d3233231-a1d3-12e6-a4ff-00a0231e0e11',
         u'firewall-policy mgmt',
         u'vserver FSS2220-2-CL',
         u'role cluster_mgmt',
         u'netmask-length 24',
         u'data-protocols.data-protocol none',
         u'operational-status up',
         u'ipspace Default',
         u'netmask 255.255.254.0',
         u'failover-policy broadcast_domain_wide',
         u'home-node FSS2220-2',
         u'address-family ipv4',
         u'current-port e0f-112',
         u'current-node FSS2220-2',
         u'is-dns-update-enabled false',
         u'subnet-name MGMT',
         u'listen-for-dns-query false',
         u'administrative-status up',
         u'failover-group MGMT-Netz',
         u'home-port e0f-112',
         u'is-home true',
         u'operational-speed 1000',
         u'send_data 0',
         u'send_errors 0',
         u'link-status up',
         u'recv_errors 0',
         u'send_packet 0',
         u'recv_packet 0',
         u'instance_name FSS2220-2-CL_mgmt',
         u'recv_data 0'],
        [u'interface GTB1020-2_ic1',
         u'comment -',
         u'use-failover-group unused',
         u'address 10.12.1.4',
         u'dns-domain-name none',
         u'is-auto-revert false',
         u'lif-uuid sdfd13d4d-82db-12c5-a2ff-00a123e0e49',
         u'firewall-policy intercluster',
         u'vserver FSS2220-1-DL',
         u'role intercluster',
         u'netmask-length 24',
         u'data-protocols.data-protocol none',
         u'operational-status up',
         u'ipspace Default',
         u'netmask 255.255.244.0',
         u'failover-policy local_only',
         u'home-node FSS2220-2',
         u'address-family ipv4',
         u'current-port e0f-1137',
         u'current-node FSS2220-2',
         u'listen-for-dns-query false',
         u'administrative-status up',
         u'failover-group Intercluster',
         u'home-port e0f-2231',
         u'is-home true',
         u'operational-speed 1000',
         u'send_data 142310234',
         u'send_errors 0',
         u'link-status up',
         u'recv_errors 0',
         u'send_packet 2223111',
         u'recv_packet 2223411',
         u'instance_name FSS2220_ic1',
         u'recv_data 122333190']]


discovery = {'': [('1', "{'state': ['1'], 'speed': 1000000000}"),
                  ('2', "{'state': ['1'], 'speed': 1000000000}")]}


checks = {'': [('1',
                {'errors': (0.01, 0.1), 'speed': 1000000000, 'state': ['1']},
                [(0, u'[GTB1020-2-CL_mgmt] (up) 1 Gbit/s', []),
                 (0, u'Current Port: e0f-112 (is home port)', [])]),
               ('2',
                {'errors': (0.01, 0.1), 'speed': 1000000000, 'state': ['1']},
                [(0, u'[GTB1020-2_ic1] (up) 1 Gbit/s', []),
                 (0, u'Current Port: e0f-2231 (is home port)', [])])]}
