import requests
from datetime import datetime

#links to view profile and graph
#https://pixe.la/@alvarohernan
#https://pixe.la/v1/users/alvarohernan/graphs/graph1.html
USERNAME = 'alvarohernan'
TOKEN = 'ar9asf00+q#4@/grt%'
GRAPH_ID = 'graph1'

body = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# create user
#response = requests.post("https://pixe.la/v1/users", json=body)
#print(response.text)

# create graph
headers = {
    'X-USER-TOKEN': TOKEN,
}
graph_request_body = {
    "id": GRAPH_ID,
    "name": 'graph1',
    'unit': 'commit',
    'type': 'int',
    'color': 'ajisai',
    'startOnMonday': True,
}

#graph_response = requests.post(f"https://pixe.la/v1/users/{USERNAME}/graphs", headers=headers, json=graph_request_body)
#print(graph_response.text)

today = datetime.now().strftime('%Y%m%d')
pixel_resquest_body = {
    'date': today,
    'quantity': "5",
}

#pixel_respsonse = requests.post(f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}", headers=headers, json=pixel_resquest_body)
#print(pixel_respsonse.status_code)
#print(pixel_respsonse.text)
#print(pixel_respsonse.json())

pixel_put_request_body = {
    'quantity': "5",
}

#pixel_update_response = requests.put(f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{today}", headers=headers, json=pixel_put_request_body)
#print(pixel_update_response.text)

pixel_delete_response = requests.delete(f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{today}", headers=headers)
print(pixel_delete_response.text)



