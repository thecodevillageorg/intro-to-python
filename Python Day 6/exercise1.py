# Ask the user for 3 numbers
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
third_number = int(input("Enter the third number: "))
# Calculate the sum of the three numbers
sum = first_number + second_number + third_number
# if the values are equal then return thrice of their sum
if first_number == second_number == third_number:
    print(f"Thrice the sum is: {sum*3}")
# else, return the sum
else:
    print(f"The sum is: {sum}")

