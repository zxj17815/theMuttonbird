from django.db import models
from datetime import datetime


# Create your models here.
class WeChatMiniProgramToken(models.Model):
    """微信小程序的access_token
    """
    app_id = models.CharField(max_length=128, blank=True, null=True, verbose_name='AppId')  # appid
    expires_in = models.DateTimeField(verbose_name='ExpiresIn',
                                      default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), auto_now=False,
                                      auto_now_add=False)  # 过期时间
    token = models.CharField(max_length=255, unique=True, blank=True, null=True, verbose_name='Token',
                             db_index=True)  # access_token 这里要注意长度，太短存储会失败 token官方给出的长度是512个字符空间

    class Meta:
        verbose_name = '小程序access_token信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.app_id
