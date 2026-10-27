s=input("enter the string: ")

a=set()

for i in s:
    recon=0
    for j in s:
      if j == i:
        recon+=1
    if recon != 1:
       a.add(i)

print(a)       