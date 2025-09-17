import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Browser to run tests"
    )

# Fixture initiate browser
@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        chrome_options = Options()
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-save-password-bubble")
        chrome_options.add_argument("--disable-features=PasswordManager,AutofillSaveCard")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--log-level=3")

        driver = webdriver.Chrome(service=Service(), options=chrome_options)

    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    driver.maximize_window()
    driver.implicitly_wait(5)


    yield driver
    driver.quit()
