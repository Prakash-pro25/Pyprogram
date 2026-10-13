# Find the largest of two numbers
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

if a > b:
    print("Largest number:", a)
elif b > a:
    print("Largest number:", b)
else:
    print("Both numbers are equal")
