import requests
from bs4 import BeautifulSoup
import json
#Indormation for weather application
while True:
    api_key = "your_api_key"
    try:
        city_name = input("City Name: ")
        base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

        response = requests.get(base_url)
        print(response.text)
        data=json.loads(response.text)
        print(f'cordinates are: {data["coord"]}')
        print(f'tempreature is: {data["main"]["temp"]}°C')
        print(f'humidity is: {data["main"]["humidity"]}°C')
        print(f'wind\'s speed is like: {data["wind"]["speed"]} m/s')
        print(f'clouds are like: {data["clouds"]}')
    except Exception as e:
        print('make sure you enter a city that exists')