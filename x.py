word = input("Enter a word").lower()
vowels = "aeiou"
for vowel in vowels:
    if vowel in word:
        print(vowel)







user_input = True

while user_input :
    if user_input == "quit":
        user_input = False
    else:
        user_input = input("Enter something: ").lower()
