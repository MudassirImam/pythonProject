# Create Booking testcase
# verify that booking is not null
# status code, Headers...

# Request Module - Module -> Package or library contains functions which you can use easily
# pip install request
# To make the HTTP - Methods
# GET, POST, PUT, PATCH, DELETE, OPTIONS...HTTP Methods
# URL, Auth, Cookies, Verification with pytest.
# Request(Client-Server)

# GET Request Automation
# 1. URL
import pytest
import allure
import requests

@allure.title("Test GET Request - RestFUL Booker Project#1")
@allure.description("TC#1-> verify that GET Request with ID works")
@allure.tag("regression","p0","smoke")
@allure.label("owner","Md Mudassir")
@allure.testcase("TC#1")
@pytest.mark.smoke
def test_get_single_request_by_id_positive():
    url = "https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url)
    print(response_data.text)
    print(response_data.json())
    print(response_data.headers)
    assert response_data.status_code == 200

# Negative TC
@allure.title("Test GET Request - RestFUL Booker Project#2")
@allure.description("TC#2-> verify that GET Request with invalid booking")
@pytest.mark.smoke
def test_get_single_request_by_id_negative():
    url = "https://restful-booker.herokuapp.com/booking/-1"
    response_data = requests.get(url)
    print(response_data.text)
    assert response_data.status_code == 404

# Negative TC3
@allure.title("Test GET Request - RestFUL Booker Project#3")
@allure.description("TC#3-> verify that GET Request with invalid booking")
@pytest.mark.smoke
def test_get_single_request_by_id_negative_invalid():
    url = "https://restful-booker.herokuapp.com/booking/invalid"
    response_data = requests.get(url)
    print(response_data.text)
    assert response_data.status_code == 404
