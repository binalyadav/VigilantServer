# Generated by Django 3.0.8 on 2020-08-04 18:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('v_server', '0008_auto_20200804_0042'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='userList', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='OrganizationUsers',
        ),
    ]
