# Loops
"""
Loops in Python - "for loop" and "while loop"
Loops allow us to rerun the same lines of code several times. 
Loops will always run until a condition is met.
Each time a loop runs is known as iteration.
"""
# For Loop - used to loop a set number of times
"""
syntax:
for num in range(5):

range(start,stop,step) (0,100+1,2)
range(0,5,1)
range(6)
range(2,10)

for - keyword that begins loop
num - temp variable, also known as counter or index
in - keyword
range function - allows us to count from one number to another while being able to define
the start and end
"""
# ex 
for num in range(5+1): # range counts up to but not including
    print(f"Value: {num}")

for greeting in range(10):
    print("hello world")

for i in range(0,101,2):
    print(i)

for j in range(0,101,5):
    print(j)


