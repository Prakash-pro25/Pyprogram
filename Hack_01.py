from itertools import permutations
s, n = input().split()
s = s.upper()
n = int(n)

s= "".join(sorted(s))

a=permutations(s,n)

for i in a:
    print("".join(i))