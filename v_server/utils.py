from django.shortcuts import render
import requests
from django.http import JsonResponse
from .ipaddress import find_ipadd

def makeRequest(request, endpoint):
    print(request.META.get('REMOTE_ADDR'))
    response = requests.get('https://www.hatchways.io/api/assessment/students')
    geodata = response.json()
    find_ipadd(request.META.get('REMOTE_ADDR'))
    return JsonResponse({"data": geodata})
