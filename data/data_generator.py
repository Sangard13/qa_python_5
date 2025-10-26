import random
import string
from datetime import datetime


class DataGenerator:
    """Класс для генерации динамических тестовых данных"""

    @staticmethod
    def generate_unique_email(prefix="test.user"):
        """Генерирует уникальный email"""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        random_suffix = ''.join(random.choices(string.ascii_lowercase, k=5))
        return f"{prefix}.{timestamp}.{random_suffix}@example.com"

    @staticmethod
    def generate_password(length=8):
        """Генерирует случайный пароль"""
        chars = string.ascii_letters + string.digits
        return ''.join(random.choices(chars, k=length))

    @staticmethod
    def generate_user_name():
        """Генерирует случайное имя пользователя"""
        names = ["Иван", "Мария", "Петр", "Анна", "Сергей", "Ольга"]
        return random.choice(names)