from .models import *
from rest_framework import serializers


class AddedSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Added
       fields = [
           'id',
           'date_added',
           'user',
           'beauty_title',
           'title',
           'other_titles',
           'connects',
           'cords',
           'status',
           'winter',
           'spring',
           'summer',
           'autumn',
       ]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'phone',
            'email'
        ]


class CordsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cords
        fields = [
            'id',
            'latitude',
            'longitude',
            'height'
        ]


class ImagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Images
        fields = [
            'date_added',
            'img',
            'added',
            'title'
        ]