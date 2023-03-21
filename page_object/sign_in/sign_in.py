from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class SignIn:
    def __init__(self, driver):
        self.driver = driver
        self.get_email_field = '//input[@type="email"]'
        self.get_password_field = '//input[@type="password"]'
        self.get_signin_button = '//button[@type="submit"]'

    def input_email_field(self):
        wait = WebDriverWait(self.driver, 2)
        email_field = wait.until(EC.visibility_of_element_located((By.XPATH, self.get_email_field)))
        return email_field

    def input_password_field(self):
        wait = WebDriverWait(self.driver, 2)
        password_field = wait.until(EC.visibility_of_element_located((By.XPATH, self.get_password_field)))
        return password_field

    def signin_button(self):
        wait = WebDriverWait(self.driver, 2)
        signin_button = wait.until(EC.visibility_of_element_located((By.XPATH, self.get_signin_button)))
        return signin_button

    def login(self, email, password):
        self.input_email_field().send_keys(email)
        self.input_password_field().send_keys(password)
        self.signin_button().click()
