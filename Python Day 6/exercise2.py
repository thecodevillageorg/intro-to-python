# ask user for the year of birth
# calculate the current age
# if the age is less than or equal to 1, return "Infancy"
# if the age is greater than 1 but less than or equal to 3, return "Toddlerhood"
# if the age is greater than 3 but less than 13, return "Childhood"
# if the age is greater than or equal to 13 but less than or equal to 19, return "Adolescence"
# else, return "Adult"

year_of_birth = int(input("What's your year of birth? "))
current_year = 2020
age = current_year - year_of_birth

if age <=1:
    print("Infancy")
elif age > 1 and age <=3:
    print("Toddlerhood")
elif age > 3 and age < 13:
    print("Childhood")
elif age >= 13 and age <=19:
    print("Adolescence")
else: 
    print("Adult")