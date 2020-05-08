from django.urls import include, path, re_path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'category', views.CategoryViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'product_spec', views.ProductSpecViewSet)
router.register(r'spec', views.SpecViewSet)
router.register(r'spec_info', views.SpecInfoViewSet)

app_name = 'Product'

urlpatterns = [
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # 模型路由
    re_path(r'^(?P<version>(v1|v2))/', include(router.urls)),
]