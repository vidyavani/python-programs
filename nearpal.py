str=input()
if(len(str)%2==0):
    m=str[:len(str)//2]
    n=m+m[::-1]
    print(int(n))
else:
    m=str[:len(str)//2]
    ch=str[len(str)//2+1]
    n=m+ch+m[::-1]
    print(int(n))
    
