#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File        :serializers.py
@Description :
@DateTiem    :2020-05-01 12:02:50
@Author      :Jay Zhang
"""
import datetime
import json
from django.conf import settings
from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers
from . import models
from Base import models as Base_models
from Product import models as Product_models


class OrderPackageSerializer(serializers.ModelSerializer):
    """订单产品 序列化类
    """
    product_sku = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Product_models.ProductSku.objects.all())

    class Meta:
        model = models.OrderPackage
        fields = '__all__'
        extra_kwargs = {'product_sku': {'required': True}}
        depth = 1

    def validate(self, attrs):
        # 检查是否超过库存
        if attrs['product_sku'].quantity - attrs['quantity'] < 0:
            raise serializers.ValidationError(
                {'product_sku': '{},The stock quantity is not enough'.format(attrs['product_sku'].id)})
        return super().validate(attrs)

    def create(self, validated_data):
        # 在新增时把sku的库存树扣除
        product_sku = validated_data['product_sku']
        product_sku.quantity = product_sku.quantity - validated_data['quantity']
        product_sku.save()
        return super().create(validated_data)


class OrderSerializer(WritableNestedModelSerializer):
    """订单 序列化类
    """
    order_package = OrderPackageSerializer(
        many=True, required=True, allow_null=False)
    user = serializers.PrimaryKeyRelatedField(
        queryset=Base_models.User.objects.all())

    def create(self, validated_data):
        # 在执行新增前先把外部订单号字段生成写入validated_data
        # 根据当前系统时间来生成商品订单号。时间精确到微秒
        date = datetime.datetime.now()
        validated_data['out_trade_no'] = date.strftime("%Y%m%d%H%M%S%f")
        price = 0  # 订单总价（下单商品*数量*单价）
        for item in validated_data["order_package"]:
            print(item)
            price = price + (item["product_sku"].product.price * item["quantity"])
        validated_data['total_price'] = int(price)
        return super().create(validated_data)

    class Meta:
        model = models.Order
        fields = '__all__'
        extra_kwargs = {'total_price': {'required': False},
                        'create_time': {'read_only': True, 'format': '%Y-%m-%d %H:%M:%S'},
                        'edit_time': {'read_only': True, 'format': '%Y-%m-%d %H:%M:%S'},
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
