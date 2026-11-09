
import product
from supplier import Supplier

class Inventory:

    def __init__(self):

        self.products: list[product.Product] = []


    def add_product(self, product: product.Product) -> None:

        self.products.append(product)


    def remove_product(self, product_id: str) -> bool:

        for product in self.products:

            if product.id == product_id:

                self.products.remove(product)
                return True
            
        return False


    def find_product(self, product_id: str) -> product.Product | None:

        for product in self.products:

            if product.product_id == product_id:
                return product
            
        return None

    def display_all_products(self) -> None:

        for product in self.products:
            product.display_information()





