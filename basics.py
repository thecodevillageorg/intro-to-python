# variables 
# allow us to save values into memory using a name that we assign
# ex
name = "Ben"
age = 20

print(name)
print(age)

# variable naming rules
# cannot !@#$$%&* except _
_name = "Nelly"
print(_name)

# cannot start with a number
# 3name = "Nelly"
# print(3name)
# cannot start with a keyword - if, else, True, False, class...

# single line comment
# multi-line comment or docstrings
"""
This is multi-line comment
"""
'''
Comment
'''

# Data types
# how we define values, like words or numbers
# integers, floats, booleans, strings
age = 30
price = 5.2
active = True #or False
name = "Ken"

print(type(age))
print(type(price))
print(type(active))
print(type(name))

# user input using input()
# input -> process -> output
name = input("What is your name?")
print(name)

# exercise
# folder Python Day One
# file exercise1.py
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
sum = num1 + num2
print(sum)



# string manipulation
# f string
# .format()