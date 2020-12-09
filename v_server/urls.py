from django.urls import include, path, re_path
from rest_framework import routers
from . import views
from .utils import *

router = routers.SimpleRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'organizations', views.OrganizationViewSet)
router.register(r'endpoints', views.EndpointViewSet)
router.register(r'logs', views.LogsViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('setOrg/', views.OrganizationViewSet.setOrganizationUser,  name='setOrgUser'),
    path('getLogs/', views.LogsViewSet.getLogsByType,  name='getLogsByType'),
    path('userCount/', views.UserViewSet.getCount,  name='userCount'),
    path('organizationCount/', views.OrganizationViewSet.getCount,
         name='organizationCount'),
    path('endpointCount/', views.EndpointViewSet.getCount,  name='endpointCount'),
    path('getLogsByDateTimeRange/', views.LogsViewSet.getLogsByDateTimeRange,
         name='getLogsByDateTimeRange'),
    path('vserver/<path:endpoint>', makeRequest,  name='makeRequest'),
    path('', include(router.urls)),
    path('', include('rest_framework.urls', namespace='rest_framework'))
]
