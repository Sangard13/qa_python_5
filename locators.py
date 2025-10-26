from selenium.webdriver.common.by import By

class LoginPageLocators:
    EMAIL_FIELD = (By.NAME, "name")
    PASSWORD_FIELD = (By.NAME, "Пароль")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")


class MainPageLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")


class PersonalAccountLocators:
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    PROFILE_SECTION = (By.XPATH, "//a[contains(@class, 'Account_link') and contains(@href, '/profile')]")

# URL
BASE_URL = "https://stellarburgers.education-services.ru/login"
REGISTER_URL = f"{BASE_URL}/register"
LOGIN_URL = f"{BASE_URL}/login"
ACCOUNT_URL = f"{BASE_URL}/account"

# Поля формы логина
LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@type='email' or @name='email' or @name='name']")
LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")

# Поля формы регистрации
REGISTER_NAME_INPUT = (By.XPATH, "//input[@name='name']")
REGISTER_EMAIL_INPUT = (By.XPATH, "//input[@type='email']")
REGISTER_PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")

# Кнопки на главной странице
LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")

# Ошибки
ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'input__error')]")