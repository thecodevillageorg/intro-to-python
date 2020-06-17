# While Loop
"""
A while loop is generally used when you need to loop based on a condition rather than counting.

syntax:
while condition:
    do something

"""
lives = 1
while lives < 4: # 3, 2, 1+1 +1
    print(lives)
    lives = lives + 1 

health = 10
while health > 0:
    print(health)
    health -= 1

#  While vs. For
"""
For loops are generally used when you need to count or iterate over
a collection of elements. While loops are generally used when doing condition-based
looping. When using a while loop, often you’ll use boolean variables. Each loop has
their use cases; in most cases it’s personal preference, but the general rule of thumb is
counting with for loops, conditions with while loops.

Note: The pass, break, and continue statements all work the same way for while
loops as well.
"""

# Infinite Loops
"""
An infinite loop will continue to run until te program breaks, the compute is shut down, 
or until time stops. Knowing this, stay away from creating infinite loops by creating an exit 
condition.
Always make sure to exit your loops, whether it be by a break or by a condition.
# """
game_over = False
while not game_over:
    print(game_over)
    break



