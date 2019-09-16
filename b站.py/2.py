n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
tem=sorted(arr,key=lambda x:x[1])

m=tem[-1][0]
for i in range(len(tem)-1,0,-1):
    if tem[i][1]==tem[i-1][1]:
        m=max(tem[i][0],tem[i-1][0])
    else:

        break
print(m)

# tem=sorted(dic.item,key=lambda x:x[1])