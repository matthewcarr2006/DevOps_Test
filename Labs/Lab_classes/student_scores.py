# Labs for Writing Classes in Python
# Duration: 30 minutes
# Objective 
# This is a short exercise to practice creating classes that follow the 4 OOP principles.
# Part 1 
# Create a Student class that takes the name and age on creation.
# Create 2 objects of your student class and get the age of one of them.
# Part 2
# With your Student class, make modifications for the class to accept the student’s current class (as in a classroom) on creation.
# Then add a method that takes 3 test scores and calculates the student’s average test score.
# Part 3
# Create 3 classes, A bird parent class and then an Owl and Dodo class.
# Make use of the 4 OOP Principles.





class Student:
    def __init__(self, name, age, current_class_="tbc"):
        self.name = name
        self.age = age
        self.current_class_ = current_class_
        self.test_scores = []

    def add_test_scores(self, score):
        self.test_scores.append(score)

    def calcuate_average(self):
        if len(self.test_scores) > 0:
            return sum(self.test_scores) / len(self.test_scores)
        else: return 0



# Two student objects
student_1 = Student("Sebastian", 8, "4W")
#student_2 = Student("Freya", 6, "Wren")
student_1.add_test_scores(80)
student_1.add_test_scores(93)
student_1.add_test_scores(100)


# Age of a student
print(f"{student_1.name} is {student_1.age} years old.")
average_score = student_1.calcuate_average()
print(average_score)






