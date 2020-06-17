from School import School
from Student import Student
from Subject import Subject
from grading_function import grading


noOfStudents = int(input('Enter the no. of students: '))

students = []
schools = []
# input details for multiple students
for n in range(1,noOfStudents+1):
    student_name = input('Enter Name of Student \n')
    student_stream = input('Enter Reg Number \n')

    school_name = input('Enter Name of School \n')
    school_address = input('Enter School Address \n')
 
    # create instance of school to be saved later
    school = School(school_name,school_address)
    
    # collect subject details
    nofsubjects= int(input('Enter no. of subjects \n'))
    subjects = []
    for s in range(1,nofsubjects+1):
        subject_name = input('Enter name of Subject \n'.strip())
        subject_score = int(input('Enter the score for {} \n'.format(subject_name)))
        subject = Subject(subject_name,subject_score)
        subjects.append(subject) # store subject
        

    # create instance of student to be saved
    student = Student(student_name,student_stream)

    students.append(student)
    schools.append(school)
    



for student in students:
    print(student.student_name,student.student_stream.student,len(student.subjects))
    for subject in subjects:
        print(subject.name,':',subject.score,'Grade : ',grading(subject.score))
    
    