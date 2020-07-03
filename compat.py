t=int(input())
for i in range(t):
    n=int(input())
    for i in range(n):
        l=list(map(int,input().split()))
l.sort()
a=min(l)
c=max(l)
for i in l:
    if a<i:
        b=i
        break
print(a,b,c)
print(a-b+c)
