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


class SkuKeySerializer(WritableNestedModelSerializer):
    """SkuKey 序列化类
    """
    class Meta:
        model = models.SkuKey
        fields = ['name']
        depth = 1

class SkuValueSerializer(serializers.ModelSerializer):
    """SkuValue 序列化类
    """
    sku_key=serializers.SlugRelatedField(read_only=True,slug_field='name')
    class Meta:
        model = models.SkuValue
        fields = ['sku_key','name']
        depth = 2

class ProductSkuSerializer(serializers.ModelSerializer):
    """商品SKU 序列化类
    """
    sku_value=SkuValueSerializer(many=True)
    class Meta:
        model = models.ProductSku
        # fields = '__all__'
        exclude = ['product',]
        depth = 3

class SpecContentSerializer(serializers.ModelSerializer):
    """商品属性 序列化类
    """
    spec=serializers.SlugRelatedField(many=False,read_only=True,slug_field='name')
    class Meta:
        model = models.SpecContent
        # fields = '__all__'
        fields = ['spec','content']
        depth = 3

class CategorySerializer(serializers.ModelSerializer):
    """类别 序列化类
    """
    father = serializers.PrimaryKeyRelatedField(
        many=False, read_only=False, queryset=models.Category.objects.all(), required=False, help_text='int,父类')
    spec = serializers.PrimaryKeyRelatedField(
        many=True, read_only=False, queryset=models.SkuKey.objects.all(), help_text='int,属性')

    class Meta:
        model = models.Category
        fields = '__all__'
        # exclude = ['user_type',]
        depth = 3

class ProductSerializer(serializers.ModelSerializer):
    """Product 序列化类
    """
    category=serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=models.Category.objects.all(), help_text='int,类别')  
    product_sku=ProductSkuSerializer(many=True, read_only=False)
    spec_content=SpecContentSerializer(many=True,read_only=True)
    class Meta:
        model = models.Product
        # fields = '__all__'
        exclude = ['create_time','update_time','is_history','on_sale']
        depth = 3