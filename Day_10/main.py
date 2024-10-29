import sys
from os import system
from art import logo

def add(n1, n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

function_mapping = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)
    first_number = float(input("What's the first number?"))
    to_continue = True

    while to_continue:
        print("+\n-\n*\n/")
        to_call = input("Pick an operation:\n")
        second_number = float(input("What's the second number?"))
        result= function_mapping[to_call](first_number, second_number)
        print(f"{first_number} {to_call} {second_number} = {result}\n")
        carry_on= input(f"Type 'y'to continue calculating with {result}, type 'n' to start a new calculation, or type any other key to exit the program.").lower()

        if carry_on == "y":
            first_number = result
        elif carry_on == "n":
            to_continue = False
            system("clear")
            calculator()
        else:
            sys.exit(0)

calculator()
        
