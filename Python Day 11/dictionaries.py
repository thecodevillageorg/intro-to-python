"""
A dictionary is a collection of unordered data, which is stored in key-value pairs. What
is meant by “unordered” is the way it is stored in memory. It is not accessible through
an index, rather it is accessed through a key.


key - tag
value - compartment
"""
# empty
my_dictionary = {}

# a dictionary with two key-value pairs
person = {
    'name':'Morty',
    'age': 20
}

# declare using constructor
person2 = dict(first_name="Valentine",age=23)

name_of_dictionary = dict(name="Wycliffe",address="Nairobi",age=30)


# access 
print(person['name'])
print(name_of_dictionary['name'])

# access using .get method
print(person.get('age'))
print(name_of_dictionary.get('address'))

# add key/value pair
person['address'] = 'Mombasa'
name_of_dictionary['year_of_birth'] = 1989

print(person)
print(name_of_dictionary)

# access keys
print(person.keys())
print(name_of_dictionary.keys())
# access values
print(person.values())
print(name_of_dictionary.values())
# access items
person.items()
print(name_of_dictionary.items())

# remove key-value pair - del() or pop()
# del(person['age'])
del(name_of_dictionary['age'])
print(name_of_dictionary)
# person.pop('age')
# print(person)
# name_of_dictionary.pop('age')
# # clear
# person.clear()
# print(person)
# name_of_dictionary.clear()
# print(name_of_dictionary)

# check length/ number of key-value pairs
print(len(person2))
print(len(name_of_dictionary))

# lists in dictionaries
cities = {
    'African': ['Nairobi','Kigali', 'Bujumbura'],
    'European': ['Helsinki','Prague']
}

print(cities['African'])
print(cities['European'][1])

# copy - .copy()

person_clone = person.copy()
name_of_dictionary_copy = name_of_dictionary.copy()
print(person_clone)
print(name_of_dictionary_copy)

# looping through a dictionary

# keys only
for key in name_of_dictionary.keys():
    print(key)
# # values only
for value in name_of_dictionary.values():
    print(value)
# # key - value pairs
for key, value in name_of_dictionary.items():
    print(f'Key: {key} : Value: {value}')




