from http.client import responses

import allure
import pytest
import requests

@allure.title("TC#1 - Create Booking CRUD Positive")
@allure.description("TC#1 - Verify the create Booking!")
@pytest.mark.crud
def test_create_booking_positive_tc1():
    # To make request
    # URL
    # Method - POST
    # Headers - Content-type=Application/json
    # Payload/Data/Body - Dict/JSON
    # Auth(No)
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url+ base_path
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=payload)
    assert response.status_code ==200
    responseData = response.json()

    # Response Body Verification,
    # Headers
    bookingid = responseData["bookingid"]
    assert bookingid is not None
    assert bookingid > 0
    assert type(bookingid) == int

    firstname = responseData["booking"]["firstname"]
    lastname = responseData["booking"]["lastname"]
    totalprice = responseData["booking"]["totalprice"]
    depositpaid = responseData["booking"]["depositpaid"]

    assert firstname == "Jim"
    assert lastname == "Brown"
    assert totalprice == 111
    assert depositpaid == False

    checkin = responseData["booking"]["bookingdates"]["checkin"]
    checkout = responseData["booking"]["bookingdates"]["checkout"]
    assert checkin == "2018-01-01"
    assert checkout == "2019-01-01"

    # JSON Schema Validatio
    # Time Response


@allure.title("TC#2 - Create Booking CRUD Negative")
@allure.description("TC#2 - Verify booking is not created with {} data")
@pytest.mark.crud
def test_create_booking_negative_tc2():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url+ base_path
    headers = {"Content-Type": "application/json"}
    json_payload = {}
    response = requests.post(url=URL, headers=headers, json=json_payload)
    print(type(URL))
    print(type(headers))
    print(type(json_payload))

    # Assertions
    assert response.status_code == 500

@allure.title("TC#3 - Create Booking CRUD Negative")
@allure.description("TC#3 - Verify booking with totalprice string negative ")
@pytest.mark.crud
def test_create_booking_negative_tc3():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url+ base_path
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": "mudassir",
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=payload)

    # Assertion
    assert response.status_code == 500