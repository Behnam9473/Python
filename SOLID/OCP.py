
# whene we want to add some feature it must be add as extension NOT Modification

from enum import Enum

class Size(Enum):
    SMALL = 1
    MED = 2
    LARGE = 3
    XLARGE = 4

class Cloth(Enum):
    TSHIRT = 1
    JEAN = 2
    SKIRT = 3


class Order:
    def __init__(self, name, size, cloth):
        self.name = name
        self.size = size
        self.cloth = cloth


class OrderFilter:
    def filter_size(self, orders, size):
        return [order for order in orders if order.size == size]




# If we want to add filer by size we are not allowd to add adnother filter def here


    # def filter_cloth(self, Order, cloth):

        #return [order for order in orders if order.cloth == cloth]

# print(OrderFilter.filter_size(order, 2))
# orders = [
#     Order("Order1", Size.SMALL, Cloth.TSHIRT),
#     Order("Order2", Size.MED, Cloth.JEAN),
#     Order("Order3", Size.MED, Cloth.SKIRT),
#     Order("Order4", Size.MED, Cloth.TSHIRT)
# ]

# order_filter = OrderFilter()

# filtered_orders = order_filter.filter_size(orders, Size.MED)

# for order in filtered_orders:
#     print(f'{order.name} {order.size.name} {order.cloth.name}')




class Specification:
    def is_satisfied(self, item):
        pass

class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size

class ClothSpecification(Specification):
    def __init__(self, cloth):
        self.cloth = cloth

    def is_satisfied(self, item):
        return item.cloth == self.cloth

class AndSpecification(Specification):
    def __init__(self, *specs):
        self.specs = specs

    def is_satisfied(self, item):
        return all(spec.is_satisfied(item) for spec in self.specs)

class OrderFilter:
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item

# Create some orders
orders = [
    Order("Order1", Size.SMALL, Cloth.TSHIRT),
    Order("Order2", Size.MED, Cloth.JEAN),
    Order("Order3", Size.LARGE, Cloth.SKIRT),
    Order("Order4", Size.XLARGE, Cloth.TSHIRT)
]

# Create specifications
size_spec = SizeSpecification(Size.MED)
cloth_spec = ClothSpecification(Cloth.TSHIRT)

# Filter orders
order_filter = OrderFilter()

print("Orders with size MED:")
for order in order_filter.filter(orders, size_spec):
    print(f'{order.name} {order.size.name} {order.cloth.name}')

print("\nOrders with cloth TSHIRT:")
for order in order_filter.filter(orders, cloth_spec):
    print(f'{order.name} {order.size.name} {order.cloth.name}')

# Combining specifications
combined_spec = AndSpecification(size_spec, cloth_spec)

print("\nOrders with size MED and cloth TSHIRT:")
for order in order_filter.filter(orders, combined_spec):
    print(f'{order.name} {order.size.name} {order.cloth.name}')