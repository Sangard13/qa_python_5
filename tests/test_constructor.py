import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from locators.personal_account_locators import PersonalAccountLocators

# Данные пользователя для тестов
USER_NAME = "Aleksandr"
USER_EMAIL = "Alex.Br_33@gmail.com"
USER_PASSWORD = "1Qasw234RTy"
BASE_URL = "https://stellarburgers.education-services.ru"


class TestNavigationFromAccount:

    def login_user(self, driver, wait):
        """Вспомогательный метод для логина"""
        print("Выполняю вход пользователя...")
        driver.get(f"{BASE_URL}/login")

        email_input = wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))
        password_input = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        login_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)

        email_input.send_keys(USER_EMAIL)
        password_input.send_keys(USER_PASSWORD)
        login_button.click()

        # Ждем перехода на главную страницу
        wait.until(EC.url_to_be(f"{BASE_URL}/"))
        print("Пользователь успешно авторизован")

    def test_navigate_to_constructor_via_constructor_button(self, driver):
        """Тест перехода из личного кабинета в конструктор по кнопке 'Конструктор'"""
        wait = WebDriverWait(driver, 10)

        # Логинимся
        self.login_user(driver, wait)

        # Переходим в личный кабинет
        print("Переходим в личный кабинет...")
        personal_account_button = wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON))
        personal_account_button.click()

        # Ждем загрузки личного кабинета
        wait.until(EC.url_contains("/account/profile"))
        print("Личный кабинет загружен")

        # Нажимаем кнопку "Конструктор"
        print("Нажимаем кнопку 'Конструктор'...")
        constructor_button = wait.until(EC.element_to_be_clickable(PersonalAccountLocators.CONSTRUCTOR_BUTTON))
        constructor_button.click()

        # Ждем перехода на главную страницу
        wait.until(EC.url_to_be(f"{BASE_URL}/"))
        print("Успешно перешли на главную страницу")

        # Проверяем что мы на главной странице (конструктор)
        order_button = wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
        assert order_button.is_displayed()
        print("Кнопка 'Оформить заказ' отображается - мы в конструкторе")

        # Дополнительная проверка - наличие разделов конструктора
        buns_section = wait.until(EC.visibility_of_element_located(MainPageLocators.BUNS_SECTION))
        sauces_section = driver.find_element(*MainPageLocators.SAUCES_SECTION)
        fillings_section = driver.find_element(*MainPageLocators.FILLINGS_SECTION)

        assert buns_section.is_displayed()
        assert sauces_section.is_displayed()
        assert fillings_section.is_displayed()
        print("Все разделы конструктора отображаются")

    def test_navigate_to_constructor_via_logo(self, driver):
        """Тест перехода из личного кабинета в конструктор по логотипу"""
        wait = WebDriverWait(driver, 10)

        # Логинимся
        self.login_user(driver, wait)

        # Переходим в личный кабинет
        print("Переходим в личный кабинет...")
        personal_account_button = wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON))
        personal_account_button.click()

        # Ждем загрузки личного кабинета
        wait.until(EC.url_contains("/account/profile"))
        print("Личный кабинет загружен")

        # Нажимаем на логотип Stellar Burgers
        print("Нажимаем на логотип Stellar Burgers...")
        logo = wait.until(EC.element_to_be_clickable(PersonalAccountLocators.LOGO))
        logo.click()

        # Ждем перехода на главную страницу
        wait.until(EC.url_to_be(f"{BASE_URL}/"))
        print("Успешно перешли на главную страницу по логотипу")

        # Проверяем что мы на главной странице (конструктор)
        order_button = wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
        assert order_button.is_displayed()
        print("Кнопка 'Оформить заказ' отображается - мы в конструкторе")

        # Проверяем URL
        current_url = driver.current_url
        assert current_url == f"{BASE_URL}/", f"Ожидали URL: {BASE_URL}/, получили: {current_url}"
        print(f"URL корректный: {current_url}")

