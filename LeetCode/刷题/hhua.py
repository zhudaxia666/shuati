n=int(input())
l=[[0]*3 for _ in range(4)]
for i in range(n):
    a=input().split()
    x,y=int(a[0]),int(a[-1])
    l[x][y]=1
print(l)
