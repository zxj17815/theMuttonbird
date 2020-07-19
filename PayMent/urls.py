from django.urls import include, path, re_path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'we_chat_pay', views.WeChatPay)
router.register(r'we_chat_pay_call_back', views.WeChatPayCallBack)

app_name = 'PayMent'

urlpatterns = [
    # 模型路由
    re_path(r'^(?P<version>(v1|v2))/', include(router.urls)),
]
