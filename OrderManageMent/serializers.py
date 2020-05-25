#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File        :serializers.py
@Description :
@DateTiem    :2020-05-01 12:02:50
@Author      :Jay Zhang
'''

import json
from django.conf import settings
from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers
from . import models
from Base import models as Base_models


class OrderPackageSerializer(serializers.ModelSerializer):
    """订单产品 序列化类
    """
    class Meta:
        model = models.OrderPackage
        fields = '__all__'
        depth = 1


class OrderSerializer(WritableNestedModelSerializer):
    """订单 序列化类
    """
    user=serializers.PrimaryKeyRelatedField(queryset=Base_models.User.objects.all())
    class Meta:
        model = models.Order
        fields = '__all__'
        extra_kwargs = {'create_time': {'read_only': True, 'format': '%Y-%m-%d %H:%M:%S'}, 
                        'edit_time': {'read_only': True,'format': '%Y-%m-%d %H:%M:%S'},
                        'receive_time': {'read_only': True, 'format': '%Y-%m-%d %H:%M:%S'}}
        depth = 1


class RefundPackageSerializer(serializers.ModelSerializer):
    """退款订单产品 序列化类
    """
    class Meta:
        model = models.RefundPackage
        fields = '__all__'
        depth = 1


class RefundSerializer(WritableNestedModelSerializer):
    """退款订单 序列化类
    """
    class Meta:
        model = models.Refund
        fields = '__all__'
        extra_kwargs = {'create_time': {'read_only': True, 'format': '%Y-%m-%d %H:%M:%S'},
                        'edit_time': {'read_only': True, 'format': '%Y-%m-%d %H:%M:%S'}}
        depth = 1
