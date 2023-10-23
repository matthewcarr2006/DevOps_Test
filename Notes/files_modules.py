# modules

# modules are just files that we use to extend our functionality.
# We can import existing modules or make our own
# Many modules are built-in and do not require any set-up.
# Some need to be installed - pip

"""
import math # importing the entire module

number = 10

answer = math.sqrt(number) # syntax for feferencing an object from a module.
print(answer)
"""

# Importing everything form math and random
"""
import math
import random

def random_pi():
    return math.ceil(random.randint(1,10) * math.pi)
    # ceil rounds up to nearest whole number

for i in range(5):
    print(random_pi())
"""

# Just with desired objects = saves memory + increases peerformance

"""
from math import pi, ceil , floor
from random import randint

def random_pi():
    return floor(randint(1,10) * pi)

for i in range(1,10):
    print(random_pi())
"""

# Prints math content (not very useful though)
"""
import math
print(dir(math))
"""

# create an __init__.py to initialise a python folder
 

# files
# Read, write, and edit files
# Most file types will work, some will need to import modules

# e.g.
"""
file = open("filename.txt", "mode") # mode can be r (read only), w (write), r+ (read and write), a (append).

file.close() # Must remember to close the file after use. Will close the most recently opened file.
"""


# to read
# open file, tehn we use readline() - reads a line and moves onto the next.
# readlines()/read() - read all lines
# seek() - usefule for making sure we are reading from the beginning.
# seek(0) place us at start of file.

# e.g.
"""
file = open("filename.txt", "r")
print(file.readline()) # printing line 1 moves onto 2
file.readline() # Reads line 2 and moves onto line 3.
print(file.readline()) # print line 3
file.seek(0) # returns to start
print(file.readline()) # printing line 1 moves onto line 2

file.close
"""

"""
file = open("lines.txt", "r")
lines = file.readlines() # store file in our own new variable
print(lines)
file.close
"""

"""
# writing files
file = open("line1.txt", "w")

for n in range(1, 11):
    newline = "this is line " + str(n) + "\n"
    file.write(newline)

file.close()
"""

file = open("line1.txt", "r")

outfile = ""

for line in range(1, 10):
    if line %2 == 0: # even numbers
        outfile += file.readline()
    else:
        file.readline()

file = open("line1.txt", "w")

file.write(outfile)
file.close












