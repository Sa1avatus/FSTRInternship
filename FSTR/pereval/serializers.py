from .models import *
from rest_framework import serializers
from .exceptions import *
from django.db.utils import OperationalError
from rest_framework.exceptions import NotFound
import base64
from django.forms import model_to_dict
from drf_writable_nested import WritableNestedModelSerializer


class UserSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    fam = serializers.CharField(source='last_name', label='Surname', allow_blank=True)
    otc = serializers.CharField(source='patronymic_name', label='Patronymic', allow_blank=True)
    name = serializers.CharField(source='first_name', label='Name', allow_blank=True)

    class Meta:
        model = User
        fields = [
            #'id',
            'name',
            'fam',
            'otc',
            'phone',
            'email'
        ]
        extra_kwargs = {
            'email': {'validators': []},
        }


class CordsSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):

    class Meta:
        model = Cords
        fields = [
            #'id',
            'latitude',
            'longitude',
            'height'
        ]


class ImagesSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    data = serializers.CharField(source='img')
    class Meta:
        model = Images
        fields = [
            #'date_added',
            'data',
            'title'
        ]


class AddedSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    connect = serializers.CharField(source='connects', label='Connects', allow_blank=True)
    coords = CordsSerializer(source='cords')
    user = UserSerializer()
    level = serializers.DictField(source='get_levels')
    images = ImagesSerializer(source='added_images', many=True)

    class Meta:
        model = Added
        fields = [
           #'id',
           #'date_added',
           'user',
           'beauty_title',
           'title',
           'other_titles',
           'connect',
           'coords',
           #'status',
           #'winter',
           #'spring',
           #'summer',
           #'autumn',
           'level',
           'images',
            ]
        read_only_fields = [
             'id',
             'status',
        #     'user'
         ]

    def create(self, request):
        cords = request.pop('cords')
        user = request.pop('user')
        images = request.pop('added_images')
        levels = request.pop('get_levels')
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
            for image in images:
                # data = base64.encodebytes(image['img'])
                data = image['img'].encode('utf-8')
                # data = base64.b64encode(data)
                Images.objects.create(added=pass_instance, img=data, title=image['title'])
            return pass_instance
        except OperationalError:
            raise DBConnectException()

    def retrieve(self, request):
        pk = request.pop('id')
        try:
            if not Added.objects.filter(id=pk).exists():
                raise NotFound
            return super().retrieve(request)
        except OperationalError:
            raise DBConnectException()

    def update(self, request, instance):
        pk = request.id
        coords = instance.pop('coords', None)
        user = instance.pop('user', None)
        levels = instance.pop('get_levels', None)
        images = instance.pop('added_images', None)
        try:
            queryset = Added.objects.filter(id=pk)
            if not queryset.exists():
                raise NotFound
            query_object = queryset.first()
            if not query_object.status == "('new', 'new')":
                raise ObjectStatusException
            if coords:
                coords_fields = model_to_dict(request.cords)
                coords_fields = coords_fields | coords
                coords_fields.pop('id', None)
                coords_instance, created = Cords.objects.get_or_create(**coords_fields)
                request.cords = coords_instance
            if levels:
                levels_fields = request.get_levels()
                levels_fields = levels_fields | levels
                request.set_levels(**levels_fields)
            if images:
                Images.objects.filter(added=request).delete()
                for image in images:
                    data = image['img'].encode('utf-8')
                    Images.objects.create(added=request, img=data, title=image['title'])
            return super().update(request, instance)
        except OperationalError:
            raise DBConnectException()