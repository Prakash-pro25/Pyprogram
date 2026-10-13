# Check whether the last digit of an integer is 5
num = int(input("Enter an integer: "))

if abs(num) % 10 == 5:
    print("The last digit is 5")
else:
    print("The last digit is not 5")
