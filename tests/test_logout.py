import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

USER_EMAIL = "Alex.Br_33@gmail.com"
USER_PASSWORD = "1Qasw234RTy"
BASE_URL = "https://stellarburgers.education-services.ru"


class TestLogout:

    def test_logout_from_personal_account(self, driver):
        """Тест выхода из аккаунта через личный кабинет"""
        wait = WebDriverWait(driver, 10)

        # Логинимся
        driver.get(f"{BASE_URL}/login")
        email_input = wait.until(EC.visibility_of_element_located((By.NAME, "name")))
        email_input.send_keys(USER_EMAIL)

        password_input = driver.find_element(By.NAME, "Пароль")
        password_input.send_keys(USER_PASSWORD)

        login_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
        login_button.click()

        # Ждем главную страницу
        wait.until(EC.url_to_be(f"{BASE_URL}/"))

        # Переходим в личный кабинет
        personal_account_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Личный Кабинет']")))
        personal_account_button.click()

        # Ждем загрузки личного кабинета
        wait.until(EC.url_contains("/account/profile"))

        # Выходим из аккаунта
        logout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Выход']")))
        logout_button.click()

        # Проверяем переход на страницу логина
        wait.until(EC.url_to_be(f"{BASE_URL}/login"))

        # Проверяем что мы на странице логина
        login_header = wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))
        assert login_header.is_displayed()

        print("Выход из аккаунта выполнен успешно!")