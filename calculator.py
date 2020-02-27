#!/usr/bin/env python
"""calculator.py

A working calculator environment."""

__author__ = "Ryan Morehouse"
__license__ = "MIT"

def get_float(msg):
    while(True):
        try:
            arg = (float)(raw_input(msg))
            return arg
        except(ValueError):
            print("Input is invalid, try again.")

def get_operation():
    while(True):
        try:
            operation = raw_input("Please enter operation (+,-,*,/): ")
            if operation in ['+', '-', '*', '/']:
                return operation
            else:
                raise ValueError
        except(ValueError):
            print("Input is invalid. Please try again.")

def get_result(arg1, arg2, operation):
    if(operation == '+'):
        return (arg1 + arg2)
    elif(operation == '-'):
        return (arg1 - arg2)
    elif(operation == '*'):
        return (arg1 * arg2)
    elif(operation == '/'):
        return (arg1 / arg2)
    else:
        return "ERROR"

def main():
    arg1 = get_float("First number: ")
    operation = get_operation()
    arg2 = get_float("Second number: ")
    result = get_result(arg1, arg2, operation)
    print("{} {} {} = {} ".format(arg1, operation, arg2, result))
    

if __name__ == "__main__":
    main()
