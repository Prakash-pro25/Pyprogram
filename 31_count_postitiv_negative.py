a=[-2,40,8,-30,5,-6,-90,-70,6,83,20]

cPve=0
cNve=0

for i in a:
    if i>0:
        cPve+=1
    elif i<0:
        cNve+=1
    else:
        print("it is 0")       

print(f"number of +ve element in list :{cPve}")        
print(f"number of -ve element in list :{cNve}") 