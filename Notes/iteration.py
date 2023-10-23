# iteration is anotehr word for loops, repeating blocks of code over and over.
# saves time without having to write our code multiple times.

# 2 types of loops:
# while loops
# for loops


# while loops
# a while loop will constantly execute code wjilst a condition 
# or when another condition is met.
# if a condition is never true the while loop will never start.
"""
print(1)
print(2)
print(3)

x = 0
while x <= 100:
    print(x)
    x += 10 # same as x= x + 1
"""

# break
"""
i = 1

while i < 6:
    if i == 3:
        break
    print(i)
    i += 1
"""

# continue
"""
j = 0

while j < 6:
    j += 1
    if j == 3:
        continue # will ignore 3 and continue with the loop without movinbg to print(j)
    print(j)
"""
"""
k = 1

while k < 6:
    print(k)
    k += 1
else:
    print("k is no longer less than 6")
"""
"""
while True:
    name = input("Enter your name: ")
    if name == "quit":
        print("You have succesfully quit.")
        break
    else:
        print(f"Hello {name}")
"""



# for loops
# a for loop will iterate over any iterable collection: lists/strings/dictionaries/etc...
# useful for when we want to use data from a collection.
# Do things to a individual items in a collection.

# iterating through lists
"""
my_fruits = ["apple", "orange", "pear"]

for fruits in my_fruits:
    print(fruits)
"""

"""
numbers = [1, 2, 3, 4, 5, 6]

for number in numbers:
    print(number)

l = 0
while l < len(numbers):
    print(numbers[l])
    l += 1
"""


# range
"""
for a in range(5):
    print(a) # 0, 1, 2, 3, 4 (doesn't include 5)

for a in range(1,5):
    print(a) # 1, 2, 3, 4

for a in range(1, 10, 2): # start at 1, up to 10-1, steps of 2)
    print(a) # 1-9 steps of 2
"""

# strings
"""
for letter in "hello":
    print(letter)

for word in "hello world".split():
    print(word)
"""

# list comprehension
"""
result = [x**2 for x in range(5)]
print(result)

# the same as but faster and neater than:
results = []
for x in range(5):
    results.append(x**2)
    print(results)
"""


# dictionaries
"""
for i in {"drink": "wine", "drink2": "milkshake"}:
    print(i)

for i in {"food": "jam", "food2": "cake"}.values():
    print(i)

for i in {"shape": "square", "shape2": "circle"}.items():
    print(i)
"""

# break and continue
"""
for i in range(10):
    if i == 5:
        continue
    print(i)
"""
"""
for i in range(10):
    print(i)
    if i == 5:
        break
"""

# nested loops
"""
for i in range(1,3):
    for j in range(1,4):
        print(i, "x", j, "=", i*j)
"""



# write a while loop that asks for the names of five people.
# for each person print out their name, followed by some text
# "is awsome!"
# counter + while loop, an input, a print, a +=1.

#result = [x**2 for x in range(5)]
"""
names = [input("What is your name? ") for name in range(5)]
for name in names: print(f"{name} is awesome!")

i = 0
while i < 5:
    name = input("what is your name? ")
    print(f"{name} is awesome!")
    i += 1

for i in range(5):
    name = input("what is your name? ")
    print(f"{name} is awesome!")
"""

for name in [input("What is your name? ") for name in range(5)]: print(f"{name} is awesome!")
# or
#[print(f"{name} is awesome!") for name in [input("enter a name: ") for x in range(5)]]


# task 5 use a while loop, not a for loop



# Exercise 1: Fibonacci Series
# Write a program to generate the Fibonacci series up to a given number "n" using a for loop.




# Exercise 2: Prime numbers
# Write a program to print all prime numbers within a given range (start and end) using a for loop.

# Exercise 3: Perfect Numbers
# Write a program to find all perfect numbers within a given range (start and end) using a for loop.
# A perfect number is a positive integer that is equal to the sum of its proper divisors. ie 6 has proper
# divisors of 1, 2 and 3 (not 5 or 6), and 1 + 2 + 3 = 6, so 6 is a perfect number. 8 has proper divisors of 1, 2
# and 4. 1 + 2 + 4 is 7, so 8 is not a perfect number. 

# Exercise 4 : Multiplication Table
# Write a program to generate the multiplication table for a 
# given number (n) up to a certain limit (limit) using a for loop.





