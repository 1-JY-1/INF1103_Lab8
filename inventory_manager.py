
from mainprogram import MainProgram


toQuit = False

print("===========================================================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("===========================================================================")

start = MainProgram()

while not toQuit:
    print("\n================================= Menu ====================================")
    print("Welcome to the Smart Inventory Auditor!")
    print("You can add items to the inventory or quit the program.")
    print("The maximum inventory limit is 500 items.")
    print(
        "1. Display All Products\n"
        "2. Add Product\n"
        "3. Update Stock\n"
        "4. Search Product\n"
        "5. Save Inventory\n"
        "6. Exit"
    )

    userinput = input("Your choice: ")

    start.getuserinput(userinput)

    if userinput.strip() == "6":
        toQuit = True

