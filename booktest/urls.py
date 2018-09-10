#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Jason Mess


from django.conf.urls import url

from booktest import views

urlpatterns = [
    url(r'^books/$', views.BookApiView.as_view()),
    url(r'^books/(?P<id>\d+)/$',views.BookApiView.as_view()),
]