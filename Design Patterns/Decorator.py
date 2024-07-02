"""

The decorator design pattern in Python is a structural pattern that allows you
to dynamically add behavior or responsibilities to objects without modifying their code.
Decorators provide a flexible alternative to subclassing for extending functionality.

"""

# Basic decorator
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.",'\n')
    return wrapper

@my_decorator
def say_hello():
    print("Hello!" )

say_hello()

# Decorator with arguments

def arg_decorator(func):
    def wrapper(*args, **kwargs):
        print('\n',"Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.",'\n')
        return result
    return wrapper

@arg_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")


# Decorator can be used to decorate methods in classes

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

class MyClass:
    @my_decorator
    def instance_method(self):
        print("This is an instance method.")

obj = MyClass()
obj.instance_method()
