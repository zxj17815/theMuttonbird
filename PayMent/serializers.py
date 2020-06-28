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
        return order


class WeChatPayReturnSerializer(serializers.Serializer):
    """微信支付返回数据"""
    timeStamp = serializers.CharField(read_only=True, help_text='时间戳', default=str(int(time.time())))
    nonceStr = serializers.CharField(read_only=True, help_text='nonce_str')
    package = serializers.CharField(read_only=True, help_text='prepay_id=prepay_id')
    signType = serializers.CharField(read_only=True, help_text='MD5')
    paySign = serializers.CharField(read_only=True, help_text='paySign')
