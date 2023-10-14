from geopy.geocoders import Yandex
from weather_project.config import Config


class SearchGeoCity():

    def search(city):
        coordinates = Yandex(api_key=Config.geo_yandex_api_key).geocode(city)
        lat, lon = coordinates.latitude, coordinates.longitude
        return [lat, lon]
