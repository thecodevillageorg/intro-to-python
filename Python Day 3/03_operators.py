# Arithmetic Operators 
## Addition operator +
greeting = "hello" + " " + "world" # string concatenation
print(greeting)
num1 = 2
num2 = 4
sum = num1 + num2
print(sum)

## Subtraction - 
difference = num2 - num1
print(difference)

## Multiplication * 
#multiplying strings to form a string with a repeating sequence
lots_of_hellos = "\nhello "* 10 # escape character
print(lots_of_hellos)

product = num1 * num2
print(product)

## Division /
result = num2 / num1
print(result)

## Modulus % 
modulus = num2 % num1
print("Modulus",modulus)


## Exponent **
exponent = num1**2
print(exponent)


# Comparison Operators
# Equality ==
# Inequality !=
# Greater than >
# Less than <
# Greater than or equal >=
# Less or equal <=


# Logical Operators
## Logical Operator "and"
"""
Ensures that when you check for multiple conditions, both sides of the condition are True.
This means that if either the condition to the left or right of the “and” is False, 
then the code will not run the block of code.
"""
# ex
# using the keyword 'and' in an 'if statement'
x = 5 
y = 10 
z = 5
if x < y and x == z:
      print("Both statements were true")


## Logical Operator "or"
"""
Checks for one or both conditions to be true. Such that if the condition to the left is False 
and the condition to the right is True, the block of code will still run because at least 
one condition was True. The only time an “if block” will not run using an “or” operator is 
when both conditions are False. 
"""
# ex 
# using the keyword 'or' in an 'if statement'
x = 5 
y = 10
z = 5
if x < y or x != z:
      print("One or both statements were true")



## Logical Operator "not"
"""
Checks for the opposite of a value. The “not” operator is used for just that. 
It essentially returns the opposite of whatever the current value is.
"""
# ex
# using the keyword 'not' within an 'if statement'
flag = False
if not flag:                  # same as saying if not true
      print("Flag is False")





# Assignment Operators
# Bitwise Operators
# Membership Operators

