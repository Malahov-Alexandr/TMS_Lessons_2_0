from datetime import datetime

import pytest
import requests

OUR_NAME = "TMS_PET_{}"


class Status:
    AVAILABLE = "available"
    PENDING = "pending"
    SOLD = "sold"


class PetStore:
    HOST = "https://petstore.swagger.io/v2"
    PET = "/pet"
    PET_FIND_BY_STATUS = "/pet/findByStatus?status={0}"
    PET_PET_ID = "/pet/{petId}"


@pytest.fixture
def pet_info():
    current_timestamp = int(datetime.now().timestamp())
    data = {
        "id": 0,
        "category": {"id": 0, "name": "string"},
        "name": OUR_NAME.format(current_timestamp),
        "photoUrls": ["string"],
        "tags": [{"id": 0, "name": "string"}],
        "status": "available",
    }

    return data


# === ACTIONS ==================================================================


def create_pet(pet_info):
    # Arrange
    url = f"{PetStore.HOST}{PetStore.PET}"

    # Act
    response = requests.post(url, json=pet_info)
    check_response(response)

    return response


def get_pets_by_status(target_status):
    url = f"{PetStore.HOST}{PetStore.PET_FIND_BY_STATUS.format(target_status)}"
    response = requests.get(url)

    check_response(response)
    data = response.json()
    return data


# === VALIDATIONS ==============================================================


def check_response(response):
    assert response.ok, f"{response.status_code = }"


def check_name(response, expected_name):
    json_data = response.json()
    assert json_data["name"] == expected_name, f'{json_data["name"] = }'


# === TEST CLASS ===============================================================

class TestPetStore:
    def test_create_pet(self, pet_info):
        # Arrange + Act
        response = create_pet(pet_info)

        # Assert
        check_response(response)
        check_name(response, pet_info["name"])

    def test_read_pet_available(self):
        # Arrange + Act
        response = get_pets_by_status(Status.AVAILABLE)
        print(response[0])
        # Assert

        first_pet = response[0]

        expected_keys = [
            "id",
            "category",
            "name",
            "photoUrls",
            "tags",
            "status",
        ]
        err_msg = f"There were unexpected keys, {first_pet.keys}"
        assert list(first_pet.keys()) == expected_keys, err_msg
    def test_update_pet(self, pet_info):
        # Arrange
        response_1 = create_pet(pet_info)
        json_data = response_1.json()
        pet_id = json_data["id"]
        name_current = json_data["name"]
        name_new = name_current.replace("TMS_", "SMS_")
        json_data["name"] = name_new

        url = f"{PetStore.HOST}{PetStore.PET}"

        # Act
        response_2 = requests.put(url, json=json_data)
        check_response(response_2)

        url = f"{PetStore.HOST}{PetStore.PET_PET_ID.format(petId=pet_id)}"
        response_3 = requests.get(url)

        # Assert
        check_name(response_3, name_new)

    def test_delete_pet(self, pet_info):
        # Arrange
        # Create a pet
        # Act
        # Delete a pet
        # Assert
        # Iterate through all pets and not find the one that we deleted
        pass
