# Checkout Overview Page functionality
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from test_data.constants import BACKPACK_NAME
from pages.base_page import BasePage


class CheckoutOverviewPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def verify_checkout(self):
        item_name = self.browser.find_element(
            By.CSS_SELECTOR, "#item_4_title_link .inventory_item_name").text
        assert item_name == BACKPACK_NAME

    def finish_order(self):
        self.browser.find_element(By.CSS_SELECTOR, "#finish").click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".complete-header")))
