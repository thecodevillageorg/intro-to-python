# Ask for user input, and write a for loop that will output all the vowels within it. 
# example:
# "Valentine" -> "aei"
# "Wycliffe" -> "ei"

name = input("Enter your name: ")

vowels = "aeiou"

for vowel in vowels:
    if vowel in name:
        print(vowel)