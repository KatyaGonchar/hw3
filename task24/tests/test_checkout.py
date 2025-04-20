# End-to-end item purchase test flow
from selenium.webdriver.support.ui import WebDriverWait
from flow.constants import TIMEOUT
from flow.saucedemo_flow import (
    login, add_item_to_cart, view_cart,
    initiate_checkout, verify_checkout, complete_order
    )


def test_checkout_flow(browser):
    wait = WebDriverWait(browser, TIMEOUT)

    login(browser, wait)
    add_item_to_cart(browser, wait)
    view_cart(browser, wait)
    initiate_checkout(browser, wait)
    verify_checkout(browser, wait)
    complete_order(browser, wait)
