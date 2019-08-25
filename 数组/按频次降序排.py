def sort(li):
    a={}
    res=[]
    for i in li:
        a[i]=a.get(i,0)+1
    a=sorted(a.items(),key=lambda item:item[1],reverse=True)
    print(a)
    for key in a:
        res.extend([key[0]]*key[1])
    print(res)
sort([1,3,3,1,1,1,4,4,6,6,6])
