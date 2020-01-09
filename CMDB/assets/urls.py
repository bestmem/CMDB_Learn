#!/usr/bin/env python
# coding:utf8
# date: 2020/1/3 11:50
# author: bestmem
from django.urls import path
from assets import views

app_name = 'assets'

urlpatterns = [
    path('report/', views.report, name='report'),
]