# Find the smallest of three numbers
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

if a <= b and a <= c:
    print("Smallest number:", a)
elif b <= a and b <= c:
    print("Smallest number:", b)
else:
    print("Smallest number:", c)
