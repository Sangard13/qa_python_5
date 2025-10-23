from selenium.webdriver.common.by import By

class RegistrationLocators:
    NAME_INPUT = (By.XPATH, "//label[contains(text(), 'Имя')]/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")
    PASSWORD_ERROR = (By.XPATH, "//p[contains(@class, 'input__error')]")
    LOGIN_HEADER = (By.XPATH, "//h2[contains(text(), 'Вход')]")