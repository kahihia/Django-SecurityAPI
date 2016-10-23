#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
import django.contrib.auth.views

#from .admin import admin_site
from .views import *

urlpatterns = [
	url(r'^$', index, name='index'),
]
