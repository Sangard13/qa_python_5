import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators
from utils.data_generator import DataGenerator
from helpers.auth_helper import AuthHelper


class TestConstructor:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Фикстура для настройки перед каждым тестом"""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.base_url = DataGenerator.get_base_url()
        self.auth_helper = AuthHelper(driver)

    @pytest.fixture
    def authenticated_user(self):
        """Фикстура для авторизованного пользователя на главной странице"""
        self.auth_helper.login()
        self.driver.get(f"{self.base_url}/")

    @pytest.mark.parametrize("section,expected_text", [
        ("buns", "Булки"),
        ("sauces", "Соусы"),
        ("fillings", "Начинки")
    ])
    def test_constructor_section_switch(self, authenticated_user, section, expected_text):
        """Тест переключения между разделами конструктора"""
        # Кликаем на нужный раздел
        if section == "buns":
            section_element = self.wait.until(
                EC.element_to_be_clickable(MainPageLocators.BUNS_SECTION)
            )
        elif section == "sauces":
            section_element = self.wait.until(
                EC.element_to_be_clickable(MainPageLocators.SAUCES_SECTION)
            )
        elif section == "fillings":
            section_element = self.wait.until(
                EC.element_to_be_clickable(MainPageLocators.FILLINGS_SECTION)
            )

        section_element.click()

        # Проверяем что раздел активен
        active_section = self.wait.until(
            EC.visibility_of_element_located(MainPageLocators.ACTIVE_SECTION)
        )
        assert expected_text in active_section.text

    def test_constructor_buns_section_displayed(self, authenticated_user):
        """Тест что раздел 'Булки' отображается"""
        buns_section = self.wait.until(
            EC.visibility_of_element_located(MainPageLocators.BUNS_SECTION)
        )
        assert buns_section.is_displayed()

    def test_constructor_sauces_section_displayed(self, authenticated_user):
        """Тест что раздел 'Соусы' отображается"""
        sauces_section = self.wait.until(
            EC.visibility_of_element_located(MainPageLocators.SAUCES_SECTION)
        )
        assert sauces_section.is_displayed()

    def test_constructor_fillings_section_displayed(self, authenticated_user):
        """Тест что раздел 'Начинки' отображается"""
        fillings_section = self.wait.until(
            EC.visibility_of_element_located(MainPageLocators.FILLINGS_SECTION)
        )
        assert fillings_section.is_displayed()

    def test_constructor_default_active_section(self, authenticated_user):
        """Тест что по умолчанию активен раздел 'Булки'"""
        active_section = self.wait.until(
            EC.visibility_of_element_located(MainPageLocators.ACTIVE_SECTION)
        )
        assert "Булки" in active_section.text