#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals # for Python 3 with Python 2 retrocompatibility

from rest_framework.views import APIView
from rest_framework.response import Response
from braces.views import CsrfExemptMixin

from time_funcs import get_timestamp

class Example_Class(CsrfExemptMixin, APIView):
    def makePayload(self,request,type):
        payload = dict()
        payload ["success"] = True
        payload ["timestamp"] = get_timestamp()
        payload ["method"] = type
        return payload

    def get(self, request):
        return makePayload(self,request,"GET")

    def post(self, request):
        return makePayload(self,request,"post")
