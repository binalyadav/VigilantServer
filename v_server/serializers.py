from rest_framework import serializers

from django.contrib.auth.models import User, Group

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
    def to_internal_value(self, data):
        instance = super(UserSerializer, self).to_internal_value(data)
        instance["password"] = data['first_name'] + "@" + data['last_name']
        return instance

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']