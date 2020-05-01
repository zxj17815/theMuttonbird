import json
from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group, Permission
from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    """部门 序列化类
    """
    class Meta:
        model = models.User
        fields = '__all__'
        # exclude = ['user_type',]
        depth = 3

class GroupSerializer(serializers.ModelSerializer):
    """原生 组 序列化类
    """
    permissions=serializers.PrimaryKeyRelatedField(many=True,read_only=False,queryset=Permission.objects.all(),help_text='数组，权限id')
    class Meta:
        model = Group
        fields = '__all__'
        depth = 1
        extra_kwargs = {
            'name': {'help_text': '组名'},
        }

class PermissionSerializer(serializers.ModelSerializer):
    """原生 权限 序列化类
    """
    class Meta:
        model = Permission
        fields = '__all__'
        depth = 3  