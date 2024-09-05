import json
import requests

APIkey = "eabe63516f383f603021f22d04b2e697"
location = input("Insert name of the location of which you wish to search for weather data: ")
location.lower()
location.capitalize()
try:
    Lrequest = f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid={APIkey}"
    location_request = requests.get(Lrequest)
    if location_request.status_code == 200:
        location_data = location_request.json()
        lat = location_data[0]["lat"]
        lon = location_data[0]["lon"]
        Wrequest = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,daily,alerts&units=metric&appid={APIkey}"
        weather_request = requests.get(Wrequest)
        if weather_request.status_code == 200:
            weather_data = weather_request.json()
            weather = weather_data["current"]["weather"][0]["main"]
            temp = weather_data["current"]["temp"]
            print(f"Weather in {location} is {weather} and temperature is {temp}°C")
except requests.exceptions.RequestException as e:
    print("Unable to run")
