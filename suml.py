l=[]
list=[int(item) for item in input().split()]
n=int(input())
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if sum(l)<n:
          l.append(list[j])
          l.append(list[i])
          for i in range(len(l)):
              if(sum(l)>n):
                 l.pop()
          if(sum(l)==n):
            print(str(l),end=" ")
            l.clear()
        
