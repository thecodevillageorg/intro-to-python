# from grading_system import grading, total
import grading_system # user-defined
import math # in-built
import datetime

print(math.pi)
print(math.pow(2,2))


# # import module_name

marks1 = int(input("Enter the marks for the subject : "))
marks2 = int(input("Enter the marks for the subject : "))
marks3= int(input("Enter the marks for the subject : "))
marks4 = int(input("Enter the marks for the subject : "))


grading_system.grading(marks1)
grading_system.grading(marks2)
grading_system.grading(marks3)
grading_system.grading(marks4)



total = grading_system.total(marks1,marks2,marks3,marks4)
print(total)

# in-built
# user-defined - custom
# 3rd party - install using pip package manager then import it