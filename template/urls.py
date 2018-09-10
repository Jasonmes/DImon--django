#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Jason Mess
from django.conf.urls import url
from template import views

urlpatterns = [
    url(r'^index/$', views.index),
]