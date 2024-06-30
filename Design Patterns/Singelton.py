"""
The Singleton design pattern is a creational pattern that ensures a class has only one instance
and provides a global point of access to that instance.
This pattern is useful when exactly one object is needed to coordinate actions across the system.

"""
# A basic way to implement a Singleton is to use a class variable to store the instance.
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

# Example usage:
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # Output: True

#Another way is to use a decorator to wrap a class and ensure it behaves as a Singleton.
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Singleton:
    pass

# Example usage:
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # Output: True

#More advanced method is to use a metaclass to control the creation of the Singleton class.

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    pass

# Example usage:
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # Output: True


#To ensure that the Singleton implementation is thread-safe, you can use threading locks.

import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

# Example usage:
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # Output: True
