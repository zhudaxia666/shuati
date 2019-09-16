def delchar(s):
    c=0
    res=[]
    for ch in s:
        if ch=='(':
            c+=1
        elif ch==')':
            c-=1
        elif c==0:
            if ch=='<':
                if len(res)>0:
                    res.pop()
            else:
                res.append(ch)
    return res
    
s=input()
print(''.join(delchar(s)))

#第三题减leetcode354
# def lengthLTS(nums):
#     size=len(nums)
#     if size<2:
#         return size
#     dp=[1]*size
#     for i in range(1,size):
#         for j in range(i):
#             if nums[i]>nums[j]:
#                 dp[i]=max(dp[i],dp[j]+1)
#     return max(dp)
# n=int(input())
# res=[]
# for i in range(n):
#     res.append(list(map(int,input().split())))
# res.sort()
# # print(res)
# tmp=[]
# for i in range(n):
#     tmp.append(res[i][1])
# # print(tmp)
# print(lengthLTS(tmp))
