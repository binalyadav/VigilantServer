from django.shortcuts import render

from rest_framework import viewsets

from .serializers import *
from django.contrib.auth.models import User, Group
from .models import *
from rest_framework.permissions import IsAuthenticated
from django.contrib.sessions.models import Session


class UserViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    # permission_classes = (IsAuthenticated,)
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Organization.objects.all().order_by('name')
    serializer_class = OrganizationSerializer
