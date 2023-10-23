# LAB 3
#
# Task 3 - Investment 
# 1.	Add a new file: Investment.py and make it the startup file.  
# 2.	Calculates how many years it will take an initial investment of £100 to grow to a target value of £1000 if the interest rate is 10%.
# Tip: Do not start writing code until you've a plan of action!
# 3.	Save and run.   
# 
# 4.	Make your calculation more usable by inputting the following values:
#	Initial investment  
#   Target value  
#   Interest rate  
# 5.	Save and run.   


initial_investment_GBP = int(input("Please enter your planned initial investment in GBP: "))
target_value_GBP = int(input("Please enter your target value in GBP: "))
interest_rate = 0.1

investment_GBP = initial_investment_GBP
year = 0

while investment_GBP <= target_value_GBP:
    year += 1
    investment_GBP = investment_GBP * (interest_rate + 1)
    print (f"year {year}: {investment_GBP}")

print(f"Your initial investment of £{initial_investment_GBP} will reach £{target_value_GBP} after interest is calculated at year {year} (based on interest paid on the anniversary of your inestment each year with no further investemnt contributed).")