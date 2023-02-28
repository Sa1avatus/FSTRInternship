"""FSTR URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, permissions
from pereval import views
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = routers.DefaultRouter()
router.register(r'added', views.AddedViewset)
router.register(r'user', views.UserViewset)
router.register(r'cords', views.CordsViewset)
router.register(r'images', views.ImagesViewset)
added = views.AddedViewset.as_view({
    'post': 'create'
})
added_detail = views.AddedViewset.as_view({
    'get': 'retrieve',
    'patch': 'update',
})
added_list = views.AddedViewset.as_view({
    'get': 'list',
})

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('submitData', added, name='added'),
    path('submitData/<int:pk>', added_detail, name='added-detail'),
    path('submitData/', added_list, name='added-list'),
    re_path(r'^swagger(\?P\.json|\.yaml)$', views.schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', views.schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', views.schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
