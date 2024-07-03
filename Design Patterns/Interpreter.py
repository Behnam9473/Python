""" 
The Interpreter design pattern is a behavioral design pattern that is used to define
a grammar for a language and provide an interpreter to interpret sentences in that language.
This pattern is particularly useful for designing and implementing domain-specific languages, parsing expressions, and scripting languages.

Components of the Interpreter Design Pattern:
    AbstractExpression: Declares an abstract 'interpret' method that all concrete expressions must implement.
    TerminalExpression: Implements the 'interpret' method for terminal symbols in the grammar.
    NonterminalExpression: Implements the 'interpret' method for nonterminal symbols in the grammar, typically composed of multiple other expressions.
    Context: Contains information that is global to the interpreter and is used during the interpretation process.
    Client: Builds and uses the Abstract Syntax Tree (AST) to interpret sentences. 
    
    
Use Cases:
    Compilers and Interpreters: To parse and interpret programming languages.
    Configuration Files: To interpret custom configuration file formats.
    SQL Parsing: To parse and execute SQL queries.
    Mathematical Expressions: To evaluate mathematical expressions provided as strings.
Benefits:
    Extensibility: Easy to extend the language grammar by adding new expression types.
    Separation of Concerns: Separates parsing logic from execution logic.
Drawbacks:
    Complexity: Can become complex and hard to manage for large grammars.
    Performance: May not be efficient for high-performance requirements due to recursive interpretation.
 
"""

from abc import ABC, abstractmethod

class Expression(ABC):
    @abstractmethod
    def interpret(self) -> int:
        pass

class Number(Expression):
    def __init__(self, value: int):
        self.value = value

    def interpret(self) -> int:
        return self.value

class Add(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self) -> int:
        return self.left.interpret() + self.right.interpret()

class Subtract(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self) -> int:
        return self.left.interpret() - self.right.interpret()

# Example usage:
# The expression (5 + 3) - (2 + 1)

# Creating the AST (Abstract Syntax Tree)
expression = Subtract(
    Add(Number(5), Number(3)),
    Add(Number(2), Number(1))
)

# Interpreting the expression
result = expression.interpret()
print(f"The result of the expression is: {result}")
