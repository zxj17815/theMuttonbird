#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File        :views.py
@Description :
@DateTiem    :2020-05-01 15:02:34
@Author      :Jay Zhang
'''

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

class P20(PageNumberPagination):
    #每页显示的数据条数
    page_size =20 #每页显示的多少

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    '''
    list:
        获取商品大类列表  
        商品类别用于确认商品除基本属性外的各个属性
    retrieve:
        获取单个大类信息  
        商品类别用于确认商品除基本属性外的各个属性
    create:
        新增大类  
        spec选择属性，father指定父类
    update:
        更新大类  
        全部数据
    partial_update:
        部分更新
    destroy:
        删除资源
    '''
    # permission_classes = [permissions.DjangoModelPermissions]
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    filterset_fields = '__all__' 

class ProductViewSet(viewsets.ModelViewSet):
    '''
    list:
        获取商品列表 
        商品有商品历史记录
    retrieve:
        获取单个大类信息  
        商品属性包含基本属性和自定义属性
    create:
        新增商品
        商品新增时需要不同类别定义的属性
    update:
        更新大类  
        更新商品
    partial_update:
        部分更新
    destroy:
        删除资源
    '''
    # permission_classes = [permissions.DjangoModelPermissions]
    queryset = models.Product.objects.filter(is_history=False).all()
    serializer_class = serializers.ProductSerializer
    # filterset_fields = '__all__' 

class ProductSpecViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,mixins.RetrieveModelMixin):
    '''
    list:
        获取商品-属性关系列表 
        所有属性
    retrieve:
        获取单个信息  
    '''
    # permission_classes = [permissions.DjangoModelPermissions]
    queryset = models.ProductSpec.objects.all()
    serializer_class = serializers.ProductSpecSerializer
    filterset_fields = '__all__' 

class SpecViewSet(viewsets.ModelViewSet):
    '''
    list:
        获取商品属性列表 
    retrieve:
        获取单个属性大类信息  
    create:
        新增商品属性
        新增时直接同步新增SpecInfo（属性值）
    update:
        更新大类  
        同步新增|删除SpecInfo
    partial_update:
        部分更新
    destroy:
        删除资源
    '''
    # permission_classes = [permissions.DjangoModelPermissions]
    queryset = models.Spec.objects.all()
    serializer_class = serializers.SpecSerializer
    filterset_fields = '__all__' 

class SpecInfoViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    '''
    list:
        获取属性值列表 
    '''
    # permission_classes = [permissions.DjangoModelPermissions]
    queryset = models.SpecInfo.objects.all()
    serializer_class = serializers.SpecInfoSerializer
    filterset_fields = '__all__' 