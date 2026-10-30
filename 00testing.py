""" print(f"you are eligible to place in training" if (input("dept:")=="IT" and float(input("CGPA:"))>=8) else "you are not eligible") """
""" 
a="hello"
a='k'+a[1:]

print(a) """

""" name=input("enter a name:")
age=int(input("enter a age"))

print(f"my name is {name} and my age is {age}")
print("my name is "+name+" and my age is",age)
print("my name is",name,"and my age is",age,sep=' ') """

""" 
a=input('enter the string: ')

print("true"if a[0]==a[-1] else "false") """

""" 
a="hello world"

print(a[::-1]) """
""" 
a=10
while a>0:
    
    print(a)
    a-=1 """

""" s=input()
print(set(s))

for ch in set(s):
    if s.count(ch)>1:
        print(ch)
         """
""" 
class Solution(object):
    def mergeAlternately(self, word1, word2):

        max_len = max(len(word1), len(word2))
        word1 = word1.ljust(max_len)
        word2 = word2.ljust(max_len)
        words=" "
        i=0
        while i<max_len:

            words+=word1[i]+word2[i] 
            i+=1
        return words   """       


""" if "IV" in s:
            while "IV" in s:
                total+=4
                s=s.replace("IV","",1)
        if "CM" in s:
                    while "CM" in s:
                        total+=900
                        s=s.replace("CM","",1)
        if "XC" in s:
                    while "XC" in s:
                        total+=90
                        s=s.replace("XC","",1)    """
""" from itertools import permutations
s, n = input().split()
s = s.upper()
n = int(n)

s= "".join(sorted(s))

a=permutations(s,n)

for i in a:
    print("".join(i)) """

""" sub=["java",'py','js','C#']
m=[20,35,59,40]

for i in sub:
    print(i,end=" ")

total=sum(m)
avg=total/len(m)

print("\ntotal\navg") """

""" 

n = int(input())
a=[i for i in range(1,n+1)]
total=0

for i in a:
    total+=i

print(a,total)     """



ls = [1, 2, 3, 4, 5]
s = 0
print([s   := s + i for i in ls])