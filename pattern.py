n=int(input())
i=1
list=[]
while(i<n+1):
    list.append(i)
    list.append(-n)
    i=i+1
    n=n-1
list.pop()
for i in list:
    print(i,end=" ")
    
