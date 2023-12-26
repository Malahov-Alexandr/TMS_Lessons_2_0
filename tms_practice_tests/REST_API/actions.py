from validations import *
import requests


class UsersEndpoints:
    HOST = "https://petstore.swagger.io/v2"
    USER = "/user/"
    USER_LOGIN = "/user/login?username={name}&password={password}"
    USER_LOGOUT = '/user/logout'


def create_user(user_info):
    url = f'{UsersEndpoints.HOST}{UsersEndpoints.USER}'
    response = requests.post(url, json=user_info)
    check_response(response, 200)
    return response


def get_user(user_info):
    name = user_info["username"]
    url = f'{UsersEndpoints.HOST}{UsersEndpoints.USER}{name}'
    print(url)
    response = requests.get(url)
    return response


def update_user_data(user_info, field, value):
    name = user_info["username"]
    get_response = get_user(user_info)
    user_data = get_response.json()
    user_data[field] = value
    url = f'{UsersEndpoints.HOST}{UsersEndpoints.USER}{name}'
    new_response = requests.put(url, json=user_data)
    check_response(new_response, 200)


def user_login(user_info):
    name = user_info['username']
    password = user_info['password']
    url = f"{UsersEndpoints.HOST}{UsersEndpoints.USER_LOGIN.format(name=name, password=password)}"
    response = requests.get(url)
    check_response(response, 200)
    return response


# it has code 200 only
# def user_logout():
#     url = f"{UsersEndpoints.HOST}{UsersEndpoints.USER_LOGOUT}"
#     response = requests.get(url)
#     check_response(response, 200)
def delete_user(name):
    url = f'{UsersEndpoints.HOST}{UsersEndpoints.USER}{name}'
    response = requests.delete(url)
    check_response(response, 200)
    return response
