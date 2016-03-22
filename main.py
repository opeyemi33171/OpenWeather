import requests

api_key = 'bf892e0a4d0418090091a347c667c910'


def url_request(url):
    global api_key
    return requests.get(url + '&APPID=' + api_key).json()

#location = 'http://api.openweathermap.org/data/2.5/weather?q={0}&APPID=bf892e0a4d0418090091a347c667c910'.format()

#print(url_request(location))
