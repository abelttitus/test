#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 17:01:20 2019

@author: iist
"""

from rest_framework import serializers
from .models import Songs

class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Songs
        fields=("title","artist")
        
        