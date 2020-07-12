import requests
import json

from django.http import HttpResponse
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, views, viewsets, mixins, permissions  # RestFul API视图
# 引入token应用，用于手动签发token
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.response import Response  # 返回
from .access_key import wx_key
from . import models, serializers
from Base import models as Base_models
# 微信小程序的appid和secret
APPID = wx_key.MINIPROGRAM['APP_ID']
SECRET = wx_key.MINIPROGRAM['SECRET']


# Create your views here.
class WxMiniProgramLogin(viewsets.GenericViewSet, mixins.CreateModelMixin):
    """
    微信小程序登录接口
    """
    # permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.DjangoModelPermissions]
    queryset = models.WeUser.objects.all()
    serializer_class = serializers.WeUserSerializer

    @swagger_auto_schema(operation_summary="微信小程序登录，创建Token获取", request_body=serializers.GetTokenSerializer,
                         operation_description="code小程序wx.login的code;user_info为小程序获取的userInfo")
    def create(self, request, *args, **kwargs):
        user_info_ser = serializers.GetTokenSerializer(data=request.data)
        user_info_ser.is_valid(raise_exception=True)
        res = requests.get('https://api.weixin.qq.com/sns/jscode2session',
                           {
                               "appid": APPID,
                               "secret": SECRET,
                               "js_code": user_info_ser.data['js_code'],
                               "grant_type": "authorization_code"
                           }
                           )
        data = json.loads(res.content.decode('utf-8'))
        if 'openid' in data:
            openid = data["openid"]
            userInfo = user_info_ser.data["user_info"]
            obj_weuser = models.WeUser.objects.filter(open_id=openid).first()
            if not obj_weuser:
                # 新增系统用户
                user = Base_models.User.objects.create()
                # 新增WeChat用户
                models.WeUser(user=user, open_id=openid, nick_name=userInfo['nickName'],
                              avatar_url=userInfo['avatarUrl'], city=userInfo['city'],
                              province=userInfo['province'], country=userInfo['country'], gender=userInfo['gender'],
                              language=userInfo['language']).save()
                token = get_tokens_for_user(user)
                return HttpResponse(json.dumps(token), content_type="application/json,charset=utf-8")
            else:
                user = obj_weuser.user
                # 判断用户名是否相等，不相等则更新数据
                if not user.username == userInfo['nickName']:
                    # 更新weuser表
                    obj_weuser.nickName = userInfo['nickName']
                    obj_weuser.avatar_url = userInfo['avatarUrl']
                    obj_weuser.city = userInfo['city']
                    obj_weuser.province = userInfo['province']
                    obj_weuser.country = userInfo['country']
                    obj_weuser.gender = userInfo['gender']
                    obj_weuser.language = userInfo['language']
                    obj_weuser.save()
                token = get_tokens_for_user(user)
                return HttpResponse(json.dumps(token), content_type="application/json,charset=utf-8")
        else:
            return Response(data)


def get_tokens_for_user(user):
    """手动签发token方法，传入一个用户
    """

    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
