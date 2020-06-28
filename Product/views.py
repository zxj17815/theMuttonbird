#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File        :views.py
@Description :
@DateTiem    :2020-05-01 15:02:34
@Author      :Jay Zhang
"""

from django.conf import settings
from django.shortcuts import render
import csv
import json
import requests  # python http请求模块
import datetime
from django.http import HttpResponse
from django.contrib.auth.models import Permission
from django.views import generic as django_generic  # Django Form视图
from rest_framework import permissions  # 权限
from django.contrib.auth.models import Group, Permission
from rest_framework import generics, views, viewsets, mixins  # RestFul API视图
from rest_framework.decorators import action
from rest_framework.response import Response  # Http返回
from rest_framework import filters, status  # 状态码
from rest_framework.pagination import PageNumberPagination  # 分页器
from . import models
from django.db.models import Q, F
from . import serializers


# Create your views here.

class CategoryViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    """
    list:

        获取商品大类列表
        商品类别用于确认商品除基本属性外的各个属性
    retrieve:

        获取单个大类信息
        商品类别用于确认商品除基本属性外的各个属性
    """
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    filterset_fields = '__all__'


class ProductViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    """
    list:

        获取商品列表
    retrieve:

        获取单个大类信息
        商品属性包含基本属性和自定义属性（spec_content）和商品SKU库存（product_sku）
    """
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    queryset = models.Product.objects.filter(is_history=False).all()
    serializer_class = serializers.ProductSerializer
    # filterset_fields = '__all__' 


class ProductSkuViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    """
    list:
        获取商品-属性关系列表
        所有属性
    retrieve:
        获取单个信息
    """
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    queryset = models.ProductSku.objects.all()
    serializer_class = serializers.ProductSkuSerializer
    filterset_fields = '__all__'


class SpecViewSet(viewsets.ModelViewSet):
    """
    list:

        获取商品SkuKey列表
    retrieve:

        获取单个属性SkuKey信息
    create:

        新增商品属性
        新增时直接同步新增SkuKey（属性值）
    update:

        更新大类
        同步新增|删除SkuKey
    partial_update:

        部分更新
    destroy:

        删除资源
    """
    # permission_classes = [permissions.DjangoModelPermissions]
    queryset = models.SkuKey.objects.all()
    serializer_class = serializers.SkuKeySerializer
    filterset_fields = '__all__'


class SkuValueViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """
    list:
        获取属性值列表
    """
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    queryset = models.SkuValue.objects.all()
    serializer_class = serializers.SkuValueSerializer
    filterset_fields = '__all__'
