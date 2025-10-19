import sys
print("Python path:", sys.executable)
print("Python version:", sys.version)

try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    print("✅ SUCCESS: Selenium imports work!")
    print("By.NAME =", By.NAME)
except ImportError as e:
    print("❌ ERROR:", e)