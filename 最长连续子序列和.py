def lianxu(arr):
    cur=0
    m=-float('inf')
    res=[]
    for i in arr:
        if cur<0:
            cur=i
        else:
            cur+=i
        if cur>m:
            m=cur
    return m
arr=list(map(int,input().split()))
print(lianxu(arr))