from django.db import models
from django.contrib.auth.models import User


class Endpoint(models.Model):
    port = models.IntegerField()
    host = models.CharField(max_length=50)
    endpoint = models.CharField(max_length=1000)
    parameters = models.CharField(max_length=1000)

    def __str1__(self):
        return self.endpoint

    def __str2__(self):
        return self.port

    def __str3__(self):
        return self.host

    def __str4__(self):
        return self.endpoint


class Organization(models.Model):
    name = models.CharField(max_length=30)
    users = models.ManyToManyField(
        User, related_name="userList", blank=True)
    endpoints = models.ManyToManyField(
        Endpoint, related_name="endpointList", blank=True)

    def __str__(self):
        return self.name


class Logs(models.Model):
    ipAddress = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    latitude = models.CharField(max_length=30)
    longitude = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ipAddress
