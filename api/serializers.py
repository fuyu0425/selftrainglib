from rest_framework import serializers
from api.models import *


class GalleyGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ('title', 'serial', 'cover', 'begin', 'end',)


class GalleyDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ('title', 'cover', 'begin', 'end', 'people', 'place', 'description')


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('serial', 'title', 'imgPath',)
