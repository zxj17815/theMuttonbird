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
from drf_yasg.utils import swagger_auto_schema

# Create your views here.


class OrderViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    # permission_classes = [permissions.DjangoModelPermissions]
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    filterset_fields = '__all__'

    @swagger_auto_schema(operation_summary="新增订单", request_body=serializers.OrderSerializer, operation_description="下单后,根据返回的订单信息请求支付接口")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class RefundViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    # permission_classes = [permissions.DjangoModelPermissions]
    queryset = models.Refund.objects.all()
    serializer_class = serializers.RefundSerializer
    filterset_fields = ['id', 'order']
