from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

def test_cart_flow(driver):
    home = HomePage(driver)
    product = ProductPage(driver)
    cart = CartPage(driver)

    home.select_first_product()
    product.set_quantity(3)
    product.add_to_cart()

    driver.get("https://automationteststore.com/")

    home.select_second_product()
    product.add_to_cart()

    cart.open_cart()

    line_items = cart.get_line_items_count()
    total_qty = cart.get_total_quantity()

    print("Line items:", line_items)
    print("Total quantity:", total_qty)

    assert line_items == 2
    assert total_qty >= 2

    cart.update_quantity(0, 2)

    if line_items > 1:
        cart.remove_item(1)

    cart.checkout()