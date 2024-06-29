# Prototype: A partially or fully initialized object that you copy(clone) and make use of it

"""
    This pattern is useful when the creation of an object is costly or complex.
    Instead of creating a new instance from scratch, you clone the prototype.
"""


import copy

# class Prototype:
#     def clone(self):
#         return copy.deepcopy(self)

# class ConcretePrototype(Prototype):
#     def __init__(self, value):
#         self.value = value

#     def __str__(self):
#         return f"ConcretePrototype(value={self.value})"

# # Usage
# prototype = ConcretePrototype("Initial Value")
# print(f"Original Prototype: {prototype}")

# # Cloning the prototype
# cloned_prototype = prototype.clone()
# print(f"Cloned Prototype: {cloned_prototype}")

# # Modifying the clone to show they are distinct objects
# cloned_prototype.value = "Modified Value"
# print(f"Modified Cloned Prototype: {cloned_prototype}")
# print(f"Original Prototype after clone modification: {prototype}")

# Using Prototype in factory methods:

class Products:
    def __init__(self, name, description, category, price, stock_qty):
        self.name = name
        self.description = description
        self.category = category
        self.price = price
        self.stock_qty = stock_qty
        
    def __str__(self) -> str:
        return f"Product name: {self.name}, description: {self.description}, " +\
               f"category: {self.category}, Price: {self.price}, QTY: {self.stock_qty}"

class Store:
    def __init__(self, store_name, available_products):
        self.store_name = store_name
        self.available_products = available_products
        
    def __str__(self) -> str:
        products_str = "\n".join(str(product) for product in self.available_products)
        return f"Store Name: {self.store_name}, Available Products:\n{products_str}"

class StoreFactory:
    main_store = Store("HQ", [Products('407', "brand new car", "Vehicle", 50000, 50)])
    
    @staticmethod
    def __new_store(prototype, name, product_name, product_price, product_quantity):
        new_store = copy.deepcopy(prototype)
        new_product = Products(product_name, "Description for " + product_name, "Category for " + product_name, product_price, product_quantity)
        new_store.store_name = name
        new_store.available_products = [new_product]
        return new_store
    
    @staticmethod
    def updated_available_products(name, product_name, product_price, product_quantity):
        return StoreFactory.__new_store(StoreFactory.main_store, name, product_name, product_price, product_quantity)

Shiraz = StoreFactory.updated_available_products('Shiraz', "truck", 5, 5)
Ahvaz = StoreFactory.updated_available_products('Ahvaz', "911", 5000, 14)
print(Ahvaz)