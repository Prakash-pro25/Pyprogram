n=int(input("enter the number:"))

n=str(n)
total=0

for i in range(len(n)):
    total+=int(n[i])**(i+1)

print(f"it is{" " if int(n)==total else " not "}a Disarium number")    