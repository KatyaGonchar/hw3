#
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--incognito")

    browser = webdriver.Chrome(options=options)
    try:
        yield browser
    finally:
        browser.quit()
