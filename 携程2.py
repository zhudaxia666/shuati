s=list(input())
dic={}
res=[]
cur=0
for c in s:
    if c in dic:
        dic[c]-=1
        if dic[c]==0:
            del dic[c]
        if dic=={}:
            res.append(cur+1)
            cur=0
        else:
            cur+=1
    else:
        dic[c]=s.count(c)-1
        if dic[c]==0:
            del dic[c]
        if dic=={}:
            res.append(cur+1)
            cur=0
        else:
            cur+=1
for i in res[:-1]:
    print(i,end=',')
print(res[-1])