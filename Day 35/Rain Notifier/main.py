import requests, os
from twilio.rest import Client

api_key = os.environ.get('TWILIO_API_KEY')
params = {'lat': 41.493488, 'lon': -1.365700, 'appid': api_key, 'cnt': 4,}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=params)
response.raise_for_status()

weather_data = response.json()['list']
weather_conditions_codes = (item['weather'][0]['id'] for item in weather_data)
it_will_rain = any(code < 700 for code in weather_conditions_codes)

if it_will_rain:
    # send sms
    account_sid, auth_token = os.environ.get('TWILIO_ACCOUNT_SID'), os.environ.get("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)
    message = client.messages.create(from_='+19522436053', body='grab an ☂️️', to='+56928121317')
    print(message.sid)