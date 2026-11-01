from pathlib import Path
import os
import json

from src.modules.inventory import Inventory                                                                                                                                                                                                                                                              
from src.modules.product import Product    
from src.modules.physicalProduct import PhysicalProduct
from src.modules.digitalProduct import DigitalProduct                                                                                                                                                                                                                                                             

class FileHandler:
    def __init__(self, filepath: str = "src/model/inventory.json"):
        self.filepath = Path(filepath)


    def file_exist(self):
        return self.filepath.is_file() and self.filepath.suffix.lower() == ".json"

    # def load_data
    def load_data(self, inventory: Inventory):
        if self.file_exist():

            try:
                with open(self.filepath, "r", encoding="utf-8") as f:
                    raw_data = json.load(f)
            except json.JSONDecodeError:
                return
            for item in raw_data: 
                if item["type"] == "physical":
                    #init the physical product class!
                    product = PhysicalProduct(
                        product_id = item["id"],
                        name = item["name"],
                        price = item["price"],
                        stock = item["stock"],
                        weight = item["weight"]
                    )
                elif item["type"] == "digital": 
                    product = DigitalProduct(
                        product_id = item["id"],
                        name = item["name"],
                        price = item["price"],
                        stock = item["stock"],
                        download_size = item["download_size"]
                    )
                inventory.add_product(product)
            # try:
            #     with open(self.filepath, "r", encoding="utf-8") as f:
            #         return json.load(f)  # Returns list of dicts 
            # except json.JSONDecodeError:
            #     return []  

    # save data
    def save_data(self, products: list) -> None: 
            data = [prod.to_dict() for prod in products]                                                                                                                                                                                                                             
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)




