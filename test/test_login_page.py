from selenium import webdriver
from page_object.sign_in.sign_in import SignIn
import json
import time

driver = webdriver.Chrome()
driver.maximize_window()
base_url = 'https://react-redux.realworld.io/'
driver.get(base_url + '#/login?_k=p42wmk')

sign_in = SignIn(driver)
with open("../fixtures/sign_in_data/sign_in_data.json", "r") as f:
    test_data = json.load(f)


def test_signin_page():
    email = test_data["email"]
    password = test_data["password"]
    # sign_in.input_email_field().send_keys("email")
    # sign_in.input_password_field().send_keys("password")
    sign_in.login(email, password)
    time.sleep(10)

