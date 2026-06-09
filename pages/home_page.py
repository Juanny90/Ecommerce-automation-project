from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):

    PRODUCT = (By.CSS_SELECTOR, ".fixed_wrapper .prdocutname")

    def select_first_product(self):
        products = self.find_all(self.PRODUCT)

        print("DEBUG - productos encontrados:", len(products))

        if len(products) == 0:
            raise Exception("No se encontraron productos - revisar locator o carga de página")

        products[0].click()

    def select_second_product(self):
        products = self.find_all(self.PRODUCT)
        products[1].click()