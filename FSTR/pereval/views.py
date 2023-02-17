from django.shortcuts import render
from rest_framework import viewsets
from django.db.utils import OperationalError
# Create your views here.
<<<<<<< Updated upstream
=======


class AddedViewset(viewsets.ModelViewSet):
   queryset = Added.objects.all()
   serializer_class = AddedSerializer
   test = '<картинка1>'.encode('utf-8')
   print(test)
   print(type(test))


class UserViewset(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer


class CordsViewset(viewsets.ModelViewSet):
   queryset = Cords.objects.all()
   serializer_class = CordsSerializer


class ImagesViewset(viewsets.ModelViewSet):
   queryset = Images.objects.all()
   serializer_class = ImagesSerializer

>>>>>>> Stashed changes
