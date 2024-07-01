import requests
from dotenv import load_dotenv
import os
import datetime

load_dotenv()

def add_records_to_sheet(workout_params):
    # 
    # "date": "30/06/2024",
    # "time": "15:18:32",
    # "exercise": "running",
    # "duration": "35",            "calories": "200" }  

    sheety_endpoint  =  os.getenv("SHEETY_ENDPOINT")
    headers = {
        "Authorization": f"{os.getenv('SHEETY_BASIC_AUTH')}"
    }
    sheety_params = {"workout":
                     workout_params }
    r = requests.post(url=sheety_endpoint, headers=headers, json=sheety_params)
    r.raise_for_status()
    pass

def process_exercises(query):

    headers = {
        "x-app-id": os.getenv("NUTRITIONIX_ID"),
        "x-app-key": os.getenv("NUTRITIONIX_KEY"),
        "Content-Type": "application/json"
    }

    host = "https://trackapi.nutritionix.com"
    # endpoint = "/v2/search/instant"

    # r = requests.get(url=f"{host}{endpoint}",headers=headers, params={"query":"apple"})


    # process exercises
    endpoint = "/v2/natural/exercise"

    r = requests.post(url=f"{host}{endpoint}", headers=headers, json={
        "query": exercise_input,
        "gender": "male",
        "weight_kg": 95,
        "height_cm": 185,
        "age": 38
    })

    r.raise_for_status()
    data = r.json()
    a = []
    for exercise in data["exercises"]:
        a.append({"exercise" : exercise["name"]
                  , "duration": exercise["duration_min"]
                  , "calories" : exercise["nf_calories"]}
                )
        
    return a


if __name__ == "__main__":
    exercise_input  = input("Tell me which exercises you did: ")
    process_exercises(exercise_input)   
    today = datetime.datetime.now()
    date = today.strftime("%d/%m/%Y")
    time = today.strftime("%H:%M:%S")
    dttm_dict = {"date": date, "time": time}
    for result in process_exercises("apple"):
        add_records_to_sheet (workout_params={ **dttm_dict,
                                               **result } )
