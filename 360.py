def tran(num,b):
    tmp=-float('inf')
    for i in range(len(b)):
        if (num+b[i])%m>tmp:
            b1=b[i]
            tmp=(num+b[i])%m
    return (num+b1)%m,b1




n,m=list(map(int,input().split()))
a=list(map(int,list(input().split())))
b=list(map(int,list(input().split())))
a=sorted(a)
b=sorted(b)
res=[]
i=0
flag=True
for i in range(n):
    if flag:
        t1,t2=tran(a[i],b)
        res.append(t1)
        # b.remove(t2)
    else:
        t1,t2=tran(b[i],a)
        res.append(t1)
        # a.remove(t2)
    flag=not flag
for i in res:
    print(i,end=' ')


    


# for i in range(len(a)):
#     tmp=-float('inf')
#     for j in range(len(b)):
#         if (a[i]+b[j])%m>tmp:
#             a1=a[i]
#             b1=b[j]
#             tmp=(a[i]+b[j])%m
#     res.append((a1+b1)%m)
#     a.remove(a1)
#     b.remove(b1)
# print(res)
