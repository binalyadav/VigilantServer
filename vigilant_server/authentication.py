from django.contrib.auth import authenticate, login
from django.views.generic.base import RedirectView
from django.http import HttpResponseRedirect, HttpResponse

from django.http import JsonResponse
import ast


def my_view(request):
    user = authenticate(request, username=ast.literal_eval(
        request.body.decode('utf-8'))['username'], password=ast.literal_eval(request.body.decode('utf-8'))['password'])
    if user is not None:
        login(request, user)
        return JsonResponse({"status": 202})

    else:
        return HttpResponse('Invalid Username or Password', content_type='application/json', 
        status=404 , reason=None, charset=None)
