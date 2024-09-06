import requests
from datetime import datetime
import os

APP_ID = "7f22d128"
API_KEY = "f8c1cd061cc22832b8638efa7df35016"

sheet_endpoint = "https://api.sheety.co/de010897c8493f503fdd78fb6bc7bc47/myExercise/workouts"

GENDER = "female"
WEIGHT = 58
HEIGHT = 154
AGE = 23
query_text = input("which exercise do you do today?")

parameter = {
    "query": query_text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=parameter, headers=header)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    #sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        auth=(
            "janeabisha",
             "Janeabisha@28",
        )
    )

    print(sheet_response.status_code)

    print(sheet_response.text)



