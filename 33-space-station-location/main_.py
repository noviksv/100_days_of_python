import requests
import datetime

# responce = requests.get("http://api.open-notify.org/iss-now.json")
# responce.raise_for_status()

# data = responce.json()
# print(data)

# longitude = data["iss_position"]["longitude"]   
# latitude = data["iss_position"]["latitude"]

# iss_position = (longitude, latitude)

# print(iss_position)

params={"lat": 52.26131518259818, "lng": 20.95682398281323, "formatted": 0}
#https://api.sunrise-sunset.org/json?lat=52.26131518259818&lng=20.95682398281323&formatted=0
responce = requests.get(url="https://api.sunrise-sunset.org/json", params=params)

responce.raise_for_status()

data = responce.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise, sunset)

print(datetime.datetime.fromisoformat(sunrise))