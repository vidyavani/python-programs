count=0
list=[]
l=[]
n=int(input())
for i in range(n):
    c=int(input())
    list.append(c)
list.sort()
print(list)
for i in list:
    l.append(1)
    if(i<i+1):
        l.append(2)
        count+=1
        if(count==2):
            l.append(3)
    elif(i==i+1):
        l.append(1)
        count=0
    else:
        count=0
print(l)
print(sum(l))

    
