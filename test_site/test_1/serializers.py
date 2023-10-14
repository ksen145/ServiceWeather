from rest_framework import serializers
from .models import City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('temp', 'wind_speed', 'pressure_mm')
