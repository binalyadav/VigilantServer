from django.db import models
from django.contrib.auth.models import User


class Organization(models.Model):
    name = models.CharField(max_length=30)
    users = models.ManyToManyField(
        User, related_name="userList", blank=True)

    def __str__(self):
        return self.name
