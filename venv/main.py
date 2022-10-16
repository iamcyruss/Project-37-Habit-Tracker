# create user
# curl -X POST https://pixe.la/v1/users -d '{"token":"yum", "username":"iamcyruss", "agreeTermsOfService":"yes", "notMinor":"yes"}'

import requests
import os
import datetime

currentDate = datetime.date.today()
currentDate = currentDate.strftime("%Y%m%d")

USERNAME = "iamcyruss"
PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")
GRAPH_ID = "pianograph01"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": PIXELA_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

pixela_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
headers = {
    "X-USER-TOKEN": PIXELA_TOKEN,
}

graph_params = {
    "id": GRAPH_ID,
    "name": "Habit Tracker - Test",
    "unit": "hours",
    "type": "float",
    "color": "kuro",
}

#date = input("What's today's date in yyyyMMdd format? ")
hours = input("How many hours did you spend practicing? ")
create_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

graph_update = {
    "date": currentDate,
    "quantity": hours,
}

update_graph = {
    "quantity": "0.5"
}

update_pixel_endpoint = f"{create_pixel_endpoint}/{currentDate}"

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.json()["message"])
graph_response = requests.post(url=pixela_graph_endpoint, json=graph_params, headers=headers)
print(graph_response.json())
# https://pixe.la/v1/users/iamcyruss/graphs/pianograph01.html
create_graph_response = requests.post(url=create_pixel_endpoint, headers=headers, json=graph_update)
print(create_graph_response.json())
update_graph_response = requests.put(url=update_pixel_endpoint, headers=headers, json=update_graph)
print(update_graph_response.json())

