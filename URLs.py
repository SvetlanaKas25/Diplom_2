class URL:
    BASE_URL = "https://stellarburgers.education-services.ru"
    
    # Ручка - Создание пользователя
    CREATE_USER_ENDPOINT = f"{BASE_URL}/api/auth/register"
    
    # Ручка - Авторизация пользователя
    LOGIN_USER_ENDPOINT = f"{BASE_URL}/api/auth/login"

    # Ручка - Удаление пользователя
    DELETE_USER_ENDPOINT = f"{BASE_URL}/api/auth/user"

    # Ручка - Получение данных об ингредиентах
    INGREDIENTS_ENDPOINT = f"{BASE_URL}/api/ingredients"

    # Ручка - Создание заказа
    CREATE_ORDER_ENDPOINT = f"{BASE_URL}/api/orders" 
    
    