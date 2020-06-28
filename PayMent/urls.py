from django.urls import include, path, re_path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'wechat_pay', views.WeChatPay)

app_name = 'PayMent'

urlpatterns = [
    # 模型路由
    re_path(r'^(?P<version>(v1|v2))/', include(router.urls)),
]