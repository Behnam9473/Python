""" 
The Iterator design pattern is a behavioral design pattern that provides
a way to access the elements of a collection (such as a list or a tree) sequentially without exposing the underlying representation.
The main idea is to decouple the logic for accessing and traversing the elements of a collection from the actual data structure,
allowing different traversal strategies to be implemented and used interchangeably.

Components of the Iterator Design Pattern:
    Iterator: An interface or abstract class that defines the methods for accessing and traversing elements (e.g., next(), has_next()).
    ConcreteIterator: A class that implements the Iterator interface and keeps track of the current position in the traversal.
    Aggregate: An interface or abstract class that defines a method for creating an iterator (e.g., create_iterator()).
    ConcreteAggregate: A class that implements the Aggregate interface and returns an instance of a ConcreteIterator.
    
    
Use Cases:
    Collections: Standard collections such as lists, sets, maps, and trees often use iterators to provide a way to traverse their elements.
    Data Streams: Iterating over elements in a data stream, such as lines in a file or records from a database query.
    Composite Patterns: Traversing components in composite structures like tree hierarchies.
Benefits:
    Encapsulation: Provides a way to access elements without exposing the underlying representation.
    Flexibility: Supports different traversal strategies by implementing different iterators.
    Polymorphism: Allows different collections to be iterated in a uniform manner.
Drawbacks:
    Overhead: Can introduce additional overhead, especially if creating a new iterator object for each traversal.
    Complexity: May add complexity when the collection structure is simple and doesn't require multiple traversal strategies. 

"""



from collections.abc import Iterator, Iterable

class CustomIterator(Iterator):
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def __next__(self):
        try:
            value = self._collection[self._index]
        except IndexError:
            raise StopIteration()
        self._index += 1
        return value

class CustomList(Iterable):
    def __init__(self):
        self._items = []

    def add(self, item):
        self._items.append(item)

    def __iter__(self):
        return CustomIterator(self._items)

# Example usage:
custom_list = CustomList()
custom_list.add(1)
custom_list.add(2)
custom_list.add(3)

for item in custom_list:
    print(item)


""" 
Python's standard library provides built-in support for iterators and iterables.
The iter() function returns an iterator from an iterable, and the next() function retrieves the next item from an iterator.

"""

numbers = ['a', 'b', 'c', 'd', 'e',]
iterator = iter(numbers)

while True:
    try:
        number = next(iterator)
        print(number)
    except StopIteration:
        break
