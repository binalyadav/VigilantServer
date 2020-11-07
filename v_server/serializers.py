from rest_framework import serializers

from django.contrib.auth.models import User, Group
from .models import *
from django.contrib.auth.hashers import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', "url"]

    def to_internal_value(self, data):
        instance = super(UserSerializer, self).to_internal_value(data)
        passwordStr = data['first_name'] + "@" + data['last_name']
        encryptedPassword = make_password(passwordStr)
        instance["password"] = encryptedPassword
        return instance


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class OrganizationSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), many=True, required=False)
    endpoints = serializers.PrimaryKeyRelatedField(
        queryset=Endpoint.objects.all(), many=True, required=False)

    class Meta:
        model = Organization
        fields = ["id", "name", "url", "users", "endpoints"]


class EndpointSerializer(serializers.ModelSerializer):

    class Meta:
        model = Endpoint
        fields = ["id", "port", "host", "url", "endpoint", "parameters"]


class LogsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Logs
        fields = ["id", "ipAddress", "city", "region",
                  "country", "latitude", "longitude"]
