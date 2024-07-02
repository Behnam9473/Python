""" 
The Proxy design pattern is a structural design pattern that provides an object representing another object.
This proxy object controls access to the original object, allowing for additional functionality
like lazy initialization, access control, logging, or caching without changing the original object's code.

Key Components of the Proxy Pattern:
    Subject: An interface or abstract class defining the common interface for RealSubject and Proxy.
    RealSubject: The actual object that the proxy represents.
    Proxy: The object that controls access to the RealSubject. It implements the same interface as the RealSubject and holds a reference to it.
Benefits:
    Control over object access: Can provide controlled access to the RealSubject.
    Lazy initialization: Can delay the creation and initialization of expensive objects until they are actually needed.
    Logging and auditing: Can add logging or other functionalities transparently.
    Remote proxies: Can represent objects that are in different address spaces.

"""

from abc import ABC, abstractmethod

# Subject
class Image(ABC):
    @abstractmethod
    def display(self):
        pass

# RealSubject
class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.load_image_from_disk()

    def load_image_from_disk(self):
        print(f"Loading image {self.filename} from disk...")

    def display(self):
        print(f"Displaying image {self.filename}")

# Proxy
class ProxyImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None

    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        self.real_image.display()

# Usage
image1 = ProxyImage("photo1.jpg")
image2 = ProxyImage("photo2.jpg")

# Image is loaded from disk only when display() is called
image1.display()  # Output: Loading image photo1.jpg from disk... Displaying image photo1.jpg
image1.display()  # Output: Displaying image photo1.jpg
image2.display()  # Output: Loading image photo2.jpg from disk... Displaying image photo2.jpg
