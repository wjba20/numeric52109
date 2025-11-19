###
## simple_package - Module operations.py
## Basic online calculator
###

## Here I have defined four functions for the four
## basic operations. 
##
## 1) You should provide an interface function
##    that will prompt the user for input and
##    call the appropriate function based on the
##    user's input. The interface function should
##    continue to prompt the user for input until
##    the user enters'exit'. 
##
## 2) The interface function should also handle
##    any exceptions that might be thrown by the
##    basic operations functions. If an exception 
##    is thrown,the interface function should print 
##    an error message and continue to prompt the 
##    user for input.
##
## 3) Add other "operations" to the calculator, that
##    involve complicated operations (e.g., 
##    trigonometric functions, logarithms, etc.).
##

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract one number from another."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide one number by another."""
    return a / b

import math

def calculator():
    """
    Interactive calculator interface.
    Prompts the user for an operation until 'exit' is entered.
    Handles errors efficiently.
    """

    print("Welcome to the simple_package calculator!")
    print("Available operations: add, subtract, multiply, divide, sin, cos, log")
    print("Type 'exit' to quit.\n")

    while True:
        op = input("Enter an operation: ").strip().lower()

        if op == "exit":
            print("Goodbye!")
            break

        if op in ["add", "subtract", "multiply", "divide"]:
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                if op == "add":
                    result = add(a, b)
                elif op == "subtract":
                    result = subtract(a, b)
                elif op == "multiply":
                    result = multiply(a, b)
                elif op == "divide":
                    result = divide(a, b)

                print("Result:", result)

            except Exception as e:
                print("Error:", e)

        elif op in ["sin", "cos", "tan", "log", "exp"]:
            try:
                x = float(input("Enter a number: "))

                if op == "sin":
                    result = math.sin(x)
                elif op == "cos":
                    result = math.cos(x)
                elif op == "tan":
                    result = math.tan(x)    
                elif op == "log":
                    result = math.log(x)
                elif op == "exp":
                    result = math.exp(x)    

                print("Result:", result)

            except Exception as e:
                print("Error:", e)

        else:
            print("Unknown operation. Please try again.")

