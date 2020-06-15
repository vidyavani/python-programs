student=[]
    scorelist=[] 
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student+=[[name,score]]
        scorelist+=[score]
    scorelist=set(scorelist)
    scorelist=sorted(scorelist)
    sm=scorelist[1]
    for n,s in sorted(student):
        if sm==s:
           print(n)
