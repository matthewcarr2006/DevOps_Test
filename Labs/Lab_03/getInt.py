# LAB 3

# Task 4 – Input an Integer Between Two Limits

# In this part you'll ask the user to input an#  integer between a minimum and maximum values.
# 	If the user fails to enter an acceptable#  value for three times then you stop asking!# 
# 1.	Add a new file: getInt.py and make it th# e startup file.# 
# 2.	Create two variables for the min and max#  values. # 
# Set two values for these variables such as 1#  and 100.# 
# 3.	Write a while loop that attempts to get # an intege# r from#  the user between the limits # of#  min and max values.
# 4.	If the user has tried three times and fa# ils then # print # None. # 
# If a valid value is entered, just end the lo# op and pr# int it# s valu# e.# 
# 
# Note: None is a valid keyword in Python whic# h stands # for Nu# ll.# 



min_value = 0
max_value = 10

max_attemps = 3
counter = 0

while counter < max_attemps:
    counter = counter + 1
    user_input_value = int(input(f"Please enter an integer between {min_value} and {max_value}: "))
    
    if user_input_value in  range(min_value, max_value):
        print(f"{user_input_value} is a valid integer.") 
        counter = 4
        break
    elif counter == 3:
        print(None)
        break
    else:
        print(f"Try again. You have {max_attemps - counter} remaining attempts.")

    
