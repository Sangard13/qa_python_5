import pytest
import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Добавляем пути для импорта
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)
sys.path.insert(0, os.path.join(project_root, 'pages'))
sys.path.insert(0, os.path.join(project_root, 'locators'))
sys.path.insert(0, os.path.join(project_root, 'data'))


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=chrome_options
    )

    driver.maximize_window()
    yield driver
    driver.quit()

    @pytest.fixture
    def driver():
        """Фикстура для инициализации и закрытия браузера"""
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1920,1080")

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

        yield driver
        driver.quit()

    @pytest.fixture
    def wait(driver):
        """Фикстура для WebDriverWait"""
        return WebDriverWait(driver, 15)

    @pytest.fixture
    def authenticated_user(driver, wait):
        """Фикстура для аутентифицированного пользователя"""
        from helpers.account_helper import AccountHelper
        AccountHelper.login_user(driver, wait)
        yield



