from .serializers import *
from rest_framework import viewsets
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import response, schemas
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# Create your views here.


class AddedViewset(viewsets.ModelViewSet):
   queryset = Added.objects.all()
   serializer_class = AddedSerializer


class UserViewset(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer


class CordsViewset(viewsets.ModelViewSet):
   queryset = Cords.objects.all()
   serializer_class = CordsSerializer


class ImagesViewset(viewsets.ModelViewSet):
   queryset = Images.objects.all()
   serializer_class = ImagesSerializer


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)