from django.urls import include, path, re_path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'wx_mini_program_login', views.WxMiniProgramLogin)

app_name = 'CustomerManageMent'

urlpatterns = [
    # 模型路由
    re_path(r'^(?P<version>(v1|v2))/', include(router.urls)),
]
