import sys

print("=== ПРОВЕРКА ПАКЕТОВ ===")
print(f"Python путь: {sys.executable}")
print(f"Версия Python: {sys.version}")

try:
    import pytest
    print("pytest установлен")
except ImportError:
    print("pytest НЕ установлен")

try:
    from selenium import webdriver
    print("selenium установлен")
except ImportError:
    print("selenium НЕ установлен")

try:
    from selenium.webdriver.support.ui import WebDriverWait
    print("WebDriverWait доступен")
except ImportError:
    print("WebDriverWait НЕ доступен")

try:
    from selenium.webdriver.support import expected_conditions as EC
    print("expected_conditions доступен")
except ImportError:
    print("expected_conditions НЕ доступен")

print("=== ПРОВЕРКА ЗАВЕРШЕНА ===")