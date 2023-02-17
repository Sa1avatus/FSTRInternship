from .models import *
from rest_framework import serializers
from .exceptions import *
from django.db.utils import OperationalError


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
    class Meta:
        model = Images
        fields = [
            'date_added',
            'img',
            'added',
            'title'
        ]


class AddedSerializer(serializers.ModelSerializer):
    connect = serializers.CharField(source='connects', label='Connects', allow_blank=True)
    coords = CordsSerializer(source='cords')
    user = UserSerializer()
    level = serializers.DictField(source='set_levels')
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
            ]

    def create(self, request):
        cords = request.pop('cords')
        user = request.pop('user')
        #images = request.pop('img')
        levels = request.pop('set_levels')
        try:
            #user_instance, created = User.objects.get_or_create(**user)
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
            # for image in images:
            #     Images.objects.create(mpass=pass_instance, **image)
            return pass_instance
        except OperationalError:
            raise DBConnectException()

