import allure
import pytest

from api_methods.order_methods import OrderMethods
from api_methods.auth_methods import AuthMethods
from helpers import generate_order_data
from messages import NO_INGREDIENTS



@allure.feature("Создание заказа")
class TestOrderCreation:

    @allure.title("Успешное создание заказа авторизованным пользователем")
    def test_create_order_authorized(self, new_user, ingredients):
        login_pass = new_user
        order_data = generate_order_data(ingredients)
        token = AuthMethods.auth_token(login_pass)
        response = OrderMethods.create_order(token, order_data)
        
        assert response.status_code == 200, f"Ожидаемый статус код 200, но получили {response.status_code}"
        assert response.json()["success"] is True


    @allure.title("Успешное создание заказа неавторизованным пользователем")
    def test_create_order_not_authorized(self, ingredients):
        order_data = generate_order_data(ingredients)
        response = OrderMethods.create_order("", order_data)
        
        assert response.status_code == 200, f"Ожидаемый статус код 200, но получили {response.status_code}"
        assert response.json()["success"] is True


    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self):
        response = OrderMethods.create_order("", [])
        
        assert response.status_code == 400, f"Ожидаемый статус код 400, но получили {response.status_code}"
        assert NO_INGREDIENTS in response.json()["message"]
