#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals # for Python 3 with Python 2 retrocompatibility

# Needed for OAuth2
from django.conf.urls import url, include
import oauth2_provider.views as oauth2_views
from django.conf import settings

# For authentification purposes
from django.contrib.auth.models import User, Group
from django.contrib.auth import views as auth_views

# For administration
from django.contrib import admin
admin.autodiscover()

# Personnal settings and views
from .views import home,handler404
from .settings import LOGIN_URL

# For registration view
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

# Needed for REST Framework and OAuth2
from rest_framework import routers
from .views import UserSerializer, GroupSerializer,UserViewSet,GroupViewSet


# OAuth2 provider endpoints
oauth2_endpoint_views = [
    url(r'^authorize/$', oauth2_views.AuthorizationView.as_view(), name="authorize"),
    url(r'^token/$', oauth2_views.TokenView.as_view(), name="token"),
    url(r'^revoke-token/$', oauth2_views.RevokeTokenView.as_view(), name="revoke-token"),
]

if settings.DEBUG:
    # OAuth2 Application Management endpoints
    oauth2_endpoint_views += [
        url(r'^applications/$', oauth2_views.ApplicationList.as_view(), name="list"),
        url(r'^applications/register/$', oauth2_views.ApplicationRegistration.as_view(), name="register"),
        url(r'^applications/(?P<pk>\d+)/$', oauth2_views.ApplicationDetail.as_view(), name="detail"),
        url(r'^applications/(?P<pk>\d+)/delete/$', oauth2_views.ApplicationDelete.as_view(), name="delete"),
        url(r'^applications/(?P<pk>\d+)/update/$', oauth2_views.ApplicationUpdate.as_view(), name="update"),
    ]

    # OAuth2 Token Management endpoints
    oauth2_endpoint_views += [
        url(r'^authorized-tokens/$', oauth2_views.AuthorizedTokensListView.as_view(), name="authorized-token-list"),
        url(r'^authorized-tokens/(?P<pk>\d+)/delete/$', oauth2_views.AuthorizedTokenDeleteView.as_view(),
            name="authorized-token-delete"),
    ]


# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    url(r'^rest/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)), # Administration pannel
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')), # OAuth
    # Previously : url(r'^o/', include(oauth2_endpoint_views, namespace='oauth2_provider')),
    url(r'^$',home,name='home'), # Home Page
    url(LOGIN_URL, auth_views.LoginView.as_view(template_name ='login.html')),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name ='logout.html')),
    url(r'^change-password/$', auth_views.PasswordChangeView.as_view(template_name='passwordReset.html')),
    url(r'^signup/?$', CreateView.as_view(template_name='signup.html',form_class=UserCreationForm,success_url='/')),
    url(r'(?P<typed>.+)$',handler404,name='handler404'), # Hacky way to redirect to a 404 error page
]
