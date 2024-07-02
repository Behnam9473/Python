""" 
The Command design pattern is a behavioral design pattern that turns a request into a stand-alone
object containing all the information about the request. This transformation allows for parameterizing
methods with different requests, queuing or logging requests, and supporting undoable operations.

Conceptual Overview:
    Command Interface/Abstract Class: Declares an interface for executing an operation.
    Concrete Commands: Implement the Command interface to define a binding between a receiver and an action.
    Invoker: Asks the command to carry out the request.
    Receiver: Knows how to perform the operations associated with carrying out a request.

"""

# Command Interface
class Command:
    def execute(self):
        pass

# Concrete Commands
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()

# Receiver
class Light:
    def on(self):
        print("The light is on")

    def off(self):
        print("The light is off")

# Invoker
class RemoteControl:
    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()

# Client code
light = Light()
light_on = LightOnCommand(light)
light_off = LightOffCommand(light)

remote = RemoteControl()
remote.set_command(light_on)
remote.press_button()  # Output: The light is on

remote.set_command(light_off)
remote.press_button()  # Output: The light is off
