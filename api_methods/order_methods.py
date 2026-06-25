import requests
import allure

from URLs import URL

class OrderMethods:

    @staticmethod
    @allure.step("Получение списка ингредиентов")
    def get_ingredients():
        return requests.get(URL.INGREDIENTS_ENDPOINT)
    
        
    @staticmethod
    @allure.step("Создание заказа")
    def create_order(token, ingredients):
        headers = {'Authorization': token}
        data = {"ingredients": ingredients}
        return requests.post(URL.CREATE_ORDER_ENDPOINT, json=data, headers=headers)
    
    