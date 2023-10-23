# Functions challenges:
# 
# 1)	Password checker:
# Write a function that has a list with some common passwords as strings (stored as a variable) inside it. Have an input statement that asks the user for a password. If the input matches any string from the list print ‘Use a safer password {password} is compromised’, else print ‘password is safe’. 


def password_cheecker(user_password):

    common_passwords = ["password", "password1", "1231456", "12345", "qwerty", "qwerty1", "54321", "123456789", "qwert123", "1111", "2222", "3333", "4444", "5555", "6666", "7777", "8888", "9999", "0000", "1q2w3e", "qwertyuiop"]

    if user_password.lower() in common_passwords:
        return f"Use a safer password, {user_password} is compromised!"
    else:
        return "Password is safe."



user_password = input("Please input your password: ")

password_status = password_cheecker(user_password)

print(password_status)

