import allure
import pytest
import requests

def test_selenium(launch_browser, close_browser):
    launch_browser
    print("Do Tc")
    close_browser

