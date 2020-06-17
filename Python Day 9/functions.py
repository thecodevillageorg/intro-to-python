# a = 2 # 3
# b = 3 # 5

# # sum = a+ b
# print(sum)

# syntax : def function_name(parameters or arguments):


"""
sandwich - bread, meat, vegetables

bread - brown, white, wholemeal
meat - ham, brawn etc
vegetables - lettuce, cabbage, celery

def sandwich(bread,meat,veggies):
    sandwich = bread + meat + veggies
    return sandwich

sandwich(brown,ham,lettuce) # calling or invoking a function

"""
# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# c = int(input("Enter a number: "))


# def product(a,b,c):
#     product = a * b * c
#     return product

# # calling or invoking
# result = product(a,b,c)
# print(result)




# def sum(a,b):
#     sum = a + b
    
#     return sum


# sum1 = sum(2,3)
# sum2 = sum(5,6)
# sum3 = sum(7,60)

# print(f"Sum 1: {sum1} Sum 2:  {sum2} Sum 3: {sum3}")

# # "Hello Nick"


# name = input("Enter your name: ")

# def greeting(name):
#     greeting = "Hello " + name
#     return greeting

# greeting = greeting(name)

# print(greeting)

# # product = (sum(4,5) * 3)
# # print(product)



# Functions with default parameters
def sayHello(name="John"):
    return f'Hello {name}'

print(sayHello())

# Return values
def getSum(num1, num2):
    total = num1 + num2
    return total

result = getSum(4,9)
print(result)


# anonymous functions/lambda functions
"""
An anonymous function is a function that is defined without a name.
While normal functions are defined using the def keyword in Python, 
anonymous functions are defined using the lambda keyword.

Hence, anonymous functions are also called lambda functions.

syntax:

lambda arguments: expression

Note: Lambda functions can have any number of arguments but only one expression. 
The expression is evaluated and returned.

"""

sum = lambda number1,number2: number1 + number2
print(sum(5,6))