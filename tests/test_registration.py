import pytest
import random
from pages.registration_page import RegistrationPage
from data.registration_data import RegistrationData
from locators.registration_locators import RegistrationLocators


class TestRegistration:

    def test_successful_registration(self, driver):
        """Тест успешной регистрации с валидными данными"""
        registration_page = RegistrationPage(driver)
        unique_email = f"test_{random.randint(100000, 999999)}@yandex.ru"

        registration_page.open()
        registration_page.register_user(
            RegistrationData.USER_NAME,
            unique_email,
            RegistrationData.USER_PASSWORD
        )

        registration_page.wait_for_url_contains("/login")
        assert "/login" in registration_page.get_current_url()

    def test_registration_minimum_password(self, driver):
        """Тест регистрации с паролем минимальной длины"""
        registration_page = RegistrationPage(driver)
        unique_email = f"test_{random.randint(100000, 999999)}@yandex.ru"

        registration_page.open()
        registration_page.register_user(
            RegistrationData.USER_NAME,
            unique_email,
            "123456"
        )

        registration_page.wait_for_url_contains("/login")
        assert "/login" in registration_page.get_current_url()

    def test_registration_short_password_error(self, driver):
        """Тест ошибки при коротком пароле"""
        registration_page = RegistrationPage(driver)
        unique_email = f"test_{random.randint(100000, 999999)}@yandex.ru"

        registration_page.open()
        registration_page.register_user(
            RegistrationData.USER_NAME,
            unique_email,
            "12345"
        )

        assert registration_page.is_password_error_visible()
        assert "Некорректный пароль" in registration_page.get_password_error_text()

    def test_registration_empty_name(self, driver):
        """Тест регистрации с пустым именем"""
        registration_page = RegistrationPage(driver)
        unique_email = f"test_{random.randint(100000, 999999)}@yandex.ru"

        registration_page.open()
        registration_page.driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(unique_email)
        registration_page.driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(
            RegistrationData.USER_PASSWORD)
        registration_page.driver.find_element(*RegistrationLocators.REGISTER_BUTTON).click()

        assert "/register" in registration_page.get_current_url()

    def test_registration_invalid_email(self, driver):
        """Тест регистрации с невалидным email"""
        registration_page = RegistrationPage(driver)

        registration_page.open()
        registration_page.register_user(
            RegistrationData.USER_NAME,
            "invalid-email",
            RegistrationData.USER_PASSWORD
        )

        assert "/register" in registration_page.get_current_url()