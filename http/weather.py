# import requests

# API_KEY = "c4f7874f9fc064b9bb8b2a60dc0d3f57"

# def get_weather(lat, lon):
#     params = {
#         "lat": lat,
#         "lon": lon,
#         "appid": API_KEY,
#         "units": "metric" 
#     }
#     url = "https://api.openweathermap.org/data/2.5/weather"
#     res = requests.get(url=url, params=params)
#     if res.status_code == 200:
#         return res.json()
#     raise ValueError("Ошибка", res.text)


# lat = 51.1801
# lon = 71.446
# weather = get_weather(lat, lon)


# def print_weather_info(weather):
#     print("Город:", weather["name"])
#     print("Максимальная температура:", weather["main"]["temp_max"], "градусов")
#     print("Минимальная температура:", weather["main"]["temp_min"], "градусов")
#     print("Скорость ветра:", weather["wind"]["speed"], "м\с")
#     print("Координаты: широта -", weather["coord"]["lat"], ", долгота -", weather["coord"]["lon"])

# print_weather_info(weather)


import requests

API_KEY = "c4f7874f9fc064b9bb8b2a60dc0d3f57"

def get_weather_by_name(city_name):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"
    }
    res = requests.get(url=url, params=params)
    if res.status_code == 200:
        weather_data = res.json()
        print_weather_info(weather_data)
    else:
        raise ValueError("Ошибка", res.text)

def print_weather_info(weather):
    print("Город:", weather["name"])
    print("Максимальная температура:", weather["main"]["temp_max"], "градусов")
    print("Минимальная температура:", weather["main"]["temp_min"], "градусов")
    print("Скорость ветра:", weather["wind"]["speed"], "м\с")
    print("Координаты: широта -", weather["coord"]["lat"], ", долгота -", weather["coord"]["lon"])

city_name = "Астана"
get_weather_by_name(city_name)
