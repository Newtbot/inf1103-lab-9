# 1.2 Create a PhysicalProduct class
# Create a new class called PhysicalProduct that inherits from Product.
# Considering this is a physical item it should retain the attributes and behaviour of a regular product while
# introducing new attributes and behaviours that are unique to a physical product, let’s add weight!
# • weight: the weight of the product in kilograms.
# Your implementation should:
# 6. Reuse the existing Product constructor using super().
# 7. Initialise the additional weight attribute.
# 8. Provide a method called display_information() that displays the product’s existing information alongside its
# weight.
# Test your class by creating a PhysicalProduct object from your external code (where you run your program!) and
# displaying its information


from src.modules.product import Product   
from src.modules.canBeShipped import CanBeShipped  


class PhysicalProduct(Product, CanBeShipped): 
    def __init__(self, product_id: str, name: str , price: float, stock: int ,weight: float):
        # In Python, super() function is used to call methods from a parent (superclass) 
        # inside a child (subclass). It allows to extend or override inherited methods 
        # while still reusing the parent's functionality.
        # super().__init__(id, name)   #Calls Emp’s __init__

        #parent attributes.. 
        super().__init__(product_id, name, price, stock)
        #my Physical Product attributes
        self._weight = weight


    @property
    def weight(self) -> float: 
        return self._weight

    def display_information(self) -> None:
        super().display_information()          
        print(f"Weight: {self.weight:.2f} kg")

    #method override.. they always read child class than adult methods
    def to_dict(self) -> dict: 
        data = super().to_dict()
        data["type"] = "physical"
        data["weight"] = self.weight
        return data
 
    def get_fulfillment_info(self) -> None:
        return f"Shipped via postal courier. Weight: {self.weight:.2f} kg."

    def calculate_shipping_cost(self) -> float:
            rate_per_kg = 2.0
            return self.weight * rate_per_kg


