# class User:
#     def __init__(self, username: str, email: str):
#         # Instance attributes
#         self.username = username
#         self.email = email
#         self.is_active = True

#     # Instance method
#     def deactivate(self) -> None:
#         self.is_active = False

#     # String representation for printing/debugging
#     def __repr__(self) -> str:
#         return f"User(username='{self.username}', active={self.is_active})"


# # Creating an instance (instantiation)
# user1 = User("alice", "alice@example.com")
# print(user1.username)    # Output: alice

# user1.deactivate()
# print(user1.is_active)   # Output: False
# print(user1)             # Output: User(username='alice', active=False)



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

#void is there to represent it doesnt return the data..
class Product:
    def __init__(self, product_id: str, name: str , price: float, stock: int ):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
        
    @property
    def product_id(self) -> str:
        return self.__product_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> float:
        return self.__price

    @property
    def stock(self) -> int:
        return self.__stock

    # def get_id(self) ->  str: 
    #     return self.__product_id


    #methods go here
    def update_stock(self, quantity: int) -> None:
        if self.__stock < 0:
            print("Product Quantity cannot be 0 or negative number.")
        self.__stock = quantity


    def get_details(self) -> str:
            """Returns the base product string so subclasses can extend it (OCP)."""
            return (
                f"ID: {self.product_id} | "
                f"Name: {self.name} | "
                f"Price: ${self.price:.2f} | "
                f"Stock: {self.stock}"
        )

    # once __init__ finsihes it will destroy name price etc. hence we must use self_ .. to access the var
    def display_information(self) -> None: 
        print(self.get_details())

    def to_dict(self) -> dict:                                                                                                                                                                                                                                                         
        return {                                                                                                                                                                                                                                                                       
                "id": self.__product_id,                                                                                                                                                                                                                                                   
                "name": self.__name,                                                                                                                                                                                                                                                       
                "price": self.__price,                                                                                                                                                                                                                                                     
                "stock": self.__stock,                                                                                                                                                                                                                                                     
            } 
