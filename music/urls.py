#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 16:56:14 2019

@author: iist
"""

from django.urls import path
from .views import ListSongsView,methodinfo

urlpatterns=[path('songs/',ListSongsView.as_view(),name="songs-all"),
             
             path('display/',methodinfo,name="json-response"),
             ]
