import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators
from utils.data_generator import DataGenerator


class TestConstructorBuns:

    def test_constructor_buns_section_displayed(self, driver):
        """Test that buns section is displayed and active"""
        wait = WebDriverWait(driver, 10)
        base_url = DataGenerator.get_base_url()

        driver.get(base_url)

        # Проверяем что раздел булок активен по умолчанию
        active_section = wait.until(
            EC.visibility_of_element_located(MainPageLocators.ACTIVE_SECTION)
        )
        assert "Булки" in active_section.text

    def test_buns_section_is_clickable(self, driver):
        """Test that buns section is clickable"""
        wait = WebDriverWait(driver, 10)
        base_url = DataGenerator.get_base_url()

        driver.get(base_url)

        # Проверяем что раздел булок кликабелен
        buns_section = wait.until(
            EC.element_to_be_clickable(MainPageLocators.BUNS_SECTION)
        )
        assert buns_section.is_displayed()

    def test_buns_section_has_correct_text(self, driver):
        """Test that buns section has correct text"""
        wait = WebDriverWait(driver, 10)
        base_url = DataGenerator.get_base_url()

        driver.get(base_url)

        # Проверяем что раздел булок имеет правильный текст
        buns_section = wait.until(
            EC.visibility_of_element_located(MainPageLocators.BUNS_SECTION)
        )
        assert "Булки" in buns_section.text