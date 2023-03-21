from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.get_your_feed = 'a.nav-link.active'

    def get_your_feed_tab(self):
        wait = WebDriverWait(self.driver, 2)
        your_feed = wait.until(EC.visibility_of_element_located((By.XPATH, self.get_your_feed)))
        return your_feed
