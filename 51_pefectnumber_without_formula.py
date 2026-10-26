num=int(input("enter the number:"))


""" a=[] """
total=0

for i in range(1,num):
    if num%i==0:
        """ a.append(i) """  
        total+=i  


""" for i in a:
    total+=i """



print(f"it is {""if total==num else "not "}an perfect number " )