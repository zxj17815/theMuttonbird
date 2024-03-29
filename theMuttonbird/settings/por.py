#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File        :dev.py
@Description :生产环境settings配置
@DateTiem    :2020-05-01 15:12:51
@Author      :Jay Zhang
'''

from .base import *

DEBUG = False

WSGI_APPLICATION = 'theMuttonbird.wsgi_por.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'theMuttonbird',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'CHARSET': 'utf8',
        'ATOMIC_REQUESTS': True,
        'OPTIONS': {'charset': 'utf8mb4'},
    },
}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'upload')
MEDIA_URL = '/media/'
