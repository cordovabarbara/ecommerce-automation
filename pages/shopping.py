from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShopPage:
    CART_BUTTON = (By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
    SHOP_INVENTORY = (By.CSS_SELECTOR, '[data-test="inventory-item"]')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    @property
    def products(self):
        return self.driver.find_elements(*self.SHOP_INVENTORY)


    def add_all_products_to_cart(self):
        for product in self.products:
            title = product.find_element(By.CSS_SELECTOR, '[data-test="inventory-item-name"]').text
            price = product.find_element(By.CSS_SELECTOR, '[data-test="inventory-item-price"]').text
            button = product.find_element(By.CSS_SELECTOR, 'button')
            print(f" Added: {title} - {price}")
            button.click()

    def go_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.CART_BUTTON)).click()

