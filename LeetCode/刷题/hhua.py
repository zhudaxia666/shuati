import sys
def dijian(a):
    if len(a)<=0:
        return 0
    # print(a)
    flag=0
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            flag+=1
    if flag>1:
        return 0
    else:
        return 1
# a=list(map(int,input().split()))
b=sys.stdin.readline().strip()
b=list(map(int,b.split()))
# print(dijian(a))
print(dijian(b))