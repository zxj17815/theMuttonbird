from django.conf import settings
from django.shortcuts import render
import csv
import json
import requests  # python http请求模块
import datetime
from django.http import HttpResponse
from django.contrib.auth.models import Permission
from django.views import generic as django_generic  # Django Form视图
# from rest_framework import permissions  # 权限
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


class UserViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin):
    """
    基本用户表
    """
    # permission_classes = [permission.WeChatWorkPermission]
    # permission_classes = [ReadOnly]
    # authentication_classes = [auth.WeChatWorkAuthentication]
    pagination_class = P20
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    # filter_backends = [filters.OrderingFilter]
    # ordering_fields = '__all__'
    filterset_fields = '__all__'

    # def get_serializer_class(self):
    #     if self.action == 'batch_pass':
    #         return serializers.BatchPass
    #     return serializers.Z98CgjySerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    # permission_classes = [permissions.DjangoModelPermissions]
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer

class PermissionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows permission to be viewed or edited.
    """
    # permission_classes = [permissions.IsAdminUser]
    queryset = Permission.objects.all()
    serializer_class = serializers.PermissionSerializer
    filterset_fields = '__all__' 