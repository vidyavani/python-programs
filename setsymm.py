m=int(input())
s1=set(map(int,input().split()))
n=int(input())
s2=set(map(int,input().split()))
s=s1.symmetric_difference(s2)
print(len(s))
