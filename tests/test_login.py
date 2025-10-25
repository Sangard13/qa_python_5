import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.user_data import UserData
from locators.main_page_locators import MainPageLocators
from locators.login_page_locators import LoginPageLocators


class TestLogin:
    def test_login_via_personal_account_button(self, driver):
        """Вход через кнопку 'Личный кабинет' на главной странице"""
        # Инициализация ожидания
        wait = WebDriverWait(driver, 10)

        # Открытие главной страницы
        driver.get(UserData.BASE_URL)

        # Ожидание и клик по кнопке "Личный кабинет"
        personal_account_button = wait.until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        personal_account_button.click()

        # Ожидание перехода на страницу логина
        wait.until(EC.url_contains("/login"))

        # Ввод email в поле ввода
        email_field = wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))
        email_field.send_keys(UserData.USER_EMAIL)

        # Ввод пароля в поле ввода
        password_field = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_field.send_keys(UserData.USER_PASSWORD)

        # Нажатие кнопки "Войти"
        login_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

        # Ожидание перехода на главную страницу после входа
        wait.until(EC.url_to_be(f"{UserData.BASE_URL}/"))

        # Переход в личный кабинет для проверки авторизации
        personal_account_button = wait.until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        personal_account_button.click()

        # Проверка что попали в личный кабинет
        wait.until(EC.url_contains("/account/profile"))
        assert "/account/profile" in driver.current_url

    def test_login_via_main_login_button(self, driver):
        """Вход через кнопку 'Войти в аккаунт' на главной странице"""
        # Инициализация ожидания
        wait = WebDriverWait(driver, 10)

        # Открытие главной страницы
        driver.get(UserData.BASE_URL)

        # Ожидание и клик по кнопке "Войти в аккаунт"
        login_button = wait.until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)
        )
        login_button.click()

        # Ожидание перехода на страницу логина
        wait.until(EC.url_contains("/login"))

        # Ввод email в поле ввода
        email_field = wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))
        email_field.send_keys(UserData.USER_EMAIL)

        # Ввод пароля в поле ввода
        password_field = wait.until(EC.visibility_of_element_located(LoginPageLocators.PASSWORD_INPUT))
        password_field.send_keys(UserData.USER_PASSWORD)

        # Нажатие кнопки "Войти"
        login_button = wait.until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON))
        login_button.click()

        # Ожидание редиректа после логина
        wait.until(lambda driver: "/login" not in driver.current_url)

        # Проверка успешного входа по наличию кнопки "Личный кабинет"
        personal_account_button = wait.until(
            EC.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        assert personal_account_button.is_displayed()

        # Дополнительная проверка - переход в личный кабинет
        personal_account_button.click()
        wait.until(EC.url_contains("/account"))
        assert "/account" in driver.current_url

    def test_login_with_invalid_email(self, driver):
        """Вход с неверным email"""
        # Инициализация ожидания
        wait = WebDriverWait(driver, 15)

        # Открытие страницы логина
        driver.get(f"{UserData.BASE_URL}/login")

        # Ввод неверного email
        email_field = wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))
        email_field.send_keys("invalid@email.com")

        # Ввод пароля
        password_field = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_field.send_keys(UserData.USER_PASSWORD)

        # Нажатие кнопки "Войти"
        login_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

        # Проверка что остались на странице логина
        assert "/login" in driver.current_url

    def test_login_with_invalid_password(self, driver):
        """Вход с неверным паролем"""
        # Инициализация ожидания
        wait = WebDriverWait(driver, 15)

        # Открытие страницы логина
        driver.get(f"{UserData.BASE_URL}/login")

        # Ввод email
        email_field = wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))
        email_field.send_keys(UserData.USER_EMAIL)

        # Ввод неверного пароля
        password_field = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_field.send_keys("wrongpassword")

        # Нажатие кнопки "Войти"
        login_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

        # Проверка что остались на странице логина
        assert "/login" in driver.current_url

    def test_login_with_empty_credentials(self, driver):
        """Вход с пустыми полями"""
        # Инициализация ожидания
        wait = WebDriverWait(driver, 15)

        # Открытие страницы логина
        driver.get(f"{UserData.BASE_URL}/login")

        # Нажатие кнопки "Войти" без заполнения полей
        login_button = wait.until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON))
        login_button.click()

        # Проверка что остались на странице логина
        assert "/login" in driver.current_url