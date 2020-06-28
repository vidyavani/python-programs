n = int(input())
s = set(map(int, input().split()))
m=int(input())
for i in range(m):
    str=input().split()
    if(str[0]=="pop"):
        s.pop()
    if(str[0]=="remove"):
        s.remove(int(str[1]))
    if(str[0]=="discard"):
        s.discard(int(str[1]))
print(sum(s))
