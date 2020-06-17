# takes in the number of students 
number_of_students = int(input("How many students? ")) 

# create a list to store the names of students
students = []

# loop the user input to capture the number of students
for student in range(number_of_students):
    name = input("Enter the student name: ")
    students.append(name)

# for loop to print the list of students
for student in students:
    print(student)

