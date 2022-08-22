from rest_framework import serializers
from disease.models import Country, Data


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        # fields = '__all__'
        fields = ['iso_code', 'data']

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        # fields = '__all__'
        fields = ['iso_code', 'name']