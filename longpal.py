str=input()
substr=[str[i:j] for i in range(len(str)) for j in range(i+1,len(str)+1)]
print(substr)
palindrome=[n for n in substr if(n[::-1]==n)]
print(palindrome)
max=-1
for ele in palindrome:
    if(len(ele)>max):
        max=len(ele)
        long=ele
print(long)
