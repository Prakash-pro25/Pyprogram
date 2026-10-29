# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

s, n = input().split()
s = s.upper()
n = int(n)

s= "".join(sorted(s))

a=combinations_with_replacement(s,n)

for i in a:
    print("".join(i))