import requests
import json
from .config import Config


class RequestWeather():

    def request(coordinates):

        url = f'https://api.weather.yandex.ru/v2/forecast?lat={coordinates[0]}&lon={coordinates[1]}'
        headers = {'X-Yandex-API-Key': Config.weather_yandex_api_key}

        req = requests.get(url, headers=headers)
        data = json.loads(req.text)

        temp = data['fact']['temp']
        wind_speed = data['fact']['wind_speed']
        pressure_mm = data['fact']['pressure_mm']

        return {
            'temp': temp,
            'wind_speed': wind_speed,
            'pressure_mm': pressure_mm
            }
