# ask the user for the number of students
number_of_students = int(input("Enter the number of students: "))
# list to hold students
students = []
# for each student, ask for their name, registration number,name of the school
for student in range(number_of_students):
    subjects = []
    
    name = input("Enter the name: ")
    

    # for each student, ask for the number of subjects they'd like to enter
    number_of_subjects = int(input("Enter the number of subjects: "))
    # list to hold subjects
    

    for subject in range(number_of_subjects):
        

        # for each subject, record the name
        subject_name =  input("Enter the subject name: ")
        subjects.append(subject_name)

    students.append(name)  

    

# output the student details:
for student in students:
    print(f'\nStudent Name: {student}')

    for subject in subjects:
        print(f'\nStudent Name: {student}')


       

# - name of student
# - school name
# - subject and mark
# 

