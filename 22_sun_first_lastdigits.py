num = int(input("Enter an integer: "))

if 10 <= abs(num) <= 99:
  num1 = num % 10  # last digit
  num2 = num // 10  # first digit
  print(f"the sum of the first and last digits is {num1 + num2}")
else:
  print("this number not two digits")