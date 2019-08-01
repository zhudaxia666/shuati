def huan(A):
    if not A:
        return False
    dic={}
    for s in A[1:]:
        dic[s[0]]=s[-1]
    key=A[0][0]
    value=A[0][-1]
    res=[key,value]
    while true:
        if res[-1] in dic.keys():
            res.append(res[-1])
            value=
        else:
            return False
        
    if key not in dic.values():
        return False
    flag=0
    for k,v in dic.items():




A=input().strip().split()
print(huan(A))


