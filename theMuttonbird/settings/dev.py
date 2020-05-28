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

WSGI_APPLICATION = 'theMuttonbird.wsgi_dev.application'

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

MEDIA_ROOT = os.path.join(BASE_DIR, 'upload') # 注意此处不要写成列表或元组的形式
MEDIA_URL = '/media/' # 配置 MEDIA_URL 作为公用 URL，指向上传文件的基本路径