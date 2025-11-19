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

#Adding the interface function (can be called from test_sp.py as sp.operations.interface())
#add all the functions defined above in the interface function

def interface():
    #modify this to have a loist of operations too so that if wrong operation is entered 
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
            #add other functions here as elif statements
            elif user_input == 'logarithm':
                print(f"Result: {logarithm(a, b)}")
            elif user_input == 'sine':
                print(f"Result: {sine(a)}")
            elif user_input == 'cosine':
                print(f"Result: {cosine(a)}")
            elif user_input == 'tangent':
                print(f"Result: {tangent(a)}")
            elif user_input == 'power':
                print(f"Result: {power(a, b)}")
            elif user_input == 'square_root':
                print(f"Result: {square_root(a)}")
            elif user_input == 'factorial':
                print(f"Result: {factorial(int(a))}") #factorial only takes integers
            else:
                print("The operation is not recognized. Please try again!")
        except Exception as e:
            print(f"Error: {e}. Please try again.")

#Adding other functions to the operations module
def logarithm(a, base=10):
    """Calculate logarithm of a number with given base."""
    return math.log(a, base)
def sine(a):
    """Calculate sine of a number (in radians)."""
    return math.sin(a)
def cosine(a):
    """Calculate cosine of a number (in radians)."""
    return math.cos(a)
def tangent(a):
    """Calculate tangent of a number (in radians)."""
    return math.tan(a)  
def power(a, b):
    """Calculate a raised to the power of b."""
    return math.pow(a, b)
def square_root(a):
    """Calculate square root of a number."""
    return math.sqrt(a)
def factorial(a):
    """Calculate factorial of a number."""
    return math.factorial(a)



if __name__ == '__main__':
    '''This code snipped runs when the script is executed directly. (For testing purposes)'''
    interface()