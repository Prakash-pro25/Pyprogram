n=int(input())

for i in range(n,0,-1):
    for k in range(i,n):
        print(" ",end="")
      
    for j in range(i-1):  
          print("*",end=' ')
    print()   


print("\n")   


for i in range(n,0,-1):
    for k in range(i-1):
        print(" ",end="")
      
    for j in range(i,n):  
          print("*",end=' ')
    print()   