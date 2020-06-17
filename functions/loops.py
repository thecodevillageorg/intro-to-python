# counting through a collection of items (iterate)
# strings,lists,dictionaries, sets,tuples,frozensets

# strings
sentence = "Welcome to Nairobi"

# for each item in the collection
for letter in sentence:
    print(letter)

# list
fruits = ['Banana','Mango','Apples']

for fruit in fruits:
    print(fruit)

# dictionaries - its a collection key-value pairs
person = {
    'name':'Wycliffe',
    'age': 30
}

print(person['name'])
person['name'] = "Valentine"

print(person['name'])

# keys
keys = person.keys()
print(keys)

# loop keys
for key in person.keys():
    print(key)

# values
values = person.values()
print(values)

#loop values
for value in person.values():
    print(value)

# items or key-value pairs
items = person.items()
print(items)

# loop key-value pairs
for key,value in person.items():
    print(key,value)

