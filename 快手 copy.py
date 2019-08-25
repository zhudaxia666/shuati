# def fun(s):
#     a=s.replace('=','-(')+')'
#     c=eval(a,{'X':1j})
#     return -c.real /c.imag if c.imag else -1
# s=input()
# print(int(fun(s)))
n=int(input())
dis=list(map(int,input().split()))
e=list(map(int,input().split()))
res=[]

for i in range(n-1):
    tmp=0
    for j in range(i+1,n):
        tmp=max(tmp,dis[j]*2+e[j])
    tmp=max(dis[-1]*2+e[i],tmp)
    res.append(tmp)
for i in res:
    print(i)