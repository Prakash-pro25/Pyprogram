# Check whether a character is an alphabet, digit, or special character
char = input("Enter one character: ")

if len(char) != 1:
    print("Please enter exactly one character")
elif char.isalpha():
    print("Alphabet")
elif char.isdigit():
    print("Digit")
else:
    print("Special character")
