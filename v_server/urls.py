from django.urls import include, path, re_path
from rest_framework import routers
from . import views
from .utils import *

router = routers.SimpleRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'organizations', views.OrganizationViewSet)
router.register(r'endpoints', views.EndpointViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('setOrg/', views.OrganizationViewSet.setOrganizationUser,  name='setOrgUser'),
    path('vserver/<path:endpoint>/', makeRequest,  name='makeRequest'),
    path('', include(router.urls)),
    path('', include('rest_framework.urls', namespace='rest_framework'))
]
