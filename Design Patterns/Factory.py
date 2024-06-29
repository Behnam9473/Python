"""
The Factory pattern is used when:

1 - You have multiple classes that implement the same interface or inherit from the same parent class.
2 - The exact class of the object that needs to be created is determined at runtime.
3 - The creation logic is simple and based on input parameters.


"""


from abc import ABC, abstractmethod

# Abstract Product
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

# Concrete Products
class Circle(Shape):
    def draw(self):
        return "Drawing Circle"

class Square(Shape):
    def draw(self):
        return "Drawing Square"

# Factory
class ShapeFactory:
    @staticmethod
    def create_shape(shape_type):
        if shape_type == 'circle':
            return Circle()
        elif shape_type == 'square':
            return Square()
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")

# Client Code
shape_factory = ShapeFactory()
shape = shape_factory.create_shape('circle')
print(shape.draw())  # Output: Drawing Circle

"""
 the ShapeFactory creates different Shape objects based on the input parameter.
 The client does not need to know the details of object creation.

"""