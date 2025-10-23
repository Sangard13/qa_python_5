from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_page_locators import LoginPageLocators
from utils.data_generator import DataGenerator


class AuthHelper:
    """Вспомогательный класс для работы с авторизацией"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.base_url = DataGenerator.get_base_url()
        self.user_data = DataGenerator.get_user_data()

    def login(self):
        """Выполняет авторизацию пользователя"""
        self.driver.get(f"{self.base_url}/login")

        email_input = self.wait.until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        password_input = self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        login_button = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)

        email_input.send_keys(self.user_data["email"])
        password_input.send_keys(self.user_data["password"])
        login_button.click()

        # Ждем перехода на главную страницу
        self.wait.until(EC.url_to_be(f"{self.base_url}/"))