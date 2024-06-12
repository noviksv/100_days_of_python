import requests
import datetime as dt


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
        print("There is a daylight hours.")
        return True
    else:
        print("There is nighttime.")
        return False

def check_iss_position():
    responce = requests.get("http://api.open-notify.org/iss-now.json")
    responce.raise_for_status()

    data = responce.json()
    #print(data)

    longitude = data["iss_position"]["longitude"]   
    latitude = data["iss_position"]["latitude"]

    iss_position = (longitude, latitude)

    return (iss_position)

def check_iss_position_v2():
    #second provider for iss position
    responce = requests.get("https://api.wheretheiss.at/v1/satellites/25544")
    responce.raise_for_status()

    data = responce.json()
    #print(data)

    longitude = data["longitude"]   
    latitude = data["latitude"]

    iss_position = (longitude, latitude)

    return (iss_position)

def is_iss_nearby():
    try:
        iss_position = check_iss_position_v2()
    except:
        iss_position = check_iss_position()

    print(f"Current position of iss is {iss_position}")
    if MY_LAT-5 <= iss_position[0] <= MY_LAT+5 and MY_LONG-5 <= iss_position[1] <= MY_LONG+5:
        #print("ISS is nearby.")
        return True
    else:
        #print("ISS is not nearby.")
        return False


if __name__ == "__main__":
    if not is_daylight_hours() and is_iss_nearby():
        print("Look up, ISS is nearby.")
    else:
        print("ISS is not nearby or it is daylight.")