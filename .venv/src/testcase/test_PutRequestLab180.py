from http.client import responses

# PUT - REquest
# URL
# Path - Booking ID
# Token - Auth
# Payload
# Headers

import allure
import pytest
import requests


# Create Token - POST
# def create_token():
#     url = "https://restful-booker.herokuapp.com/auth"
#     headers = {"Content-Type": "application/json"}
#     json_payload = {
#         "username": "admin",
#         "password": "password123"
#     }
#     response = requests.post(url=url, headers=headers, json=json_payload)
#     token = response.json()["token"]
#     print(token)
#     return token
#
#
# Create Booking - POST
def create_booking():
    # Booking ID
    print("Create Booking Testcase")
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "firstname": "Amit",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=url, headers=headers, json=json_payload)
    print(type(url))
    print(type(headers))
    print(type(json_payload))

    #Assertion
    assert response.status_code == 200
    #get the response Body and verify the JSON, Booking ID is not None
    data = response.json()
    booking_id = data["bookingid"]
    return booking_id


# PUT REquest
def test_put_request_positive():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking())
    PUT_URL = base_url + base_path
    cookie = "token=" + create_token()
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }
    json_payload = {
        "firstname": "Amit",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.put(url=PUT_URL, headers=headers, json=json_payload)
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data["firstname"] == "Amit"
