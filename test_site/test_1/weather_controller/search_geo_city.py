from geopy.geocoders import Yandex
from .config import Config


class SearchGeoCity():

    def search(city):

        try:
            coordinates = Yandex(api_key=Config.geo_yandex_api_key).geocode(city)

            if coordinates is None:
                return 2

            lat, lon = coordinates.latitude, coordinates.longitude
            return [lat, lon]

        except:
            return 1
