class LoginData:
        # Базовый URL
        BASE_URL = "https://stellarburgers.education-services.ru"

        # Полные URL формируются на основе BASE_URL
        LOGIN_URL = f"{BASE_URL}/login"
        REGISTER_URL = f"{BASE_URL}/register"
        FORGOT_PASSWORD_URL = f"{BASE_URL}/forgot-password"
        ACCOUNT_URL = f"{BASE_URL}/account"
        PROFILE_URL = f"{BASE_URL}/account/profile"

        # Тестовые данные
        USER_EMAIL = "Alex.Br_33@gmail.com"
        USER_PASSWORD = "1Qasw234RTy"