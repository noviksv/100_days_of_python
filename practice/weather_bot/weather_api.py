import requests
from dotenv import load_dotenv
import logging
import os
import json

logging.basicConfig(level=logging.DEBUG)

load_dotenv()

OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
API_KEY = os.getenv("API_KEY")
LAT = os.getenv("LAT")
LON = os.getenv("LON")

params = {
    "lat": LAT,
    "lon": LON,
    "appid": API_KEY,
    "units": "metric",
    "cnt": 4
}

responce = requests.get(url=f'{OWM_Endpoint}', params=params)

#https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

#print (responce.status_code)
responce.raise_for_status()
data = responce.json()


def is_raining(data):
    for dates in data['list']:
        for weather in dates['weather']:
            logging.debug((dates['dt_txt'], weather))
            
            if weather['id'] < 700:
                return True
    
    return False


#print(data['list'][0]['weather'][0]['id'])

# with open(file="forecast.json", mode='w') as file:
  
#     file.write(str( json.dumps(data, indent=4)))

if is_raining(data=data):
    logging.debug('Do not forget the umbrella!!!')
else:
    logging.debug('Relax! Sky si blue')