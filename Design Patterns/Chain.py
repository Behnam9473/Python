""" 
The Chain of Responsibility is a behavioral design pattern used to process a request through a series of handlers.
Each handler decides either to process the request or to pass it to the next handler in the chain.
This pattern decouples the sender of the request from its receivers,
allowing multiple objects to handle the request without the sender needing to know which object will handle it.


Conceptual Overview:
    Handler Interface/Abstract Class: Defines an interface for handling requests and an optional method to set the next handler in the chain.
    Concrete Handlers: Implements the handler interface and processes requests it can handle; otherwise, it forwards the request to the next handler.
    Client: Initiates the request and sends it to the first handler in the chain.

"""

class Handler:
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler

    def handle(self, request):
        if self.next_handler:
            return self.next_handler.handle(request)
        return None

class LowLevelHandler(Handler):
    def handle(self, request):
        if request == "low":
            return "Handled by LowLevelHandler"
        else:
            return super().handle(request)

class MidLevelHandler(Handler):
    def handle(self, request):
        if request == "mid":
            return "Handled by MidLevelHandler"
        else:
            return super().handle(request)

class HighLevelHandler(Handler):
    def handle(self, request):
        if request == "high":
            return "Handled by HighLevelHandler"
        else:
            return super().handle(request)

# Client code
low_handler = LowLevelHandler()
mid_handler = MidLevelHandler()
high_handler = HighLevelHandler()

low_handler.set_next(mid_handler).set_next(high_handler)

# Sending requests to the chain
print(low_handler.handle("low"))  # Output: Handled by LowLevelHandler
print(low_handler.handle("mid"))  # Output: Handled by MidLevelHandler
print(low_handler.handle("high")) # Output: Handled by HighLevelHandler
print(low_handler.handle("unknown")) # Output: None (request was not handled)
