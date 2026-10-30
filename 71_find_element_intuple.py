""" n=int(input())


a=()

for i in range(n):
    c=int(input(f"num{i}: "))
    a=a+(c,)

ch=int(input())
con=0
for i in a:
    if ch==i:
        con+=1

print(con)  """     

""" a=tuple(input().split())

target=int(input())



con=i for i in a if    
print(a) """

n=int(input())

a=(int(input()) for i in range(n))

ch = int(input())

con = sum(1 for i in a if i == ch)

print(con)




