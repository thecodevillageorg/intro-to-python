"""
A tuple is identical to a list, except that it is immutable. 
This means that it cannot be altered once declared.
They're useful for storing info that you don't want to change.
They're ordered like lists, so you can iterate through them using an index.
"""

# declaring a tuple
fruits = ('Apples','Oranges','Grapes')

# using a constructor
# fruits2 = tuple(('Apples','Oranges','Grapes'))

# single value needs a trailing comma
fruits2 = ('Banana',)

print( type(fruits2) )

# access
print(fruits[0])

# immutable
# fruits[0] = 'Pineapple'
# if you want to change values, declare the tuple afresh

# loop or iterate
for fruit in fruits:
    print(f'FRUIT: {fruit}')


print(fruits)
