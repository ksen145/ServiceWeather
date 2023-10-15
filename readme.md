# Сервис погоды

Сервис позволяет получать данные о погоде, а именно:

Температуру в градусах цельсия, скорос ветра в м\с, давление в мм рт. ст.

Данные можно получать через телеграмм бота или API

## Перед запуском
Перед запуском необходимо изменить ключи для внешних API yandex с которыми работает сервис.

Данные ключи находятся в файле конфигурации по пути:

~/weather_project/test_site/test_1/weather_controller/config.py

## Запуск

Чтобы запустить программу, запустите файл start.sh

## API

Для работы с API выполните GET запрос следующего формата:

/weather?city=<city_name> - где <city_name> название города

Формат ответа JSON вида:

{
    "temp": 8,
    "wind_speed": 3,
    "pressure_mm": 756
}