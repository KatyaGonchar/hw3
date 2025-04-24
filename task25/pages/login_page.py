# Login page functionality
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from test_data.constants import URL, USERNAME, PASSWORD
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def login(self):
        self.open(URL)
        self.browser.find_element(By.CSS_SELECTOR, "#user-name").send_keys(USERNAME)
        self.browser.find_element(By.CSS_SELECTOR, "#password").send_keys(PASSWORD)

    def go_to_products(self):
        self.browser.find_element(By.CSS_SELECTOR, "#login-button").click()
        self.wait.until(EC.visibility_of_element_located((
            By.CSS_SELECTOR, "#inventory_container")))
