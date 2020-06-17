subject1 = int(input("Enter the marks for the first subject: "))
subject2 = int(input("Enter the marks for the second subject: "))
subject3 = int(input("Enter the marks for the third subject: "))
subject4 = int(input("Enter the marks for the fourth subject: "))




# def function_name(parameters or arguments):
"""
sandwich - bread, meat, veggies

def sandwich(bread,meat,veggies):
    sandwich = bread + meat + veggies
    return sandwich


"""


def grading_system(mark):
    if mark >= 80 and mark <=100:
        print("A")
    elif mark >= 60 and mark < 80:
        print("B")
    elif mark >= 50 and mark < 60:
        print("C")
    elif mark >= 45 and mark < 50:
        print("D")
    elif mark >= 25 and mark < 45:
        print("E")
    else:
        print("F")

        


    


grading_system(subject1)
grading_system(subject2)
grading_system(subject3)
grading_system(subject4)



