import requests
from datetime import datetime

TOKEN = " "             # ENTER YOUR TOKEN FROM API
USERNAME = " "    # ENTER YOUR USERNAME FROM API
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()  # Can be used to add yesterday or days prior.
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many km did you cycle today? "),
}

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"
pixel_update = {
    "quantity": "10",
}

today_date = "20240729"
pixel_delete = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"
response = requests.delete(url=pixel_delete, headers=headers)
print(response.text)
