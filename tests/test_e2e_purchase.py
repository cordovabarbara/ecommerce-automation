import pytest
from pages.login import LoginPage

def test_login(browserInstance):
    driver = browserInstance
    driver.get("https://www.saucedemo.com/")

    # login
    login_page = LoginPage(driver)

    # Use methods
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # Verification
    assert "inventory" in driver.current_url