# 1.3 Create a DigitalProduct class
# Create another class called DigitalProduct that inherits from Product.
# A digital product exists in the virtual realm, so doesn’t actually have a weight, but it does have a download size,
# which is a suitable new attribute to be added, so now let’s add download_size:
# • download_size: the size of the downloadable product in megabytes.
# Your implementation should:
# 9. Reuse the existing Product constructor using super().
# 10. Initialise the additional download_size attribute.
# 11. Provide its own display_information() method that displays the product’s existing information alongside its
# download size.
# Test your class by creating a DigitalProduct object and displaying its information.


from src.modules.product import Product 
import pathlib                                                                                                                                                                                                                                                              

class DigitalProduct(Product): 
    def __init__(self, product_id: str, name: str , price: float, stock: int ,download_size: float):
        # In Python, super() function is used to call methods from a parent (superclass) 
        # inside a child (subclass). It allows to extend or override inherited methods 
        # while still reusing the parent's functionality.
        # super().__init__(id, name)   #Calls Emp’s __init__

        #parent attributes.. 
        super().__init__(product_id, name, price, stock)
        #my digital Product attributes
        self._download_size = download_size

    @property
    def download_size(self) -> float: 
        return self._download_size

    def display_information(self) -> None:
        file_size_mb = self._download_size / (1024 * 1024)

        super().display_information()          
        print(f"Download Size: {file_size_mb:.2f} MB")

    #method override.. they always read child class than adult methods
    def to_dict(self) -> dict: 
        data = super().to_dict()
        data["type"] = "digital"
        data["download_size"] = self.download_size
        return data

    def get_fulfillment_info() -> None:
        pass