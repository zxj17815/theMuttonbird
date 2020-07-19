"""
@File        :serializers.py
@Description :
@DateTiem    :2020-05-01 12:02:50
@Author      :Jay Zhang
"""
import time

from rest_framework import serializers

from OrderManageMent import models as OrderManageMent_models


class WeChatPaySerializer(serializers.Serializer):
    """微信支付订单数据"""
    order = serializers.PrimaryKeyRelatedField(write_only=True, queryset=OrderManageMent_models.Order.objects.all(),
                                               help_text="Order的ID")

    def validate_order(self, order):
        if not self.context['request'].user == order.user:
            raise serializers.ValidationError('This order does not belong to this user')
        # 判断是否已经付款
        if order.state >= 1:
            raise serializers.ValidationError('This order has been paid')
        return order

    def to_representation(self, instance):
        return instance


class WeChatPayReturnSerializer(serializers.Serializer):
    """微信支付返回数据"""
    timeStamp = serializers.CharField(read_only=True, help_text='时间戳', default=str(int(time.time())))
    nonceStr = serializers.CharField(read_only=True, help_text='nonce_str')
    package = serializers.CharField(read_only=True, help_text='prepay_id=prepay_id')
    signType = serializers.CharField(read_only=True, help_text='MD5')
    paySign = serializers.CharField(read_only=True, help_text='paySign')


class PayCallBack(serializers.Serializer):
    """支付回调序列化
    """
    appid = serializers.CharField(required=False)
    coupon_type = serializers.CharField(required=False)
    nonce_str = serializers.CharField(required=False)
    trade_type = serializers.CharField(required=False)
    time_end = serializers.CharField(required=False)
    sub_mch_id = serializers.CharField(required=False)
    sign = serializers.CharField(required=False)
    out_trade_no = serializers.CharField(required=False)
    attach = serializers.CharField(required=False)
    mch_id = serializers.CharField(required=False)
    coupon_count = serializers.CharField(required=False)
    coupon_id = serializers.CharField(required=False)
    transaction_id = serializers.CharField(required=False)
    coupon_fee_0 = serializers.CharField(required=False)
    total_fee = serializers.FloatField(required=False)
    fee_type = serializers.CharField(required=False)
    result_code = serializers.CharField(required=False)
    is_subscribe = serializers.CharField(required=False)
    openid = serializers.CharField(required=False)
    return_code = serializers.CharField()
    bank_type = serializers.CharField(required=False)
