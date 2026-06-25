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


    @pytest.mark.parametrize("key,value", [
        ("email", "wrongemail@yandex.ru"),
        ("password", "wrongpassword"),
        ])
    @allure.title("Проверка, система вернёт ошибку, если неправильно указать email или пароль")
    @allure.description("Тест проверяет, что при вводе неверного email или пароля из пары email-password зарегистрированного пользователя, система вернёт ошибку")
    def test_incorrect_data_login_user_returns_error(self, new_user, key, value):
        user_data = new_user.copy()
        user_data[key] = value

        with allure.step(f"Попытка авторизации пользователя с неверным полем: {key}"):
            response = UserMethods.login_user(user_data)
        assert response.status_code == 401, f"Ожидаемый статус код 401, но получили {response.status_code}"
        assert INCORRECT_DATA in response.json()["message"]

