#！/usr/bin/env python
#-*- coding:utf-8 -*-
from django.conf.urls import url
from web import views
urlpatterns = [
    url(r"index/",views.index),
]
