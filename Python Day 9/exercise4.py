# ask user for a number, which is the radius a circle
# if the number <= 10, calculate the circumference
# if the number is greater than 10, calculate the area
# should have functions for calculating circumference and area

radius = int(input("Enter a number: "))

def circumference(radius):
    circumference = 3.14 * 2 * radius
    return circumference

def area(radius):
    area = 3.14 *radius*radius
    return area

if radius <=10:
    result = circumference(radius)
    print(f"The circumference is: {result}")

elif radius > 10:
    result = area(radius)
    print(f"The area is: {result}")
