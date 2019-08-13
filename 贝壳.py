# def GetResult(K):
#     s=1
#     i=1
#     while s<=K:
#         i+=1
#         s+=1/i
#     return i

# _K = int(input())
# res = GetResult(_K)
# print(res)

# arr=list(map(int,list(input().split())))
# a=arr[0]
# j=len(arr)-1
# while a==a[]
n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,list(input().split()))))
fa=arr[0][0]+arr[0][2]
fb=arr[0][1]
for i in range(1,n):
    fa=min(fa+arr[i][0],fb+arr[i][2]+arr[i][0])
    fb=min(fb+arr[i][1],fa+arr[i][2]+arr[i][1])
print(min(fa,fb))
# dp=[0]*n
# index=[]
# if arr[0][0]+arr[0][2]>=arr[0][1]:
#     dp[0]=arr[0][1]
#     index.append(1)
# else:
#     dp[0]=arr[0][0]+arr[0][2]
#     index.append(0)
# for i in range(1,n):
#     tmp=1 if index[i-1]==0 else 0
#     if dp[i-1]+arr[i][index[i-1]]>dp[i-1]+arr[i][2]+arr[i][tmp]:
#         dp[i]=dp[i-1]+arr[i][2]+arr[i][tmp]
#         index.append(tmp)
#     else:
#         dp[i]=dp[i-1]+arr[i][index[i-1]]
#         index.append(index[i-1])
# print(dp[-1])


