from django.urls import include, path, re_path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'order', views.OrderViewSet)
router.register(r'refund', views.RefundViewSet)

app_name = 'OrderManageMent'

urlpatterns = [
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # 模型路由
    re_path(r'^(?P<version>(v1|v2))/', include(router.urls)),
]
