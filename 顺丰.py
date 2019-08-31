# def find(root):#查找根节点
#     son=root
#     while root!=pre[root]:#寻找根节点
#         root=pre[root]
#     while son!=root:#路径压缩
#         tmp=pre[son]
#         pre[son]=root
#         son=tmp
#     return root
# def join(root1,root2):
#     x=find(root1)
#     y=find(root2)
#     if x!=y:#如果不连通，就把他们所在的连通分支合并
#         pre[x]=y

# n,m,k=list(map(int,input().split()))
# arr=[]
# for i in range(k):
#     arr.append(list(map(int,input().split())))
# pre=[0]*(n+1)#存放第i个元素的父节点
# for i in range(1,n+1,1):#初始化并查集表
#     pre[i]=i
# total=n-1#共有num-1个门派
# for start in range(k-1):
#     for end in range(i+1,k):
#     # start,end=list(map(int,list(input().split())))
#     # end=list(map(int,list(input().split())))
#         root1=find(start)
#         root2=find(end)
#         if root1!=root2:#掌门不同，踢馆
#             pre[root1]=root2
#             total-=1#门派少一个，敌人就少一个
#     # k-=1
# print(total)

class Node():
    def __init__(self, x):
        self.val = x
        self.father = None
n, m, k = map(int, input().split(' '))
p_l = []
for i in range(k):
    p_l.append(list(map(int, input().split(' '))))
l_dict = {}
p_dict = {}
for i in p_l:
    l_dict[i[1]] = 1
    if i[0] not in p_dict:
        p_dict[i[0]] = []
    p_dict[i[0]].append(i[1])
for l in l_dict:
    l_dict[l] = Node(l)
for p in p_dict:
    p0 = p_dict[p][0]
    f0 = l_dict[p0]
    while f0.father:
        if f0.father.father:
            f0.father = f0.father.father
        f0 = f0.father
    for p1 in p_dict[p][1:]:
        f1 = l_dict[p1]
        while f1.father:
            if f1.father.father:
                f1.father = f1.father.father
            f1 = f1.father
        if f1 != f0:
            f1.father = f0
cont = n - len(p_dict)
if l_dict:
    cont -= 1
for l in l_dict:
    if not l_dict[l].father:
        cont += 1
print(cont)