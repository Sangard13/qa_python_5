from selenium.webdriver.common.by import By


class LoginPageLocators:
    # Поля формы логина
    EMAIL_INPUT = (By.NAME, "name")
    PASSWORD_INPUT = (By.NAME, "Пароль")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

    # Ссылки
    REGISTER_LINK = (By.XPATH, "//a[contains(text(), 'Зарегистрироваться')]")
    RECOVER_PASSWORD_LINK = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")

    # URL
    LOGIN_URL = "https://stellarburgers.education-services.ru/login"

    #Кнопки
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка входа
    REGISTER_LINK = (By.LINK_TEXT, "Зарегистрироваться")  # Ссылка на регистрацию
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Восстановить пароль")  # Ссылка восстановления пароля

    # Заголовок
    LOGIN_HEADER = (By.XPATH, "//h2[text()='Вход']")  # Заголовок страницы входа

    # Поля формы
    EMAIL_INPUT = (By.NAME, "name")  # Поле ввода email
    PASSWORD_INPUT = (By.NAME, "Пароль")  # Поле ввода пароля