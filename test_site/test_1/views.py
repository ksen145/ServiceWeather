from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from .weather_controller.weather import Weather


class Test1APIView(generics.ListAPIView):
    def get(self, request, city):
        city = request.GET.get("city")
        response = Weather.get_weather(city)
        return Response(response)
