from selenium.webdriver.common.by import By


class AccountLocators:
    """Локаторы для личного кабинета"""
    PROFILE_SECTION = (By.LINK_TEXT, "Профиль")
    ORDER_HISTORY_SECTION = (By.LINK_TEXT, "История заказов")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")
    LOGIN_HEADER = (By.XPATH, "//h2[text()='Вход']")