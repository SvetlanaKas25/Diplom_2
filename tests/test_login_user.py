import pytest
import allure

from messages import INCORRECT_DATA
from api_methods.user_methods import UserMethods


class TestLoginUser:

    @allure.title("Авторизация пользователя")
    @allure.description("Тест проверяет, что пользователь может авторизоваться  с корректными данными")
    def test_login_user_success(self, new_user):
        data_user = new_user
        response = UserMethods.login_user(data_user)
        assert response.status_code == 200, f"Ожидаемый статус код 200, но получили {response.status_code}"
        assert response.json()["success"] is True

