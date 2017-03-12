#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from rest_framework.views import APIView
from rest_framework.response import Response
from braces.views import CsrfExemptMixin

from time_funcs import get_timestamp

class Example_Class(CsrfExemptMixin, APIView):
    def get(self, request):
        payload = dict()
        payload ["success"] = True
        payload ["timestamp"] = get_timestamp()
        payload ["method"] = "GET"
        return Response(payload)

    def post(self, request):
        payload = dict()
        payload ["success"] = True
        payload ["timestamp"] = get_timestamp()
        payload ["method"] = "POST"
        return Response(payload)
