from .serializers import *
from rest_framework import viewsets
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