from inventory import Inventory
from product import Product, physicalProduct, digitalProduct
from supplier import Supplier

from order import Order
import json


inventory = Inventory()

supplier_list = []
productdetail = {"products": [],"suppliers": []}

try:
    with open("inventory.json", "r") as file:
        productdetail = json.load(file)

except FileNotFoundError:
    productdetail = {"products": [],"suppliers": []}

    with open("inventory.json", "w") as file:
        json.dump(productdetail, file, indent=4)


for supplier_data in productdetail["suppliers"]: # file_handling.productdetail["suppliers"]:
    supplier = Supplier(
        supplier_id=supplier_data["SID"],
        name=supplier_data["name"],
        contact_email=supplier_data["email"]
    )
    supplier_list.append(supplier)

for product_data in productdetail["products"]: # file_handling.productdetail["products"]:
    product_obj = None

    if "weight" in product_data:
        for supplier in supplier_list:
            if supplier.supplier_id == product_data["SID"]:
                product_obj = physicalProduct(
                    id=product_data["ID"],
                    type=product_data["type"],
                    name=product_data["name"],
                    price=product_data["price"],
                    stock=product_data["stock"],
                    weight=product_data["weight"],
                    supplier=supplier
                )
    elif "download_size" in product_data:
        for supplier in supplier_list:
            if supplier.supplier_id == product_data["SID"]:
                product_obj = digitalProduct(
                    id=product_data["ID"],
                    type=product_data["type"],
                    name=product_data["name"],
                    price=product_data["price"],
                    stock=product_data["stock"],
                    download_size=product_data["download_size"],
                    supplier=supplier
                )
    inventory.add_product(product_obj)


print("===========================================================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("===========================================================================")



while True:
    user_input = 0

    print("\n================================= Menu ====================================")
    print("Welcome to the Smart Inventory Auditor!")
    print("You can add items to the inventory or quit the program.")
    print("The maximum inventory limit is 500 items.")
    print(
        "1. Display All Products\n"
        "2. Add Supplier\n"
        "3. Add Product\n"
        "4. Update Stock\n"
        "5. Search Product\n"
        "6. Add Order\n"
        "7. Save Inventory\n"
        "8. Exit"
    )


    try:
        user_input = int(input("Your choice:"))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 6.")
    
    if user_input == 1:
        print("\nCurrent Inventory")
        print("===========================================================================")
        if not inventory.products:
            print("No products found.")
        else:
            print("===========================================================================")
            inventory.display_all_products()
            print("===========================================================================")
        #     for product_obj in inventory.products:
        #         print("===========================================================================")
        #         product_obj.display_information()
        #         product_obj.get_fulfilment_info()
        #         print("===========================================================================")
        # print("===========================================================================")

    if user_input == 2:
        print("Add Supplier")

        try:
            new_supplier_id = input("Enter the supplier ID: ")
            duplicate = False
            for supplier in supplier_list:
                if supplier.id == new_supplier_id:
                    print("Supplier ID already exists. Please enter a unique supplier ID.")
                    duplicate = True
                    break
            if duplicate:
                continue

        except ValueError:
            print("Invalid input. Please enter a valid product ID.")
            continue

        
        new_supplier_name = input("Enter the supplier name: ")

        if not new_supplier_name:
            print("Invalid input. Supplier name cannot be empty.")
            continue


        new_supplier_email = input("Enter the supplier email: ")

        if not new_supplier_email:
            print("Invalid input. Supplier email cannot be empty.")
            continue


        supplier = Supplier(
                supplier_id = new_supplier_id,
                name = new_supplier_name,
                contact_email = new_supplier_email
            )
        
        supplier_list.append(supplier)

    elif user_input == 3:
        print("===========================================================================")
        print("Add a new product to the inventory")
        try:
            add_id = int(input("Enter the product ID: "))
            duplicate = False

            for item in inventory.products:
                if item.id == add_id:
                    print("Product ID already exists. Please enter a unique product ID.")
                    duplicate = True
                    break

            if duplicate:
                continue


        except ValueError:
            print("Invalid input. Please enter a valid product ID.")
            continue

            
        # Validate product name
        add_product = input("Enter the product name: ").strip()

        if not add_product:
            print("Invalid input. Product name cannot be empty.")
            continue
            

        # Validate price
        try:
            add_price = float(input("Enter the product price: "))

            if add_price <= 0:
                print("Invalid input. Please enter a positive number for price.")
                continue
                
        except ValueError:
            print("Invalid input. Please enter a valid product price.")
            continue

        # Validate stock
        try:
            add_stock = int(input("Enter the product stock: "))

            if add_stock <= 0:
                print("Invalid input. Please enter a positive number for stock.")
                continue
                
            if add_stock > 500:
                print("Inventory cannot exceed 500 items. Please enter a smaller amount.")
                continue
                
        except ValueError:
            print("Invalid input. Please enter a valid product stock.")
            continue


        supplier_id = input("Enter the Supplier ID: ")

        if not supplier_id:
            print("Invalid input. Supplier ID cannot be empty.")
            continue

        cancreate = False

        for supplier in supplier_list:

            if supplier.supplier_id == supplier_id:
                type_choice = input("Is this a physical product or digital product? (Enter 'physical' or 'digital'): ").strip().lower()
                if type_choice == "physical":
                    try:
                        add_weight = float(input("Enter the product weight (in kg): "))
                        cancreate = True
                        if add_weight <= 0:
                            print("Invalid input. Please enter a positive number for weight.")
                            cancreate = False
                            continue
                    except ValueError:
                        print("Invalid input. Please enter a valid product weight.")
                        continue


                    new_product = physicalProduct(add_id, type_choice, add_product, add_price, add_stock, add_weight, supplier)

                elif type_choice == "digital":
                    try:
                        add_download_size = float(input("Enter the product download size (in MB): "))
                        cancreate = True
                        if add_download_size <= 0:
                            print("Invalid input. Please enter a positive number for download size.")
                            cancreate = False
                            continue
                    except ValueError:
                        print("Invalid input. Please enter a valid product download size.")
                        continue

                    new_product = digitalProduct(add_id, type_choice, add_product, add_price, add_stock, add_download_size, supplier)
                else:
                    print("Invalid input. Please enter 'physical' or 'digital'.")
                    continue

        # Create a product object and add it to the existing list
        if cancreate == True:
            inventory.add_product(new_product)
            print("Product added successfully!")
            print("===========================================================================")

        else:
            print("Try again.")

    elif user_input == 4:
        print("===========================================================================")
        print("Update the stock of the product")

        try:
            update_id = int(input("Enter the product ID to update: "))

            id_found = False

            for item in inventory.products:
                if item.id == update_id:
                    item.updatestock()
                    id_found = True
                    break

            if not id_found:
                print("Product ID not found.")

        except ValueError:
            print("Invalid input. Please enter a valid product ID.")

        print("===========================================================================")

    elif user_input == 5:
        print("===========================================================================")
        print("Search for the product")

        try:
            search_id = int(input("Enter the product ID to search: "))
            for item in inventory.products:
                if item.id == search_id:
                    print("===================================================================================================================")
                    print(f"Product found: ID: {item.id} | Type: {item.type} | Name: {item.name} | Price: {item.price} | Stock: {item.stock}")
                    print("===================================================================================================================")
        except ValueError:
            print("Invalid input. Please enter a valid product ID.")
            break

        print("===========================================================================")

    elif user_input == 6:
        print("Add Order")

        try:
            product_id = int(input("Enter the product ID to add: "))
            order_id = input("Enter the Order ID to add: ")

            if not order_id:
                print("Order ID cannot be empty.")
                continue

            amount = int(input("Enter the amount to add: "))

            duplicate = False

            for product in inventory.products:
                if product.id == product_id:
                    order = Order(order_id)
                    order.add_order_line(product, amount)

                    order.calculate_total()
                    duplicate = True
                    break
            if duplicate:
                continue

        except ValueError:
            print("Invalid input. Please enter a valid input.")
            continue

        pass

    elif user_input == 7:
        print("===========================================================================")
        print("Save Inventory")

        data = {
            "products": [],
            "suppliers": []
                }

        for item in inventory.products:
            if "weight" in item.__dict__:
                product_data = {
                    "ID": item.id,
                    "type": item.type,
                    "name": item.name,
                    "price": item.price,
                    "stock": item.stock,
                    "weight": item.weight,
                    "SID": item.supplier.supplier_id
                }
            elif "download_size" in item.__dict__:
                product_data = {
                    "ID": item.id,
                    "type": item.type,
                    "name": item.name,
                    "price": item.price,
                    "stock": item.stock,
                    "download_size": item.download_size,
                    "SID": item.supplier.supplier_id
                }
            data["products"].append(product_data)

        for supplier in supplier_list:
            print(supplier.supplier_id)
            supplier_data = {
                "SID": supplier.supplier_id,
                "name": supplier.name,
                "email": supplier.contact_email
            }

            data["suppliers"].append(supplier_data)

        with open("inventory.json", "w") as file:
            json.dump(data, file, indent=4)

        print("\nSaving inventory...")
        print("Inventory saved successfully in inventory.json.\n")








        # inventory.storesproduct()
        print("===========================================================================")

    elif user_input == 8:
        print("===========================================================================")
        print("Quit the app")
        quit()

    else:
        print("Invalid input. Please enter a number between 1 and 6.")


# print("\n========= Print deleted product from inventory1 ============")
# physicalProduct1.display_information() # after removing the product it still can show its info, so it is aggregate 
# print("============================================================")

# for product in inventory1.products:
#     product.display_information()
#     product.get_fulfilment_info()

# print("\n============= Print product inside inventory1 ==============")
# inventory1.display_all_products()
# print("============================================================")

# inventory2.add_product(physicalProduct1)

# for product in inventory2.products:
#     product.display_information()
#     product.get_fulfilment_info()

# print("\n============= Print product inside inventory2 ==============")
# inventory2.display_all_products()
# print("============================================================")

# order = Order("Order_001")
# order.add_order_line(physicalProduct1, 2)
# order.add_order_line(digitalProduct1, 2)

# print("============================================================")
# order.calculate_total()
# print("============================================================")


