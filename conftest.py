import pytest
import allure

from api_methods.user_methods import UserMethods
from api_methods.auth_methods import AuthMethods
from api_methods.order_methods import OrderMethods
from helpers import generate_user_create_data

# Создание данных для регистрации нового пользователя, удаление пользователя после теста
@pytest.fixture(scope="function")
def create_data_user():
    user_data = generate_user_create_data()
    
    yield user_data

    login_pass = {
            "email": user_data["email"],
            "password": user_data["password"]
        }
    token = AuthMethods.auth_token(login_pass)
    UserMethods.delete_user(token)


# Создание нового пользователя, удаление пользователя после теста
@pytest.fixture(scope="function")
def new_user():
    user_data = generate_user_create_data()
    create_response = UserMethods.create_user(user_data)
    login_pass = {
            "email": user_data["email"],
            "password": user_data["password"]
        }
    
    yield login_pass
    
    token = AuthMethods.auth_token(login_pass)
    UserMethods.delete_user(token)
    