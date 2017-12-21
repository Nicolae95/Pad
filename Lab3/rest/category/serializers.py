from __future__ import unicode_literals
from rest_framework import serializers
from .models import Category
from urlparse import urlparse


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name')
