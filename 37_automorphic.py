n = int(input("enter the any number :"))

m=1

for i in range(1,len(str(n))+1):
    m*=10


if n == n**2%m:
    print("it is automorphic")
else:
    print("it is not aoutomorphic")    