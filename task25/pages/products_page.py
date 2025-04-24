# Products page functionality
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ProductsPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def add_item_to_cart(self):
        self.browser.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        cart_badge = self.wait.until(EC.visibility_of_element_located((
            By.CSS_SELECTOR, ".shopping_cart_badge")))
        assert cart_badge.text == "1"

    def go_to_cart(self):
        self.browser.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart_list")))
