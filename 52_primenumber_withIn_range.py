range1=int(input("give the range of the prime find num1:"))
range2=int(input("give the range of the prime find num2:"))

for n in range(range1,range2+1):
    if  n==2 :
        a=True
    elif n%2==0 or n==1:
        a=False
    else:

        for i in range(2,n):
            if n%i==0:
                a=False 
                break  
            else:    
                a=True     
    if a:
     print(n)

