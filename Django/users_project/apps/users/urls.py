# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^update$', views.update),
    url(r'^(?P<user_id>\d+)$', views.show),
    url(r'^(?P<user_id>\d+)/edit$', views.edit),
    url(r'^(?P<user_id>\d+)/destroy$', views.destroy),

]
