
from src.modules.product import Product  
from src.modules.physicalProduct import PhysicalProduct
from src.modules.digitalProduct import DigitalProduct                                                                                                                                                                                                                                                         
from src.modules.inventory import Inventory 
from src.modules.fileHandler import FileHandler
from src.utils.check_user_input import check_user_input

# inventory_data = display_all()
inventory = Inventory()
fileHandler = FileHandler()

fileHandler.load_data(inventory)

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
            if not inventory.products:                
                print("Inventory Not found") 
            else:
                inventory.display_products()

        elif check_user_input(user_option) == "2":

            print("\nAdd New Product\n")
            print("Select Product Type:")
            print("1. Physical Product")
            print("2. Digital Product")
            product_type = input("Enter choice (1/2): ").strip()

            if product_type not in ("1", "2"):
                print("Invalid product type selected. Returning to menu.")
                continue   
            product_id = input("Product ID: ").strip().upper()
            product_name = input("Product Name: ").strip()
            price = float(input("Price: "))
            stock = int(input("Stock Quantity: "))
            if product_type == "1": 
                weight = float(input("Weight: "))

                new_product = PhysicalProduct(
                    product_id,
                    product_name,
                    price,
                    stock,
                    weight
                )
            # print(inventory.display_products())
            else: 
                #digital
                download_size = float(input("Download Size: "))
                new_product = DigitalProduct(
                    product_id,
                    product_name,
                    price,
                    stock,
                    download_size
                )
            inventory.add_product(new_product)

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







