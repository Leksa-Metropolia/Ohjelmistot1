import json
import requests

try:
    data = requests.get("https://api.chucknorris.io/jokes/random")
    if data.status_code == 200:
        json_data = data.json()
        print(json_data["value"])
except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")