#!/usr/bin/env python
"""simple_calculator.py

A simple working calculator environment.

If whole numbers are used, the equation will be evaluated
as integer only arithmetic. If decimal places are added,
the equation will be evaluated using real numbers.

Type 'quit' or 'exit' to quit execution."""

__author__ = "Ryan Morehouse"
__license__ = "MIT"

import parser

def get_equation():
    equation = raw_input(">")
    return equation


def calculate(equation):
    try:
        code = parser.expr(equation).compile()
        print eval(code)
    except:
        print("Syntax error.")

def main():
    quit_cmds = ["quit", "exit"] 
    print("Type 'quit' or 'exit' to quit simple calculator.")
    flag = True
    while(flag):
        equation = get_equation()
        if any(x in equation for x in quit_cmds):
            flag = False
        else:
            calculate(equation)
    

if __name__ == "__main__":
    main()
