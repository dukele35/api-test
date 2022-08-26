from dataclasses import field
from django.contrib.auth.models import User
from rest_framework import serializers
from dblapp.models import FactoryRecord

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class FactoryRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactoryRecord
        fields = "__all__"
