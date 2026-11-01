#only handle product obj?
# - __product_id:String
# - __name:String
# - __price:float
# - __stock:int
# + update_stock(quantity : int):void
# + display_information():voidclass Product: 

#__ = private 
# + = public 
# # = protected


# wat methods we need??
# store products
# add product
# searches product??
# display products?

#inventory class
# - self.product:List
# +
from src.modules.product import Product                                                                                                                                                                                                                                                                 

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        if (isinstance(product, Product)):
            self.products.append(product)
        else: 
            print("invalid data")

    def search_product(self, product_id: str):
        for prod in self.products: 
            if prod.product_id == product_id:
                return prod

    def display_products(self):
        for prod in self.products:
            prod.display_information()