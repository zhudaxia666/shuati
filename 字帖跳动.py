n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,list(input().split()))))
time=int(input())
class_time=list(map(int,list(input().split())))
if (class_time[1]-time)<0:
    class_time[0]-=1
    class_time[1]=abs(class_time[1]+60-time)
else:
    class_time[1]=class_time[1]-time
# print(class_time)
tmp=class_time[0]*60+class_time[1]
# print(tmp)
# fen=[]
min=float('inf')
index=0
for i in range(n):
    t=arr[i][0]*60+arr[i][1]
    # print(t)
    if t>tmp:
        continue
    if tmp-t<min:
        min=tmp-t
        index=i
# print(index)
for i in arr[index]:
    print(i,end=' ')


#第二道
# n,k=list(map(int,list(input().split())))
# string=list(map(int,list(input())))
# # print(n,k)
# # print(string)
# res=[]
# # length=1
# i=0
# tmp=0
# while len(res)<n:
#     if len(res)<k:
#         tmp=string[i]
#         if len(res)>0:
#             for j in res:
#                 tmp=tmp^j
#         # tmp=tmp^string[i]
#         res.append(tmp)
#     else:
#         tmp=string[i]
#         for j in res[-(k-1):]:
#             tmp=tmp^j
#         res.append(tmp)
#     # print(tmp)
#     i+=1
# for i in res:
#     print(i,end='')

n=int(input())
arr=list(map(int,list(input().split())))
res=[100]*n
# flag=[0]*n
for i in range(1,n-1):
    if arr[i]>arr[i-1] or arr[i]>arr[i+1]:
        res[i]+=100
        # flag[i]=1
    elif arr[i]<arr[i-1]:
        res[i-1]+=100
    elif arr[i]<arr[i+1]:
        res[i+1]+=100
print(sum(res))




