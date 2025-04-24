# End-to-end item purchase test flow
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.your_cart_page import YourCartPage
from pages.checkout_your_information_page import CheckoutYourInformationPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage


def test_checkout_flow(browser):
    login_page = LoginPage(browser)
    login_page.login()
    login_page.go_to_products()

    products_page = ProductsPage(browser)
    products_page.add_item_to_cart()
    products_page.go_to_cart()

    cart_page = YourCartPage(browser)
    cart_page.view_cart()
    cart_page.go_to_checkout()

    checkout_info_page = CheckoutYourInformationPage(browser)
    checkout_info_page.initiate_checkout()
    checkout_info_page.continue_to_overview()

    overview_page = CheckoutOverviewPage(browser)
    overview_page.verify_checkout()
    overview_page.finish_order()

    complete_page = CheckoutCompletePage(browser)
    complete_page.complete_order()
    complete_page.back_to_products()
