#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Ren"
# Date: 2019/4/22
# Time: 8:07 AM
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
	url(r'^(\d+)/(\d+)$',views.detail),
	url(r'^grades/$',views.grades),
	url(r'^students/$',views.students),
	url(r'^grades/(\d+)$',views.gradesStudents)
]