import json
from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group, Permission
from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers
from . import models


class WeUserSerializer(serializers.ModelSerializer):
    """微信用户 序列化类
    """
    avatarUrl = serializers.CharField(source='avatar_url')
    nickName = serializers.CharField(source='nick_name')

    class Meta:
        model = models.WeUser
        fields = ["avatarUrl", "nickName", "city", "province", "country", "gender", "language", "user_address"]
        # exclude = ["user", "open_id", "union_id"]
        # extra_kwargs = {'avatar_url': {'label': "avatarUrl"}, 'nick_name': {'label': "nickName"}}
        depth = 3


class GetTokenSerializer(serializers.Serializer):
    """微信用户获取Token请求参数序列化
    """
    js_code = serializers.CharField(required=True)
    user_info = WeUserSerializer(required=True)
