from .base_page import BasePage
from locators.login_page_locators import LoginPageLocators

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://stellarburgers.education-services.ru/login"

    def login(self, email, password):
        email_field = self.wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))
        email_field.send_keys(email)

        password_field = self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_field.send_keys(password)

        login_button = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

    def is_login_form_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))
            return True
        except:
            return False