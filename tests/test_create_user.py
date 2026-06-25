import pytest
import allure

from messages import USER_ALREADY_EXISTS, NOT_ENOUGH_CREATE_DATA
from api_methods.user_methods import UserMethods
from helpers import generate_user_create_data



class TestCreateUser:

    @allure.title("Создание пользователя")
    @allure.description("Тест проверяет, что можно создать пользователя  с корректными данными")
    def test_create_user_success(self, create_data_user):
        user_data = create_data_user
        response = UserMethods.create_user(user_data)
        assert response.status_code == 200, f"Ожидаемый статус код 200, но получили {response.status_code}"
        assert response.json()["success"] is True

