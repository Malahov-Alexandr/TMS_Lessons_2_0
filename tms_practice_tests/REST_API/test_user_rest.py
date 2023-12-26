# На сайте https://petstore.swagger.io/ покрыть минимум одним тестов ручки
# GET /user/{username}
# PUT /user/{username}
# DELETE /user/{username}
# POST /user
# Сделать это нужно в классе, каждый тест - одна функция. Прошу использовать фикстуры для создания тестовых данных.
# Можно сделать по аналогии с тем, что мы писали вчера.
# === Со звёздочкой ===
# Завершить последний тест из файлика test_petstore
from actions import *
from validations import *
import pytest


class TestUser:

    def test_user_post(self,user_info):
        create_user(user_info)

    def test_get_user_info(self,user_info):
        validation_user_data(get_user(user_info))

    def test_put_data_to_user(self,user_info):
        update_user_data(user_info,'phone','12345')
        data = get_user(user_info)
        validation_user_data(data)
        check_value(data,'phone', '12345')


    def test_user_login(self,user_info):
        user_login(user_info).json()

    def test_delete_user(self,user_info):
        name = user_info['username']
        response = delete_user(name)
        print(response.status_code)




    # def test_delete_user(self,user_info):
    #     response = delete_user(user_info['username'])
    #     response_after_deleting = get_user(user_info)
    #     check_response(response_after_deleting.json(),404)


