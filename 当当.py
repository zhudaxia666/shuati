def code(arr,l,r,num):
    less=l-1
    more=r+1
    cur=l
    while cur<more:
        if arr[cur]<num:
            less+=1
            arr[cur],arr[less]=arr[less],arr[cur]
            cur+=1
        elif arr[cur]>num:
            more-=1
            arr[cur],arr[more]=arr[more],arr[cur]
        else:
            cur+=1
    return arr
arr=list(map(int,input().split(',')))

for i in range(len(arr)-1):
    print(i,end=",")
print(arr[-1])



def fun1(s):
    if not s or len(s)>12 or len(s)<4:
        return  ''
    res=[]
    tmp=''
    k=4
    def fun2(s,k,tmp,res):
        if k==0:
            if not s:
                res.append(tmp)
        else:
            for i in range(1,4):
                if len(s)>=i and fun3(s[:i]):
                    if k==1:
                        fun2(s[i:],k-1,tmp+s[:i],res)
                    else:
                        fun2(s[i:],k-1,tmp+s[:i]+'.',res)
    fun2(s,k,tmp,res)
    return res
def fun3(s):
    if not s or len(s)>3 or (len(s)>1 and s[0]=='0'):
        return False
    r=int(s)
    return r<=255 and r>=0

s=input()
r=fun1(s)
print(','.join(r))
