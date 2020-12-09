from django.shortcuts import render
import requests
from django.http import JsonResponse
from .ipaddress import find_ipadd
from .views import OrganizationViewSet, EndpointViewSet
from .models import Logs
from django.utils import timezone


def makeRequest(request, endpoint):
    req_diff = checkLastRequest()
    if req_diff:
        return JsonResponse({"Message": "Ip address has been blocked"})
    x = endpoint.split("/,1")
    orgId = endpoint[0]
    organizationEndpoints = OrganizationViewSet.getOrgId(request, orgId)
    endPnt = EndpointViewSet.getEndpointByid(request, endpoint[2:])
    if endPnt[0]['parameters'] != None:
        parameters = endPnt[0]['parameters']
        parameters = parameters.split(',')
        queryParams = ""
        for param in parameters:
            if(request.GET.get(param, '') != ''):
                queryParams = queryParams + param + \
                    "=" + request.GET.get(param, '') + '&'
        url = endPnt[0]['host'] + \
            endPnt[0]['endpoint'] + "?" + queryParams[:-1]
    else:
        url = endPnt[0]['host'] + endPnt[0]['endpoint']
    response = requests.get(url)
    geodata = response.json()
    find_ipadd('13.71.3.3')
    return JsonResponse({"data": geodata})


def checkLastRequest():
    log = Logs.objects.filter(ipAddress='142.68.25.142')
    if len(log.values()) > 4:
        last_request = log.values()[len(log) - 1]
        now = timezone.now()
        req_diff = (now - last_request['timestamp']).total_seconds()
        if req_diff < 4:
            log = Logs(ipAddress=last_request['ipAddress'], city=last_request['city'], region=last_request['region'],
                       country=last_request['country'], latitude=last_request['latitude'], longitude=last_request['longitude'], status="blocked")
            log.save()
            return req_diff < 4
        return False
    return False
