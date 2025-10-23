import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.account_helper import AccountHelper
from data.user_data import UserData
from locators.account_locators import AccountLocators
from locators.main_page_locators import MainPageLocators


class TestPersonalAccountNavigation:
    @pytest.fixture
    def wait(self, driver):
        return WebDriverWait(driver, 15)

    def test_navigate_to_personal_account(self, driver, wait):
        """Тест перехода в личный кабинет по клику на 'Личный кабинет'"""
        # Логинимся
        AccountHelper.login_user(driver, wait)

        # Переходим на главную страницу
        driver.get(UserData.BASE_URL)

        # Кликаем на кнопку "Личный кабинет"
        personal_account_button = wait.until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        personal_account_button.click()

        # Проверяем что перешли в личный кабинет
        wait.until(EC.url_contains(f"{UserData.BASE_URL}/account/profile"))

        # Проверяем что отображается профиль пользователя
        profile_section = wait.until(
            EC.visibility_of_element_located(AccountLocators.PROFILE_SECTION)
        )
        assert profile_section.is_displayed(), "Раздел 'Профиль' не отображается"

        # Проверяем URL
        current_url = driver.current_url
        assert f"{UserData.BASE_URL}/account/profile" in current_url, f"Неправильный URL: {current_url}"

    def test_personal_account_elements_visible(self, driver, wait):
        """Тест что все элементы личного кабинета отображаются"""
        # Логинимся и переходим в личный кабинет
        AccountHelper.login_user(driver, wait)
        driver.get(f"{UserData.BASE_URL}/account/profile")

        # Проверяем основные элементы личного кабинета
        profile_element = wait.until(
            EC.visibility_of_element_located(AccountLocators.PROFILE_SECTION)
        )
        assert profile_element.is_displayed(), "Элемент 'Профиль' не отображается"

        order_history = wait.until(
            EC.visibility_of_element_located(AccountLocators.ORDER_HISTORY_SECTION)
        )
        assert order_history.is_displayed(), "Элемент 'История заказов' не отображается"

        logout_button = wait.until(
            EC.visibility_of_element_located(AccountLocators.LOGOUT_BUTTON)
        )
        assert logout_button.is_displayed(), "Кнопка 'Выход' не отображается"

        constructor_button = wait.until(
            EC.visibility_of_element_located(AccountLocators.CONSTRUCTOR_BUTTON)
        )
        assert constructor_button.is_displayed(), "Кнопка 'Конструктор' не отображается"

        logo = wait.until(
            EC.visibility_of_element_located(AccountLocators.LOGO)
        )
        assert logo.is_displayed(), "Логотип не отображается"

    def test_personal_account_requires_authentication(self, driver, wait):
        """Тест что личный кабинет требует авторизации"""
        # Пытаемся открыть личный кабинет без авторизации
        driver.get(f"{UserData.BASE_URL}/account/profile")

        # Должен произойти редирект на страницу логина
        wait.until(EC.url_contains(f"{UserData.BASE_URL}/login"))

        current_url = driver.current_url
        assert f"{UserData.BASE_URL}/login" in current_url, f"Не произошел редирект на логин. Текущий URL: {current_url}"

        # Проверяем что отображается форма логина
        login_header = wait.until(
            EC.visibility_of_element_located(AccountLocators.LOGIN_HEADER)
        )
        assert login_header.is_displayed(), "Форма логина не отображается"