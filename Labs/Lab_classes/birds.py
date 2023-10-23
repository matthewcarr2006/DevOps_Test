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


class Bird:
    def __init__(self, name, wingspan):
        self.name = name
        self.wingspan = wingspan

    def fly(self):
        print(f"{self.name} is flying with a wigspan of {self.wingspan} cm.")

    def __str__(self):
        return f"{self.name} ({self.__class__.__name__})"


class Owl(Bird):
    def __init__(self, name, wingspan, nocturnal=True):
        super().__init__(name, wingspan)
        self.nocturnal = nocturnal

    def hoot(self):
        print(f"{self.name} is hooting.")

    def __str__(self):
        return super().__str__() + f" - nocturnal: {self.nocturnal}"


class Dodo(Bird):
    def __init__(self, name, wingspan, extinct=True):
        super().__init__(name, wingspan)
        self.exticnt = extinct

    def __str__(self):
        return super().__str__() + f" - extinct: {self.exticnt}"



bird_1 = Bird("eagle", 20)
bird_2 = Owl("barn owl", 90)
bird_3 = Dodo("the dodo", 100)

bird_1.fly()
print(bird_1)

bird_2.fly()
bird_2.hoot()
print(bird_2)

bird_3.fly()
print(bird_3)

