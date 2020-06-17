# team
"""
An object is how we reference real world items.

Object Oriented Programming
Objects in Python are created from classes. The point of OOP is to reuse the same code
while giving flexibility to create each object with their own features.

Stages of OOP

First stage is the class definition. This is where you write the blueprint to be used when called.
The second stage is called instantiation. It is the process of creating an object from the
class definition. After an object is instantiated, it is known as an instance. You may have
multiple instances from a single class definition.


Car - base/blueprint   - colour, engine capacity         
- ford
- toyota
- mazda
- lambos

Person - base
- race
- weight
- height
"""
# creating and instantiating a class
# class definition
# class Car():
#     pass # placeholder


# ford = Car() # creates an instance of the Car class and stores it in the variable ford
# toyota = Car()


# attributes (variables within a class)
# class Car():
#     capacity = 2000
#     colour = 'white'

# mazda = Car()
# print(mazda.capacity,mazda.colour)


# # methods (functions within a class)
# class Dog():
#     def bark():
#         return bark

# german_shepherd = Dog()
# # access methods
# german_shepherd.bark()

# using init method
class Car():
    # initialization function or constructor method
    # self keyword refers to the current instance of the class
    def __init__(self,color,capacity): 
        self.color = color
        self.capacity = capacity


# create an instance - an instance of a class is an object
toyota = Car("red",2000)
toyota1 = Car("white",1500)
mazda = Car("grey",1800)


print(toyota.color)
print(toyota1.capacity)
print(mazda.color)








# inheritance (parent or base classes)