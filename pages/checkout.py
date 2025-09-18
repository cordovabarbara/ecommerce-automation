from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, '[data-test="checkout"]')
    INPUT_FIRST_NAME = (By.ID, "first-name")
    INPUT_LAST_NAME = (By.ID, "last-name")
    INPUT_ZIP_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, '[data-test="continue"]')
    FINISH_BUTTON = (By.CSS_SELECTOR, '[data-test="finish"]')
    SUCCESS_MSG = (By.ID, 'checkout_complete_container')


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    #Methods
    def checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON)).click()

    def enter_information(self,first_name,last_name,zip_code):
        self.driver.find_element(*self.INPUT_FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.INPUT_LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.INPUT_ZIP_CODE).send_keys(zip_code)

    def continue_checkout(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def finish_checkout(self):
        self.driver.find_element(*self.FINISH_BUTTON).click()

    def success_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MSG)).text