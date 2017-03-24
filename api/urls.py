#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals # for Python 3 with Python 2 retrocompatibility
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
import django.contrib.auth.views

#from .admin import admin_site
from .views import *

urlpatterns = [
	url(r'^public/get/example/$', Example_Class.as_view(), name='example_view'),
]
