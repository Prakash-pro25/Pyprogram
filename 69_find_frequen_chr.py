s=input()

hcon=0
frev=''
s1=''

for i in s:
     if i not in s1:
          s1+=i

for i in s1:
    recon=0
    for j in s:
        if i == j:
            recon+=1
    if recon > hcon:
            hcon=recon
            frev=i

      

print("character:",hcon)
print("Frequency:",frev)            