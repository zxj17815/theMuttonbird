#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File        :models.py
@Description :
@DateTiem    :2020-05-20 20:26:59
@Author      :Jay Zhang
"""
import os
import random
import string
import uuid
from django.db import models


def user_directory_path(instance, filename):
    """图片上传路径"""
    ext = filename.split('.').pop()
    filename = '{0}.{1}'.format('refund_' + ''.join(random.sample(string.ascii_letters + string.digits, 12)), ext)
    # 系统路径分隔符差异，增强代码重用性
    return os.path.join('images/Refund/' + instance.id, filename)


# Create your models here.
class Order(models.Model):
    """订单"""
    id = models.UUIDField('Id', primary_key=True, auto_created=True, default=uuid.uuid4,
                          editable=False, help_text="唯一编码")
    out_trade_no = models.CharField("OutTradeNo", max_length=50, null=True, blank=True, help_text='外部支付单号（如微信平台商户订单号）')
    platform = models.IntegerField("Platform", choices=((0, '微信小程序'), (1, 'WEB')), default=0)
    user = models.ForeignKey("Base.User", verbose_name="User", related_name="order", on_delete=models.CASCADE)
    address = models.TextField("Address", help_text='收货信息')
    total_price = models.FloatField("TotalPrice", help_text='总价')
    extra = models.TextField("Extra", help_text='备注', null=True, blank=True)
    state = models.IntegerField("State",
                                choices=((0, '待付款'), (1, '待发货'), (2, '待确认'), (3, '退货中'), (4, '退款中'), (5, '已完成')),
                                default=0, help_text='订单状态[0:待付款,1:待发货,2:待确认,3:退货中,4:退款中,5:已完成]')
    create_time = models.DateTimeField("CreateTime", auto_now=False, auto_now_add=True, null=True, blank=True,
                                       help_text='创建时间')
    edit_time = models.DateTimeField("EditTime", auto_now=True, auto_now_add=False, null=True, blank=True,
                                     help_text='编辑时间')
    receive_time = models.DateTimeField("ReceiveTime", auto_now=False, auto_now_add=False, null=True, blank=True,
                                        help_text='退货时间')

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class OrderPackage(models.Model):
    """订单商品"""
    id = models.UUIDField('Id', primary_key=True, auto_created=True, default=uuid.uuid4,
                          editable=False, help_text="唯一编码")
    order = models.ForeignKey("Order", verbose_name="Order", related_name="order_package", on_delete=models.CASCADE)
    product_sku = models.ForeignKey("Product.ProductSku", verbose_name="ProductSKU", related_name="order_package",
                                    on_delete=models.CASCADE)
    quantity = models.IntegerField("Quantity", help_text="数量")

    class Meta:
        verbose_name = "OrderPackge"
        verbose_name_plural = "OrderPackges"


class Refund(models.Model):
    """退货单"""
    id = models.UUIDField('Id', primary_key=True, auto_created=True, default=uuid.uuid4,
                          editable=False, help_text="唯一编码")
    order = models.ForeignKey("Order", verbose_name="Order", related_name="refund", on_delete=models.CASCADE)
    out_refund_no = models.CharField("OutRefundNo", max_length=50, help_text='退款单号', null=True, blank=True)
    extra = models.TextField("Extra", help_text='退货理由')
    images = models.ImageField("Image", blank=True, null=True, upload_to=user_directory_path, height_field=None,
                               width_field=None, max_length=None, help_text='退货附图')
    price = models.FloatField("Price", help_text='待退款金额')
    refund_type = models.IntegerField("RefundType", choices=((0, '仅退款'), (1, '退货退款')), default=0,
                                      help_text='退回类型[0:仅退款,1:退货退款]')
    state = models.IntegerField("State", choices=((0, '待通过'), (1, '待退货'), (2, '待确认'), (3, '已完成'), (4, '未通过')),
                                default=0, help_text='状态[0:待通过,1:待退货,2:待确认,3:已完成,4:未通过]')
    re_extra = models.TextField("ReExtra", help_text='商家答复信息', null=True, blank=True)
    customer_express = models.TextField("CustomerExpress", null=True, blank=True, help_text='客户寄出的快递单号')
    create_time = models.DateTimeField("CreateTime", auto_now=False, auto_now_add=True, null=True, blank=True, )
    edit_time = models.DateTimeField("EditTime", auto_now=True, auto_now_add=False, null=True, blank=True, )

    class Meta:
        verbose_name = "Refund"
        verbose_name_plural = "Refunds"


class RefundPackage(models.Model):
    """退货商品"""
    id = models.UUIDField('Id', primary_key=True, auto_created=True, default=uuid.uuid4,
                          editable=False, help_text="唯一编码")
    refund = models.ForeignKey("Refund", verbose_name="Refund", related_name="refund_package", on_delete=models.CASCADE)
    order_package = models.ForeignKey("OrderPackage", verbose_name="OrderPackage", related_name="refund_package",
                                      on_delete=models.CASCADE)
    quantity = models.IntegerField("Quantity", help_text="数量")

    class Meta:
        verbose_name = "RefundPackage"
        verbose_name_plural = "RefundPackages"
