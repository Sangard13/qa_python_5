from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.registration_locators import RegistrationLocators
from data.urls import REGISTER_URL


class RegistrationPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(REGISTER_URL)

    def register_user(self, name, email, password):
        self.wait.until(EC.visibility_of_element_located(RegistrationLocators.NAME_INPUT)).send_keys(name)
        self.driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*RegistrationLocators.REGISTER_BUTTON).click()

    def is_password_error_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located(RegistrationLocators.PASSWORD_ERROR))
            return True
        except:
            return False

    def get_password_error_text(self):
        element = self.wait.until(EC.visibility_of_element_located(RegistrationLocators.PASSWORD_ERROR))
        return element.text