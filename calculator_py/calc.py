from functions.arethmatic import Arethmatic
import re
import math
import sympy as sp

"""
print("----- Using Arethmatic class from functions/arethmatic.py -----")

userInput0 = input("Enter String number: ")

regex = r'([\+\-\*\/])'

 split user input using regex 
splited = re.split(regex, userInput0)
print(f"splited : {splited}")

# Implement BFODMAS rule
mult = [index for index, value in enumerate(splited) if value == '*'] #splited.index('*') 

print(f"mult : {mult}")

for(index, value) in enumerate(splited):
    print(f"index : {index}  value : {value}")
"""

trigSwitcher = {
        "1": math.sin,
        "2": math.cos,
        "3": math.tan
    }

arith = Arethmatic()

arithSwitcher = {
        "+": arith.add,
        "-": arith.subtract,
        "*": arith.multiply,
        "/": arith.divide,
        "1": math.sin,
        "2": math.cos,
        "3": math.tan
    }

mode = int(input("Select mode:\n1: Basic Calcualtor, \n2: Trigonometric Calculator: si, cos, tan (Enter 1 or 2): "))

if mode == 1:
    userInput1 = input("Enter first number: ")
    userOperation = input("Enter operation (+, -, *, /): ")
    userInput2 = input("Enter second number: ")

    if(userInput1.strip() == "" or userInput2.strip() == ""):
        print("Invalid input. Please enter valid numbers.")
        exit()

    userInput1 = userInput1.replace(" ", "")
    userInput2 = userInput2.replace(" ", "")

    """ Check if inputs are number/digit only """
    if not userInput1.isdigit()  or not (userInput2.isdigit()):
        print("Invalid input. Please enter valid numbers.")
        exit()

    """ Convert inputs to float for arithmetic operations """
    input1 = float(userInput1)
    input2 = float(userInput2)



    operation_func = arithSwitcher.get(userOperation)
    print(f"operation_func : {operation_func}")
    if operation_func:
        try:
            result = operation_func(input1, input2)
            print(f"The result of {input1} {userOperation} {input2} is: {result}")
        except ValueError as e:
            print(e)
    else:
        print("Invalid operation entered.") 

if mode == 2:
    print("Trigonometric Calculator")
    userTrigFunction = input("Enter trigonometric function (1 = sin, 2 = cos, 3 = tan): ").strip().lower()
    angleMode = input("Enter angle (d = deg / r = rad) default = r : ").strip()
    angleValue = input("Enter angle value: ").strip()

    if not angleValue.isdigit() and not re.match(r'^-?\d+(\.\d+)?$', angleValue):
        print("Invalid input. Please enter angle value in numbers.")
        exit()


    if(angleMode == "d" or angleMode == "D" or angleMode == "deg" or angleMode == "Deg"):
        angleValue = math.radians(float(angleValue))
    else:
        angleValue = math.radians(float(angleValue))

    trigFunction = trigSwitcher.get(userTrigFunction)
    print(f"operation_func : {trigFunction}")
    
    if trigFunction:
        result = trigFunction(angleValue)
        print(f"The result of {trigFunction}({angleValue}) is: {result} or {sp.nsimplify(result)}")
    else:
        print("Invalid trigonometric function entered.")