# Simple calculator for two numbers
a = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ").strip()
b = float(input("Enter the second number: "))

if operator == "+":
    print("Result:", a + b)
elif operator == "-":
    print("Result:", a - b)
elif operator == "*":
    print("Result:", a * b)
elif operator == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Cannot divide by zero")
else:
    print("Invalid operator")
