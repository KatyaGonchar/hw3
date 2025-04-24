from selenium.webdriver.support.ui import WebDriverWait
from test_data.constants import TIMEOUT


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, TIMEOUT)

    def open(self, url):
        self.browser.get(url)

    def find_element(self, by, value):
        return self.browser.find_element(by, value)

    def find_elements(self, by, value):
        return self.browser.find_elements(by, value)
