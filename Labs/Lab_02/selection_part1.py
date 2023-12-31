# part 1
# objective = In this lab you'll gain the experience of using conditional if…elif control flow statements in Python. 

# Steps 
# 1.	Add a new code page to your project. Call it selection_part1
# 2.	Create an IF statement to see if the person is equal 18 or over. 
# a.	Display 'You are in category A' 
# 3.	Create an IF statement to see if the person is equal 16 or over.
# a.	Display 'You are in category B' 
# 4.	Create another IF statement to see if the person is under 16 years of age.
# a.	Display 'You are in category C' 
# 5.	Save and run your code and enter 19 for age.
# 6.	As you see, there are too many confusing messages!
# Simple IF statements work fine but not in a chain of IF statements such as these.

age = int(input("Please enter our age: "))

"""
Displays confusing massages becuase anyone over 18 will fall into categories A and B 
"""
print("Displays confusing massages becuase anyone over 18 will fall into categories A and B:")
if age >= 18: print(f"You are in category A")
if age >= 16: print("You are in category B")
if age < 16: print("You are in category C")


"""
All ages can only fit into one category 
"""
print("")
print("All ages can only fit into one category:")
if age >= 18:
    print("You are in category A")
elif age >= 16:
    print("You are in category B")
else:
    print("You are in category C")