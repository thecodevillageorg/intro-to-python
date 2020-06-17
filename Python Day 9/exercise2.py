# Ask for a number, n.
# Calculate the sum of the numbers before n including the number n
# positive numbers >0


n = int(input("Enter a number: "))

sum = 0
counter = 1 

while counter <= n:
    sum = sum + counter
    counter = counter + 1
    
print(sum)







