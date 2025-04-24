# Checkout Complete page functionality
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def complete_order(self):
        complete_text = self.browser.find_element(By.CSS_SELECTOR, ".complete-header").text
        assert complete_text == "Thank you for your order!"

    def back_to_products(self):
        self.browser.find_element(By.CSS_SELECTOR, "#back-to-products").click()
        self.wait.until(EC.visibility_of_element_located((
            By.CSS_SELECTOR, "#inventory_container")))
