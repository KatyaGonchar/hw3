# Checkout Your Information Page functionality
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from test_data.constants import FIRST_NAME, LAST_NAME, POSTAL_CODE
from pages.base_page import BasePage


class CheckoutYourInformationPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def initiate_checkout(self):
        first_name_input = self.wait.until(EC.visibility_of_element_located((
            By.CSS_SELECTOR, "#first-name")))
        first_name_input.send_keys(FIRST_NAME)
        self.browser.find_element(By.CSS_SELECTOR, "#last-name").send_keys(LAST_NAME)
        self.browser.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(POSTAL_CODE)

    def continue_to_overview(self):
        self.browser.find_element(By.CSS_SELECTOR, "#continue").click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart_list")))
