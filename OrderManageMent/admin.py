#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File        :admin.py
@Description :
@DateTiem    :2020-05-08 13:34:47
@Author      :Jay Zhang
'''

from django.contrib import admin
from django.db import models
from .models import *
from django.utils.safestring import mark_safe
# Register your models here.

admin.site.site_title = "theMuttonBird"
admin.site.site_header = "theMuttonBird"

class OrderPackageSpecInline(admin.TabularInline):
    model = OrderPackage
    extra=1
    # fields = ['speninfo']    #只显示NameTwo这个字段

class OrderAdmin(admin.ModelAdmin):
    list_display = ('out_trade_no','platform','address','total_price','create_time') # list
    search_fields = ['out_trade_no']
    list_per_page = 20
    model=Order

    inlines = [OrderPackageSpecInline]

    readonly_fields = ['state','extra',"receive_time"]

    def change_view(self, request, object_id, extra_context=None):
        # self.fields.add('show_main_image')  # 将自定义的字段注册到编辑页中
        self.readonly_fields = ['state','extra',"receive_time"]  # 务必将该字段设置为仅限可读, 否则抛出异常
        return super(OrderAdmin, self).change_view(request, object_id, extra_context=extra_context)

admin.site.register(Order,OrderAdmin)
# admin.site.register([Category,Spec,SpecInfo,ProductSpec])

class RefundPackageSpecInline(admin.TabularInline):
    model = RefundPackage
    extra=1
    # fields = ['speninfo']    #只显示NameTwo这个字段

class RefundAdmin(admin.ModelAdmin):
    list_display = ('out_refund_no','refund_type','price','state','create_time') # list
    search_fields = ['out_refund_no']
    list_per_page = 20
    model=Refund

    inlines = [RefundPackageSpecInline]

    readonly_fields = ["images",'extra','state',]

    def change_view(self, request, object_id, extra_context=None):
        self.readonly_fields = ["images",'extra','state',]
        return super(RefundAdmin, self).change_view(request, object_id, extra_context=extra_context)

admin.site.register(Refund,RefundAdmin)