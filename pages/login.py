from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    USERNAME_INPUT = (By.ID, 'user-name' )
    PASSWORD_INPUT = (By.ID, 'password' )
    BUTTON_LOGIN =  (By.CSS_SELECTOR, 'input[data-test="login-button"]')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

#Methods

    def enter_username(self, username):
        element = self.wait.until(EC.visibility_of_element_located((self.USERNAME_INPUT)))
        element.send_keys(username)

    def enter_password(self, password):
        element =self.wait.until(EC.visibility_of_element_located((self.PASSWORD_INPUT)))
        element.send_keys(password)

    def click_login(self):
        element = self.wait.until(EC.element_to_be_clickable((self.BUTTON_LOGIN)))
        element.click()
