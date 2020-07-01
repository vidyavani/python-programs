from itertools import product
a=list(map(int,input().split()))
b=list(map(int,input().split()))
l=list(product(a,b))
for i in l:
    print(i,end=" ")
