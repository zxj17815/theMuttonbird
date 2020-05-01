from django.urls import include, path, re_path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'group', views.GroupViewSet)
router.register(r'permission', views.PermissionViewSet)

app_name = 'Base'

urlpatterns = [
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # 模型路由
    re_path(r'^(?P<version>(v1|v2))/', include(router.urls)),
]