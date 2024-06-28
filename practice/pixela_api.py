import requests
from dotenv import load_dotenv
import os

load_dotenv()
 

PIXELA_TOKEN = os.getenv("PIXELA_TOKEN")
PIXELA_USER = os.getenv("PIXELA_USER")
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{PIXELA_USER}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "commit",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

graph_id = "graph1"

add_pixel_endpoint = f"{pixela_endpoint}/{PIXELA_USER}/graphs/{graph_id}"

add_pixel_config = {
    "date": "20240625",
    "quantity": "1"

}

response = requests.post(url=add_pixel_endpoint, json=add_pixel_config, headers=headers)
print(response.text)