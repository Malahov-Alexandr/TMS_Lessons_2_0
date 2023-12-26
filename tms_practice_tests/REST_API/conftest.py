import pytest
from faker import Faker

from fake_data import fake_data

username, firstname, lastname, email, phone, password = fake_data()
@pytest.fixture
def user_info():
    data = {
        "id": 0,
        "username": username,
        "firstName": firstname,
        "lastName": lastname,
        "email": email,
        "password": "string",
        "phone": phone,
        "userStatus": 0
    }

    return data
