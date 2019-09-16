# n=int(input())
# arr=[]
# for i in range(n):
#     arr.append(int(input()))
# res=[1]*n
# for i in range(1,n):
#     if arr[i]>arr[i-1]:
#         res[i]=res[i-1]+1
# for i in range(n-2,-1,-1):
#     if arr[i]>arr[i+1]:
#         res[i]=max(res[i],res[i+1]+1)
# # print(res)
# print(sum(res))
m=int(input())
n=int(input())
res=[]
for i in range(m):
    res.append(list(map(int,input().split())))
dp=[[0]*len(n) for _ in range(m)]
dp[0][0]=res[0][0]
for i in range(1,n):
    dp[0][i]=dp[0][i-1]+res[0][i]
for j in range(1,m):
    dp[j][0]=dp[j-1][0]+res[j][0]
for i in range(1,m):
    for j in range(1,n):
        dp[i][j]=res[i][j]+min(dp[i-1][j],dp[i][j-1])
print(dp[m-1][n-1])