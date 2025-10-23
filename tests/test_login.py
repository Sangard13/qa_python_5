import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from data.user_data import UserData
from locators.main_page_locators import MainPageLocators
from locators.login_page_locators import LoginPageLocators


class TestLogin:

    def test_login_via_personal_account_button(self, driver):
        """Вход через кнопку 'Личный кабинет' на главной странице"""
        wait = WebDriverWait(driver, 15)
        driver.get("https://stellarburgers.education-services.ru")

        personal_account_button = wait.until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        personal_account_button.click()

        wait.until(EC.url_contains("/login"))

        email_field = wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))
        email_field.send_keys(UserData.USER_EMAIL)

        password_field = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_field.send_keys(UserData.USER_PASSWORD)

        login_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

        wait.until(EC.url_contains("/account"))
        assert "/account" in driver.current_url

    def test_login_via_main_login_button(self, driver):
        """Вход через кнопку 'Войти в аккаунт' на главной странице"""
        wait = WebDriverWait(driver, 15)

        driver.get("https://stellarburgers.education-services.ru/")

        login_button = wait.until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)
        )
        login_button.click()

        wait.until(EC.url_contains("/login"))

        email_field = wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))
        email_field.send_keys(UserData.USER_EMAIL)

        password_field = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_field.send_keys(UserData.USER_PASSWORD)

        login_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

        wait.until(EC.url_contains("/account"))
        assert "/account" in driver.current_url

    def test_login_with_invalid_email(self, driver):
        """Вход с неверным email"""
        wait = WebDriverWait(driver, 15)

        driver.get("https://stellarburgers.education-services.ru/login")

        email_field = wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))
        email_field.send_keys("invalid@email.com")

        password_field = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_field.send_keys(UserData.USER_PASSWORD)

        login_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

        assert "/login" in driver.current_url

    def test_login_with_invalid_password(self, driver):
        """Вход с неверным паролем"""
        wait = WebDriverWait(driver, 15)

        driver.get("https://stellarburgers.education-services.ru/login")

        email_field = wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))
        email_field.send_keys(UserData.USER_EMAIL)

        password_field = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_field.send_keys("wrongpassword")

        login_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

        assert "/login" in driver.current_url

    def test_login_with_empty_credentials(self, driver):
        """Вход с пустыми полями"""
        wait = WebDriverWait(driver, 15)

        driver.get("https://stellarburgers.education-services.ru/login")

        login_button = wait.until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON))
        login_button.click()

        assert "/login" in driver.current_url