import json

class FileHandling:
    def __init__(self):
        self.productdetail = {"products": []}

    def load_inventory(self):
        try:
            with open("inventory.json", "r") as file:
                self.productdetail = json.load(file)

        except FileNotFoundError:
            self.productdetail = {"products": []}

            with open("inventory.json", "w") as file:
                json.dump(self.productdetail, file, indent=4)

    def save_inventory(self, inventory):
        data = {"products": []}

        for item in inventory:
            if "weight" in item.__dict__:
                product_data = {
                    "ID": item.id,
                    "type": item.type,
                    "name": item.name,
                    "price": item.price,
                    "stock": item.stock,
                    "weight": item.weight
                }
            elif "download_size" in item.__dict__:
                product_data = {
                    "ID": item.id,
                    "type": item.type,
                    "name": item.name,
                    "price": item.price,
                    "stock": item.stock,
                    "download_size": item.download_size
                }

            data["products"].append(product_data)

        with open("inventory.json", "w") as file:
            json.dump(data, file, indent=4)

        print("\nSaving inventory...")
        print("Inventory saved successfully in inventory.json.\n")
















# import json


# class filehandling:

#     def __init__(self):
#         self.productdetail = []

#     def load_inventory(self):
#         try:
#             with open("inventory.json", "r") as file:
#                 data = json.load(file)

#                 self.productdetail = data

#         except FileNotFoundError:
#             # Create the inventory file
#             with open("inventory.json", "w") as file:
#                 json.dump({"products": []}, file, indent=4)

#     def save_inventory(self, inventory): #, product_name, quantity

#         data = {
#                 "products": []
#             }
        
#         for item in inventory:
#             product = {
#                 "ID": item[0],
#                 "name": item[1],
#                 "price": item[2],
#                 "stock": item[3]
#             }

#             data["products"].append(product)

#         with open("inventory.json", "w") as file:
#             json.dump(data, file, indent=4)

#         print("\nSaving inventory...")
#         print("Inventory saved successfully in inventory.json.\n")

#         return inventory


