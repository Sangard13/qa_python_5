import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators
from utils.data_generator import DataGenerator


class TestConstructorSauces:

    def test_constructor_sauces_section_displayed(self, driver):
        """Тест что раздел соусов отображается"""
        # Инициализация ожидания и получение базового URL
        wait = WebDriverWait(driver, 10)
        base_url = DataGenerator.get_base_url()

        # Открытие главной страницы
        driver.get(base_url)

        # Проверка что раздел соусов отображается
        sauces_section = wait.until(
            EC.visibility_of_element_located(MainPageLocators.SAUCES_SECTION)
        )
        assert sauces_section.is_displayed()

    def test_sauces_section_is_clickable(self, driver):
        """Тест что раздел соусов кликабелен"""
        # Инициализация ожидания и получение базового URL
        wait = WebDriverWait(driver, 10)
        base_url = DataGenerator.get_base_url()

        # Открытие главной страницы
        driver.get(base_url)

        # Проверка что раздел соусов кликабелен
        sauces_section = wait.until(
            EC.element_to_be_clickable(MainPageLocators.SAUCES_SECTION)
        )
        assert sauces_section.is_enabled()

    def test_sauces_section_has_correct_text(self, driver):
        """Тест что раздел соусов имеет правильный текст"""
        # Инициализация ожидания и получение базового URL
        wait = WebDriverWait(driver, 10)
        base_url = DataGenerator.get_base_url()

        # Открытие главной страницы
        driver.get(base_url)

        # Проверка что раздел соусов имеет правильный текст
        sauces_section = wait.until(
            EC.visibility_of_element_located(MainPageLocators.SAUCES_SECTION)
        )
        assert "Соусы" in sauces_section.text

    def test_switch_to_sauces_section(self, driver):
        """Тест переключения на раздел соусов"""
        # Инициализация ожидания и получение базового URL
        wait = WebDriverWait(driver, 10)
        base_url = DataGenerator.get_base_url()

        # Открытие главной страницы
        driver.get(base_url)

        # Клик на раздел соусов
        sauces_section = wait.until(
            EC.element_to_be_clickable(MainPageLocators.SAUCES_SECTION)
        )
        sauces_section.click()

        # Проверка что раздел соусов стал активным
        active_section = wait.until(
            EC.visibility_of_element_located(MainPageLocators.ACTIVE_SECTION)
        )
        assert "Соусы" in active_section.text

    def test_sauces_section_after_switching_from_buns(self, driver):
        """Тест раздела соусов после переключения из раздела булок"""
        # Инициализация ожидания и получение базового URL
        wait = WebDriverWait(driver, 10)
        base_url = DataGenerator.get_base_url()

        # Открытие главной страницы (булки активны по умолчанию)
        driver.get(base_url)

        # Переключение на раздел соусов
        sauces_section = wait.until(
            EC.element_to_be_clickable(MainPageLocators.SAUCES_SECTION)
        )
        sauces_section.click()

        # Проверка что раздел соусов активен
        active_section = wait.until(
            EC.visibility_of_element_located(MainPageLocators.ACTIVE_SECTION)
        )
        assert "Соусы" in active_section.text

        # Проверка что раздел булок больше не активен
        buns_section = wait.until(
            EC.visibility_of_element_located(MainPageLocators.BUNS_SECTION)
        )
        # Проверяем что у булок нет класса активного раздела
        assert "tab_tab_type_current" not in buns_section.get_attribute("class")