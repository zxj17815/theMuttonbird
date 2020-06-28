from django.conf import settings

from django.db import models
from Base import models as Base_models


# Create your models here.
class WeUser(models.Model):
    """微信用户 model.

    Attributes:
        user: 默认用户
        open_id: 对应微信用户的独立OpenId
        union_id: 微信开放平台下统一id
        ...: 微信用户的信息
        user_address: 微信用户收货地址信息
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='we_user', on_delete=models.CASCADE)
    # id=models.AutoField(primary_key=True)
    open_id = models.CharField("OpenId", max_length=250)
    union_id = models.CharField("UnionID", max_length=250, null=True, blank=True)
    nick_name = models.CharField("NickName", max_length=50)
    avatar_url = models.URLField("AvatarUrl", max_length=300)
    city = models.CharField("City", max_length=50)
    province = models.CharField("Province", max_length=50)
    country = models.CharField("Country", max_length=50)
    gender = models.IntegerField("Gender", choices=((1, 'man'), (2, 'woman')))
    language = models.CharField("Language", max_length=50)
    user_address = models.TextField("UserAddress", null=True, blank=True)
