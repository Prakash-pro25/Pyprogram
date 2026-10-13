a=[20,4,87,90,102,35,230,40,22,410]
L=0

for i in a:

    if L>i:
       L=L
    elif L<i:
        L=i
    else:
        L=L       

print(L)