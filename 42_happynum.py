n = int(input("Enter a number: "))
num = n
seen = set()

while num != 1 and num not in seen:
    seen.add(num)
    total = 0

    while num > 0:
        digit = num % 10
        total = total + digit * digit
        num = num // 10

    num = total

if num == 1:
    print("Happy number")
else:
    print("Not a Happy number")