str=input()
c=0
l=[]
substr=[str[i:j] for i in range(len(str)) for j in range(i+1,len(str)+1)]
for ele in substr:
   for i in range(len(ele)-1):
      if(ele[i]!=ele[i+1]):
        c+=1
   if(c==len(ele)-1):
      l.append(ele)
   c=0
print(l)
l.sort(key=len,reverse=True)
print(l)
print(l[0])
