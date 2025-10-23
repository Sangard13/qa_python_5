from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.user_data import UserData
from locators.login_locators import LoginLocators


class AccountHelper:
    """Вспомогательный класс для операций с аккаунтом"""

    @staticmethod
    def login_user(driver, wait):
        """Метод для логина пользователя"""
        # Открываем страницу логина
        driver.get(f"{UserData.BASE_URL}/login")

        # Заполняем форму логина
        email_input = wait.until(EC.visibility_of_element_located(LoginLocators.EMAIL_FIELD))
        password_input = wait.until(EC.visibility_of_element_located(LoginLocators.PASSWORD_FIELD))
        login_button = wait.until(EC.element_to_be_clickable(LoginLocators.LOGIN_BUTTON))

        email_input.send_keys(UserData.USER_EMAIL)
        password_input.send_keys(UserData.USER_PASSWORD)
        login_button.click()

        # Ждем перехода на главную страницу
        wait.until(EC.url_to_be(f"{UserData.BASE_URL}/"))