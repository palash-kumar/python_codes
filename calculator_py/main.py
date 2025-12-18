from functions.arethmatic import Arethmatic
import re
import math
import sympy as sp


arith = Arethmatic()

arithSwitcher = {
        "+": arith.add,
        "-": arith.subtract,
        "*": arith.multiply,
        "/": arith.divide,
        "^": arith.power,
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "log": math.log10,
        "ln": math.log,
        "sqrt": math.sqrt
    }

def to_radians(angle, mode):
    if mode == "d":
        return math.radians(angle)
    return angle

while True:
    print("----- Calculator -----")
    print("Select operation:")
    print(" + - * / ^ ")
    print(" log ln sqrt")
    print(" sin cos tan ")
    print(" Type 'exit' to quit the calculator.")
    print(" ")
    try:
        mode = input("Select operation: ").strip().lower()

        operation_func = arithSwitcher.get(mode)
        if mode in ["sin", "cos", "tan", ]:
            angleValue = input("Enter value: ").strip()
            if not angleValue.isdigit() and not re.match(r'^-?\d+(\.\d+)?$', angleValue):
                print("Invalid input. Please enter a valid number.")
                continue

            angleValue = to_radians(float(angleValue), "d")
            result = operation_func(angleValue)
            print(f"The result of {mode}({angleValue}) is: {sp.nsimplify(result)}  ")
            continue
        elif mode in ["log", "ln", "sqrt"]:
            angleValue = input("Enter value: ").strip()
            if not angleValue.isdigit() and not re.match(r'^-?\d+(\.\d+)?$', angleValue):
                print("Invalid input. Please enter a valid number.")
                continue

            angleValue = float(angleValue)
            result = operation_func(angleValue)
            print(f"The result of {mode}({angleValue}) is: {sp.nsimplify(result)}  ")
            continue
        elif mode in ["+", "-", "*", "/", "^"]:
            userInput1 = input("Enter first number: ").strip()
            userInput2 = input("Enter second number: ").strip() 

            """ Check if inputs are number/digit only """
            if not userInput1.isdigit()  or not (userInput2.isdigit()):
                print("Invalid input. Please enter valid numbers.")
                exit()

            """ Convert inputs to float for arithmetic operations """
            input1 = float(userInput1)
            input2 = float(userInput2)

            result = operation_func(input1, input2)
            print(f"= {input1} {mode}({input2}) is: {sp.nsimplify(result)} or ")

        elif mode == "exit":
            break
        else:
            print("Invalid operation entered.")
            continue

    except ValueError:
        print("Invalid input. Please enter a number (1 or 2).") 
