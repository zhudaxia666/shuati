'''
3
10
V_0
V_1
V_2
P_3
P_4
P_5
V_6
P_7
V_8
V_9
'''
def fun(arr,n):
    res=[]
    tmp1=[]
    tmp2=[]
    index=0
    for i in range(len(arr)):
        if 'V' in arr[i]:
            res.append(arr[i])
        else:
            index=i
            break
    if index!=len(arr):
        res.append(arr[index])
    else:
        return arr
    if index==len(arr)-1:
        return arr
    else:
        for i in arr[index+1:]:
            if "V" in i:
                tmp2.append(i)
            else:
                tmp1.append(i)
        while len(tmp2)>=n-1:
            for i in range(n-1):
                res.append(tmp2.pop(0))
            if tmp1:
                res.append(tmp1.pop(0))
            else:
                break
        if len(tmp2)>0:
            res.extend(tmp2)
        return res
n=int(input())
m=int(input())
arr=[]
for i in range(m):
    arr.append(input())
tmp=fun(arr,n)
print(len(tmp))
for i in tmp:
    print(i)