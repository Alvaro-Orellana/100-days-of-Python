import requests

params = {
    "lat": -22.4623917,
    "lng": -68.9272181,
    'formatted': 0,
}
response = requests.get('https://api.sunrise-sunset.org/json', params=params)
response.raise_for_status()
print(response.json())

