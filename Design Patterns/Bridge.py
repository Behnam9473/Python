""" 
The Bridge design pattern is a structural design pattern used to decouple an abstraction from its implementation, allowing the two to vary independently.
This pattern is particularly useful when both the abstractions and their implementations are expected to evolve frequently.

Key Components of the Bridge Pattern:
    Abstraction: Defines the abstraction's interface and maintains a reference to an object of type Implementor.
    Refined Abstraction: Extends the interface defined by Abstraction.
    Implementor: Defines the interface for implementation classes. This interface doesn't need to match the Abstraction's interface; typically, the Abstraction delegates work to the Implementor's methods.
    Concrete Implementor: Implements the Implementor interface.
    
When to Use the Bridge Pattern:
    When you want to avoid a permanent binding between an abstraction and its implementation.
    When both the abstractions and their implementations should be extensible via subclasses.
    When changes in the implementation of an abstraction should not impact clients.
    When you have a proliferation of classes due to a coupled interface and implementation hierarchy.
"""


from abc import ABC, abstractmethod

class MessageDisplay(ABC):
    @abstractmethod
    def show_message(self, message):
        pass


class ConsoleDisplay(MessageDisplay):
    def show_message(self, message):
        print(f"Console: {message}")

class PopupDisplay(MessageDisplay):
    def show_message(self, message):
        print(f"Popup: {message}")  


class Message:
    def __init__(self, display):
        self.display = display

    def show(self):
        pass


class SimpleMessage(Message):
    def __init__(self, display, text):
        super().__init__(display)
        self.text = text

    def show(self):
        self.display.show_message(self.text)

class WarningMessage(Message):
    def __init__(self, display, text):
        super().__init__(display)
        self.text = f"Warning: {text}"

    def show(self):
        self.display.show_message(self.text)


if __name__ == "__main__":
    console_display = ConsoleDisplay()
    popup_display = PopupDisplay()
    
    simple_message = SimpleMessage(console_display, "Hello, World!")
    simple_message.show()  # Output: Console: Hello, World!

    warning_message = WarningMessage(popup_display, "Low Battery")
    warning_message.show()  # Output: Popup: Warning: Low Battery
    
    # Now we can easily change the display
    simple_message = SimpleMessage(popup_display, "Hello, World!")
    simple_message.show()  # Output: Popup: Hello, World!

    warning_message = WarningMessage(console_display, "Low Battery")
    warning_message.show()  # Output: Console: Warning: Low Battery
