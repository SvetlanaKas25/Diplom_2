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

