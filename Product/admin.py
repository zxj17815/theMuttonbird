#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File        :admin.py
@Description :
@DateTiem    :2020-05-08 13:34:47
@Author      :Jay Zhang
'''

from django.contrib import admin
from .models import Product,Category,Spec,SpecInfo,ProductSpec
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['code','category','name','stock','create_time',] # list
    search_fields = ('category','name')
    list_per_page = 20

    def get_queryset(self, request):
        qs = self.model._default_manager.get_queryset().filter(is_history=False)
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs
admin.site.register(Product,ProductAdmin)
admin.site.register([Category,Spec,SpecInfo,ProductSpec])