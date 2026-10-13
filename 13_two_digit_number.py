# Check whether an integer is a two-digit number
num = int(input("Enter an integer: "))

if 10 <= abs(num) <= 99:
    print("It is a two-digit number")
else:
    print("It is not a two-digit number")
