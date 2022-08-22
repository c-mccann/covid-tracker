from api.serializers import CountrySerializer, DataSerializer
from disease.models import Country, Data
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

### classes
# Data, Read All
class DataList(generics.ListAPIView):
    queryset = Data.objects.all().order_by('iso_code')
    serializer_class = DataSerializer

# Data, Read One
class DataDetail(generics.RetrieveAPIView):
    lookup_field = 'iso_code'
    queryset = Data.objects.all()
    serializer_class = DataSerializer

# Country, Read ALL
class CountryList(generics.ListAPIView):
    queryset = Country.objects.all().order_by('name')
    serializer_class = CountrySerializer

### fn
@api_view(['GET'])
def getData(request):
    covid_data = Data.objects.all().order_by('iso_code')
    serializer = DataSerializer(covid_data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getDataByIsoCode(request, format=None, *args, **kwargs):
    covid_data = Data.objects.filter(iso_code=kwargs['iso_code']).values()[0]
    serializer = DataSerializer(covid_data, many=False)
    return Response(serializer.data)


