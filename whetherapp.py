import requests
import json
while True:
    api_key = "user_api_key"
    try:
        city_name = input("City Name: ")
        base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

        response = requests.get(base_url)
        data=json.loads(response.text)
        print(f'cordinates are: {data["coord"]}')
        print(f'tempreature is: {data["main"]["temp"]}°C')
        print(f'humidity is: {data["main"]["humidity"]}°C')
        print(f'wind\'s speed is like: {data["wind"]["speed"]} m/s')
        print(f'clouds are like: {data["clouds"]}')
    except Exception as e:
        print('make sure you enter a city that exists in this earth')
