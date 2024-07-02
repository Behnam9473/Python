"""
The Composite Design Pattern is a structural pattern that allows you to model objects in a tree-like structure,
    where you can interact with individual objects (called Leaf) and combinations of objects (called Composite).
This pattern enables you to easily create a hierarchy of objects and perform operations uniformly on all of them.

Main Components of the Composite Pattern:

    Component: A common interface for all objects in the composition, whether they are individual objects (Leaf) or composite objects.
    Leaf: Individual objects that have no subcomponents.
    Composite: Composite objects that can contain Leaf objects or other Composite objects.


"""
# Let’s assume we want to design a system for managing files and folders:
# Both files and folders can perform similar operations, such as displaying information, but folders can also contain other files and subfolders.


from abc import ABC, abstractmethod

class FileSystemComponent(ABC):
    @abstractmethod
    def show_details(self):
        pass

class File(FileSystemComponent):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def show_details(self):
        print(f"File: {self.name}, Size: {self.size}KB")

class Folder(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def show_details(self):
        print(f"Folder: {self.name}")
        for child in self.children:
            child.show_details() 


if __name__ == "__main__":
    file1 = File("File1.txt", 100)
    file2 = File("File2.txt", 150)
    
    folder1 = Folder("Folder1")
    folder1.add(file1)
    
    folder2 = Folder("Folder2")
    folder2.add(file2)
    folder2.add(folder1)
    
    folder2.show_details()
    # Output:
    # Folder: Folder2
    # File: File2.txt, Size: 150KB
    # Folder: Folder1
    # File: File1.txt, Size: 100KB
