from src.modules.product import Product                                                                                                                                                                                                                                                                 
from src.modules.physicalProduct import PhysicalProduct
from src.modules.digitalProduct import DigitalProduct


new_product = Product("P001", "Laptop", 100, 10, )
new_product.display_information()

physical_item = PhysicalProduct("P002", "Mechanical Keyboard", 89.99, 25, 1.2)
physical_item.display_information()

digital_item = DigitalProduct("P003", "Mechanical Keyboard", 89.99, 25, 10000)
digital_item.display_information()