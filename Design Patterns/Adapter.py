"""
The Adapter design pattern is a structural pattern that allows objects with incompatible interfaces to work together.
This pattern is particularly useful when you need to integrate with existing classes that have interfaces that do not match the ones you need.

================================================Components of the Adapter Pattern=====================================
Target Interface: The interface that clients expect.
Adaptee: The existing interface that needs adapting.
Adapter: A class that implements the target interface and translates the requests to the Adaptee.

=======================================================Example Scenario===============================================
Let's consider a scenario where we have a class EuropeanSocket that provides power in 220V format,
and another class AmericanSocket that needs power in 110V format. We need an adapter to allow an American device to work with a European socket.
"""

# Target Interface: The interface that our client expects to work with

class AmericanSocket:
    def proviede_power(self):
        return "110v Power"
    
# Adaptee: the existing class the needs adapting
class EuropeanSocket:
    def provide_power(self):
        return "220v power"
    
    
# Adapter: tje adapter calss that translate the interface

class SocketAdapter:
    def __init__(self, european_socket):
        self.european_socket = european_socket
        
    def provide_power(self):
        power = self.european_socket.provide_power()
        return self.convert_power(power)

    def convert_power(self, power):
        # Simulate the conversion process from 220V to 110V
        if power == "220V power":
            return "110V power"
        return power
    
    
# Client Code: Code that uses the adapter to interact with the adaptee through the target interface.

# Client expects to work with AmericanSocket
def client_code(socket):
    print(f"Client: {socket.provide_power()}")

european_socket = EuropeanSocket()
adapter = SocketAdapter(european_socket)

# The client code works with the adapter as if it was an AmericanSocket
client_code(adapter)
