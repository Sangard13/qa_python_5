from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.login_data import LoginData
from locators.login_locators import LoginLocators


class LoginHelper:
    """Вспомогательный класс для операций логина"""

    @staticmethod
    def fill_login_form(driver, wait):
        """Заполнение формы логина"""
        wait.until(EC.visibility_of_element_located(LoginLocators.EMAIL_FIELD)).send_keys(LoginData.USER_EMAIL)
        wait.until(EC.visibility_of_element_located(LoginLocators.PASSWORD_FIELD)).send_keys(LoginData.USER_PASSWORD)
        wait.until(EC.element_to_be_clickable(LoginLocators.LOGIN_BUTTON)).click()

    @staticmethod
    def wait_for_login_page(wait):
        """Ожидание загрузки страницы логина"""
        wait.until(EC.url_contains("/login"))

    @staticmethod
    def wait_for_account_page(wait):
        """Ожидание загрузки личного кабинета"""
        wait.until(EC.url_contains("/account"))