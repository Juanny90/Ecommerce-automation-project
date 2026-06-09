from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):

    ROWS = (By.CSS_SELECTOR, ".cart-info tbody tr")
    QUANTITY_INPUTS = (By.CSS_SELECTOR, ".cart-info tbody tr input[type='text']")
    REMOVE_BUTTONS = (By.CSS_SELECTOR, ".remove")
    CHECKOUT = (By.ID, "cart_checkout2")

    def open_cart(self):
        self.driver.get("https://automationteststore.com/index.php?rt=checkout/cart")

    def get_line_items_count(self):
        rows = self.driver.find_elements(By.CSS_SELECTOR, ".cart-info tbody tr")

        real_items = 0

        for row in rows:
            has_qty = len(row.find_elements(By.CSS_SELECTOR, "input[type='text']")) > 0
            has_text = row.text.strip() != ""

            if has_qty and has_text:
                real_items += 1

        return real_items

    def get_total_quantity(self):
        inputs = self.driver.find_elements(By.CSS_SELECTOR, ".cart-info tbody tr input[type='text']")

        total = 0

        for i in inputs:
            value = i.get_attribute("value")

            if value and value.strip().isdigit():
                total += int(value)

        return total

    def get_quantity(self, index):
        inputs = self.find_all(self.QUANTITY_INPUTS)
        return int(inputs[index].get_attribute("value"))

    def update_quantity(self, index, qty):
        inputs = self.find_all(self.QUANTITY_INPUTS)

        if index >= len(inputs):
            raise IndexError("Producto no existe en carrito")

        field = inputs[index]
        field.clear()
        field.send_keys(str(qty))

    def remove_item(self, index):
        buttons = self.find_all(self.REMOVE_BUTTONS)

        if index >= len(buttons):
            raise IndexError("Producto no existe para eliminar")

        buttons[index].click()

    def checkout(self):
        self.click(self.CHECKOUT)