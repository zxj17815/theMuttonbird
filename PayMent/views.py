import datetime
import time
import requests
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, views, viewsets, mixins, permissions, status  # RestFul API视图
from rest_framework.response import Response  # 返回
from rest_framework_xml.parsers import XMLParser  # xml获取
from rest_framework_xml.renderers import XMLRenderer  # xml获取
from OrderManageMent import models as OrderManageMent_models
from . import serializers
# 内部方法
from .tools.wx_payment import PayMent


def _get_wx_pay_call_back_url(request):
    """返回微信支付回调地址"""
    return 'https://{}/payment/v1/pay_call_back/'.format(request.META['HTTP_HOST'])


# Create your views here.
class WeChatPay(viewsets.GenericViewSet, mixins.CreateModelMixin):
    """微信支付接口"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = OrderManageMent_models.Order.objects.all()

    @swagger_auto_schema(operation_summary="微信支付", request_body=serializers.WeChatPaySerializer,
                         responses={200: serializers.WeChatPayReturnSerializer},
                         operation_description="下单后,据返回的订单信息请求本接口")
    def create(self, request, *args, **kwargs):
        serializer = serializers.WeChatPaySerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        weuser = request.user.we_user  # 微信用户
        order = serializer.data['order']
        body = str(order.order_package.all()[0].product_sku.product.name) + (
            '等商品' if len(order.order_package.all()) > 1 else '')  # 统一下单-商品 string(128)
        price = 0  # 订单总价（下单商品*数量*单价）
        for item in order.order_package.all():
            price = price + (item.product_sku.product.price * item.quantity)
        xml = PayMent().get_bodyData(openid=weuser.open_id, client_ip=request.META['REMOTE_ADDR'],
                                     notify_url=_get_wx_pay_call_back_url(request), body=body, price=int(price),
                                     out_trade_no=order.out_trade_no)
        # return Response(xml)
        head = {"Content-Type": "text/xml; charset=UTF-8", 'Connection': 'close'}
        res = requests.post('https://api.mch.weixin.qq.com/pay/unifiedorder', data=xml, headers=head)
        xml = PayMent().xml_to_dict(xml)
        res = PayMent().xml_to_dict(res.text.encode('iso-8859-1').decode('utf8'))
        if res['return_code'] == 'FAIL':
            return Response(res, status=status.HTTP_400_BAD_REQUEST)
        if res['result_code'] == 'SUCCESS':
            # 统一下单成功,Order添加
            order.out_trade_no = xml['out_trade_no']
            order.save()
            # 返回信息给小程序支付
            time_stamp = int(time.time())
            paySign = PayMent().get_paysign(res['prepay_id'], time_stamp, xml['nonce_str'])
            res_data = {
                'timeStamp': str(time_stamp),
                'nonceStr': xml['nonce_str'],
                'package': 'prepay_id=' + res['prepay_id'],
                'signType': 'MD5',
                'paySign': paySign
            }
            return Response(res_data)
        else:
            head = {"charset=UTF-8"}
            return Response(res, status=status.HTTP_400_BAD_REQUEST)


class WeChatPayCallBack(viewsets.GenericViewSet, mixins.CreateModelMixin):
    # TODO: 申请一个地址测试付款，添加付款回调接口改变订单状态
    """后台-支付成功回调"""
    renderer_classes = [XMLRenderer]
    parser_classes = [XMLParser]

    def create(self, request, *args, **kwargs):
        log = open('pay_call_back.log', 'r+')
        log.read()
        _xml = request.body
        # 拿到微信发送的xml请求 即微信支付后的回调内容
        xml = str(_xml, encoding="utf-8")
        xml = PayMent().xml_to_dict(xml)
        serializer = serializers.PayCallBack(xml)
        data = serializer.data
        log.write('\n' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S WeChatPayCallBack:\n') + str(data))
        log.close()
        if data['return_code'] == 'SUCCESS' and data['result_code'] == 'SUCCESS':
            out_trade_no = data['out_trade_no']  # 商户订单号
            order = OrderManageMent_models.Oreder.objects.get(out_trade_no=out_trade_no)
            if order:
                order.state = 1
                order.save()
        res = {
            "return_code": "SUCCESS",
            "return_msg": "OK"
        }
        return Response(res)
