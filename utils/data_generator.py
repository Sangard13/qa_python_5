class DataGenerator:

    @staticmethod
    def get_base_url():
        """Возвращает базовый URL"""
        return "https://stellarburgers.education-services.ru"

    @staticmethod
    def get_user_data():
        """Возвращает данные пользователя для тестов"""
        return {
            "name": "Aleksandr",
            "email": "Alex.Br_33@gmail.com",
            "password": "1Qasw234RTy"
        }

    @staticmethod
    def get_user_name():
        return "Александр"

    @staticmethod
    def get_valid_password():
        return "1Qasw234RTy"

    @staticmethod
    def get_minimum_password():
        return "123456"

    @staticmethod
    def get_short_password():
        return "12345"

    @staticmethod
    def get_invalid_email():
        return "invalid-email"