""" 
The Mediator design pattern is a behavioral design pattern that defines an object (the mediator) that encapsulates how a set of objects interact.
This pattern promotes loose coupling by preventing objects from referring to each other explicitly and allows their interaction to be varied independently.

Components of the Mediator Design Pattern:
    Mediator: An interface that defines methods for communication between colleague objects.
    ConcreteMediator: A class that implements the Mediator interface and coordinates the interaction between colleague objects.
    Colleague: An abstract class or interface for objects that communicate via the mediator.
    ConcreteColleague: A class that implements the Colleague interface and communicates with other colleagues through the mediator.
    
Use Cases:
    GUI Components: To manage interactions between various UI components.
    Chat Systems: To manage communication between users.
    Aircraft Control: To manage communication between different aircrafts via a control tower.
    Workflow Systems: To manage interactions between different components in a workflow.
Benefits:
    Loose Coupling: Reduces dependencies between colleague objects, promoting loose coupling.
    Simplified Communication: Centralizes complex communication logic in one place.
    Single Responsibility: Each colleague only knows about the mediator, not other colleagues.
Drawbacks:
    Mediator Complexity: The mediator can become complex as it handles more interactions.
    Performance Overhead: Adds an additional layer of abstraction that may introduce performance overhead in highly time-sensitive applications.

"""

from abc import ABC, abstractmethod

# Mediator Interface
class ChatRoomMediator(ABC):
    @abstractmethod
    def show_message(self, user, message):
        pass

# Concrete Mediator
class ChatRoom(ChatRoomMediator):
    def show_message(self, user, message):
        print(f"[{user.get_name()}]: {message}")

# Colleague Interface
class User(ABC):
    def __init__(self, name, mediator):
        self._name = name
        self._mediator = mediator

    def send_message(self, message):
        self._mediator.show_message(self, message)

    def get_name(self):
        return self._name

# Concrete Colleague
class ChatUser(User):
    pass

# Example usage:
mediator = ChatRoom()

user1 = ChatUser("Alice", mediator)
user2 = ChatUser("Bob", mediator)

user1.send_message("Hi Bob!")
user2.send_message("Hello Alice!")
#==============================================Sensor Example=========================================

class SensorMediator(ABC):
    @abstractmethod
    def notify(self, sender, event):
        pass

class SensorSystem(SensorMediator):
    def __init__(self):
        self._sensors = []

    def add_sensor(self, sensor):
        self._sensors.append(sensor)
        sensor.set_mediator(self)

    def notify(self, sender, event):
        for sensor in self._sensors:
            if sensor != sender:
                sensor.receive_event(event)

class Sensor(ABC):
    def __init__(self, name):
        self._name = name
        self._mediator = None

    def set_mediator(self, mediator):
        self._mediator = mediator

    def send_event(self, event):
        self._mediator.notify(self, event)

    @abstractmethod
    def receive_event(self, event):
        pass

class TemperatureSensor(Sensor):
    def receive_event(self, event):
        print(f"TemperatureSensor received event: {event}")

class PressureSensor(Sensor):
    def receive_event(self, event):
        print(f"PressureSensor received event: {event}")

# Example usage:
mediator = SensorSystem()

temp_sensor = TemperatureSensor("TempSensor")
pressure_sensor = PressureSensor("PressureSensor")

mediator.add_sensor(temp_sensor)
mediator.add_sensor(pressure_sensor)

temp_sensor.send_event("Temperature High")
pressure_sensor.send_event("Pressure Low")

"""
The Mediator design pattern is useful for managing complex interactions and promoting loose coupling in systems where components interact frequently.
"""
