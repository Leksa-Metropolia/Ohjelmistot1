import json
import requests

with open('keys.json') as config_file:
    config = json.load(config_file)
APIkey = config['API_key']
location = input("Insert name of the location of which you wish to search for weather data: ")
location = location.capitalize()
try:
    request = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={APIkey}&units=metric"
    weather_request = requests.get(request)
    if weather_request.status_code == 200:
        weather_data = weather_request.json()
        weather = weather_data["weather"][0]["main"]
        temp = weather_data["main"]["temp"]
        print(f"Weather in {location} is {weather} and temperature is {round(temp)}°C")
except requests.exceptions.RequestException as e:
    print("Unable to run")
