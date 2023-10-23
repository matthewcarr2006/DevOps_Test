# classes is part of OOP (object orientated programming)

# key concepts:
# class = a blueprint of attribute (vars/args) and methods (functions) we can use against an object of a class/
# object = this is an instance of a class

# methods = functions internal to a class
# allows us to easily make multiple objects of teh same type.

"""
class Dog: # creates a class called Dog
    energy = "high" # setting an attribute for the class

    def speak(self): # creating a method (like a function)
        print("bark")

fido = Dog() # sets an object of the class called fido
sienna = Dog()

fido.energy = "low" # setting attribute value (no longer default)

print(fido.energy)
print(sienna.energy) # remains high from class

fido.speak()
"""
#################################################################################

"""
class  Students():
    pass


student_1 = Students()
student_2 = Students()

print(student_1)
print(student_2)

student_1.first = "Sebastian"
student_1.last = "Carr"
student_1.age = 8

print(student_1.first, student_1.last)
print(student_1.age)

student_2.first = "Freya"
student_2.last = "Carr"
student_2.age = 6

print(student_2.first, student_2.last)
print(student_2.age)
"""

"""
class Student:
                                        # 'self' refers to the object itself
    def __init__(self, first, last, age): # __ indicates a background task __
        self.frst = first # init method initialises teh object with these attributes
        self.last = last # refers to the object itself
        self.age = age # self maps the class data to the object


student_1 = Student("Sebastian", "Carr", 8)
student_2 = Student("Freya", "Carr", 6)

#print(student_1.first, student_2.first)
"""


"""
class Student:
                                        # 'self' refers to the object itself
    def __init__(self, first, last, age): # __ indicates a background task __
        self.frst = first # init method initialises teh object with these attributes
        self.last = last # refers to the object itself
        self.age = age # self maps the class data to the object
        self.full = first + " " + last

student_1 = Student("Sebastian", "Carr", 8)
student_2 = Student("Freya", "Carr", 6)

print(student_1.full)
"""

"""
# as a method
class Student:
                                        # 'self' refers to the object itself
    def __init__(self, first, last, age): # __ indicates a background task __
        self.first = first # init method initialises teh object with these attributes
        self.last = last # refers to the object itself
        self.age = age # self maps the class data to the object
        
    def fullName(self):
        return(self.first + " " + self.last)


student_1 = Student("Sebastian", "Carr", 8)
student_2 = Student("Freya", "Carr", 6)

print(student_1.fullName())
# or
print(Student.fullName(student_2))
"""

"""
# Change an attribute with a method
class Student:
                                        # 'self' refers to the object itself
    def __init__(self, first, last, age): # __ indicates a background task __
        self.first = first # init method initialises teh object with these attributes
        self.last = last # refers to the object itself
        self.age = age # self maps the class data to the object

    def fullName(self):
        return(self.first + " " + self.last)

    def change_age(self):
        self.age = int(self.age + 1)


student_1 = Student("Sebastian", "Carr", 8)
student_2 = Student("Freya", "Carr", 6)

print(student_1.age, student_2.age)

student_1.change_age()
student_2.change_age()

print(student_1.age, student_2.age)
"""

"""
# self-class variables
class Student:

    age_increase_amount = 25
                                        # 'self' refers to the object itself
    def __init__(self, first, last, age): # __ indicates a background task __
        self.first = first # init method initialises teh object with these attributes
        self.last = last # refers to the object itself
        self.age = age # self maps the class data to the object

    def fullName(self):
        return(self.first + " " + self.last)

    def change_age(self):
        self.age = int(self.age + self.age_increase_amount)

student_1 = Student("Sebastian", "Carr", 8)
student_2 = Student("Freya", "Carr", 6)

#print(student_1.age)
#student_1.change_age()
#print(student_1.age)

print(student_1.age_increase_amount)
print(student_2.age_increase_amount)


# __dict__

print(student_1.__dict__)
print(student_2.__dict__)
print(Student.__dict__)

# change the variable
Student.age_increase_amount = 20

print(Student.__dict__)

student_1.age_increase_amount = 10
student_1.change_age()

print(student_1.age)
print(student_1.__dict__)
print(student_2.__dict__)
"""

"""
# non self class variable

class Student:

    age_increase_amount = 25
    num_of_students = 0

                                        # 'self' refers to the object itself
    def __init__(self, first, last, age): # __ indicates a background task __
        self.first = first # init method initialises teh object with these attributes
        self.last = last # refers to the object itself
        self.age = age # self maps the class data to the object

        Student.num_of_students += 1        

    def fullName(self):
        return(self.first + " " + self.last)

    def change_age(self):
        self.age = int(self.age + self.age_increase_amount)

print(Student.num_of_students)
student_1 = Student("Sebastian", "Carr", 8)
print(Student.num_of_students)
student_2 = Student("Freya", "Carr", 6)
print(Student.num_of_students)
"""


# parent class
"""
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        print(f"{self.name} is eating.")

#child class of animal

class Cat(Animal): # inheriting from animal
    def __init__(self, name, species, breed):
        super().__init__(name, species) # super(parent) attributes 
        self.breed = breed

    def meaow(self):
        print("meow")


my_cat = Cat("Smudge", "cat", "tabby")

my_cat.meaow()
my_cat.eat()

print(my_cat)
"""


# string method
"""
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        print(f"{self.name} is eating.")

    def __str__(self):
        return f"{self.name} {self.species}"
    

class Cat1(Animal): # inheriting from animal
    def __init__(self, name, species, breed):
        super().__init__(name, species) # super(parent) attributes 
        self.breed = breed

    def meaow(self):
        print("meow")

    def __str__(self):
        return f"{self.name}, {self.species}, {self.breed}"
    
my_cat1 = Cat1("Smudge", "cat", "tabby")

print(my_cat1)
"""



# __ attribute is only accesible when calling with the class name
# access by _classname__attribute name
# trailing_ it's a way of using python keywords
# _leading underscore = idicates an attribute is private


class Feline:
    __family = "something"

cat3 = Feline()

print(cat3.__Feline.__family)
