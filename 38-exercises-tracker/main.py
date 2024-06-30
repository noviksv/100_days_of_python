import requests
from dotenv import load_dotenv
import os
import datetime

load_dotenv()


def process_exercises(query):

    headers = {
        "x-app-id": os.getenv("NUTRITIONIX_ID"),
        "x-app-key": os.getenv("NUTRITIONIX_KEY"),
        "Content-Type": "application/json"
    }

    host = "https://trackapi.nutritionix.com"
    # endpoint = "/v2/natural/nutrients"
    # r = requests.post(url=f"{host}{endpoint}",headers=headers, params={"query":"1 large apple"})


    endpoint = "/v2/search/instant"
    r = requests.get(url=f"{host}{endpoint}",headers=headers, params={"query":"apple"})


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
    for exercise in data["exercises"]:
        print(exercise["name"], exercise["duration_min"], exercise["nf_calories"])


if __name__ == "__main__":
    exercise_input  = input("Tell me which exercises you did: ")
    process_exercises(exercise_input)   
