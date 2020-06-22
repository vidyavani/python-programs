str=input()
c=0
l=[]
s=['a','e','i','o','u']
substr=[str[i:j] for i in range(len(str)) for j in range(i+1,len(str)+1)]
for ele in substr:
   for i in ele:
      if i in s:
        c+=1
   if(c==len(ele)):
      l.append(ele)
   c=0
print(l)
l.sort(key=len,reverse=True)
print(l)
print(l[0])
