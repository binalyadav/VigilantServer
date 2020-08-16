from django.db import models
from django.contrib.auth.models import User
from .models import *

class Endpoint(models.Model):
    port = models.IntegerField()
    host = models.CharField(max_length=50)
    endpoint = models.CharField(max_length=50)
    
    def __str__(self):
        return self.endpoint
    def __str__(self):
        return self.port
    def __str__(self):
        return self.host
    def __str__(self):
        return self.endpoint

class Organization(models.Model):
    name = models.CharField(max_length=30)
    users = models.ManyToManyField(
        User, related_name="userList", blank=True)
    endpoints = models.ManyToManyField(
      Endpoint  , related_name="endpointList", blank=True)

    def __str__(self):
        return self.name

