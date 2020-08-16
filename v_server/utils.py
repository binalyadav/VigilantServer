from django.shortcuts import render
import requests
from django.http import JsonResponse


def makeRequest(request, endpoint):
    print(request.META.get('REMOTE_ADDR'))
    # print('third party api request ' + endpoint)
    response = requests.get('https://www.hatchways.io/api/assessment/students')
    geodata = response.json()

    return JsonResponse({"data": geodata})
