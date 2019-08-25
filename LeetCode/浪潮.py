from collections import OrderedDict
def test(arr):
    tmp=OrderedDict()
    for i in range(len(arr)-1):
        if i==0 and arr[i]!=1:
            tmp[1]=(arr[i]-1)//2
        else:
            tmp[i]=(arr[i+1]-arr[i])//2+1
    tmp[arr[-1]+2]=(99-arr[-1])//2+1
    return sorted(tmp.items(),key=lambda x:x[1],reverse=True)

n=int(input())
arr=list(map(int,input().split()))
odd=[]
os=[]
for i in arr:
    if i%2==0:
        os.append(i)
    else:
        odd.append(i)
os.sort()
odd.sort()

if len(odd)!=0 and len(os)!=0:
    t1=test(odd)
    t2=test(os)
    if t1[0][1]>=t2[0][1]:
        print(t1[0][0],end=' ')
        print(t1[0][1])
    else:
        print(t2[0][0],end=' ')
        print(t2[0][1])
elif len(odd)!=0 and len(os)==0:
    t1=test(odd)
    print(t1[0][0],end=' ')
    print(t1[0][1])
elif len(odd)==0 and len(os)!=0:
    t1=test(os)
    print(t1[0][0],end=' ')
    print(t1[0][1])
else:
    print()