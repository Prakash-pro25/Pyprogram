s=input()

s=s.split()
a=[]

for i in s:
    a.append(i[::-1])

a=" ".join(a)
print(a)

