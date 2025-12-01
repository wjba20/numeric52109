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

import math

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


# Task 3: Add advanced mathematical functions
def power(a, b):
    """Raise a to the power of b."""
    return a ** b

def square_root(a):
    """Calculate the square root of a number."""
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(a)

def logarithm(a, base=10):
    """Calculate logarithm of a number with specified base."""
    if a <= 0:
        raise ValueError("Logarithm input must be positive")
    if base <= 0 or base == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1")
    return math.log(a, base)

def sine(angle_degrees):
    """Calculate sine of an angle in degrees."""
    return math.sin(math.radians(angle_degrees))

def cosine(angle_degrees):
    """Calculate cosine of an angle in degrees."""
    return math.cos(math.radians(angle_degrees))

def tangent(angle_degrees):
    """Calculate tangent of an angle in degrees."""
    return math.tan(math.radians(angle_degrees))

def factorial(a):
    """Calculate factorial of a non-negative integer."""
    if a < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if not isinstance(a, int):
        raise ValueError("Factorial is only defined for integers")
    return math.factorial(a)


# Task 1 & 2: Interface function with error handling
def calculator_interface():
    """
    Interactive calculator interface.
    
    Provides a user-friendly command-line interface for mathematical operations.
    Continues until user enters 'exit'.
    """
    
    print("Welcome to the Simple Calculator!")
    print("Available operations:")
    print("  + : Addition")
    print("  - : Subtraction")
    print("  * : Multiplication")
    print("  / : Division")
    print("  ^ : Power")
    print("  sqrt : Square Root")
    print("  log : Logarithm (base 10)")
    print("  ln : Natural Logarithm")
    print("  sin : Sine (degrees)")
    print("  cos : Cosine (degrees)")
    print("  tan : Tangent (degrees)")
    print("  ! : Factorial")
    print("  exit : Quit the calculator")
    print()
    
    while True:
        try:
            # Get operation from user
            operation = input("Enter operation (or 'exit' to quit): ").strip().lower()
            
            if operation == 'exit':
                print("Thank you for using the calculator. Goodbye!")
                break
            
            # Handle single-argument operations
            if operation in ['sqrt', '!']:
                num = float(input("Enter number: "))
                
                if operation == 'sqrt':
                    result = square_root(num)
                    print(f"√{num} = {result}")
                elif operation == '!':
                    result = factorial(int(num))
                    print(f"{int(num)}! = {result}")
            
            # Handle two-argument operations
            elif operation in ['+', '-', '*', '/', '^', 'log', 'ln']:
                num1 = float(input("Enter first number: "))
                
                if operation in ['log', 'ln']:
                    if operation == 'log':
                        result = logarithm(num1)
                        print(f"log₁₀({num1}) = {result}")
                    else:  # ln
                        result = logarithm(num1, math.e)
                        print(f"ln({num1}) = {result}")
                else:
                    num2 = float(input("Enter second number: "))
                    
                    if operation == '+':
                        result = add(num1, num2)
                        print(f"{num1} + {num2} = {result}")
                    elif operation == '-':
                        result = subtract(num1, num2)
                        print(f"{num1} - {num2} = {result}")
                    elif operation == '*':
                        result = multiply(num1, num2)
                        print(f"{num1} * {num2} = {result}")
                    elif operation == '/':
                        result = divide(num1, num2)
                        print(f"{num1} / {num2} = {result}")
                    elif operation == '^':
                        result = power(num1, num2)
                        print(f"{num1} ^ {num2} = {result}")
            
            # Handle trigonometric functions
            elif operation in ['sin', 'cos', 'tan']:
                angle = float(input("Enter angle in degrees: "))
                
                if operation == 'sin':
                    result = sine(angle)
                    print(f"sin({angle}°) = {result}")
                elif operation == 'cos':
                    result = cosine(angle)
                    print(f"cos({angle}°) = {result}")
                elif operation == 'tan':
                    result = tangent(angle)
                    print(f"tan({angle}°) = {result}")
            
            else:
                print("Error: Unknown operation. Please try again.")
                continue
                
            print()  # Empty line for readability
            
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again with valid numbers.\n")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
            print("Please try again with a non-zero divisor.\n")
        except OverflowError:
            print("Error: Result too large to calculate.")
            print("Please try again with smaller numbers.\n")
        except Exception as e:
            print(f"Unexpected error: {e}")
            print("Please try again.\n")

# Example usage when module is run directly
if __name__ == "__main__":
    calculator_interface()