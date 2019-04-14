# def mintime(m,list1):

n=int(input())
l=[]
for i in range(n-1):
    l.append(list(map(int,input().split())))
# print(sorted(l))
s=[]
for i in range(1,n+1,1):
    tem=[]
    for j in l:
        if i in j and :
            index=j.index(i)
            tem.append(j[1-index])
    s.append(tem)
print(s)
# num=0
# while s[0]:
#     num+=1
#     l=[]
#     for i in range(len(s[0])):
#         l.append(s[0].pop)
#     # num+=1 
#     if l:
#         num+=1
#         for i in l:
#             if s[i-1]:
#                 b=s[i-1].pop()
#                 if s[b-1]:
#                     s[i-1].append(s[b-1][0])
#                 s[0].append(b)
# print(num)

        

    