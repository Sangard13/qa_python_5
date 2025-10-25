import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from data.user_data import UserData


class TestPersonalAccount:
    def test_navigate_to_personal_account_from_main_page(self, driver):
        """Тест перехода в личный кабинет с главной страницы"""
        wait = WebDriverWait(driver, 10)

        # Открытие страницы логина
        driver.get(f"{UserData.BASE_URL}/login")

        # Ввод email
        email_field = wait.until(EC.visibility_of_element_located((By.NAME, "name")))
        email_field.send_keys(UserData.USER_EMAIL)

        # Ввод пароля
        password_field = driver.find_element(By.NAME, "Пароль")
        password_field.send_keys(UserData.USER_PASSWORD)

        # Нажатие кнопки входа
        login_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
        login_button.click()

        # Ожидание главной страницы
        wait.until(EC.url_to_be(f"{UserData.BASE_URL}/"))

        # Нажатие кнопки личного кабинета
        personal_account_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//p[text()='Личный Кабинет']"))
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
        email_field = wait.until(EC.visibility_of_element_located((By.NAME, "name")))
        email_field.send_keys(UserData.USER_EMAIL)
        password_field = driver.find_element(By.NAME, "Пароль")
        password_field.send_keys(UserData.USER_PASSWORD)
        login_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
        login_button.click()

        # Переходим в личный кабинет
        wait.until(EC.url_to_be(f"{UserData.BASE_URL}/"))
        personal_account_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//p[text()='Личный Кабинет']"))
        )
        personal_account_button.click()

        # Выходим из аккаунта
        wait.until(EC.url_contains("/account/profile"))
        logout_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Выход']"))
        )
        logout_button.click()

        # Проверка перехода на страницу логина
        wait.until(EC.url_contains("/login"))
        assert "/login" in driver.current_url

    def test_personal_account_requires_authentication(self, driver):
        """Тест что личный кабинет требует авторизации"""
        wait = WebDriverWait(driver, 10)

        # Пытаемся открыть личный кабинет без авторизации
        driver.get(f"{UserData.BASE_URL}/account/profile")

        # Проверка редиректа на страницу логина
        wait.until(EC.url_contains("/login"))
        assert "/login" in driver.current_url