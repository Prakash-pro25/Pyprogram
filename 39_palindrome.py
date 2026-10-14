n=int(input("enter the any number: "))

n=str(n)
p=""

for i in  reversed(n):
    p+=i


if int(n) == int(p):
    print("it is palindrome")
else:
    print("it is not a palindrome")    