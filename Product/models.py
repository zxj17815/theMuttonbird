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
    return json.dumps({'v':value}) 

def user_directory_path(instance, filename):
    '''上传路径'''
    ext = filename.split('.').pop()
    filename = '{0}{1}.{2}'.format(instance.name, instance.identity_card, ext)
    return os.path.join(instance.major.name, filename) # 系统路径分隔符差异，增强代码重用性

# models
class Product(models.Model):
    '''商品表'''
    code=models.UUIDField('Code',auto_created=True, default=uuid.uuid4, editable=False,help_text="string(150),商品唯一编码")
    category=models.ForeignKey("Category", verbose_name="Category",related_name='product', on_delete=models.CASCADE)
    name = models.CharField("Name", blank=False, null=False, max_length=150, help_text="string(150),商品名称")
    main_image=models.ImageField("MainImage", blank=True, null=True,upload_to=user_directory_path, height_field=None, width_field=None, max_length=None,help_text="file,主图")
    image1=models.ImageField("Image1", blank=True, null=True,upload_to=user_directory_path, height_field=None, width_field=None, max_length=None,help_text="file,图1")
    image2=models.ImageField("Image2", blank=True, null=True,upload_to=user_directory_path, height_field=None, width_field=None, max_length=None,help_text="file,图2")
    image3=models.ImageField("Image3", blank=True, null=True,upload_to=user_directory_path, height_field=None, width_field=None, max_length=None,help_text="file,图3")
    image4=models.ImageField("Image4", blank=True, null=True,upload_to=user_directory_path, height_field=None, width_field=None, max_length=None,help_text="file,图4")
    image5=models.ImageField("Image5", blank=True, null=True,upload_to=user_directory_path, height_field=None, width_field=None, max_length=None,help_text="file,图5")
    description=models.TextField("Description",blank=True, null=True,help_text="text,详情描述")
    stock = models.IntegerField("Stock",default=0,help_text="int,商品库存")
    discount = models.FloatField("Discount",blank=True, null=True,help_text="float,折扣")
    on_sale=models.BooleanField("OnSale", default=True ,help_text="bool,是否在售")
    create_time=models.DateTimeField("CreateTime", auto_now=False, auto_now_add=True,help_text="datetime,创建时间")
    update_time=models.DateTimeField("UpdateTime", auto_now=True, auto_now_add=False,help_text="datetime,更新时间")
    is_history=models.BooleanField("IsHistory",default=False,help_text="bool,是否历史")
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

class Category(models.Model):
    '''商品类别'''
    name = models.CharField("Name", unique=True, blank=False, null=False, max_length=50, help_text="string(150),类别名称,unique")
    spec = models.ManyToManyField("Spec", verbose_name="Spec")
    father = models.ForeignKey("self", verbose_name="Father",blank=True, null=True, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "ProductCategory"
        verbose_name_plural = "ProductCategorys"

class Spec(models.Model):
    '''属性类别表spec'''
    name=models.CharField("Name", max_length=50,help_text="string(50),属性名")
    class Meta:
        verbose_name = "Spec"
        verbose_name_plural = "Specs"

class SpecInfo(models.Model):
    '''属性值表spec_info'''
    spec=models.ForeignKey("Spec", verbose_name="Spec",related_name="spec_info", on_delete=models.CASCADE)
    name=models.CharField("Name", max_length=50,help_text="string(50),属性值名称")
    class Meta:
        verbose_name = "SpecInfo"
        verbose_name_plural = "SpecInfos"

class ProductSpec(models.Model):
    product=models.ForeignKey("Product", verbose_name="Product",related_name="product_spec",on_delete=models.CASCADE)
    spec=models.ForeignKey("Spec", verbose_name="Spec",related_name="product_spec",on_delete=models.CASCADE)
    speninfo=models.ForeignKey("SpecInfo", verbose_name="SpecInfo",related_name="product_spec",on_delete=models.CASCADE)
    class Meta:
        verbose_name = "ProductSpec"
        verbose_name_plural = "ProductSpecs"
