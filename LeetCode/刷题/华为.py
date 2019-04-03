def pr(n,str1):
    if n<=0:
        return 
    list1=[]
    for i in range(n):
        a=str1[i*9:(i+1)*9]
        if a[0]=="0":
            a=a[1:]
            list1.append(a[::-1])
        else:
            a=a[1:]
            list1.append(a)
        if i<n-1:
            list1.append(' ')
    res=''
    for i in list1:
        res+=i
    return res

n=3
str1='012345678112345678087654321'
print(pr(n,str1))