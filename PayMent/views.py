from django.shortcuts import render

# 内部方法
def _get_wx_wx_pay_call_back_url(request):
    '''返回微信支付回调地址'''
    return 'https://{}/payment/v1/pay_call_back/'.format(request.META['HTTP_HOST'])

# Create your views here.
