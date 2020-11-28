# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^read_log/', views.read_log, name='read_log'),
]
