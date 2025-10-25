from selenium.webdriver.common.by import By


class PersonalAccountLocators:
    # Элементы личного кабинета
    PROFILE_LINK = (By.XPATH, "//a[contains(text(), 'Профиль')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")

    # URL
    ACCOUNT_URL = "https://stellarburgers.education-services.ru/account"

    # Навигация
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  # Кнопка перехода в конструктор
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")  # Логотип Stellar Burgers

    # Профиль
    PROFILE_BUTTON = (By.LINK_TEXT, "Профиль")  # Кнопка профиля
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Кнопка выхода
    PROFILE_SECTION = (By.XPATH, "//a[contains(@href, '/account/profile')]")

    # Дополнительные локаторы для личного кабинета
    ORDER_HISTORY = (By.LINK_TEXT, "История заказов")  # История заказов
    USER_NAME = (By.XPATH, "//input[@name='Name']")  # Поле имени пользователя
    USER_EMAIL = (By.XPATH, "//input[@name='name']")  # Поле email пользователя

    # История заказов
    ORDER_HISTORY = (By.LINK_TEXT, "История заказов")  # История заказов
