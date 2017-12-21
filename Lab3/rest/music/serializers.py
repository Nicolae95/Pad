from __future__ import unicode_literals
from rest_framework import serializers
from .models import Music
from urlparse import urlparse
from category.serializers import CategorySerializer


class MusicSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()
    class Meta:
        model = Music
        fields = ('id', 'title', 'singer', 'album', 'category')
        
class MusicListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Music
        fields = ('id', 'title', 'singer', 'album', 'category')
     