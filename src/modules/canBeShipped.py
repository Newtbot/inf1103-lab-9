# 4.1 Create a CanBeShipped interface
# Create a new abstract base class called CanBeShipped.
# It should define an abstract method called calculate_shipping_cost(). The method should specify that
# implementing classes must provide a way to calculate shipping costs.
# Do not add product-specific attributes or shipping implementation details to this interface. The interface is a
# contract that should be signable by any object that can-be-shipped.

from abc import ABC, abstractmethod

class CanBeShipped(ABC):

    @abstractmethod
    def calculate_shipping_cost():
        """Calculate and return the shipping cost for this shippable item."""
        pass

# 4.2 Implement the interface
# Update PhysicalProduct so that it implements the CanBeShipped interface. Implement calculate_shipping_cost()
# using a simple rule of your choice. For example, calculate shipping based on the product’s weight.
# Test the method with physical products of different weights.
# Do not make DigitalProduct implement CanBeShipped, as digital products do not require physical shipping.
# Important: Remember to stick with single class inheritance. PhysicalProduct should inherit from Product, and
# CanBeShipped should remain a separate interface-style ABC. Avoid multiple inheritance relationships, but a single
# inheritance and multiple interface relationships is ok!