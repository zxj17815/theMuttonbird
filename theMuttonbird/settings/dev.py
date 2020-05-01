#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File        :dev.py
@Description :
@DateTiem    :2020-05-01 15:39:50
@Author      :Jay Zhang
'''

from .base import *
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'theMuttonbird',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'CHARSET': 'utf8',
        'ATOMIC_REQUESTS': True
    },
}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)