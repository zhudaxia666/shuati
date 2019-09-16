# s,m=list(map(int,input().split()))
# w=[0]*s
# v=[0]*s
# for i in range(s):
# 	w[i],v[i]=list(map(int,input().split()))
# def bags(v,w,bagv):
#     row=len(v)
#     col=bagv
#     dp=[[0]*(col+1) for i in range(row+1)]
#     for i in range(1,row):
#         for j in range(1,col+1):
#             if j<w[i]:
#                 dp[i][j]=dp[i-1][j]
#             else:
#                 dp[i][j]=max(dp[i-1][j],dp[i-1][j-w[i]]+v[i])
#     print(dp[row-1][col])3
# def bag(n,m,w,v):
#     value=[0 for i in range(m+1)]
#     for i in range(1,n+1):
#         for j in range(m,0,-1):
#             if j>=w[i-1]:
#                 value[j]=max(value[j-w[i-1]]+v[i-1],value[j])
#     print(value[-1])
# # w=[0,15,10,12,8]
# # v=[0,12,8,9,5]
# bag(s,m,w,v)

#第一题
# s,n=input().split()
# n=int(n)
# length=len(s)
# tmp=list(map(int,s))
# # print(tmp,n)
# res=[]
# i=0
# su=0
# while i<length-n:
#     m=max(tmp)
#     index=tmp.index(m)
#     # res.append(index)
#     su=su*10+m
#     tmp[index]=-1
#     i+=1
#     print(tmp)
# res.sort()
# su=0
# for i in res:
#     su=su*10+int(s[i])
# print(su)
# s=list(s)
# if len(s)==n:
#     print(0)
# else:
#     while n!=0:
#         i=0
#         while len(s)-1>i and s[i]>s[i+1]:
#             i+=1
#         s.pop(i)
#         n-=1
#     while len(s)!=0:
#         s.pop()
#     if len(s)==0:
#         print(0)
#     else:
#         print(s)

# print(res)
def removeKdigits(num, k):
    num_length = len(num)
    if num_length <= k:
        return "0"
    
    left_count = num_length - k
    res = ""
    count = 0
    begin = 0
    
    while count < left_count:
        min_index = 0
        min_num = float('inf')
        for i in range(begin, k + count + 1):
            # 找到最小数
            if int(num[i]) < min_num:
                min_index = i
                min_num = int(num[i])
        # 把找到的最小数加入结果列表
        res += str(min_num)
        # 设置下一轮查找范围的起点
        begin = min_index + 1
        count += 1
        
    return "0" if len(res) == 0 else str(int(res))

n,m=input().split()
l = len(n)
m = int(m)
s=0 
begin = 0 
t = m 
for j in range(l-m):
    maxx = '0'  
    for i in range(begin,t+1): 
        if maxx<n[i]:
            p=i
            maxx = n[i]  
    print(maxx,end='')
    begin = p+1  
    t = t+1
print(removeKdigits(n,m))