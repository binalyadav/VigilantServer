from django.shortcuts import render

from rest_framework import viewsets

from .serializers import *
from django.contrib.auth.models import User, Group
from .models import *
from rest_framework.permissions import IsAuthenticated
from django.contrib.sessions.models import Session
from django.db.models import Count
from django.http import JsonResponse
import ast
import json
from datetime import datetime, timedelta
import pytz
from rest_framework import filters


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

    def getCount(self):
        count = User.objects.count()
        return JsonResponse({"data": {"userCount": count}})


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

    def getOrgId(self, orgId):
        queryset = Organization.objects.select_related().all()
        # print(queryset.values())
        if orgId is None:
            return None
        queryset = queryset.filter(id=orgId)
        return list(queryset.values('endpoints'))

    def getCount(self):
        count = Organization.objects.count()
        return JsonResponse({"data": {"organizationCount": count}})


class EndpointViewSet(viewsets.ModelViewSet):
   # permission_classes = [IsAuthenticated]
    queryset = Endpoint.objects.all()
    serializer_class = EndpointSerializer

    def getEndpointByid(self, ept):
        queryset = Endpoint.objects.all()
        if ept is None:
            return None
        # print(ept)
        queryset = queryset.filter(endpoint=ept)
        return list(queryset.values())

    def getCount(self):
        count = Endpoint.objects.count()
        return JsonResponse({"data": {"endpointCount": count}})


class LogsViewSet(viewsets.ModelViewSet):
    queryset = Logs.objects.all()
    serializer_class = LogsSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['timestamp']

    def getLogsByType(self):
        queryset = Logs.objects.values(self.GET.get(
            'type')).annotate(count=Count(self.GET.get('type')))
        return JsonResponse({"data": list(queryset)})

    def getLogsByDateTimeRange(self):
        queryset = Logs.objects.all()
        timestamp_to = datetime.now().date() + timedelta(days=1)
        timestamp_from = datetime.now().date() - timedelta(days=2)
        print(timestamp_from)
        print(timestamp_to)
        queryset = queryset.filter(timestamp__gte=timestamp_from,
                                   timestamp__lte=timestamp_to)
        return JsonResponse({"data": list(queryset.values())})
