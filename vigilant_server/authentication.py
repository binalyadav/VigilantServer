from django.contrib.auth import authenticate, login
from django.views.generic.base import RedirectView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout

from django.http import JsonResponse
import ast


def userLogin(request):
    user = authenticate(request, username=ast.literal_eval(
        request.body.decode('utf-8'))['username'], password=ast.literal_eval(request.body.decode('utf-8'))['password'])
    if user is not None:
        login(request, user)
        return JsonResponse({"status": 202})

    else:
        return HttpResponse('Invalid Username or Password', content_type='application/json',
                            status=404, reason=None, charset=None)


def userLogout(request):
    logout(request)
    if not request.user.is_authenticated:
        response = HttpResponse("User logged out")
        response.delete_cookie('orgId')
        response.delete_cookie('orgName')
        return response
