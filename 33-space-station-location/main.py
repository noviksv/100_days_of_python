import requests
import datetime as dt
from config import send_email
import logging

logging.basicConfig(level=logging.DEBUG)


MY_LAT = 52.26131518259818
MY_LONG = 20.95682398281323

def is_daylight_hours():
    params={"lat": MY_LAT, "lng": MY_LONG, "formatted": 0}
    #https://api.sunrise-sunset.org/json?lat=52.26131518259818&lng=20.95682398281323&formatted=0
    responce = requests.get(url="https://api.sunrise-sunset.org/json", params=params)

    responce.raise_for_status()

    data = responce.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]
    #check if current time is daylight hours

    if  dt.datetime.fromisoformat(sunrise)<= dt.datetime.now(dt.UTC) <= dt.datetime.fromisoformat(sunset):
        logging.debug("There is a daylight hours.")
        return True
    else:
        logging.debug("There is nighttime.")
        return False

def check_iss_position():
    #first provider for iss position
    responce = requests.get("http://api.open-notify.org/iss-now.json")
    responce.raise_for_status()

    data = responce.json()
    #logging.info(data)

    longitude = data["iss_position"]["longitude"]   
    latitude = data["iss_position"]["latitude"]

    iss_position = (longitude, latitude)

    return (iss_position)

def check_iss_position_v2():
    #second provider for iss position
    responce = requests.get("https://api.wheretheiss.at/v1/satellites/25544")
    responce.raise_for_status()

    data = responce.json()
    #logging.info(data)

    longitude = data["longitude"]   
    latitude = data["latitude"]

    iss_position = (longitude, latitude)

    return (iss_position)

def is_iss_nearby():
    try:
        iss_position = check_iss_position_v2()
    except:
        iss_position = check_iss_position()

    logging.debug(f"Current position of iss is {iss_position}")
    if MY_LAT-5 <= iss_position[0] <= MY_LAT+5 and MY_LONG-5 <= iss_position[1] <= MY_LONG+5:
        return True
    else:
        return False


if __name__ == "__main__":
    if not is_daylight_hours() and is_iss_nearby():
        logging.debug("Look up, ISS is nearby.")
        send_email("Look at the sky", "Look up, ISS is nearby.")
    else:
        logging.debug("ISS is not nearby or it is daylight.")