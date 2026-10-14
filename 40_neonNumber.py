n=int(input("enter any number : "))

nPower=n**2
total=0

for i in str(nPower):
    i = int(i)
    total+=i  

if n == total:
    print("The number is neonNumber")  
else:
    print("The number is not a neonNumber")      
