# Check whether a single character is uppercase or lowercase
char = input("Enter one character: ")

if len(char) == 1 and char.isalpha():
    if char.isupper():
        print("Uppercase letter")
    else:
        print("Lowercase letter")
else:
    print("Please enter exactly one alphabetic character")
