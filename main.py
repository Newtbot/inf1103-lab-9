
from src.modules.product import Product                                                                                                                                                                                                                                                                 
from src.modules.inventory import Inventory 
from src.modules.fileHandler import FileHandler
from src.utils.check_user_input import check_user_input

# inventory_data = display_all()
inventory = Inventory()
fileHandler = FileHandler()
saved_data = fileHandler.load_data()                                                                                                                                                                                                                                                   

if saved_data:                                                                                                                                                                                                                                                                         
    for item in saved_data:                                                                                                                                                                                                                                                              
        product = Product(item["id"], item["name"], item["price"], item["stock"])                                                                                                                                                                                                          
        inventory.add_product(product) 

while True:
    # the list will host product dict
    # option 1 will read the json file and represent it as a dict
    # option 2 will append the user input to a dict
    # option 3 will update the product based on dict keys and dict values
    # option 4 will get values by dict key 
    # option 5 will save the list to json file
    # option 6 will save the data and exit 
    # if true run the program
        print(
            "========================================================\n"
            "INVENTORY MANAGEMENT SYSTEM\n"
            "========================================================\n\n"
            "inventory.json found.\n"
            "Inventory loaded successfully\n\n"
            "----------- MENU -----------\n"
            "1. Display All Products\n"
            "2. Add Product\n"
            "3. Update Stock\n"
            "4. Search Product\n"
            "5. Save Inventory\n"
            "6. Exit\n"
            "----------------------------\n"
            )

        user_option = input("Enter Option: ")
        if check_user_input(user_option) == "1":
            print(
                "--------------------------------------------------------\n"
                "Current Inventory\n"
                "--------------------------------------------------------"
                )
            if not fileHandler.load_data():
                print("Inventory Not found") 
            else:
                inventory.display_products()

        elif check_user_input(user_option) == "2":
            print("\nAdd New Product\n")
            product_id = input("Product ID: ").strip().upper()
            product_name = input("Product Name: ").strip()

            # Convert price to float and stock to int
            price = float(input("Price: "))
            stock = int(input("Stock Quantity: "))

            new_product = Product(product_id, product_name, price, stock)

            inventory.add_product(new_product)
            
            print(inventory.display_products())

        elif check_user_input(user_option) == "3":
            print("Update Stock")
            product_id = input("Product ID: ").strip().upper()

            product_item = inventory.search_product(product_id)
            if product_item:
                product_stock = int(input("New Stock Quantity: "))
                product_item.update_stock(product_stock)
            else:
                print("Product not found.")


        elif check_user_input(user_option) == "4":
            print("Search Stock")
            product_id = input("Product ID: ").strip().upper()
            product_item = inventory.search_product(product_id)            
            if product_item:
                product_item.display_information()
            else: 
                print("Product not found")

        elif check_user_input(user_option) == "5":
            print("Saving inventory......")
            print("Inventory saved successfully to inventory.json.")
            fileHandler.save_data(inventory.products)
        
        elif check_user_input(user_option) == "6":
            fileHandler.save_data(inventory.products)
            print("Saving inventory before exit...")
            print(f"Inventory saved successfully.\n")
            print(
                f"Thank you for using Inventory Management System.\n"
                f"Program terminated.")
            break

        else:
            print("Please enter a valid integer. Eg. `1` ")







