n = int(input())
""" 
for i in range(1, n + 1):

    print("*" * i + " " * (2 * (n - i)) + "*" * i)
    

for i in range(n, 0, -1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)
 """ 
for i in range(1,n+1):
    for j in range (1,i+1):
        if j==i:
          print("*",end=' ')
        else:
          print(" ",end=" ")
    for j in range (1,2*(n-i)+1):  
        print(" ",end=" ")
    for j in range(1,i+1):
        if j==1:
          print("*",end=" ")
        else:
           print(" ",end=" ")
    print()

for i in range(n,0,-1):
    for j in range (1,i+1):
        if j==i:
          print("*",end=' ')
        else:
           print(" ",end=" ")
    for j in range (1,2*(n-i)+1):
        print(" ",end=" ")
    for j in range(1,i+1):
        if j==1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print() 