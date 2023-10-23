# Task 1 - Count Vowels    
# 1.	Add a new file: CountVowels.py and make it the startup file.  
# 2.	Inputs a word (a string).
# 3.	Counts how many vowels are in the word.   
# Tip: You can scroll through every character of a string in the same way as you do with 	numbers in a range() function. 
# Use a simple if statement/s to detect if the character is 'a', 'e', 'i' 'o’ or  'u'
# Every time you find a vowel you must increase a counter (an integer variable)
# Or (better), you may consider using the 'in' keyword.
# 4.	Save and run.


word = input("Give me a word: ")
vowels = "aeiou"
vowel_counter = 0

for letter in word:
    if letter.lower() in vowels:
        vowel_counter += 1

print(f"There are {len(word)} letters in {word}, {vowel_counter} or which are vowels.")