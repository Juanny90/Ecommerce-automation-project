from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):

    ADD_TO_CART = (By.CSS_SELECTOR, ".cart")
    QUANTITY_INPUT = (By.ID, "product_quantity")

    def set_quantity(self, qty):
        field = self.find(self.QUANTITY_INPUT)
        field.clear()
        field.send_keys(qty)

    def add_to_cart(self):
        self.click(self.ADD_TO_CART)