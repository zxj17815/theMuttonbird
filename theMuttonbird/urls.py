"""theMuttonbird URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework.documentation import include_docs_urls  # 自带api文档
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Docs info

schema_view = get_schema_view(
    openapi.Info(
        title="灰鹱商店Api",
        default_version='v1',
        description="灰鹱商店Api",
        terms_of_service="https://github.com/zxj17815/theMuttonbird",
        contact=openapi.Contact(email="hades922@outlook.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('docs/', include_docs_urls(title='FS API文档')),
                  # path('base/', include('Base.urls')),
                  path('product/', include('Product.urls')),
                  path('order/', include('OrderManageMent.urls')),
                  path('pay/', include('PayMent.urls')),
                  path('cstomer/', include('CustomerManageMent.urls')),

                  re_path(r'^swagger(?P<format>\.json|\.yaml)$',
                          schema_view.without_ui(cache_timeout=0), name='schema-json'),
                  re_path(r'^swagger/$', schema_view.with_ui('swagger',
                                                             cache_timeout=0), name='schema-swagger-ui'),
                  re_path(r'^redoc/$', schema_view.with_ui('redoc',
                                                           cache_timeout=0), name='schema-redoc'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
