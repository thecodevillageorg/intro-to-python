"""
elif statements give us the ability to run separate blocks of code
depending on the condition. They are also known as "else if statements".

elif statements must be associated with an if statement, meaning
that you cannot create an elif without an if. Python works in top to bottom order, so
it checks the first if statement; if that statement is False, it continues to the first elif
statement and checks that condition. If that condition returns False as well, it continues
to the next conditional statement until there are no more to check. However, once a
single conditional statement returns True, all other conditionals are skipped, even if
they are True. It works so that the first conditional to return True is the only block of
code that runs.
"""
# ex
x = 5
y = 10
if x > y:
      print("x is greater")
elif x < y:
      print("x is less")

"""
Checking Multiple Elif Conditions
Having the ability to write multiple decisions based on a single variable is a necessity,
which is why elif statements were built. 
"""
# ex
# checking more than one elif conditional statement
x = 5
y = 10
if x > y:
      print("x is greater")
elif (x + 10) < y:                    # checking if 15 is less than 10
      print("x is less")
elif (x + 5) == y:                    # checking if 10 is equal to 10
      print("equal")


""""
Conditionals Within Conditionals
What if we added an if statement within an if statement?
"""
# writing multiple conditionals within each other - multiple block levels
x = 5 
y = 10
z = 5
if x > y:
      print("greater")
elif x <= y:
      if x == z:
              print("x is equal to z")       # resulting output
      elif x != z:
              print("x is not equal to z")   # won't get hit


"""
If Statements vs. Elif Statements
A major difference that you’ll need to understand going forward is the use for elif
statements against using multiple if statements. All elif statements are connected to one
original if statement, so that once a single conditional is True, the rest do not run.
"""
# example:
# testing output of two if statements in a row that are both true
x = 5 
y = 10
z = 5
if x < y:
      print("x is less")
if x == z:
      print("x is equal")

"""
Notice that the resulting output is both print statements
here. This is due in part to having two if statements. These if statements are not related to
each other; they are separate conditional statements, whereas an elif is always connected
to an if.
"""
# testing output of an if and elif statement that are both true
x, y, z = 5, 10, 5
if x < y:
      print("x is less")
elif x == z:
      print("x is equal to z")

"""
Notice that the output here is only “x is less” and doesn’t
include the second print statement. That’s because an elif is attached to an if statement,
and once one of the conditionals returns True, all others will not be checked even if they
are True themselves.
"""