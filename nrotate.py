list=[]
count=0
n=int(input())
for i in range(n):
    str=input()
    list.append(str)
for i in list:
    count=0
    for k in range(len(i)):
        s=i[k:]+i[:k]
        count+=1
        if(list[0]==s):
           print(i,"-",count)
           break
    else:
        print(i,"-",'0')
