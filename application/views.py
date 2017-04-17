from __future__ import print_function, absolute_import # For Py2 retrocompatibility
from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse,Http404
from django.shortcuts import render,redirect

# In order to define serializers and viewsets
from rest_framework import permissions, serializers, viewsets
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope
from django.contrib.auth.models import User, Group

# Serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group

# ViewSets
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

# Views
def handler404(request,typed):
    """A basic 404 error handler"""
    response = render(request,'404.html', {"typed":typed})
    response.status_code = 404
    return response

def home(request):
    """Returns the homepage"""
    return render(request,'home.html', {})
