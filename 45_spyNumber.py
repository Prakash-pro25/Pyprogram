n = int(input("enter the number:"))
Mnum=1
Snum=0
for i in str(n):
    i=int(i)
    
    Mnum*=i
    Snum+=i

print(f"it is{" " if Mnum==Snum else " not "}a spy number")