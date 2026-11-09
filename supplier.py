

class Supplier:
    def __init__(self, supplier_id:str, name:str, contact_email:str):
        self.supplier_id = supplier_id
        self.name = name
        self.contact_email = contact_email

    def get_supplier_details(self):
        return {
            "supplier_id": self.supplier_id,
            "name": self.name,
            "contact_email": self.contact_email
        }

    def display_information(self) -> None:
        print(f"Supplier ID: {self.supplier_id}")
        print(f"Supplier Name: {self.name}")
        print(f"Contact Email: {self.contact_email}") 