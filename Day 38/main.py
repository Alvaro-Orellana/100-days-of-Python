import requests

APP_KEY = 'nix_live_9x1aMPoW9YIJcWaqYXJoCSwyUiwM3TCO'
APP_ID = 'app_209039621b3d48cd913938e9'
BASE_URL = 'https://app.100daysofpython.dev'

endpoint = '/v1/nutrition/natural/exercise'

headers = {
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY
}

exersise = input("Tell me which exercises you did today: ")
body = {
    "query": exersise
}

response = requests.post(BASE_URL+endpoint, headers=headers, json=body)
response.raise_for_status()

data = response.json()

print(data['exercises'][0])