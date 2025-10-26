import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators
from utils.data_generator import DataGenerator


class TestConstructorFillings:

    def test_constructor_fillings_section_displayed(self, driver):
        """Тест что раздел начинок отображается"""
        # Инициализация ожидания и получение базового URL
        wait = WebDriverWait(driver, 10)
        base_url = DataGenerator.get_base_url()

        # Открытие главной страницы
        driver.get(base_url)

        # Проверка что раздел начинок отображается
        fillings_section = wait.until(
            EC.visibility_of_element_located(MainPageLocators.FILLINGS_SECTION)
        )
        assert fillings_section.is_displayed()

    def test_fillings_section_is_clickable(self, driver):
        """Тест что раздел начинок кликабелен"""
        wait = WebDriverWait(driver, 10)
        base_url = DataGenerator.get_base_url()

        # Открытие главной страницы
        driver.get(base_url)

        # Проверка что раздел начинок кликабелен
        fillings_section = wait.until(
            EC.element_to_be_clickable(MainPageLocators.FILLINGS_SECTION)
        )
        assert fillings_section.is_enabled()

    def test_fillings_section_has_correct_text(self, driver):
        """Тест что раздел начинок имеет правильный текст"""
        # Инициализация ожидания и получение базового URL
        wait = WebDriverWait(driver, 10)
        base_url = DataGenerator.get_base_url()

        # Открытие главной страницы
        driver.get(base_url)

        # Проверка что раздел начинок имеет правильный текст
        fillings_section = wait.until(
            EC.visibility_of_element_located(MainPageLocators.FILLINGS_SECTION)
        )
        assert "Начинки" in fillings_section.text

    def test_switch_to_fillings_section(self, driver):
        """Тест переключения на раздел начинок"""
        # Инициализация ожидания и получение базового URL
        wait = WebDriverWait(driver, 10)
        base_url = DataGenerator.get_base_url()

        # Открытие главной страницы
        driver.get(base_url)

        # Клик на раздел начинок
        fillings_section = wait.until(
            EC.element_to_be_clickable(MainPageLocators.FILLINGS_SECTION)
        )
        fillings_section.click()

        # Проверка что раздел начинок стал активным
        active_section = wait.until(
            EC.visibility_of_element_located(MainPageLocators.ACTIVE_SECTION)
        )
        assert "Начинки" in active_section.text

    def test_fillings_section_after_switching_from_buns(self, driver):
        """Тест раздела начинок после переключения из раздела булок"""
        # Инициализация ожидания и получение базового URL
        wait = WebDriverWait(driver, 10)
        base_url = DataGenerator.get_base_url()

        # Открытие главной страницы (булки активны по умолчанию)
        driver.get(base_url)

        # Переключение на раздел начинок
        fillings_section = wait.until(
            EC.element_to_be_clickable(MainPageLocators.FILLINGS_SECTION)
        )
        fillings_section.click()

        # Проверка что раздел начинок активен
        active_section = wait.until(
            EC.visibility_of_element_located(MainPageLocators.ACTIVE_SECTION)
        )
        assert "Начинки" in active_section.text

        # Проверка что раздел булок больше не активен
        buns_section = wait.until(
            EC.visibility_of_element_located(MainPageLocators.BUNS_SECTION)
        )
        # Проверяем что у булок нет класса активного раздела
        assert "tab_tab_type_current" not in buns_section.get_attribute("class")
