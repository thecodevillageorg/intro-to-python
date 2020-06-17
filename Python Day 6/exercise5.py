# A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.

marks1 = int(input("Enter the marks for the subject : "))
marks2 = int(input("Enter the marks for the subject : "))
marks3= int(input("Enter the marks for the subject : "))
marks4 = int(input("Enter the marks for the subject : "))

def grading(score):
    if score>= 80 and score<=100:
        print("A")
    elif score>= 60 and score< 80:
        print("B")
    elif score>= 50 and score< 60:
        print("C")
    elif score>= 45 and score< 50:
        print("D")
    elif score>= 25 and score< 45:
        print("E")
    else:
        print("F")

grading(marks1)
grading(marks2)
grading(marks3)
grading(marks4)






# def grading(score):
#     if score >= 80 and score <=100:
#         print("A")
#     elif score >= 60 and score < 80:
#         print("B")
#     elif score >= 50 and score < 60:
#         print("C")
#     elif score >= 45 and score < 50:
#         print("D")
#     elif score >= 25 and score < 45:
#         print("E")
#     else:
#         print("F")


# # invoke or call
# grading(marks1)
# grading(marks2)
# grading(marks3)
# grading(marks4)

# if marks2 >= 80 and marks2 <=100:
#     print("A")
# elif marks2 >= 60 and marks2 < 80:
#     print("B")
# elif marks2 >= 50 and marks2 < 60:
#     print("C")
# elif marks2 >= 45 and marks2 < 50:
#     print("D")
# elif marks2 >= 25 and marks2 < 45:
#     print("E")
# else:
#     print("F")

# if marks3 >= 80 and marks3 <=100:
#     print("A")
# elif marks3 >= 60 and marks3 < 80:
#     print("B")
# elif marks3 >= 50 and marks3 < 60:
#     print("C")
# elif marks3 >= 45 and marks3 < 50:
#     print("D")
# elif marks3 >= 25 and marks3 < 45:
#     print("E")
# else:
#     print("F")

# if marks4 >= 80 and marks4 <=100:
#     print("A")
# elif marks4 >= 60 and marks4 < 80:
#     print("B")
# elif marks4 >= 50 and marks4 < 60:
#     print("C")
# elif marks4 >= 45 and marks4 < 50:
#     print("D")
# elif marks4 >= 25 and marks4 < 45:
#     print("E")
# else:
#     print("F")