n=int(input("enter the any number:"))

""" if  n==2 or n==1:
      a="this is a prime number"
elif n%2==0 :
      a="not a prime number"
else:     """

for i in range(2,n):
    if n%i==0:
        a="not a prime number"
        break  
    else:    
        a="this is a prime number" 
print(a)