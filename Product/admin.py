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
from .models import Product, Category, SkuKey, SkuValue, ProductSku, Spec, SpecContent
from django.utils.safestring import mark_safe
from . import widgets

# Register your models here.

admin.site.site_title = "theMuttonBird"
admin.site.site_header = "theMuttonBird"


class ProductSkuInline(admin.TabularInline):
    model = ProductSku
    extra = 1
    fields = ['sku_value', 'quantity']  # 只显示NameTwo这个字段


class SpecContentInline(admin.TabularInline):
    model = SpecContent
    extra = 1
    fields = ['spec', 'content']  # 只显示NameTwo这个字段


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_category', 'create_time', 'on_sale', 'show_main_image')  # list
    search_fields = ('category', 'name')
    list_per_page = 20
    model = Product

    def get_category(self, obj):
        print('obj', obj)
        return obj.category.name

    get_category.short_description = '类别'

    def show_main_image(self, obj):
        try:
            img = mark_safe('<img src="%s" width="200px" />' % (obj.main_image.url))
        except Exception as e:
            img = ''
        return img

    def get_queryset(self, request):
        qs = self.model._default_manager.get_queryset().filter(is_history=False)
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs

    inlines = [ProductSkuInline, SpecContentInline]

    # def get_form(self, request, obj=None, **args):
    #     defaults = {}
    #     if obj is not None:
    #         if (len(obj.category.spec.all())>0):
    #             self.inlines = [SpecInline]       #设置内联
    #         else:
    #             self.inlines = []                 #如果不是继承，就取消设置

    #     defaults.update(args)
    #     return super(ProductAdmin, self).get_form(request, obj, **defaults)

    formfield_overrides = {
        models.ImageField: {'widget': widgets.UpLoadFile},
    }

    def change_view(self, request, object_id, extra_context=None):
        print('self.fields', self.fields)
        # self.fields.add('show_main_image')  # 将自定义的字段注册到编辑页中
        # self.readonly_fields = ("show_main_image",)  # 务必将该字段设置为仅限可读, 否则抛出异常
        return super(ProductAdmin, self).change_view(request, object_id, extra_context=extra_context)

    # def save_model(self, request, obj, form, change):
    #     # 重写保存方法
    #     # if form.is_valid():
    #     #     album = form.save()

    #     #     if form.cleaned_data['zip'] is not None:
    #     #         zip = zipfile.ZipFile(form.cleaned_data['zip'])
    #     #         for filename in sorted(zip.namelist()):

    #     #             file_name = os.path.basename(filename)
    #     #             if not file_name:
    #     #                 continue

    #     #             data = zip.read(filename)
    #     #             contentfile = ContentFile(data)

    #     #             img = AlbumImage()
    #     #             img.album = album
    #     #             filename = '{0}{1}.jpg'.format(album.slug[:8], str(uuid.uuid4())[-13:])
    #     #             img.alt = filename
    #     #             img.image.save(filename, contentfile)

    #     #             img.thumb.save('thumb-{0}'.format(filename), contentfile)
    #     #             img.save()
    #     #         zip.close()
    #     print('change',change) #如果是修改，则change返回Ture
    #     print('obj',obj)
    #     print('from',form)
    #     if change:
    #         if form.is_valid():
    #             form.save()
    #             obj.is_history=True
    #             obj.save()
    #     else:
    #         super().save_model(request, obj, form, change)


admin.site.register(Product, ProductAdmin)
admin.site.register([Category, SkuKey, SkuValue, ProductSku, Spec, SpecContent])
