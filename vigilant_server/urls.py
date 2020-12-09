"""vigilant_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.views.generic import TemplateView
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .authentication import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [

    path('admin/', admin.site.urls),
    path('view/login/', TemplateView.as_view(template_name='login.html')),
    path('view/register/', TemplateView.as_view(template_name='register.html')),
    path('view/users/', TemplateView.as_view(template_name='users.html')),
    path('view/report/', TemplateView.as_view(template_name='report.html')),
    path('view/organizations/',
         TemplateView.as_view(template_name='organization.html')),
    path('view/endpoints/', TemplateView.as_view(template_name='endpoints.html')),
    path('view/dashboard/', TemplateView.as_view(template_name='dashboard.html')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('authenticate/', csrf_exempt(userLogin), name='authenticate'),
    path('view/unauthorized/', TemplateView.as_view(template_name='unauthorized.html')),
    path('logout/', csrf_exempt(userLogout), name='logout'),
    path('', include('v_server.urls'))

]
