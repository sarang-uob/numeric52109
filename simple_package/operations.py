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

#Adding the interface function (can be called from test_sp.py as sp.operations.interface())
def interface():
    """Interface function"""
    while True: #makes sure that the function continues to ask user untill 'exit' is entered
        user_input = input("Enter operation (add, subtract, multiply, divide) or 'exit' to quit: ")
        if user_input == 'exit':
            break
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            if user_input == 'add':
                print(f"Result: {add(a, b)}")
            elif user_input == 'subtract':
                print(f"Result: {subtract(a, b)}")
            elif user_input == 'multiply':
                print(f"Result: {multiply(a, b)}")
            elif user_input == 'divide':
                print(f"Result: {divide(a, b)}")
            else:
                print("Invalid operation. Please try again.")
        except Exception as e:
            print(f"Error: {e}. Please try again.")