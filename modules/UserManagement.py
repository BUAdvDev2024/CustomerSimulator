import json
import requests
import config

'''
Returns either an error or the auth token
'''
def loginWithCustomerCredentials(email: str, password: str):
    url = "".join((
        config.urls["route_url"], ":", 
        config.urls["user_management"]["port"],
        config.urls["user_management"]["route_path"],
        config.urls["user_management"]["endpoints"]["login"]
    ))
    print(f"url: {url}")

    response = requests.post(url, json={ "email": email, "password": password})
    print(f"Response from server: status code: {response.status_code}, message: {response.json().get("message")}")

def registerCustomerWithCredentials(email: str, password):
    url = "".join((
        config.urls["route_url"], ":", 
        config.urls["user_management"]["port"],
        config.urls["user_management"]["route_path"],
        config.urls["user_management"]["endpoints"]["register"]
    ))
    print(f"url: {url}")

    response = requests.post(url, json={ "email": email, "password": password})
    print(f"Response from server: status code: {response.status_code}, message: {response.json().get("message")}")

