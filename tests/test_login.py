import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class TestLoginDebug:
    USER_EMAIL = "Alex.Br_33@gmail.com"
    USER_PASSWORD = "1Qasw234RTy"

    def test_debug_personal_account(self, driver):
        """Отладочная версия теста"""
        wait = WebDriverWait(driver, 15)

        print("Начало отладочного теста")

        # 1. Открываем главную страницу
        driver.get("https://stellarburgers.education-services.ru/")
        print(f"Открыта страница: {driver.current_url}")
        time.sleep(3)

        # 2. Пробуем найти кнопку "Личный кабинет" разными способами
        selectors = [
            "//p[text()='Личный Кабинет']",
            "//p[contains(text(), 'Личный')]",
            "//a[contains(@href, 'account')]",
            "//*[contains(text(), 'Личный кабинет')]",
            "//*[contains(text(), 'Личный Кабинет')]"
        ]

        button_found = False
        for selector in selectors:
            try:
                button = driver.find_element(By.XPATH, selector)
                print(f"Найдена кнопка с селектором: {selector}")
                print(f"   Текст кнопки: {button.text}")
                button.click()
                print("🖱Кнопка нажата")
                button_found = True
                break
            except:
                print(f"Не найдено с селектором: {selector}")
                continue

        if not button_found:
            print("Не удалось найти кнопку 'Личный кабинет'")
            driver.save_screenshot("button_not_found.png")
            return

        time.sleep(3)
        print(f"Текущий URL после клика: {driver.current_url}")

        # 3. Если нас перенаправило на логин - логинимся
        if "/login" in driver.current_url:
            print("Пытаемся войти в систему")

            # Вводим email
            try:
                email_field = driver.find_element(By.NAME, "name")
                email_field.send_keys(self.USER_EMAIL)
                print("Email введен")
            except:
                print("Не удалось ввести email")
                driver.save_screenshot("email_error.png")
                return

            # Вводим пароль
            try:
                password_field = driver.find_element(By.NAME, "Пароль")
                password_field.send_keys(self.USER_PASSWORD)
                print("Пароль введен")
            except:
                print("Не удалось ввести пароль")
                driver.save_screenshot("password_error.png")
                return

            # Нажимаем кнопку входа
            try:
                login_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
                login_button.click()
                print("🖱Кнопка входа нажата")
            except:
                print("Не удалось нажать кнопку входа")
                driver.save_screenshot("login_button_error.png")
                return

            time.sleep(5)
            print(f"Текущий URL после логина: {driver.current_url}")

            # Проверяем результат
            if "/account" in driver.current_url:
                print("УСПЕХ: Вошли в личный кабинет!")
            else:
                print(f"НЕ УДАЛОСЬ ВОЙТИ. Текущий URL: {driver.current_url}")
                driver.save_screenshot("login_failed.png")
        else:
            print(f"Неожиданное поведение. URL: {driver.current_url}")
            driver.save_screenshot("unexpected_behavior.png")