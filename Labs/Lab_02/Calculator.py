# Task 1 - Create a Calculator

number1 = int(input("Enter your first number: "))
number2 = int(input("Enter your second number: "))

calculator_menu = {"Add       ": "+", "Subtract  ": "-", "Multiply  ": "*", "Divide    ": "/", "Square    ": "s"}

"""prints the dictionary row by row"""
print("")
print("Operation  Symbol")
print("-----------------")
for function, symbol in calculator_menu.items():
    print('{} {}'.format(function, symbol))
print("-----------------")

calculatior_function = input("Select the operation symbol you want to perform from the functions available: ")

"""
Executes the chosen calculation
"""
if calculatior_function == "+":
    calculation = number1 + number2 
elif calculatior_function == "-":
    calculation = number1 - number2 
elif calculatior_function == "*":
    calculation = number1 * number2 
elif calculatior_function == "/":
    calculation = number1 / number2 
elif calculatior_function == "s":
    calculation = number1 ** number2  

"""
Print the equation and answer
"""
print(f"{number1} {calculatior_function} {number2} = {calculation}")

