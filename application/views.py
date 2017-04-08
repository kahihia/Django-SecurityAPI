from __future__ import print_function, absolute_import # For Py2 retrocompatibility
from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse,Http404
from django.shortcuts import render,redirect


def handler404(request,typed):
    """A basic 404 error handler"""
    response = render(request,'404.html', {"typed":typed})
    response.status_code = 404
    return response
