from selenium.webdriver.common.by import By

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