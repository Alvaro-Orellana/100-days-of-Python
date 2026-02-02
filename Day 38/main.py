import requests
import datetime
import os


APP_ID = os.environ.get("APP_ID")
APP_KEY = os.environ.get("APP_KEY")
SHEET_API_ENDPOINT = os.environ.get("SHEET_API_ENDPOINT")
SHEETY_ACCESS_TOKEN = os.environ.get("SHEETY_ACCESS_TOKEN")

BASE_URL = 'https://app.100daysofpython.dev'
ENDPOINT = '/v1/nutrition/natural/exercise'

headers = {
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY
}
exercise = input("Tell me which exercises you did today: ")
body = {
    "query": exercise
}

response = requests.post(BASE_URL + ENDPOINT, headers=headers, json=body)
response.raise_for_status()
data = response.json()
print(data['exercises'][0])

duration = data['exercises'][0]['duration_min']
exercise = data['exercises'][0]['name']
calories = data['exercises'][0]['nf_calories']
ahora = datetime.datetime.now()


sheety_body = {
    'workout' : {
        'Date' : ahora.strftime("%d/%m/%Y"),
        'Time' : ahora.strftime("%H:%M:%S"),
        'Exercise' : exercise,
        'Duration' : duration,
        'Calories' : calories,
    }
}
header2 = {
    'Authorization': f"Authorization: Bearer {SHEETY_ACCESS_TOKEN}",
    'Content-Type': 'application/json',
}

response = requests.post(SHEET_API_ENDPOINT, headers=header2, json=sheety_body)
response.raise_for_status()
print(response.json())
