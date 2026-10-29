
s=input()
s1=""
s2=""

for i in s:

    if 65 <=ord(i)<=90:
        s1+=chr((ord(i)+32))
    elif 97<ord(i)<=122:
        s1+=chr(ord(i)-32)
    elif 0<=i<=9:
        s1+=i 
    else:
        continue  


for i in s:

    if i.isupper():
        s2+=i.lower()
    elif i.islower():
        s2+=i.upper()
    elif i.isdigit():
        s2+=i    
    else:
        continue         

print(s1)
print(s2)   
  
