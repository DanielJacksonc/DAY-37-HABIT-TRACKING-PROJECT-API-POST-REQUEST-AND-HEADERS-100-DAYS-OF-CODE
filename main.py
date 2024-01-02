import requests
from datetime import datetime


today_date = datetime.now().today().date().strftime("%Y%m%d")
print(today_date)
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "danielj"
TOKEN = "Ehyrtb4snj3orjdn"
GRAPH_ID= "graph3"
API_PARAM = {
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
""" we use json in posting instead of our normal params"""
# response = requests.post(url=PIXELA_ENDPOINT, json=API_PARAM)
# print(response.text)

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config= {
    "id": GRAPH_ID,
    "name": "Coding Tracker",
    "unit": "Min",
    "type": "float",
    "color": "ajisai",
}

headers = {"X-USER-TOKEN": TOKEN}
graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(graph_response.text)



pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
header = {"X-USER-TOKEN": TOKEN}
pixel_config = {
    # Initially the date was hardcoded i.e "date":"20230101, but using the stfttime function, i made it dynamic
    "date": today_date,
    "quantity": input("How Many hours did you code today? 😊"),

}

pixels_response = requests.post(url=pixel_endpoint, json=pixel_config, headers =header)
print(pixels_response.text)

# Lets assume i masde a mistake in my data entry and want to change the data, i will use put
# create a change endpoint
change_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{20240101}"

# create change parameters
change_config = {
"quantity":"10",
}

change_response = requests.put(url=change_endpoint, json=change_config, headers=header)
print(change_response.text)



# to delete an entry

# delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{20240101}"
# delete_response = requests.delete(url=delete_endpoint,headers=header)
# print(delete_response.text)
