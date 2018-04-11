# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^ninja_gold/$', views.money_maker),
    url(r'^ninja_gold/process$', views.process),
    url(r'^ninja_gold/clear$', views.clear),

]
