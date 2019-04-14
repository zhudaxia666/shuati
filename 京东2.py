# def huanyuan(m,l):
#     index=l.index(0)
#     if index==0:
#         return l[1]
#     else:
#         return 1



# n=int(input())
# l=list(map(int,input().split()))
# print(huanyuan(n,l))
#coding:utf8
def outer(x):
    def inner(y):
        nonlocal x
        x+=y
        return x
    return inner


a = outer(10)
print(a(1)) #11
print(a(3)) #14
print(a(3))