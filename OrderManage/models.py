#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File        :models.py
@Description :
@DateTiem    :2020-05-20 20:26:59
@Author      :Jay Zhang
'''

from django.db import models

# Create your models here.
class Order(models.Model):
    out_trade_no=models.CharField("OutTradeNo", max_length=50,help_text='string，外部订单号（微信商户订单号）')
    platform=models.IntegerField("Platform",choices=((0,'微信小程序'),(1,'WEB')),default=0)
    user=models.ForeignKey("Base.User", verbose_name="User", related_name="order", on_delete=models.CASCADE)
    address=models.TextField("Address",help_text='收货信息')
    total_price=models.FloatField("TotalPrice",help_text='总价')
    extra=models.TextField("Extra",help_text='备注', null=True, blank=True)
    state=models.IntegerField("State",choices=((0,'待付款'),(1, '待发货'),(2, '待确认'),(3, '退货中'),(4,'退款中'),(5,'已完成')),default=0,help_text='int，订单状态')
    create_time = models.DateTimeField( "CreateTime", auto_now=False, auto_now_add=True,null=True, blank=True,help_text='创建时间')
    edit_time = models.DateTimeField("EditTime", auto_now=True, auto_now_add=False, null=True, blank=True,help_text='编辑时间')
    receive_time = models.DateTimeField("ReceiveTime", auto_now=False, auto_now_add=False, null=True, blank=True,help_text='退货时间')

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

class OrderPackage(models.Model):
    order=models.ForeignKey("Order", verbose_name="Order", related_name="order_package", on_delete=models.CASCADE)
    procuct_sku=models.ForeignKey("Product.ProductSpec", verbose_name="ProductSKU", related_name="order_package", on_delete=models.CASCADE)
    quantity=models.IntegerField("Quantity",help_text="数量")
    class Meta:
        verbose_name = "OrderPackge"
        verbose_name_plural = "OrderPackges"

