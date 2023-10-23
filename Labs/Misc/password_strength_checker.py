# write an application that checks the strength of a password.
# Requirements:
# 
# Write a class that has a method that checks the password strength.
# Use factors like length, upper/lower case and if it has a number and special character.
# ratings should be very weak - weak - moderate - strong - very strong 
# Check against a list of common passwords 10-20 common password = very weak
# User input that loops until the user quits
# A dictionary that returns a history of passwords/strengths whilst in the loop.

# Write tests to check your code
# Achieve a high score with pylint.

# Code must be pushed to a repo and 1 person per group must share with me. 
# 12.15 deadline


import time

class PasswordStrengthChecker:
    def __init__(self):
        pass

    def strength_test(self):

        password = input("Please enter your password or enter 'quit' to exit: ")

        commom_passwords = ['password', '123456', 'admin', 'qwerty', 'secret', 'letmein', 'dragon', 'baseball', 'football', 'iloveyou', 'password1', 'password2', 'password3', 'password4', 'password5', 'password6', 'password7', 'password8', 'password9', 'password10']
        
        password_length = len(password)

        contains_lower = any(char.islower() for char in password)
        contains_upper = any(char.isupper() for char in password)
        contains_digit = any(char.isdigit() for char in password)
        special_characters = [ "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "=", "{", "}", "[", "]", "|", "\\", ":", ";", "'", '"', "`", "~", "<", ">", ",", ".", "/", "?"]

        #contains_special_character = 
        
        #Could use if not alphanumeric 
        
        
        score = 0

        if password.lower() == "quit":
            return "quit"
        else:
            for char in password:
                if char in special_characters == True:
                    score += 1
                    break
            if contains_upper == True:
                score += 1
            else: score -= 1
            if contains_lower == True:    
                score += 1
            else: score -= 1
            if contains_digit == True:
                score += 1
            else: score -= 1
            if password_length <= 3: 
                score -= 1
            elif password_length <= 5:
                score += 0
            elif password_length <= 8:
                score += 1
            else: score += 2

            print(f"Length = {password_length}")
            print(f"Score = {score}")

        if score <= 0:
            return "Very weak"  
        elif score == 1:
            return "Weak"
        elif score == 2:
            return "Moderate"
        elif score <= 4:
            return "Strong"
        elif score > 4:
            return "Very strong"

while True:

    password_history = {}

    check_password = PasswordStrengthChecker()
    strength = check_password.strength_test()

    if strength == "quit":
        print(f"You have quit. Goodbye.")
        break
    else:
        print(f"Your password is {strength}.")

    