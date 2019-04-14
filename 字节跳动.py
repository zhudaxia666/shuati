# # l=[]
# # while True:
# #     a=list(map(int,input().split()))
# #     if not a:
# #         break
# #     else:
# #         l.append(a)
# # print(l)
# # n=int(input())
# # num=[]
# # t=[]
# # if n==0:
# #     print(0)
# # else:
# #     for i in range(n):
# #         num=int(input())
# #         t=list(map(int,input().split()))
# n=int(input())
# if n==0:
#     print(0)
# else:
#     res=[]
#     for _ in range(n):
#         time=0
#         num=int(input())
#         t=list(map(int,input().split()))
#         if num<=3:
#             res.append(max(t))
#         else:
#             t=sorted(t)
#             min_time=t[:2]
#             t=t[2:]
#             while len(t)>1:
#                 time+=t.pop()
#                 time+=min(min_time)
#             time+=t[0]
#             res.append(time)       
# for i in res:
#     print(i)

n=int(input())
h=list(map(int,input().split()))
print(int(sum(h)/n))



    