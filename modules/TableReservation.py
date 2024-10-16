import json
import requests
import config


def createTableReservation(data):
    url = "".join((
        config.urls["route_url"], ":", 
        config.urls["table_reservation"]["port"],
        config.urls["table_reservation"]["route_path"],
        config.urls["table_reservation"]["endpoints"]["reserve"]
    ))
    print(f"url: {url}")

    response = requests.post(url, json=data)
    print(f"Response from server: status code: {response.status_code}, message: {response.content}")