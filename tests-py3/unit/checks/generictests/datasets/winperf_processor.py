#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# yapf: disable
# type: ignore

checkname = 'winperf_processor'

info = [[u'1556221294.75', u'238', u'10000000'],
        [u'5', u'instances:', u'0', u'1', u'2', u'3', u'_Total'],
        [
            u'-232', u'20854932656250', u'20941215937500', u'20895696562500', u'20931057343750',
            u'20905725625000', u'100nsec_timer_inv'
        ],
        [
            u'-96', u'767188437500', u'738879375000', u'737527500000', u'742882343750',
            u'746619414062', u'100nsec_timer'
        ],
        [
            u'-94', u'121450781250', u'63474218750', u'110345468750', u'69629843750',
            u'91225078125', u'100nsec_timer'
        ],
        [u'-90', u'506534602', u'346655884', u'508018892', u'352757259', u'1713966637', u'counter'],
        [
            u'458', u'30148750000', u'2639375000', u'23398281250', u'2215468750', u'14600468750',
            u'100nsec_timer'
        ],
        [
            u'460', u'5290312500', u'3367968750', u'4306406250', u'5563281250', u'4631992187',
            u'100nsec_timer'
        ],
        [u'1096', u'173713449', u'37720286', u'172867460', u'31918437', u'416219632', u'counter'],
        [u'1098', u'2', u'0', u'1', u'0', u'3', u'rawcount'],
        [
            u'1508', u'20744654902969', u'20848687646812', u'20771013615262', u'20842396380778',
            u'20801688136455', u'100nsec_timer'
        ],
        [
            u'1510', u'20744654902969', u'20848687646812', u'20771013615262', u'20842396380778',
            u'20801688136455', u'100nsec_timer'
        ], [u'1512', u'0', u'0', u'0', u'0', u'0', u'100nsec_timer'],
        [u'1514', u'0', u'0', u'0', u'0', u'0', u'100nsec_timer'],
        [
            u'1516', u'393050574', u'290618823', u'401461357', u'296238855', u'1381369609',
            u'bulk_count'
        ], [u'1518', u'0', u'0', u'0', u'0', u'0', u'bulk_count'],
        [u'1520', u'0', u'0', u'0', u'0', u'0', u'bulk_count']]


def mock_util(*args):
    return {
        ('winperf_util.util', None): (1556221234.75, 20905725624000),
        ('winperf_util.core0.util', None): (1556221234.75, 20854932656100),
        ('winperf_util.core1.util', None): (1556221234.75, 20941215937000),
        ('winperf_util.core2.util', None): (1556221234.75, 20895696561500),
        ('winperf_util.core3.util', None): (1556221234.75, 20931057343740),
        ('winperf_util.user', None): (1556221234.75, 746619411062),
        ('winperf_util.privileged', None): (1556221234.75, 91225078025),
    }[args]


mock_item_state = {'util': mock_util}

discovery = {
    'util': [(None, {}),],
}

checks = {
    'util': [(None, {
        'levels': (90, 95)
    }, [
        (2, 'Total CPU: 100% (warn/crit at 90.0%/95.0%)', [
            ('util', 99.99983122362869, 90, 95, 0, 4),
        ]),
        (0, 'user perc: 0.0 %', [
            ('user', 0.0005063291139240507, None, None, None, None),
        ]),
        (0, 'privileged perc: 0.0 %', [('privileged', 1.6877637130801688e-05)]),
        (0, '4 CPUs', [('cpus', 4)]),
    ]),],
}
