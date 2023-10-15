from .models import City
from .weather_controller.request_weather import RequestWeather
from .weather_controller.search_geo_city import SearchGeoCity
import datetime
from .parse_time import ParseTime


class ModelsController():

    def new_model(city):

        new_city = City()

        new_city.name = city

        coordinates = SearchGeoCity.search(city)
        new_city.lat = coordinates[0]
        new_city.lon = coordinates[1]

        data = RequestWeather.request(coordinates)
        new_city.temp = data.get('temp')
        new_city.wind_speed = data.get('wind_speed')
        new_city.pressure_mm = data.get('pressure_mm')

        new_city.time_last = str(datetime.datetime.now())

        new_city.save()

        return data

    def update_model(city):

        model_city = City.objects.get(name=city)

        result = ParseTime.parse(datetime.datetime.now(), model_city.time_last)

        if result == 1:

            coordinates = [model_city.lat, model_city.lon]
            data = RequestWeather.request(coordinates)
            model_city.temp = data.get('temp')
            model_city.wind_speed = data.get('wind_speed')
            model_city.pressure_mm = data.get('pressure_mm')
            model_city.time_last = str(datetime.datetime.now())

            model_city.save()

            return data

        else:

            return {
                'temp': model_city.temp,
                'wind_speed': model_city.wind_speed,
                'pressure_mm': model_city.pressure_mm
            }
