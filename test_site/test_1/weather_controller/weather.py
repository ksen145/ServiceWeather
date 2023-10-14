from abc import ABC, abstractmethod
from ..models import City


class WeatherABC(ABC):

    @abstractmethod
    def get_weather(city):
        raise NotImplementedError


class Weather(WeatherABC):

    def get_weather(city):

        model_citys = City.objects.all()

        if city not in model_citys:
            print("ok")
        else:
            print("error")

        return {'temp': 1, 'wind_speed': 1, 'pressure_mm': 1}
