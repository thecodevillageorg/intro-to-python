# strings
course = 'Python for Beginners'
          
print(len(course))


# String Index
# When a computer saves a string into memory, each character within the string is
# assigned what we call an “index.” An index is essentially a location in memory.

# formatted strings
first_name = 'john'
last_name = 'smith'

# String Slicing
greeting = "Hello world"
greeting_copy = greeting[:]
print(greeting[0])
print(greeting[-1])

# [start:end]
print(greeting[3:7])
print(greeting[3:])
print(greeting_copy)



# string methods
# .title() - capitalizes all first letters in each word or a string
print(first_name.title())

# .replace()
print(last_name.replace('th','xz'))

# .find() - returns the index
string = "Look over there"
print(string.find("over"))


# .strip() - you want to get rid of a certain character on the left and right side of
# a string, you would use the strip method. By default, it will remove spaces.
# there's .lstrip() and .rstrip()
price = " $100 "
print(price.strip('$'))
print(price.lstrip())


# .split() - returns a list []
sentence = "These are words in a sentence"
print(sentence.split(' '))

# len() - general purpose function and not limited to checking length of strings 

# upper(), 
name = "Wycliffe"
print(name.upper())

# lower(), 
print(name.lower())


print(course)


