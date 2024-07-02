""" 
The Flyweight design pattern is a structural pattern that focuses on minimizing memory usage by sharing as much data as possible with similar objects.
It is particularly useful when working with a large number of objects that share common data.
The key idea is to store common data externally and reuse it among different objects, rather than storing it in each object individually.

Key Components of the Flyweight Pattern:
    Flyweight: The shared object that can be used in multiple contexts simultaneously. It stores intrinsic data (common to all objects).
    Flyweight Factory: Creates and manages flyweight objects. It ensures that flyweights are shared properly.
    Client: Maintains references to flyweight objects and computes extrinsic data (unique for each object).
Benefits:
    Reduced memory usage: By sharing common data, the memory footprint is significantly reduced.
    Performance improvement: Reduces the number of objects created and thus can improve performance.

"""

class TreeType:
    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, x, y):
        print(f"Drawing a {self.name} tree of color {self.color} and texture {self.texture} at ({x}, {y})")

class TreeFactory:
    _tree_types = {}

    @classmethod
    def get_tree_type(cls, name, color, texture):
        key = (name, color, texture)
        if key not in cls._tree_types:
            cls._tree_types[key] = TreeType(name, color, texture)
        return cls._tree_types[key]

class Tree:
    def __init__(self, x, y, tree_type):
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def draw(self):
        self.tree_type.draw(self.x, self.y)

class Forest:
    def __init__(self):
        self.trees = []

    def plant_tree(self, x, y, name, color, texture):
        tree_type = TreeFactory.get_tree_type(name, color, texture)
        tree = Tree(x, y, tree_type)
        self.trees.append(tree)

    def draw(self):
        for tree in self.trees:
            tree.draw()

# Usage
forest = Forest()
forest.plant_tree(1, 1, "Oak", "Green", "Rough")
forest.plant_tree(2, 3, "Pine", "Green", "Smooth")
forest.plant_tree(1, 1, "Oak", "Green", "Rough")  # Reuses the existing Oak tree type

forest.draw()
