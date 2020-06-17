"""
Sets share the same characteristics of lists and dictionaries. 
A set is a collection of info like a list; however, like a key in a dictionary, 
sets can only contain unique values. They are also an unordered collection meaning 
that they cannot be accessed by index but rather by the value itself like dictionary keys. 
They can be iterated through, just like how dictionary keys can be looped over. 
Sets are practical in situations of storing unique items.


Declaring a Set
There are two ways to declare a set. The first way is by using the keyword “set” followed
by parenthesis and enclosing square brackets. The second way, which is more practical,
looks like a dictionary being declared by using a set of curly brackets.
"""
# declaring a set
fruits = {'Apples', 'Oranges','Mango','Mango'} # most common

fruits2 = set(['Grapes','Avocados'])

# access
print('Apples' in fruits)
    

# add to set
fruits.add('plum')

# remove from set
fruits.remove('Apples')

# clear
# fruits.clear()

# loop

for fruit in fruits:
    print(f'FRUIT: {fruit}')


print(fruits)