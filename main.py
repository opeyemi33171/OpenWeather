import requests

api_key = 'dghsmksndfngdsfn5df4g5s4654as65'
current_weather_url = 'http://api.openweathermap.org/data/2.5/weather?'


def url_request(url, key):
    return requests.get(url + '&APPID=' + key).json()


def city_weather(url, city_name):
    return url + 'q=' + city_name

city = input('Please enter the name of a city: ')

url_request(city_weather(current_weather_url, city), api_key)

print(url_request(city_weather(current_weather_url, city), api_key)['weather'][1]['description'])