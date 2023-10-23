# exercise: create 2 files, one called dice.py - write a function that will generate a random number between 1 and 6.
# In the second file, use dice module to simulate throwing 2 dice and print it's value.

from random import randint

def dice_roll():
    dice_result = randint(1,6)
    return int(dice_result)