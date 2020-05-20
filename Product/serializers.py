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


class SpecInfoSerializer(serializers.ModelSerializer):
    """属性值 序列化类
    """
    class Meta:
        model = models.SpecInfo
        fields = ['id', 'name']
        depth = 1

class SpecSerializer(WritableNestedModelSerializer):
    """属性 序列化类
    """
    spec_info = SpecInfoSerializer(many=True, help_text="[spec_info]数组")

    class Meta:
        model = models.Spec
        fields = '__all__'
        # exclude = ['user_type',]
        depth = 1

class ProductSpecSerializer(serializers.ModelSerializer):
    """商品属性 序列化类
    """
    class Meta:
        model = models.ProductSpec
        fields = '__all__'
        # exclude = ['user_type',]
        depth = 3

class CategorySerializer(serializers.ModelSerializer):
    """类别 序列化类
    """
    father = serializers.PrimaryKeyRelatedField(
        many=False, read_only=False, queryset=models.Category.objects.all(), required=False, help_text='int,父类')
    spec = serializers.PrimaryKeyRelatedField(
        many=True, read_only=False, queryset=models.Spec.objects.all(), help_text='int,属性')

    class Meta:
        model = models.Category
        fields = '__all__'
        # exclude = ['user_type',]
        depth = 3


class ProductSerializer(serializers.ModelSerializer):
    """Product 序列化类
    """
    category=serializers.PrimaryKeyRelatedField(
        many=False, read_only=False, queryset=models.Category.objects.all(), help_text='int,类别')  
    
    class Meta:
        model = models.Product
        fields = '__all__'
        # exclude = ['user_type',]
        depth = 3
    def validate(self, data):
        print('data',data)
        # if data['start'] > data['finish']:
        #     raise serializers.ValidationError("finish must occur after start")
        return data