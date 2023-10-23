# LAB 3

# Task1 - Squares
#1.	Add a new file: Squares.py to your existing Solution and make it the startup file. 
#2.	Write a while loop that starts at 1 and ends at 100.  
#3.	Calculates and display each number and its square.  
#4.	End the loop if that square is bigger than 2000.  
#5.	Save and run.  

i = 1
while i <= 100:
    square_calculation = i**2
    if square_calculation > 2000:
        break
    print(f"{i} squared = {square_calculation}")
    i += 1


"""
for i in range(1,101):
    calculation = i**2
    if calculation > 2000:
        break
    print(f"{i} squared = {calculation}")
"""