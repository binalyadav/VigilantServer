from django.shortcuts import render

from rest_framework import viewsets

from .serializers import *
from django.contrib.auth.models import User, Group
from .models import *
from rest_framework.permissions import IsAuthenticated
from django.contrib.sessions.models import Session
from django.http import JsonResponse
import ast
import json


class UserViewSet(viewsets.ModelViewSet):
   # permission_classes = [IsAuthenticated]
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer

    def get_queryset(self):
        username = self.request.query_params.get('username')
        if username is not None:
            queryset = User.objects.all().order_by('username')
            queryset = queryset.filter(username=username)
            print(queryset.values())
            return queryset
        queryset = User.objects.all().order_by('username')
        return queryset


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
   # permission_classes = [IsAuthenticated]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
  #  permission_classes = [IsAuthenticated]
    queryset = Organization.objects.all().order_by('name')
    serializer_class = OrganizationSerializer

    def setOrganizationUser(self):
        queryset = Organization.objects.all().order_by('name')
        user = ast.literal_eval(self.GET.get('user'))

        if user is None:
            return queryset
        queryset = queryset.filter(users__id=user)
        self.session['userOrg'] = list(queryset.values())[0]['id']
        response = JsonResponse({"data": list(queryset.values())})
        response.set_cookie('orgId',  list(queryset.values())[0]['id'])
        response.set_cookie('orgName',  list(queryset.values())[0]['name'])
        return response


class EndpointViewSet(viewsets.ModelViewSet):
   # permission_classes = [IsAuthenticated]
    queryset = Endpoint.objects.all()
    serializer_class = EndpointSerializer
