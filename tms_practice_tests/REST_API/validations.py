from pydantic import BaseModel, EmailStr, ValidationError


class UserData(BaseModel):
    id: int = 0
    username: str
    firstName: str
    lastName: str
    email: EmailStr
    password: str
    phone: str
    userStatus: int = 0


def validation_user_data(user_data):
    try:
        user_model = UserData(**user_data.json())
        print("User information:")
        print("User ID:", user_model.id)
        print("Username:", user_model.username)
        print("First Name:", user_model.firstName)
        print("Email:", user_model.email)
        print("Last Name:", user_model.lastName)
        print("User Status:", user_model.userStatus)
        print("User phone:", user_model.phone)
    except ValidationError as e:
        print("Validation failed.")
        print(e)



def check_response(response,code):
    assert response.status_code == code, f'Status code is {response.status_code}'



def check_value(response,field, expected_value):
    json_data = response.json()
    assert json_data[field] == expected_value, f'{json_data[field]}'