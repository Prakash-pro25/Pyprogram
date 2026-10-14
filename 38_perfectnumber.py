n =int(input("enter any number:"))


for p in range(1,n+1):
    if (2**(p-1)*(2**p-1))==n:
        a="it is an perfect number"
        break
    else:
        a="it is not an perfect number"   

print(a)
