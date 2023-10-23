# Chapter 05 Lab
# 
# Objective 
# In this lab you'll gain some experience of using a few of Python's inbuilt functions. 
# 
# Instructions
# Your task is to present some statistics on the following students' grades that are read from a file.
# 1.	data="100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"
# 2.	Add a new code files to your existing labs project and make it the startup file.
# 3.	Copy the data string above into this file.
# 4.	To extract information from this string, you'll need to split it by ',' as delimiter.
# Put the resulting List into a variable called grades.
# Tip: use the string's split function and pass it ',' as delimiter.
# 5.	Display the minimum value of the grades.
# Tip: use the min() function
# 6.	Display the maximum value of grades.
# Tip: use the max() function
# 7.	Test your code and check if the values are correct.
# Did your code display 100 for the minimum value and 99 for the maximum?
# But how can 100 be a minimum? Any ideas why this is so. 
# Think about this before reading the next step.
# 8.	OK, as you've guessed it, we're dealing with a list of strings who just look like a List of numbers! That is why "100" is less than "17" because the first character '1' is the same but the second character '0' is less than the letter '3'.
# 9.	So, you need to cast every element of a List of strings into a List of integers. This is a common task and a hard one to code but the clever Python 3.0 gives us a tool called map to do this task. 
# The map function was not covered in the lectures, so we'll cover this useful function here in this lab.
# Just after splitting the string into a list of strings called grades, type:
# grades = list(map(int, grades))
# This line of code casts grades into a list of ints.
# 10.	Now, run your code again. Does it give the right values for min and max (14 & 100)?
# 11.	Display the average of grades to 2 decimal points.
# Tip: use the sum(), len() and round() functions.
# 12.	Import the statistics library.
# Tip: at the first line of your file type import statistics
# 13.	Use the statistics' mean() function to get the average grade to 2 decimal places.
# Tip: use the statistics.mean() function
# 14.	Display the median values using the statistics.median() function.
# Note: this is not the same as the mean value. Please investigate what a median is if you're not sure.
# 15.	Use the string.format() function to display the min, max,average, mean() and median values.
# 
# *** End ***

import statistics

data = "100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"

grades = data.split(",")
grades = list(map(int, grades))
#grades = [eval(i) for i in grades]
#grades = [int(x) for x in data.split(',')]
#Or use for loop
print(f"Newly formatted list: {grades}")
print("")
min_grade = min(grades)
max_grade = max(grades)
print(f"The minimum grade value is {(min_grade)}")
print(f"The maximum grade value is {(max_grade)}")
print("")
grade_average = round(sum(grades) / len(grades),2)
print(f"The grade average for the data set is {grade_average}")
print("")
grade_mean = round(statistics.mean(grades),2)
print(f"The mean of the grades data set is {grade_mean}")
print("")
grade_median = int(statistics.median(grades))
print(f"The median of the grades data set is {grade_median}")
print("")
print("Step 15")
min_grade = ">> The minimum grade value is: {min_grade}".format(min_grade = min_grade)
print(min_grade)
max_grade = ">> The maximum grade value is: {max_grade}".format(max_grade = max_grade)
print(max_grade)
grade_average = ">> The average grade value of the data set is: {grade_average}".format(grade_average = grade_average)
print(grade_average)
grade_mean = ">> The mean grade value of the data set is: {grade_mean}".format(grade_mean = grade_mean)
print(max_grade)
grade_median = ">> The median grade value of the data set is: {grade_median}".format(grade_median = grade_median)
print(grade_median)
print("")