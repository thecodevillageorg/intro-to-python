"""
variables and keywords
-Variables allow us to save values into memory using a name that we assign. This allows us to use those values later 

variable naming rules
-Variable names can contain only letters, underscores and numbers; however, they cannot start with a number
-Variable names cannot contain python keywords - if, else, True, False, class, def
""" 
# ex:
name = "Ben" # declaration - giving a variable a value
age = 20
year = "2020"

print(name)
print(age)


"""
Handling Naming Errors
- All programmers make mistakes, so it’s not a problem if you run into errors. It just comes
with the job. Let’s look at a common mistake that occurs with variables:
>>> Sport = 'baseball'    # capital 'S'
>>> print(sport)          # lowercase 'S'
If we try to run this code, we’ll get the following error/output:
NameError: name 'sport' is not defined
This is because the names are completely different. We referenced a variable with a
lowercase “s” but declared one with capital “S.” To fix this we would capitalize the “s” in
sport within print.
"""

"""
Integer and Float Variables

To store an integer or float in a variable, we give a name to the left of the operator and write
a number on the right side. In the next cell, let’s go ahead and write the following code:
"""
# ex:
num1 = 5           # storing an integer into a variable
num2 = 8.4         # storing a float into a variable
print(num1, num2)  # you can print multiple items using commas

"""
Boolean Variables
The boolean data type is either a True or False value. Think of it like a switch, where it’s
either off or on. It can’t be assigned any other value except for True or False. Booleans
are a key data type, as they provide several uses. One of the most common is for tracking
whether something occurred.
"""
# ex:
switch = True
print(switch)

"""
Strings are nothing more than a set of characters, symbols, numbers, whitespace, and even empty space between two
sets of quotation marks. In Python we can use either single or double quotes to create
a string. Most of the time it’s personal preference, unless you want to include quotes
within a string. Whatever is wrapped inside of the quotation
marks will be considered a string, even if it’s a number. 
"""
# ex:
print(" ")
print("There's a snake in my boot!")
print('True')
# Note : The output will include an empty line at the top, as we print out nothing in the first statement.

"""
Using Multiple Variables
In almost any program you’ll write, you’re going to need to perform some calculations or
manipulation on variables. In the following code, we access the values from previously
declared variables and add them together to create a sum
"""
# ex:
# using two variables to create another variable
result = num1 + num2
print(result)


"""
Using Operators on Numerical Variables
Think of Python as a calculator, where we can alter any variables we want. In the
following code, we alter the “result” variable defined previously:
"""
# adding, deleting, multiplying, dividing from a variable
result += 1   # same as saying result = result + 1
print(result)
result *= num1   # same as saying result = result * num1
print(result)
