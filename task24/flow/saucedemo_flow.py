# Interaction with saucedemo website features
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from flow.constants import *


def login(browser, wait):
    browser.get(BASE_URL)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#user-name"))).send_keys(USERNAME)
    browser.find_element(By.CSS_SELECTOR, "#password").send_keys(PASSWORD)
    browser.find_element(By.CSS_SELECTOR, "#login-button").click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#inventory_container")))


def add_item_to_cart(browser, wait):
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, BACKPACK_SELECTOR))).click()
    cart_badge = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                              ".shopping_cart_badge")))
    assert cart_badge.text == "1"


def view_cart(browser, wait):
    browser.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart_list")))
    item_name = browser.find_element(By.CSS_SELECTOR,
                                     "#item_4_title_link .inventory_item_name").text
    assert item_name == BACKPACK_NAME


def initiate_checkout(browser, wait):
    browser.find_element(By.CSS_SELECTOR, "#checkout").click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#first-name")))
    browser.find_element(By.CSS_SELECTOR, "#first-name").send_keys(FIRST_NAME)
    browser.find_element(By.CSS_SELECTOR, "#last-name").send_keys(LAST_NAME)
    browser.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(POSTAL_CODE)
    browser.find_element(By.CSS_SELECTOR, "#continue").click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#checkout_summary_container")))


def verify_checkout(browser, wait):
    item_name = browser.find_element(By.CSS_SELECTOR,
                                     "#item_4_title_link .inventory_item_name").text
    assert item_name == BACKPACK_NAME
    browser.find_element(By.CSS_SELECTOR, "#finish").click()
    complete_text = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".complete-header"))
    ).text
    assert complete_text == "Thank you for your order!"


def complete_order(browser, wait):
    browser.find_element(By.CSS_SELECTOR, "#back-to-products").click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#inventory_container")))
