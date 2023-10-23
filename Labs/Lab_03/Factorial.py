# LAB 3

#Task 2 - Factorial  
#1.	Add a new file: Factorial.py and make it the startup file.  
#2.	Ask the user to input an integer.
#3.	Display the number's factorial using a while loop. 
#Note: the factorial of a number is that number multiplied by all the preceding numbers.
#			The factorial of 5 is =  5 x 4 x 3 x 2 x 1 = 120  
#		or if you like = 1 x 2 x 3 x 4 x 5
#4.	Save and run.


user_integer = int(input("Please enter an integer: "))

fact = 1

while user_integer > 1:
    fact *= user_integer
    user_integer -= 1

print(f"The factorial of {user_integer} is {fact}.")



# Task 2 - Factorial  
# 1.	Add a new file: Factorial.py and make it the startup file.  
# 2.	Inputs an integer.
# 3.	Display the number's factorial.
# Tip: the factorial of a number is that number multiplied by all the preceding numbers.
# The factorial of 5 is =  5 x 4 x 3 x 2 x 1 = 120  
# or if you like = 1 x 2 x 3 x 4 x 5
# 4.	Save and run.
"""
user_integer = int(input("Please enter an integer: "))
fact = 1
for n in range(1, user_integer+1):
    print(n)
    fact = fact * n
    n += 1

print(f"The factorial of {user_integer} is {fact}.")
"""