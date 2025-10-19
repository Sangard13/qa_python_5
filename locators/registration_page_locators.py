from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    # Поля формы регистрации
    NAME_INPUT = (By.XPATH, "//input[@name='name']")
    EMAIL_INPUT = (By.XPATH, "//input[@type='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")

    # Ссылки
    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]")

    # Ошибки
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'input__error')]")

    # URL
    REGISTER_URL = "https://stellarburgers.education-services.ru/register"