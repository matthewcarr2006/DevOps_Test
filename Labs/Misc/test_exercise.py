
import pytest

#####################
"""
def count(sequence, item):
    sum = 0
    for n in sequence:
        if n == item:
            sum += 1
    return sum

def test_count_int():
    assert count([4, 3, 4, 5, 6, 7, 8, 4, 4], 4) == 3
    assert count([8, 4, 6, 1, 0, 5], 0) == 1
    assert count([1,2 ,3 ,4 , 5, 6, 7], 9) == 0
"""

#####################
"""
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

def test_fact():
    assert fact(0) == 1
    assert fact(2) == 2
    assert fact(7) == 540
    assert fact(10) == 3628800
    assert fact(15) == 6227020800

"""

#####################
"""
def list_of_squares(n):
    d=dict()
    for i in range(1,n+1):
        d[i]=i*i
    return d

def test_list_of_squares():
    assert list_of_squares(2) == {1: 1, 2: 4}
    assert list_of_squares(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    assert list_of_squares(20) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
"""

#####################

def vowels(word):
    number_of_vowels = 0
    the_vowels = ["a", "e", "i", "o", "u"]
    for letter in word.lower():
        if letter in the_vowels:
            number_of_vowels += 1
    return number_of_vowels

def test_vowels():
    assert vowels("sebastIan") == 4
    assert vowels("frEya") == 2
    assert vowels("grace & monty") == 3