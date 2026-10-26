s=input('enter the string: ')
c=input('enter the char:')

count=0

for i in s:
    if i == c:
        count+=1

print(f"the number of times {c} in {s} is {count}")

