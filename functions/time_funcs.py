#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals # for Python 3 with Python 2 retrocompatibility

import datetime, time

def get_timestamp():
    return datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
