# Task 2 - Time Calculator 
# 
# Your task is to write code for a range of calculation on times.
# Times should be stored and inputted as strings in the format DD:HH:MM.  
# Days, Hours and Minutes should be stored as integers.
# 1.	Add a new file called TimeCalculator.py  and make it your start up file.
# 2.	Input two day-time strings from the user.
# Your code will do calculations until the user selects option 9 (see below).
# 3.	Print a main menu:  
#  
# 4.	Save and run.  
# Tip: there are several ways you can write code for this task. 
# You can use the split() function to split the string into a List and process the day, hour 	and the minute components.
# You may also want to investigate the mod operator (%) to find remainder of a division. 
# To get the integer part of a float, you may cast it to integer. For example: 	
# print(25/24)				         1.0416667
# print(int(27/24))		    1
# print (27 % 24)		      3
# 

while True:
    menu = {1: "Add 2 times", 2: "Find the difference between two times", 3: "Convert to hours", 4: "Convert to minutes", 5: "Convert minutes to time", 6: "Convery hours to time", 7: "Convert days to time", 8: "Exit"}

    print("1 >>> Add 2 times")
    print("2 >>> Find the difference between two times")
    print("3 >>> Convert datetime to hours")
    print("4 >>> Convert datetime to minutes")
    print("5 >>> Convert minutes to date-time")
    print("6 >>> Convery hours to date-time")
    print("")
    print("8 >>> Exit")
    print("")


    user_selection = int(input("Please enter a slection from the above menu: "))

    if user_selection == 1:
        print("You have selected option 1.")
        user_time_1 = input("Please enter a time in the format 'DD:HH:MM', where DD = number of days, HH = number of hours, and MM = number of minutes: ")
        user_time_2 = input("Please enter a second time in the format 'DD:HH:MM', where DD = number of days, HH = number of hours, and MM = number of minutes: ")


    elif user_selection == 2:
        print("You have selected option 2: Add 2 times.")
        user_time_1 = input("Please enter a time in the format 'DD:HH:MM', where DD = number of days, HH = number of hours, and MM = number of minutes: ")
        user_time_2 = input("Please enter a second time in the format 'DD:HH:MM', where DD = number of days, HH = number of hours, and MM = number of minutes: ")

    elif user_selection == 3:
        print("You have selected option 3: Find the difference between two times.")
        user_time_1 = input("Please enter a time in the format 'DD:HH:MM', where DD = number of days, HH = number of hours, and MM = number of minutes: ")
        

    elif user_selection == 4:
        print("You have selected option 4.")
        user_time_1 = input("Please enter a time in the format 'DD:HH:MM', where DD = number of days, HH = number of hours, and MM = number of minutes: ")

    elif user_selection == 5:
        print("You have selected option 5.")
        user_minutes = int(input("Please enter the number of minutes: "))



    elif user_selection == 6:
        print("You have selected option 6.")
        user_hours = int(input("Please enter the number of hours: "))
        DD = user_hours // 24
        HH = user_hours % 24
        MM = "00"
        if DD < 10:
            DD = "0" + str(DD)
        if HH < 10:
            HH = "0" + str(HH)
        print(f"{user_hours} in the format 'DD:HH:MM' is {DD}:{HH}:{MM}")
        break
    #elif user_selection == 7:
    

    elif user_selection == 8:
        print("you have chosen to exit. Good bye.")
        break

    else:
        print("You have entered an in valid option. Pleae try again or select 8 to exit.")
        print("")






      
























#import datetime
#import time

#x = datetime.datetime.now().strftime("%d:%H:%M")
#print(x)

#y = time.time()
#print(y)

#z = datetime.time()
#print(z)
