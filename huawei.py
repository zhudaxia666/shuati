# import sys
# def fun(arr,n):
#     # if bit(arr[0])==2 and bit(arr[-1])==2:
#     #     flag=0
#     #     for i in range(1,n,1):
#     #         if abs(bit(arr[i])-bit(arr[i-1]))!=1:
#     #             flag=1
#     #             break
#     #     if flag:
#     #         return 'false'
#     #     else:
#     #     for i in range(1,n-1,1):
#     #         # print(arr[i],bit(arr[i]))
#     #         if bit(arr[i])!=1:
#     #             # print(arr[i])
#     #             return 'false'
#     #     return 'true'
#     # elif bit(arr[0])==1 and bit(arr[-1])==1:
#     #     for i in range(1,n-1,1):
#     #         if bit(arr[i])!=2:
#     #             return 'false'
#     #     return 'true'
#     # else:
#     flag=0
#     for i in range(1,n,1):
#         if abs(bit(arr[i])-bit(arr[i-1]))!=1:
#             flag=1
#             break
#     # return 'true'
#     if flag==1:
#         if bit(arr[0])==bit(arr[-1]):
#             for i in range(1,n-1,1):
#                 # print(arr[i],bit(arr[i]))
#                 if bit(arr[i])==bit(arr[-1]):
#                     # print(arr[i])
#                     return 'false'
#             return 'true'
#         else:
#             return 'false'
#     else:
#         return 'true'
# def bit(num):
#     b=num
#     c=0
#     while b!=0:
#         b=b//10
#         c+=1
#     return c
# # arr=list(map(int,input().split()))
# # print(arr)
# # if bit(arr[0]==2) and bit(arr[-1]==2):
# #     for i in range(1,n-1,1):
# #         print(arr[i],bit(arr[i]))
# #         if bit(arr[i])!=1:
# #             # print(arr[i])
# #             print(False)
# # print(fun(arr,len(arr)))
# res=[]
# # arr=list(map(int,s.split()))
# # n=len(arr)
# # res.append(fun(arr,n))


# while True:
#     s=sys.stdin.readline().strip()
#     if s=='':
#         break
#     arr=list(map(int,s.split()))
#     n=len(arr)
#     res.append(fun(arr,n))
# for i in res[:-1]:
#     print(i,end=' ')
# print(res[-1],end='')


# # while True:
# #     # s=input()
# #     # if len(s)==0:
# #     #     break
# #     arr=list(map(int,input().split()))
# #     n=len(arr)
# #     # for i in arr:
# #     #     print(bit(i))
# #     if n==0:
# #         for i in res[:-1]:
# #             print(i,end=' ')
# #         print(res[-1],end='')
# #         break
# #     else:
# #         res.append(fun(arr,n))
# # for i in res[:-1]:
# #     print(i,end=' ')
# # print(res[-1],end='')
# # s=list(input())
# # n=len(s)
# # res=[]
# # for i in range(n-1,-1,-1):
# #     if 'A'<=s[i] and s[i]<='Z':
# #         s[i]=s[i].lower()
# #     elif s[i]==' ':
# #         s[i]='0'
# #     res.append(s[i])
# # print(''.join(res))

# # import sys
# # a=[]
# # for i in sys.stdin:

# #     a.append(i.split())
# # print(i)
arr=list(map(int,input().split(',')))
target=arr[0]
tem=arr[1:]
tem.sort()
m=float('inf')
c=2
l=0
r=len(tem)-1
while l<r:
    if tem[l]+tem[r]>=target:
        if m>c:
            m=c
            break
    else:
        c+=1
        l+=1
print(m)