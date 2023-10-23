# LAB 3

# Task 3 - Count Vowels    
# 1.	Add a new file: CountVowels.py and make it the startup file.  
# 2.	Inputs a word (a string).
# 3.	Counts how many vowels are in the word.   
# Tip: You can scroll through every character of a string using its index.
# For example, if word =  'hello' then word[0] is the letter h and word[1] is the letter e.
# Use the len() function to find the length of a string. For example, in the above example,  	 len(word) is 5.
# Use simple if statement/s to detect if the character is 'a', 'e', 'i', 'o'  or  'u'.
# Every time you find a vowel you must increase a counter (an integer variable).
# In the next chapter (Lists) you'll discover a much easier way of performing this task.
# 4.	Save and run.

"""
word = input("Give me a word: ")

i = 0
vowel_count = 0
vowels = ["a", "e", "i", "o", "u"]
while i < len(word):
    for vowel in vowels:
        if word[i].lower() == vowel:
            vowel_count = vowel_count + 1
            print(f"Vowel count = {vowel_count}")
    i += 1

print(f"{word} has {len(word)} letters, {vowel_count} of which are vowels.")
"""


# should have used if word[i] in "aeiou"

word = input("Give me a word: ")

i = 0
vowel_count = 0
while i < len(word):
    if word[i].lower() in "aeiou":
        vowel_count = vowel_count + 1
        print(f"Vowel count = {vowel_count}")
    i += 1

print(f"{word} has {len(word)} letters, {vowel_count} of which are vowels.")
