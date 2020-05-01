#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File        :admin.py
@Description :
@DateTiem    :2020-05-01 17:14:05
@Author      :Jay Zhang
'''

from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register([User,])
