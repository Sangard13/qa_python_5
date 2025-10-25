import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from locators.personal_account_locators import PersonalAccountLocators
from utils.data_generator import DataGenerator


class TestLogout:

    def test_logout_from_personal_account(self, driver):
        """Тест выхода из аккаунта через личный кабинет"""
        wait = WebDriverWait(driver, 10)
        user_data = DataGenerator.get_user_data()
        base_url = DataGenerator.get_base_url()

        # Логинимся
        driver.get(f"{base_url}/login")
        email_input = wait.until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        email_input.send_keys(user_data["email"])

        password_input = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input.send_keys(user_data["password"])

        login_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

        # Ждем главную страницу
        wait.until(EC.url_to_be(f"{base_url}/"))

        # Переходим в личный кабинет
        personal_account_button = wait.until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        personal_account_button.click()

        # Ждем загрузки личного кабинета
        wait.until(EC.url_contains("/account/profile"))

        # Выходим из аккаунта
        logout_button = wait.until(
            EC.element_to_be_clickable(PersonalAccountLocators.LOGOUT_BUTTON)
        )
        logout_button.click()

        # Проверяем переход на страницу логина
        wait.until(EC.url_to_be(f"{base_url}/login"))

        # Проверяем что мы на странице логина
        login_header = wait.until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_HEADER)
        )
        assert login_header.is_displayed()