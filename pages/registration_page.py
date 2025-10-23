from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://stellarburgers.education-services.ru/register")

    def register_user(self, name, email, password):
        from locators.registration_locators import RegistrationLocators
        self.wait.until(EC.visibility_of_element_located(RegistrationLocators.NAME_INPUT)).send_keys(name)
        self.driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*RegistrationLocators.REGISTER_BUTTON).click()

    def wait_for_url_contains(self, text, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.url_contains(text))

    def get_current_url(self):
        return self.driver.current_url

    def is_password_error_visible(self):
        from locators.registration_locators import RegistrationLocators
        try:
            self.wait.until(EC.visibility_of_element_located(RegistrationLocators.PASSWORD_ERROR))
            return True
        except:
            return False

    def get_password_error_text(self):
        from locators.registration_locators import RegistrationLocators
        element = self.wait.until(EC.visibility_of_element_located(RegistrationLocators.PASSWORD_ERROR))
        return element.text

    def register_user_without_name(self, email, password):
        from locators.registration_locators import RegistrationLocators
        self.driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*RegistrationLocators.REGISTER_BUTTON).click()

    def fill_field(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def click_element(self, locator):
        self.driver.find_element(*locator).click()