from itertools import combinations
s,k=input().split()
sr=''.join(sorted(s))
for i in range(1,int(k)+1):
    l=list(combinations(sr,i))
    for i in l:
        print(''.join(i))
