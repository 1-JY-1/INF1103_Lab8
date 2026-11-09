from abc import ABC, abstractmethod

from canbeshipped import CanBeShipped
from supplier import Supplier

class Product(ABC):
    def __init__(self, id:str, name:str, price:float, stock:int, supplier: Supplier):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
        self.supplier: Supplier = supplier

    @abstractmethod
    def get_fulfilment_info(self):
        pass

    def display_information(self):

        print(f"ID: {self.id}")
        print(f"Product: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Stock: {self.stock}")

    def updatestock(self):
        try:
            new_stock = int(input("Enter the new stock quantity: "))
            if new_stock < 0:
                print("Invalid input. Please enter a positive number for stock.")
                return
            
            elif new_stock > 500:
                print("Inventory cannot exceed 500 items. Please enter a smaller amount.")
                return
            
            self.stock = new_stock
            print("\nStock updated successfully.")
            print(f"Stock for product ID {self.id} updated to {new_stock}.\n")
            return
        
        except ValueError:
            print("Invalid input. Please enter a valid stock quantity.")
            return




        pass


class physicalProduct(Product, CanBeShipped):
    def __init__(self, id:str, type:str, name:str, price:float, stock:int, weight:float, supplier: Supplier):
        super().__init__(id, name, price, stock, supplier)
        self.weight = weight
        self.type = type

    def calculate_shipping_cost(self):
        shipping_cost = self.weight * 5
        return shipping_cost

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.weight:.2f} kg")
        print(f"Shipping Cost: ${self.calculate_shipping_cost():.2f}")

    def get_fulfilment_info(self):
        print("This product requires delivered physically.")

    def display_supplier(self) -> None:
        self.supplier.display_information()


class digitalProduct(Product):
    def __init__(self, id:str, type:str, name:str, price:float, stock:int, download_size:int, supplier: Supplier):
        super().__init__(id, name, price, stock, supplier)
        self.download_size = download_size
        self.type = type

    def display_information(self):
        super().display_information()
        print(f"Download Size: {self.download_size} MB")

    def get_fulfilment_info(self):
        print("This product is delivered digitally.") 