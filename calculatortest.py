"""
do_setup()
while exit_condition_not_reached:
    input = consume_input()
    output = evaluate_input(input)
    print(output)


USE .split()

# No setup
repeat forever:
    read input
    tokenize input
    if the first token is "q":
        quit
    else:
        decide which math function to call based on first token

"""

from arithmetic import *

while True:
    input_string = input("Enter operator followed by two numbers and seperated by spaces: ") 
    token= input_string.split(" ")

    operator = token[0]

    num1= token[1]
    num2 = token[2]


    if operator == "+":
        result = (add(float(num1)), float(num2))

    elif operator == "-":
        result = (subtract(float(num1)), float(num2))

    elif operator == "*":
        result = (multiply(float(num1)), float(num2))

    elif operator == "/":
        result = (divide(float(num1)), float(num2))

    elif operator == "square":
        result = (square(float(num1)))

    elif operator == "cube":
        result = (cube(float(num1)))

    elif operator == "power":
        result = (power(float(num1), float(num2)))

    elif operator == "mod":
        result = (mod(float(num1), float(num2)))

    else:
        operator == "q"
        break

print(result)