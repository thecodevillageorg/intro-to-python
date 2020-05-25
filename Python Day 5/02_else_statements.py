"""
Else statements
The final part of a good decision is what to do by default. Else statements are used to cater for this. 

How They Work
Else conditional statements are the end all be all of the if statement. Sometimes you’re
not able to create a condition for every decision you want to make, so that’s where the
else statement is useful. The else statement will cover all other possibilities not covered
and will always run the code if the program gets to it. This means that if an elif or if
statement were to return True, then it would never run the else; however, if they all
return False, then the else clause would run no matter what every time. 

Writing An Else Statement
Like an elif statement, the else clause needs to always be associated with an original
if statement. The else clause covers all other possibilities, so you don’t need to write a
condition at all; you just need to provide the keyword “else” followed by an ending
colon. Remember that an else clause will run the code inside of it if the program reaches
the statement. 
"""
# using an else statement
name = "John"

if name == "Jacob":
    print("Hello Jacob!")
elif name == "Wycliffe":
    print("Hello Wycliffe!")
elif name == "Valentine":
    print("Hello Valentine") 
else:
    print("Hello {}!".format(name) )

