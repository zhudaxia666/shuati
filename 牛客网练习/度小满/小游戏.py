t=int(input())
for i in range(t):
    a,b,n=list(map(int,input().split()))
    # print(a,b,n)
    res=0
    index=0
    tmp=-1
    while res<n:
        if tmp==res:
            break
        else:
            tmp=res
        if pow(a+1,b)<pow(a,b+1):
            a=a+1
            # res=pow(a+1,b)
        else:
            b=b+1
            # res=pow(a,b+1)
        res=pow(a,b)
        # print(res,tmp)
        
        index+=1
    # print(tmp,res)
    if tmp==res:
        print('A&B')
    else:
        if index%2==1:
            print('A')
        else:
            print('B')