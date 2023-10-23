# LAB3

# Task 5 - Exam Average  
# 1.	Add a new file: ExamAverage.py and make it the startup file.  
# 2.	Code a program that:  
# a.	Has code to calculate the average of three exam marks  
# b.	If the average mark is: o >= 65 output a "Pass" 
# c.	If it is  < 65 output a "Fail"  
# 3.	In the main body of the program input the marks for a student for Math, English and ICT exams.    
# 4.	Marks should be an integer between 0 and 100. 
# a.	Use a for loop until the user enters a valid mark.
# b.	Calculate and display their average mark and overall result.  
# c.	Please also display the average mark and print out the average.
# 5.	Save and run.  



################## NEED TOP ADD MATHS, ENGLISH AND ICT!!!!!!!!!!!!!!!!!!! >>> USE DICTIONARY


exam_marks = []

mark_count = 0
sum_of_results = 0
max_mark = 100
min_mark = 0

while mark_count < 3:
    exam_mark = int(input(f"Enter an exam mark between {min_mark} and {max_mark}, inclusive: "))
    if exam_mark in range(min_mark, max_mark+1):
        exam_marks.append(exam_mark)
        mark_count += 1
        sum_of_results = exam_mark + sum_of_results
        print(f"Exam {mark_count} is {exam_mark}.")
    else: print("Please enter a valid mark between 0 and 100, inculsive.")

exam_average = sum_of_results/(mark_count)

print(f"The average of your exam marks {exam_marks} is: {exam_average}")


FINISH
