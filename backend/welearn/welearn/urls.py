"""welearn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^rooms/$', views.rooms_list),
    url(r'^rooms/(?P<pk>[0-9]+)$', views.room_detail),
    url(r'^categories/$', views.categories_list),
    url(r'^categories/(?P<pk>[0-9]+)', views.categories_detail),
    url(r'^users/$', views.users_list),
    url(r'^users/(?P<pk>[0-9]+)$', views.users_details),
    url(r'^register/$', views.register),

    url(r'^api-token-auth/$', views.ObtainJWTToken.as_view()),
    url(r'^api-token-refresh/$', refresh_jwt_token),
    url(r'^api-token-verify/$', verify_jwt_token),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
