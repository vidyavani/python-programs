from itertools import combinations_with_replacement
s,k=input().split()
str=''.join(sorted(s))
l=list(combinations_with_replacement(str,int(k)))
for i in l:
    print(''.join(i))
