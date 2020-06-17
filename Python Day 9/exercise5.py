# create a function that takes in the name of an employee, their salary and years of service
# calculate the bonus based on the years of service:
# if years of service <= 1: 10 %
# if years of service >1 and <= 2: 20 %
# if years of service >2 and <= 3: 30 %
# if years of service >3 and <= 4: 40 %
# if years of service >4 and <= 5: 50 %
# if years of service > 5: 60 %

# print the output as follows:
# "Hi Ben, for your 5 years of service, you get 10000 as bonus"
name = input("Enter your name: ")
salary = int(input("Enter your salary: "))
year_of_employment = int(input("Enter your year of employment: "))
current_year = 2020

years_of_service = current_year - year_of_employment

def bonus_calculator(name,salary,years_of_service):
    if years_of_service <=1:
        bonus = salary * 0.01
        print(f'Hi {name}, for your {years_of_service}, you get {bonus} as bonus')
    elif years_of_service > 1 and years_of_service <=2:
        bonus = salary * 0.02
        print(f'Hi {name}, for your {years_of_service}, you get {bonus} as bonus')
    elif years_of_service > 2 and years_of_service <=3:
        bonus = salary * 0.03
        print(f'Hi {name}, for your {years_of_service}, you get {bonus} as bonus')
    elif years_of_service > 3 and years_of_service <=4:
        bonus = salary * 0.04
        print(f'Hi {name}, for your {years_of_service}, you get {bonus} as bonus')
    elif years_of_service > 4 and years_of_service <=5:
        bonus = salary * 0.05
        print(f'Hi {name}, for your {years_of_service}, you get {bonus} as bonus')
    elif years_of_service >5:
        bonus = salary * 0.06
        print(f'Hi {name}, for your {years_of_service}, you get {bonus} as bonus')

result = bonus_calculator(name,salary,years_of_service)
print(result)


