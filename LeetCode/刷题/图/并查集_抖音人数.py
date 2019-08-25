'''
n个人之间存在m个关系对，关系具有传递性，假如A关注B，B关注C，那么A就间接关注了C。如果一个人被除他之外的所有人都直接或间接关注，
那么这个人就是抖音红人，求抖音红人的总数。
'''


def find(root):#查找根节点
    son=root
    while root!=pre[root]:#寻找根节点
        root=pre[root]
    while son!=root:#路径压缩
        tmp=pre[son]
        pre[son]=root
        son=tmp
    return root
def join(root1,root2):
    x=find(root1)
    y=find(root2)
    if x!=y:#如果不连通，就把他们所在的连通分支合并
        pre[x]=y
'''
n个人之间存在m个关系对，关系具有传递性，假如A关注B，B关注C，那么A就间接关注了C。
如果一个人被除他之外的所有人都直接或间接关注，那么这个人就是抖音红人，求抖音红人的总数。
'''
n,m=list(map(int,input().split()))
pre=[0]#存放第i个元素的父节点
# total=n-1#共有n-1个门派
for i in range(1,n+1,1):#初始化并查集表
    pre.append([i])
# total=n-1#共有num-1个门派
print(pre)
count=0
while m:
    start,end=list(map(int,list(input().split())))
    # print(pre[end].append(start))
    # end=list(map(int,list(input().split())))
    pre[end]=list(set(pre[end]+pre[start]))
    # if not pre[start]:
    #     pre[end].append(start)
    # else:
    #     pre[end].append(start).extends(pre[start])
    m-=1
print(pre)
for i in range(1,n+1):
    if len(pre[i])==n:
        count+=1
print(count)
'''
数据是一个有向图，(A,B)代表A关注B，那么在这条关系在图中，存B指向A。 
要考虑个整个图可能不是连通的，所以需要对每个节点分别进行深度遍历。 
对每个节点进行深度遍历：每调用一次就让这个节点的粉丝数加1，注意在递归函数调用中，需要建立一个visited数组，代表节点以访问过，访问过的就不能遍历下去。 
每次深度遍历开始前，对visited清空，再对visited[起点]=True，代表起点已经走过了。
'''
from collections import defaultdict
n=2
m=3
li=[1,2,2,1,2,1]
son=defaultdict(list)
fans=[1]*n
visited=[False]*n
def findson(origin,i):
    for j in s[i]:
        if visited[j]!=True:
            fans[origin]+=1
            visited[j]=True
            findson(origin,j)
for i in range(m):
    a=2*i
    b=2*i+1
     #a关注b
    son[li[b]-1].append(li[a]-1)
    #原输入是123，那么程序里就是012
#建立好了有向图
for i in range(n):
    visited=[False]*n
    visited[i]=True
    findson(i,i)
count=0
for i in fans:
    if i==n:#如果粉丝为n
        count+=1
print(count)






