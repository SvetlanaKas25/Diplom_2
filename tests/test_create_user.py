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


    @allure.title('Нельзя создать двух одинаковых пользователей')
    @allure.description("Тест проверяет, что нельзя создать двух пользователей с одинаковыми данными")
    def test_cannot_create_duplicate_user(self, create_data_user):
        user_data = create_data_user
        response1 = UserMethods.create_user(user_data)
        response2 = UserMethods.create_user(user_data)
        
        assert response2.status_code == 403, f"Ожидаемый статус код 403, но получили {response2.status_code}" 
        assert response2.json()["message"] == USER_ALREADY_EXISTS

