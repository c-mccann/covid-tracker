from http.client import HTTPResponse
from xml.etree.ElementTree import tostring
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import date, datetime
from disease.models import Country, Data
import logging
import requests

from disease.models import Country, Data

log = logging.getLogger(__name__)

# Create your views here.

def covid(request):
    # return render(request, 'covid.html', {'name': 'Carl'})
    today = date.today()
    
    # countries = Country.objects.order_by('name')
    # country_names = [c.name for c in countries]

    countries = list(Country.objects.order_by('name').values())
    country_names = [c['name'] for c in countries]

    temp_iso_code = 'ie'
    covid_data = Data.objects.filter(iso_code=temp_iso_code).values()
    if covid_data:
        covid_data = covid_data[0]['data']
        
        time = covid_data['updated'] # from sample.json, from api
        updated = datetime.fromtimestamp(time/1000.0)
    else:
        updated = datetime.fromtimestamp(0)

    return render(request, 'covid.html', {
            'date': today.strftime('%d %b %Y'),
            'updated': updated.strftime('%d %b %Y %H:%M:%S'), 
            'countries': countries,
            'covid_data': covid_data
        }

    )

def covid_api(request):
    return render(request, 'covid-api.html')

def downloadinfo(request):
    url = "https://disease.sh/v3/covid-19/countries"

    response = requests.get(url)
    json_data = response.json()

    for curr_data in json_data:
        curr_iso_code = curr_data['countryInfo']['iso2']

        if curr_iso_code is not None:
            Data.objects.update_or_create(iso_code=curr_iso_code.lower(), defaults={'data': curr_data})
            
    # return HttpResponseRedirect('/disease/covid')
    return HttpResponse(status=201)
    