from pathlib import Path
import os
import json

from src.modules.inventory import Inventory                                                                                                                                                                                                                                                              
from src.modules.product import Product                                                                                                                                                                                                                                                                 




# # Persistence: At the start of the program, read the information previously saved
# # in the inventory file. If the inventory file does not exist, start with an empty
# # inventory and continue running without producing an error.
# def check_file(data_file: str) -> bool:
#     path = Path(data_file)
#     # Check that it exists, is an actual file (not a folder), and ends with .json
#     return path.is_file() and path.suffix.lower() == ".json"


class FileHandler:
    def __init__(self, filepath: str = "src/model/inventory.json"):
        self.filepath = Path(filepath)


    def file_exist(self):
        return self.filepath.is_file() and self.filepath.suffix.lower() == ".json"

    # def load_data
    def load_data(self):
        if self.file_exist():
            with open(self.filepath, "r", encoding="utf-8") as f:
                return json.load(f)  # Returns list of dicts                                                                                                                                                                                                                                   
        else:
            with open(self.filepath, "w", encoding="utf-8") as f:
                pass

    # save data
    def save_data(self, products: list) -> None: 
            data = [prod.to_dict() for prod in products]                                                                                                                                                                                                                             
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)




