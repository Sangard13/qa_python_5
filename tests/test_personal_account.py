import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

USER_NAME = "Aleksandr"
USER_EMAIL = "Alex.Br_33@gmail.com"
USER_PASSWORD = "1Qasw234RTy"
BASE_URL = "https://stellarburgers.education-services.ru"


class TestPersonalAccountNavigation:

    def login_user(self, driver, wait):
        """Вспомогательный метод для логина пользователя"""
        print("Выполняю вход пользователя...")

        # Открываем страницу логина
        driver.get(f"{BASE_URL}/login")

        # Заполняем форму логина
        email_input = wait.until(EC.visibility_of_element_located((By.NAME, "name")))
        password_input = driver.find_element(By.NAME, "Пароль")
        login_button = driver.find_element(By.XPATH, "//button[text()='Войти']")

        email_input.send_keys(USER_EMAIL)
        password_input.send_keys(USER_PASSWORD)
        login_button.click()

        # Ждем перехода на главную страницу
        wait.until(EC.url_to_be(f"{BASE_URL}/"))
        print("Пользователь успешно авторизован")

    def test_navigate_to_personal_account(self, driver):
        """Тест перехода в личный кабинет по клику на 'Личный кабинет'"""
        wait = WebDriverWait(driver, 15)

        # Логинимся
        self.login_user(driver, wait)

        # Переходим на главную страницу (если еще не там)
        driver.get(f"{BASE_URL}/")

        # Кликаем на кнопку "Личный кабинет"
        print("Кликаю на кнопку 'Личный кабинет'...")
        personal_account_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//p[text()='Личный Кабинет']"))
        )
        personal_account_button.click()

        # Проверяем что перешли в личный кабинет
        print("Проверяем переход в личный кабинет...")

        # Ждем загрузки страницы личного кабинета
        wait.until(EC.url_contains(f"{BASE_URL}/account/profile"))

        # Проверяем что отображается профиль пользователя
        profile_section = wait.until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Профиль"))
        )
        assert profile_section.is_displayed(), "Раздел 'Профиль' не отображается"

        # Проверяем URL
        current_url = driver.current_url
        assert f"{BASE_URL}/account/profile" in current_url, f"Неправильный URL: {current_url}"

        print("Успешный переход в личный кабинет")

    def test_personal_account_elements_visible(self, driver):
        """Тест что все элементы личного кабинета отображаются"""
        wait = WebDriverWait(driver, 15)

        # Логинимся и переходим в личный кабинет
        self.login_user(driver, wait)
        driver.get(f"{BASE_URL}/account/profile")

        # Проверяем основные элементы личного кабинета
        print("Проверяем элементы личного кабинета...")

        # Профиль
        profile_element = wait.until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Профиль"))
        )
        assert profile_element.is_displayed(), "Элемент 'Профиль' не отображается"
        print("Элемент 'Профиль' отображается")

        # История заказов (если есть такой элемент)
        try:
            order_history = wait.until(
                EC.visibility_of_element_located((By.LINK_TEXT, "История заказов"))
            )
            assert order_history.is_displayed()
            print("Элемент 'История заказов' отображается")
        except:
            print("ℹЭлемент 'История заказов' не найден")

        # Выход
        logout_button = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//button[text()='Выход']"))
        )
        assert logout_button.is_displayed(), "Кнопка 'Выход' не отображается"
        print("Кнопка 'Выход' отображается")

        # Конструктор
        constructor_button = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//p[text()='Конструктор']"))
        )
        assert constructor_button.is_displayed(), "Кнопка 'Конструктор' не отображается"
        print("Кнопка 'Конструктор' отображается")

        # Логотип
        logo = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]"))
        )
        assert logo.is_displayed(), "Логотип не отображается"
        print("Логотип отображается")

    def test_personal_account_requires_authentication(self, driver):
        """Тест что личный кабинет требует авторизации"""
        wait = WebDriverWait(driver, 10)

        # Пытаемся открыть личный кабинет без авторизации
        print("Пытаемся открыть личный кабинет без авторизации...")
        driver.get(f"{BASE_URL}/account/profile")

        # Должен произойти редирект на страницу логина
        wait.until(EC.url_contains(f"{BASE_URL}/login"))

        current_url = driver.current_url
        assert f"{BASE_URL}/login" in current_url, f"Не произошел редирект на логин. Текущий URL: {current_url}"

        # Проверяем что отображается форма логина
        login_header = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']"))
        )
        assert login_header.is_displayed(), "Форма логина не отображается"

        print("Личный кабинет требует авторизации - редирект на логин выполнен")