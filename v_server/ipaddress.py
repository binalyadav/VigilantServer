
from ip2geotools.databases.noncommercial import DbIpCity
from .models import Logs


def find_ipadd(ip_address):
    response = DbIpCity.get(ip_address, api_key='free')
    try:
        log = Logs(ipAddress=response.ip_address, city=response.city, region=response.region,
                   country=response.country, latitude=response.latitude, longitude=response.longitude, status="successful")
        log.save()
    except Exception as e:
        print(e)
