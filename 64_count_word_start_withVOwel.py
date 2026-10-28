s=input().lower()

vol="aeiou"

s=s.split()
count=0

for i in s:
    i=i[0]

    if i in vol:
        count+=1

print(count)

