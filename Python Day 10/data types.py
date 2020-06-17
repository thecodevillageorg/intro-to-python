# data types / data collections - data types that can store multiple items

# list, tuple,set ,dictionary

"""
List

A list is a data structure in Python that is a mutable, ordered sequence of elements. 
Also known as array.

syntax:
name_of_list = []

lists are zero-indexed 

"""
name = "Nick Kimani"

num = 4.5
data = ["word","John",45,[34,"hello",True],num] 
# for loops
for element in data:
    print(element)


data_copy = data[:]
print(data_copy)
        # 0        1   2     3              4
            # -4      -3      -2             -1

data[0] = "value"
# list[start:stop]
print(data[1:3])
print(data[:3])
print(data[:]) # copying the list


print(data)

print(data[3][1])      
# print(data[0][0])
# print(data[-2])
# print(data[4])

 
# .append()     
numbers = [1,2,3,4,[56,78,90],5]
numbers.append(7)

print(numbers)

# .insert()
numbers.insert(2,78)
print(numbers)

# .pop() - removes last item in the list. However, you can specify an index
numbers.pop(3)
print(numbers)

# .remove() - removes items from a list based on their given value
numbers.remove(5)
print(numbers)

# .len() - checks the length of the list
length = len(numbers)
print(f'The length is {len(numbers[4])}')
print(length)
