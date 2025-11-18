import requests

params = {'amount':10, 'type':'boolean',}
print("getting data from server...")
response = requests.get('https://opentdb.com/api.php', params=params)
response.raise_for_status()
print("data obtained successfully")
question_data = response.json()['results']
