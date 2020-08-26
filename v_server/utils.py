from django.shortcuts import render
import requests
from django.http import JsonResponse
from .ipaddress import find_ipadd



def makeRequest(request, endpoint):
    print(request.META.get('REMOTE_ADDR'))
    # print('third party api request ' + endpoint)
    response = requests.get('https://www.hatchways.io/api/assessment/students')
    geodata = response.json()
    find_ipadd('192.168.3.4')
    return JsonResponse({"data": geodata})
