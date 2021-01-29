"""
Python: Pytest
        Learning Pytest with Examples
        Pytest On Login Validation
"""

import pytest
import requests
import json


def main_url():
    return "https://reqres.in"


def test_login_valid(main_url="https://reqres.in"):
    url = main_url + "/api/login/"
    data = {
        "email": "eve.holt@reqres.in",
        #"email": "abc@xyz.in",
        "password": "cityslicka"
            }
    response = requests.post(url, data=data)
    token = json.loads(response.text)
    assert response.status_code == 200
    assert token['token'] == "QpwL5tke4Pnpja7X4"
