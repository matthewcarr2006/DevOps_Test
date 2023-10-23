# Chapter 06 Labs
# 
# Objective 
# In this lab you'll gain some experience of using a few of Python's inbuilt functions. 
# In this lab you'll write a function for calculating personal tax in UK.
# 
# Instructions
# The rules for simple tax calculation is as follows:
# Personal allowance:		£11,850	 
# 0 to 34,500 			taxed at 20%		
# 34,501 to 150,000 		taxed at 40%		
# Over 150,000 			taxed at 45%		
# 
# Step-by-Step Instructions:
# 1.	Add a new file: tax.py and make it the startup file.
# 2.	Create a function called getIncomeTax()
# 3.	Calculate the income tax based on the simple tax calculation rules as seen above.
# Tip: You'll need to pass the salary to this function. Use a parameter called salary and base your calculations on the value held by the salary parameter.
# 4.	After the calculation is finished you can return the tax amount.
# 5.	In the main part of your code, just below where you defined the function, 
# write code to call getIncomeTax() and print the returned value. 
# To test your code, pass different values to the function to test its functionality.


def getIncomeTax(salary):
    
    personal_allowance = 11850
    band_a_limit = 34500
    band_b_limit = 150000


    if salary <= personal_allowance:
        return 0
    elif salary <= band_a_limit:
        return (salary - personal_allowance) * 0.2
    elif salary <= band_b_limit:
        return ((band_a_limit - personal_allowance) * 0.2) + ((salary - band_a_limit) * 0.4)
    else: 
        #salary > 150000:
         return ((band_a_limit - personal_allowance) * 0.2) + ((band_b_limit - band_a_limit) * 0.4)   + ((salary - band_b_limit) * 0.45)
    
salary = int(input("Please enter a salary to calculate the required tax: "))
income_tax = getIncomeTax(salary)

print(f"The calculated income tax on {salary} is: {income_tax}")
