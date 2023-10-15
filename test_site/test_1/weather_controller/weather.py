from abc import ABC, abstractmethod
from ..models import City
from ..models_controller import ModelsController


class WeatherABC(ABC):

    @abstractmethod
    def get_weather(city):
        raise NotImplementedError


class Weather(WeatherABC):

    def get_weather(city):

        model_citys = City.objects.filter(name=city).values()

        list_result = [entry for entry in model_citys]

        if len(list_result) == 0:

            data = ModelsController.new_model(city)

            return data

        else:

            data = ModelsController.update_model(city)

            return data
