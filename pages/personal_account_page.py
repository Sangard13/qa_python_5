from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from locators.personal_account_locators import PersonalAccountLocators
from data.urls import PROFILE_URL


class PersonalAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = PROFILE_URL

    def open_profile(self):
        self.driver.get(self.url)

    def is_element_visible(self, locator, timeout=5):
        """Метод проверки видимости элемента"""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def click_constructor(self):
        constructor_button = self.wait.until(
            EC.element_to_be_clickable(PersonalAccountLocators.CONSTRUCTOR_BUTTON)
        )
        constructor_button.click()

    def click_logout(self):
        logout_button = self.wait.until(
            EC.element_to_be_clickable(PersonalAccountLocators.LOGOUT_BUTTON)
        )
        logout_button.click()