from django.shortcuts import render
from rest_framework import generics, views, viewsets, mixins  # RestFul API视图


# 内部方法
def _get_wx_pay_call_back_url(request):
    """返回微信支付回调地址"""
    return 'https://{}/payment/v1/pay_call_back/'.format(request.META['HTTP_HOST'])


# Create your views here.
# TODO 添加微信支付方式

class WeChatPay(generics.CreateAPIView):
    pass
