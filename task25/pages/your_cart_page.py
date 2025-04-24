# Your Cart Page functionality
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from test_data.constants import BACKPACK_NAME
from pages.base_page import BasePage


class YourCartPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def view_cart(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart_list")))
        item_name = self.browser.find_element(
            By.CSS_SELECTOR, "#item_4_title_link .inventory_item_name").text
        assert item_name == BACKPACK_NAME

    def go_to_checkout(self):
        self.browser.find_element(By.CSS_SELECTOR, "#checkout").click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#first-name")))
