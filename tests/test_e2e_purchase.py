from pages.login import LoginPage
from pages.shopping import ShopPage
from pages.checkout import CheckoutPage

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

    #Shop actions
    shop_page = ShopPage(driver)
    shop_page.add_all_products_to_cart()
    shop_page.go_to_cart()

    #Checkout
    checkout_page =CheckoutPage(driver)
    checkout_page.checkout()
    checkout_page.enter_information("Barbara", "Cordova", "12345")
    checkout_page.continue_checkout()
    checkout_page.finish_checkout()

    success_text = checkout_page.success_message()
    assert "thank you for your order" in success_text.lower()

