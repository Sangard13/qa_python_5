import pytest
import sys
import os

# ДОБАВЛЯЕМ ПУТИ ДЛЯ ИМПОРТА ПЕРЕД ВСЕМИ ИМПОРТАМИ
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)
sys.path.insert(0, os.path.join(project_root, 'pages'))
sys.path.insert(0, os.path.join(project_root, 'locators'))
sys.path.insert(0, os.path.join(project_root, 'utils'))

print(f"Добавлены пути: {sys.path}")

try:
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.service import Service as ChromeService

    WEBDRIVER_MANAGER_AVAILABLE = True
except ImportError:
    WEBDRIVER_MANAGER_AVAILABLE = False
    print("webdriver_manager не установлен")

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Теперь импортируем наши модули
try:
    from pages.main_page import MainPage
    from pages.login_page import LoginPage
    from pages.registration_page import RegistrationPage
    from pages.personal_account_page import PersonalAccountPage
    from utils.data_generator import DataGenerator

    print("Все модули успешно импортированы")
except ImportError as e:
    print(f"Ошибка импорта: {e}")


@pytest.fixture
def driver():
    """Фикстура для создания драйвера Chrome"""
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    if WEBDRIVER_MANAGER_AVAILABLE:
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=chrome_options
        )
    else:
        driver = webdriver.Chrome(options=chrome_options)

    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    return MainPage(driver)


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def registration_page(driver):
    return RegistrationPage(driver)


@pytest.fixture
def personal_account_page(driver):
    return PersonalAccountPage(driver)


@pytest.fixture
def user_data():
    return {
        "name": "Aleksandr",
        "email": "Alex.Br_33@gmail.com",
        "password": "1Qasw234RTy"
    }