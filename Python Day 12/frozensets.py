"""
Frozensets are essentially the combination of a set and a tuple. They are immutable,
unordered, and unique. These are perfect for sensitive information like bank account
numbers, as you wouldn’t want to alter those. They can be iterated over, but not indexed.


Declaring a Frozenset
To declare a frozenset, you use the keyword “frozenset” followed by parenthesis and
enclosing square brackets. This is the only way you can declare a frozenset.
"""
# declaring a frozenset
fset = frozenset( [1, 2, 3, 4])

print(fset)

# access
print(1 in fset) # returns boolean value

# iterable
for item in fset:
    print(item)


