# n=int(input())
# res=[]
# for i in range(n):
# 	res.append(input().split(' '))
# # print(res)
# res.sort(key=lambda x:x[1])
# # print(res)
# m=0
# s=0
# for i in range(n):
#     if res[i][0]=='1':
#         m+=1
#         s+=(i+1)
# # print(s,m)
# tmp=(s-(m*(m+1))/2)/(m*(n-m))
# print('%.2f' %tmp)
def fun(s):
    l=len(s)
    n=[0]*l
    for i in range(1,l):
        t=n[i-1]
        while s[i]!=s[t] and t:
            t=n[t-1]
        if s[i]==s[t]:
            n[i]=t+1
    p=n[-1]
    return p>0 and l%(l-p)==0
while True:
    s=input()
    if len(s)>0:
        print(fun(s))
    else:
        break

def fun(s,t):
    for i in range(len(s)):
        if s[i]>t:
            return True
    return False
def fun1(s,t):
    for i in range(len(s)):
        if s[i]>t:
            return i
s=list(input())
dic={}
for i,v in enumerate(s):
    if v not in dic:
        dic[v]=[i]
    else:
        dic[v].append(i)
res=[]
t=-1
ch=''
for i in sorted(dic.keys()):
    if fun(dic[i],t):
        if fun1(dic[i],t)==0:
            res.append(dic[i][-1]-dic[i][0]+1)
        else:
            res.pop()
            res.append(dic[i][-1]-dic[ch][0]+1)
        t=dic[i][-1]
        ch=i
        if sum(res)==len(s):
            break
for i in res[:-1]:
    print(i,end=',')
print(res[-1])
