# T=int(input())
# for i in range(T):
#     n=int(input())
#     nums=list(map(int,input().split()))
#     print(nums)
#     tmp=[]
#     flag=0
#     for num in nums:
#         if num in tmp:
#             flag=1
#             break
#         else:
#             tmp.append(num)
#     if flag:
#         print("NO")
#     else:
#         print("YES")

#2 ----------------------
# t,k=list(map(int,input().split()))
# res=[]
# for i in range(t):
#     a,b=list(map(int,input().split()))
#     count=0
#     for i in range(a,b+1):
#         #tmp=[]
#         for j in range(0,i+1,k):
#             #tmp.extend([0]*j+[1]*(i-j))#0表示白花
#             count+=i-j
#     res.append(count)
# for i in res:
#     print(i-1)
#3--------
from fractions import Fraction
def fun(n):
    if n==0 or n==1:
        return 1
    sum1=1
    for i in range(1,n+1):
        sum1*=i
    return sum1
n,p,q=list(map(int,input().split()))
s=0
tmp=fun(n)
for i in range(p,n-q+1):
    t=fun(i)*fun(n-i)
    s+=Fraction(tmp,t)
s=Fraction(s,pow(2,n))
# print(s)
s=str(s).split('/')
print((int(s[1])+1000000007)//int(s[0]))