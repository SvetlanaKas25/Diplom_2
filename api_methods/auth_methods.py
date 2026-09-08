import allure

from api_methods.user_methods import UserMethods


class AuthMethods:
    
    @staticmethod
    def auth_token(user_data):
        with allure.step("Получение токена авторизации"):
            response = UserMethods.login_user(user_data)
            return response.json()['accessToken']
    
    