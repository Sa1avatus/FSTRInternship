from .models import *
from rest_framework import serializers
from .exceptions import *
from django.db.utils import OperationalError
from rest_framework.exceptions import NotFound
import base64


class UserSerializer(serializers.ModelSerializer):
    fam = serializers.CharField(source='last_name', label='Surname', allow_blank=True)
    otc = serializers.CharField(source='patronymic_name', label='Patronymic', allow_blank=True)
    name = serializers.CharField(source='first_name', label='Name', allow_blank=True)

    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'fam',
            'otc',
            'phone',
            'email'
        ]
        extra_kwargs = {
            'email': {'validators': []},
        }


class CordsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cords
        fields = [
            'id',
            'latitude',
            'longitude',
            'height'
        ]


class ImagesSerializer(serializers.ModelSerializer):
    data = serializers.CharField(source='img')
    class Meta:
        model = Images
        fields = [
            'date_added',
            'data',
            'title'
        ]


class AddedSerializer(serializers.ModelSerializer):
    connect = serializers.CharField(source='connects', label='Connects', allow_blank=True)
    coords = CordsSerializer(source='cords')
    user = UserSerializer()
    level = serializers.DictField(source='set_levels')
    images = ImagesSerializer(source='added_images', many=True)

    class Meta:
        model = Added
        fields = [
           'id',
           'date_added',
           'user',
           'beauty_title',
           'title',
           'other_titles',
           'connect',
           'coords',
           'status',
           'winter',
           'spring',
           'summer',
           'autumn',
           'level',
           'images',
            ]
        read_only_fields = [
            'id',
            'status',
        ]

    def create(self, request):
        cords = request.pop('cords')
        user = request.pop('user')
        images = request.pop('added_images')
        levels = request.pop('set_levels')
        try:
            user_instance = User.objects.filter(email=user['email']).first()
            if not user_instance:
                user_instance = User.objects.create(**user)
            cords_instance, created = Cords.objects.get_or_create(**cords)
            pass_instance = Added.objects.create(
                user=user_instance,
                cords=cords_instance,
                **request
            )
            pass_instance.set_levels(**levels)
            for image in images: #Временно закомментировано, так как нужно понять как исправить ошибку
                # 'expected bytes-like object, not str'
                #data = base64.encodebytes(image['img'])
                data = image['img'].encode('utf-8')
                #data = base64.b64encode(data)
                #Images.objects.create(added=pass_instance, img=data, title=image['title'])
            return pass_instance
        except OperationalError:
            raise DBConnectException()

    def retrieve(self, request, *args, **kwargs):
        try:
            if not Added.objects.filter(id=kwargs['pk']).exists():
                raise NotFound
            return super().retrieve(request, *args, **kwargs)
        except OperationalError:
            raise DBConnectException()

    def update(self, request, *args, **kwargs):
        try:
            queryset = Added.objects.filter(id=kwargs['pk'])
            if not queryset.exists():
                raise NotFound
            query_object = queryset.first()
            if not query_object.status == 'new':
                raise ObjectStatusException
            response = super().partial_update(request, *args, **kwargs)
            response.data = {
                'status': response.status_code,
                'message': response.status_text,
                'state': 1,
            }
            return response
        except OperationalError:
            raise DBConnectException()
