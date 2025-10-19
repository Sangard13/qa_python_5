from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопки на главной странице
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")

    # URL
    BASE_URL = "https://stellarburgers.education-services.ru"

    # Кнопки авторизации
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт" на главной
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")  # Кнопка "Личный кабинет"

    # Разделы конструктора
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']/parent::div")  # Раздел "Булки"
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']/parent::div")  # Раздел "Соусы"
    FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']/parent::div")  # Раздел "Начинки"

    # Активный раздел
    ACTIVE_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")  # Активный раздел конструктора

    # Логотип
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")  # Логотип Stellar Burgers

    # Конструктор
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  # Кнопка "Конструктор"

    # Индикатор авторизации
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")  # Кнопка "Оформить заказ" (видна после авторизации)