name = "Sebastian"
age = 8
print(name,'is',age,'years old')
print(name+'is' + str(age) + 'years old')
print(name+' is ' + str(age) + ' years old')


name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Your name is " + name)
print("Your name is", name)
print(f"Your name is {name} and you are {age}.")
print(type(name))
print(type(age))