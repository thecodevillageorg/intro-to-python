# ask user for radius
# use a lambda function to calculate the area

radius = int(input("Enter the radius: "))

area = lambda radius: 3.14 * radius * radius
print(f'The area of the circle is {area(radius)}')
