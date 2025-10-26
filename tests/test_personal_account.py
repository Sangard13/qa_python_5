import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.user_data import UserData
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from locators.personal_account_locators import PersonalAccountLocators


class TestPersonalAccount:
    def test_navigate_to_personal_account_from_main_page(self, driver):
        """Тест перехода в личный кабинет с главной страницы"""
        wait = WebDriverWait(driver, 10)

        # Открытие страницы логина
        driver.get(f"{UserData.BASE_URL}/login")

        # Ввод email - используем локаторы из отдельного модуля
        email_field = wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))
        email_field.send_keys(UserData.USER_EMAIL)

        # Ввод пароля
        password_field = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_field.send_keys(UserData.USER_PASSWORD)

        # Нажатие кнопки входа
        login_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

        # Ожидание главной страницы
        wait.until(EC.url_to_be(f"{UserData.BASE_URL}/"))

        # Нажатие кнопки личного кабинета
        personal_account_button = wait.until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        personal_account_button.click()

        # Проверка перехода в личный кабинет
        wait.until(EC.url_contains("/account/profile"))
        assert "/account/profile" in driver.current_url

    def test_logout_from_personal_account(self, driver):
        """Тест выхода из аккаунта через личный кабинет"""
        wait = WebDriverWait(driver, 10)

        # Логинимся
        driver.get(f"{UserData.BASE_URL}/login")

        email_field = wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))
        email_field.send_keys(UserData.USER_EMAIL)

        password_field = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_field.send_keys(UserData.USER_PASSWORD)

        login_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

        # Переходим в личный кабинет
        wait.until(EC.url_to_be(f"{UserData.BASE_URL}/"))
        personal_account_button = wait.until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        personal_account_button.click()

        # Выходим из аккаунта
        wait.until(EC.url_contains("/account/profile"))
        logout_button = wait.until(
            EC.element_to_be_clickable(PersonalAccountLocators.LOGOUT_BUTTON)
        )
        logout_button.click()

        # Проверка перехода на страницу логина
        wait.until(EC.url_contains("/login"))
        assert "/login" in driver.current_url

    def test_personal_account_requires_authentication(self, driver):
        """Тест что личный кабинет требует авторизации"""
        # Пытаемся открыть личный кабинет без авторизации
        driver.get(f"{UserData.BASE_URL}/account/profile")

        # Проверяем текущий URL
        current_url = driver.current_url

        # БАГ: Личный кабинет доступен без авторизации
        assert "/account/profile" not in current_url, "БАГ: Личный кабинет доступен без авторизации"