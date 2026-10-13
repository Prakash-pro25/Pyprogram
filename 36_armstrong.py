n =int(input("enter the any number: "))


n=str(n)
Ln=len(n)
a=0
for i in n:
    i=int(i)
    i**=Ln
    a+=i

if a==int(n):
    print("this number is armstrong")
else:
    print("this number is not armstrong")    