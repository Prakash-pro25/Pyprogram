from itertools import combinations
s, n = input().split()
s = s.upper()
n = int(n)

s= "".join(sorted(s))

a=combinations(s,n)


for i in range(1,n+1):
    a=combinations(s,n)
    for j in a:
        print("".join(i))
