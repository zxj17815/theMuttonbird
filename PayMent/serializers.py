"""
@File        :serializers.py
@Description :
@DateTiem    :2020-05-01 12:02:50
@Author      :Jay Zhang
"""

import json
from abc import ABC

from django.conf import settings
from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers
from . import models
from OrderManageMent import models as OrderManageMent_models
from Product import models as Product_models


class WeChatPaySerializer(serializers.Serializer, ABC):
    """微信支付数据"""
    order = serializers.PrimaryKeyRelatedField(read_only=False, queryset=OrderManageMent_models.Order.objects.all(),
                                               help_text="Order的ID")
    # TODO 需要先在客户管理模块里添加微信用户模型，根据绑定的Base用户获取到微信用户obj到openid用于微信支付
