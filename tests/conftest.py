import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pytest_html.extras as extras

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get('browserInstance', None)
        if driver:
            try:
                reports_dir = r"C:\Users\Anais\PycharmProjects\ecommerce-automation\reports"
                screenshot_file = os.path.join(reports_dir, f"{item.name}.png")
                driver.save_screenshot(screenshot_file)
                print(f"📸 Screenshot saved: {screenshot_file}")

                if not hasattr(report, "extra"):
                    report.extra = []

                report.extra.append(extras.image(f"{item.name}.png"))

            except Exception as e:
                print(f"❌ Error capturing screenshot: {e}")

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
