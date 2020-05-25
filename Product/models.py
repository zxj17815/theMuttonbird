#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File        :models.py
@Description :
@DateTiem    :2020-05-01 08:43:12
@Author      :Jay Zhang
'''
import json
import uuid
import os
import random
import time
import string
from django.db import models

# Custom Field


class JSONField(models.TextField):
    '''Json字段'''
    description = "Json"

    def to_python(self, value):
        v = models.TextField.to_python(self, value)
        try:
            return json.loads(v)['v']
        except:
            pass
        return v

    def get_prep_value(self, value):
        return json.dumps({'v': value})


def user_directory_path(instance, filename):
    '''上传路径'''
    ext = filename.split('.').pop()
    filename = '{0}.{1}'.format(
        instance.name+'-'+''.join(random.sample(string.ascii_letters + string.digits, 12)), ext)
    # 系统路径分隔符差异，增强代码重用性
    return os.path.join('images/Product/'+instance.name, filename)

def ser_id():
    """生成流水号"""
    return str(int(time.time()*1000))+str(int(time.clock()*1000000))

# models


class Product(models.Model):
    '''商品表'''
    id = models.CharField('Id',primary_key=True, auto_created=True, default=ser_id,
                            editable=False,max_length=50, help_text="string(50),流水编码")
    code = models.UUIDField('Code', auto_created=True, default=uuid.uuid4,
                            editable=False, help_text="string(150),商品唯一编码")
    category = models.ForeignKey(
        "Category", verbose_name="Category", related_name='product', on_delete=models.CASCADE)
    name = models.CharField("Name", blank=False, null=False,
                            max_length=150, help_text="string(150),商品名称")
    main_image = models.ImageField("MainImage", blank=True, null=True, upload_to=user_directory_path,
                                   height_field=None, width_field=None, max_length=None, help_text="file,主图")
    image1 = models.ImageField("Image1", blank=True, null=True, upload_to=user_directory_path,
                               height_field=None, width_field=None, max_length=None, help_text="file,图1")
    image2 = models.ImageField("Image2", blank=True, null=True, upload_to=user_directory_path,
                               height_field=None, width_field=None, max_length=None, help_text="file,图2")
    image3 = models.ImageField("Image3", blank=True, null=True, upload_to=user_directory_path,
                               height_field=None, width_field=None, max_length=None, help_text="file,图3")
    image4 = models.ImageField("Image4", blank=True, null=True, upload_to=user_directory_path,
                               height_field=None, width_field=None, max_length=None, help_text="file,图4")
    image5 = models.ImageField("Image5", blank=True, null=True, upload_to=user_directory_path,
                               height_field=None, width_field=None, max_length=None, help_text="file,图5")
    description = models.TextField(
        "Description", blank=True, null=True, help_text="text,详情描述")
    discount = models.FloatField(
        "Discount", blank=True, null=True, help_text="float,折扣")
    on_sale = models.BooleanField(
        "OnSale", default=True, help_text="bool,是否在售")
    create_time = models.DateTimeField(
        "CreateTime", auto_now=False, auto_now_add=True, help_text="datetime,创建时间")
    update_time = models.DateTimeField(
        "UpdateTime", auto_now=True, auto_now_add=False, help_text="datetime,更新时间")
    is_history = models.BooleanField(
        "IsHistory", default=False, help_text="bool,是否历史")

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name


class Category(models.Model):
    '''商品类别'''
    name = models.CharField("Name", unique=True, blank=False,
                            null=False, max_length=50, help_text="string(150),类别名称,unique")
    sku_key = models.ManyToManyField("SkuKey", verbose_name="SkuKey",related_name="category")
    spec = models.ManyToManyField("Spec", verbose_name="Spec",related_name="category")
    father = models.ForeignKey(
        "self", verbose_name="Father", blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "ProductCategory"
        verbose_name_plural = "ProductCategorys"

    def __str__(self):
        return self.name

class Spec(models.Model):
    """商品自定义属性"""
    name=models.CharField("Name", max_length=50)
    class Meta:
        verbose_name = "Spec"
        verbose_name_plural = "Specs"
    
    def __str__(self):
        return self.name

class SpecContent(models.Model):
    '''商品自定义属性值'''
    product = models.ForeignKey("Product", verbose_name="Product",related_name="spec_content", on_delete=models.CASCADE)
    spec=models.ForeignKey("Spec", verbose_name="Spec", related_name="spen_content", on_delete=models.CASCADE)
    content=models.TextField("Content")
    class Meta:
        verbose_name = "SpecContent"
        verbose_name_plural = "SpecContents"

class SkuKey(models.Model):
    '''商品SKU键名表'''
    name = models.CharField("Name", max_length=50, help_text="string(50),属性名")
    class Meta:
        verbose_name = "SkuKey"
        verbose_name_plural = "SkuKeys"

    def __str__(self):
        return self.name

class SkuValue(models.Model):
    '''商品SKU值表'''
    sku_key = models.ForeignKey("SkuKey", verbose_name="SkuKey",
                             related_name="spec_info", on_delete=models.CASCADE)
    name = models.CharField("Name", max_length=50,
                            help_text="string(50),属性值名称")

    class Meta:
        verbose_name = "SkuValue"
        verbose_name_plural = "SkuValue"

    def __str__(self):
        return self.sku_key.name+'-'+self.name

class ProductSku(models.Model):
    '''商品属性SKU-库存'''
    product = models.ForeignKey("Product", verbose_name="Product",related_name="product_sku", on_delete=models.CASCADE)
    sku_value = models.ManyToManyField("SkuValue", verbose_name="SkuValue",related_name="product_sku")
    quantity = models.IntegerField("Quantity", default=0, help_text="int,商品库存")

    class Meta:
        verbose_name = "ProductSku"
        verbose_name_plural = "ProductSkus"
        
    def __str__(self):
        sku=''
        for target_list in self.sku_value.all().values('name'):
            sku=sku+"_"+target_list['name']
        return self.product.name+sku
