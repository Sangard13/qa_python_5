import pytest
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestRegistration:

    # Локаторы
    NAME_INPUT = (By.XPATH, "//label[contains(text(), 'Имя')]/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")
    PASSWORD_ERROR = (By.XPATH, "//p[contains(@class, 'input__error')]")
    LOGIN_HEADER = (By.XPATH, "//h2[contains(text(), 'Вход')]")

    # Тестовые данные
    USER_NAME = "Александр"
    USER_PASSWORD = "1Qasw234RTy"

    def test_successful_registration(self, driver):
        """Успешная регистрация с валидными данными"""
        wait = WebDriverWait(driver, 10)

        # Открываем страницу регистрации
        driver.get("https://stellarburgers.education-services.ru/register")

        # Генерируем уникальный email
        unique_email = f"test_{random.randint(100000, 999999)}@yandex.ru"

        # Заполняем форму
        wait.until(EC.visibility_of_element_located(self.NAME_INPUT)).send_keys(self.USER_NAME)
        driver.find_element(*self.EMAIL_INPUT).send_keys(unique_email)
        driver.find_element(*self.PASSWORD_INPUT).send_keys(self.USER_PASSWORD)
        driver.find_element(*self.REGISTER_BUTTON).click()

        # Проверяем редирект на страницу логина
        wait.until(EC.url_contains("/login"))
        assert "/login" in driver.current_url
        print("Успешная регистрация: редирект на логин")

    def test_registration_minimum_password(self, driver):
        """Регистрация с паролем минимальной длины (6 символов)"""
        wait = WebDriverWait(driver, 10)

        driver.get("https://stellarburgers.education-services.ru/register")
        unique_email = f"test_{random.randint(100000, 999999)}@yandex.ru"

        # Заполняем форму с паролем из 6 символов
        wait.until(EC.visibility_of_element_located(self.NAME_INPUT)).send_keys(self.USER_NAME)
        driver.find_element(*self.EMAIL_INPUT).send_keys(unique_email)
        driver.find_element(*self.PASSWORD_INPUT).send_keys("123456")  # Минимальная длина
        driver.find_element(*self.REGISTER_BUTTON).click()

        # Проверяем успешную регистрацию
        wait.until(EC.url_contains("/login"))
        assert "/login" in driver.current_url
        print("Регистрация с минимальным паролем успешна")

    def test_registration_short_password_error(self, driver):
        """Ошибка при регистрации с коротким паролем (<6 символов)"""
        wait = WebDriverWait(driver, 10)

        driver.get("https://stellarburgers.education-services.ru/register")
        unique_email = f"test_{random.randint(100000, 999999)}@yandex.ru"

        # Заполняем форму с коротким паролем
        wait.until(EC.visibility_of_element_located(self.NAME_INPUT)).send_keys(self.USER_NAME)
        driver.find_element(*self.EMAIL_INPUT).send_keys(unique_email)
        driver.find_element(*self.PASSWORD_INPUT).send_keys("12345")  # 5 символов
        driver.find_element(*self.REGISTER_BUTTON).click()

        # Проверяем сообщение об ошибке
        error_message = wait.until(EC.visibility_of_element_located(self.PASSWORD_ERROR))
        assert error_message.is_displayed()
        assert "Некорректный пароль" in error_message.text
        print("Ошибка для короткого пароля отображается")

    def test_registration_empty_name(self, driver):
        """Проверка обязательности поля 'Имя'"""
        wait = WebDriverWait(driver, 10)

        driver.get("https://stellarburgers.education-services.ru/register")
        unique_email = f"test_{random.randint(100000, 999999)}@yandex.ru"

        # Заполняем форму без имени
        driver.find_element(*self.EMAIL_INPUT).send_keys(unique_email)
        driver.find_element(*self.PASSWORD_INPUT).send_keys(self.USER_PASSWORD)
        driver.find_element(*self.REGISTER_BUTTON).click()

        # Проверяем что остались на странице регистрации
        assert "/register" in driver.current_url
        print("Регистрация без имени заблокирована")

    def test_registration_invalid_email(self, driver):
        """Проверка валидации email"""
        wait = WebDriverWait(driver, 10)

        driver.get("https://stellarburgers.education-services.ru/register")

        # Заполняем форму с некорректным email
        wait.until(EC.visibility_of_element_located(self.NAME_INPUT)).send_keys(self.USER_NAME)
        driver.find_element(*self.EMAIL_INPUT).send_keys("invalid-email")  # Неправильный формат
        driver.find_element(*self.PASSWORD_INPUT).send_keys(self.USER_PASSWORD)
        driver.find_element(*self.REGISTER_BUTTON).click()

        # Проверяем что остались на странице регистрации
        assert "/register" in driver.current_url
        print("Регистрация с некорректным email заблокирована")