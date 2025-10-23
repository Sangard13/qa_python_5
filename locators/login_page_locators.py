from selenium.webdriver.common.by import By

class LoginPageLocators:
    EMAIL_INPUT = (By.NAME, "name")
    PASSWORD_INPUT = (By.NAME, "Пароль")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'input__error')]")

    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    LOGIN_HEADER = (By.XPATH, "//h2[text()='Вход']")