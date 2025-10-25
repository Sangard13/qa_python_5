from .base_page import BasePage
from locators.personal_account_locators import PersonalAccountLocators

class PersonalAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://stellarburgers.education-services.ru/account/profile"

    def open_profile(self):
        self.driver.get(self.url)

    def is_profile_section_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located(PersonalAccountLocators.PROFILE_SECTION))
            return True
        except:
            return False

    def is_order_history_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located(PersonalAccountLocators.ORDER_HISTORY))
            return True
        except:
            return False

    def is_logout_button_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located(PersonalAccountLocators.LOGOUT_BUTTON))
            return True
        except:
            return False

    def is_constructor_button_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located(PersonalAccountLocators.CONSTRUCTOR_BUTTON))
            return True
        except:
            return False

    def is_logo_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located(PersonalAccountLocators.LOGO))
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