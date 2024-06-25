# An interface (or a class in Python) should have only the methods that are relevant to its clients.
# If a class has methods that are not used by all its clients,
# it's better to split the interface into smaller, more specific ones.

from abc import ABC, abstractmethod

# class Worker(ABC):
#     @abstractmethod
#     def work(self):
#         pass

#     @abstractmethod
#     def eat(self):
#         pass

# class Human(Worker):
#     def work(self):
#         print("Human working")

#     def eat(self):
#         print("Human eating")
# # Here. Because the robot can't eat; So it must have its own interface.
# class Robot(Worker):
#     def work(self):
#         print("Robot working")

#     def eat(self):
#         raise NotImplementedError("Robots do not eat")
 
 # We should split the interface into smaller, more specific ones.
 
class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Human(Workable, Eatable):
    def work(self):
        print("Human working")

    def eat(self):
        print("Human eating")

class Robot(Workable):
    def work(self):
        print("Robot working")

# Function that works with Workable objects
def manage_work(worker: Workable):
    worker.work()

# Function that works with Eatable objects
def manage_eat(eater: Eatable):
    eater.eat()

# Using the functions with different objects
human = Human()
robot = Robot()

manage_work(human)  # Output: Human working
manage_work(robot)  # Output: Robot working
manage_eat(human)   # Output: Human eating