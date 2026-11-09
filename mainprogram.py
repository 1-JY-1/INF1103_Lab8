from filehandling import FileHandling

from inventory import Inventory
from product import Product, physicalProduct, digitalProduct
from supplier import Supplier

from order import Order
# from orderline import OrderLine




Supplier1 = Supplier("S001", "Supplier 1", "Supplier1@supplier1.com")
Supplier2 = Supplier("S002", "Supplier 2", "Supplier2@supplier2.com")
Supplier3 = Supplier("S003", "Supplier 3", "Supplier3@supplier3.com")


physicalProduct1 = physicalProduct("P001", "physical", "Phone", 1000, 10, 1.5, supplier=Supplier1)
digitalProduct1 = digitalProduct("P002", "digital", "Software", 1000, 10, 5000, supplier=Supplier2)
delsupplierproduct = physicalProduct("P003", "physical", "iPhone", 1000, 10, 1.5, supplier=Supplier3)

print("\n====== Print deleted Supplier3 from delsupplierproduct ======")
del Supplier3
delsupplierproduct.display_supplier()
print("============================================================")


inventory1 = Inventory()
inventory2 = Inventory()

inventory1.add_product(physicalProduct1)
inventory1.add_product(digitalProduct1)
inventory1.remove_product("P001")

print("\n========= Print deleted product from inventory1 ============")
physicalProduct1.display_information() # after removing the product it still can show its info, so it is aggregate 
print("============================================================")


for product in inventory1.products:
    product.display_information()
    product.get_fulfilment_info()





print("\n============= Print product inside inventory1 ==============")
inventory1.display_all_products()
print("============================================================")

inventory2.add_product(physicalProduct1)

for product in inventory2.products:
    product.display_information()
    product.get_fulfilment_info()

print("\n============= Print product inside inventory2 ==============")
inventory2.display_all_products()
print("============================================================")

order = Order("Order_001")
order.add_order_line(physicalProduct1, 2)
order.add_order_line(digitalProduct1, 2)

print("============================================================")
order.calculate_total()
print("============================================================")
