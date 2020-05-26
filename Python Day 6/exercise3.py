# Take values of length and breadth of a rectangle from user and check if it is a square or a rectangle.
length = int(input("Enter the length: "))
breadth = int(input("Enter the breadth: "))

if length == breadth:
    print("This is a square")
elif  length != breadth:
    print("This is a rectangle")
else: 
    print("Invalid. Please try again")
