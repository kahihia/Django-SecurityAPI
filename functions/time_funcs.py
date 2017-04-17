#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals # for Python 3 with Python 2 retrocompatibility
from django.shortcuts import render
from django.conf import settings

import datetime, time

def get_timestamp():
    return datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

def customRender(request, template, dictionary={}):
    dictionary.update({'post_count': Post.objects.count()})

    if Option.objects.filter(parameter="display_user_count").exists():
        dictionary.update({'display_user_count': Option.objects.get(parameter="display_user_count").get_bool_value()})
    else:
        dictionary.update({'display_user_count':False})

    return render(request, template, dictionary)
