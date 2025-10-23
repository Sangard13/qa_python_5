from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы для главной страницы"""
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")


class LoginLocators:
    """Локаторы для страницы логина"""
    EMAIL_FIELD = (By.NAME, "name")
    PASSWORD_FIELD = (By.NAME, "Пароль")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")


class RegisterLocators:
    """Локаторы для страницы регистрации"""
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")


class ForgotPasswordLocators:
    """Локаторы для страницы восстановления пароля"""
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")