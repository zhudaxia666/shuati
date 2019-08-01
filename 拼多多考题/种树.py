m=int(raw_input())
a=map(int,[i for i in raw_input().split()])
maxi=max(a)
summ=sum(a)
if maxi>(summ+1)/2:
    print "-"
else:
    res=[]
    left=summ
    pre=-1
    while left>0:
        i=0
        flag=0
        while i<m:
            if a[i]>(left)/2:
                res.append(i+1)
                left-=1
                a[i]-=1
                pre=i
                flag=1
                break
            else:
                i+=1
        if flag==1:
            continue
        j=0
        while a[j]==0 or j==pre:
            j+=1
        res.append(j+1)
        left-=1
        a[j]-=1
        pre=j
    print " ".join(map(str,res))