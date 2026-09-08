from faker import Faker
from random import sample


faker = Faker()
# Метод генерирования данных для нового пользователя
def generate_user_create_data():
    data = {
        "email": faker.email(),
        "password": faker.password(),
        "name": faker.first_name()
        }
    
    return data


# Метод собирает значения поля _id каждого ингредиента в новый список и выбирает 3 уникальных идентификаторов из полученного списка.
def generate_order_data(ingredients, count=3):
    return sample([ing['_id'] for ing in ingredients], count)

