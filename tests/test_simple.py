import sys


def test_check_packages():
    print(f"Python: {sys.executable}")

    try:
        import selenium
        print("Selenium работает!")
        assert True
    except ImportError as e:
        print(f"❌ Ошибка: {e}")
        assert False


def test_check_pytest():
    try:
        import pytest
        print("Pytest работает!")
        assert True
    except ImportError as e:
        print(f"Ошибка: {e}")
        assert False


if __name__ == "__main__":
    test_check_packages()
    test_check_pytest()