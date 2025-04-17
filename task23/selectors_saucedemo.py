# Login page:
# 1. Enter username
# selector: #user-name
# 2. Enter password
# selector: #password
# 3. Press "Login" button
# selector: #login-button
# 4. Verify that "Products" page is opened.
# selector: #inventory_container
#
# Products page
# 1. Verify that "Products" page is opened.
# selector: #inventory_container
# 2. Add item to the cart. Press Add to Cart button
# (example: Sauce Labs Backpack)
# selector: #add-to-cart-sauce-labs-backpack
# 3. Verify that the cart is updated. Cart icon shows "1"
# selector: .shopping_cart_badge
# 4. Go to the cart
# selector: .shopping_cart_link
# 5. Verify that "Your Cart" page is opened
# selector: .cart_list
#
# Your Cart page
# 1. Verify that "Your Cart" page is opened
# selector: .cart_list
# 2. Verify the correct item is listed in the cart
# selector: #item_4_title_link .inventory_item_name
# (text should be "Sauce Labs Backpack")
# 3. Click "Checkout" button
# selector: #checkout
# 4. Verify that "Checkout: Your Information" page is opened
# selector: #first-name
#
# Checkout: Your Information page
# 1. Verify that "Checkout: Your Information" page is opened
# selector: #first-name
# 2. Enter First Name
# selector: #first-name
# 3. Enter Last Name
# selector: #last-name
# 4. Enter Zip/Postal Code
# selector: #postal-code
# 5. Click "Continue" button
# selector: #continue
# 6. Verify that "Checkout: Overview page" page is opened
# selector: #checkout_summary_container
#
# Checkout: Overview page
# 1. Verify that "Checkout: Overview page" page is opened
# selector: #checkout_summary_container
# 2. Verify the correct item is listed on the checkout
# selector: #item_4_title_link .inventory_item_name
# (text should be "Sauce Labs Backpack")
# 3. Click "Finish" button
# selector: #finish
# 4. Verify that "Checkout: Complete!" page is opened
# selector: .complete-header
# (text should be "Thank you for your order!")
#
# Checkout: Complete! page
# 1. Verify that "Checkout: Complete!" page is opened
# selector: .checkout_complete_container .complete-header
# (text should be "Thank you for your order!")
# 2. Click "Back Home" button
# selector: #back-to-products
# 3. Verify that "Products" page is opened.
# selector: #inventory_container
