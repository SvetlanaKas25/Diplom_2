import requests
import allure

from URLs import URL

class UserMethods:

    @staticmethod
    @allure.step("Создание нового пользователя")
    def create_user(data_user):
        return requests.post(url=URL.CREATE_USER_ENDPOINT, json=data_user)
    
    @staticmethod
    @allure.step("Авторизация пользователя")
    def login_user(data_user):
        return requests.post(url=URL.LOGIN_USER_ENDPOINT, json=data_user)
    
    @staticmethod
    @allure.step("Удаление пользователя")
    def delete_user(token):
        headers = {'Authorization': token}
        return requests.delete(URL.DELETE_USER_ENDPOINT, headers=headers)
    
    