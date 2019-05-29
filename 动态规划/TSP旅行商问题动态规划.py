'''
解题思路主要有两部分：
      第一部分：i为当前节点（城市），S为还没有遍历的节点（城市集合），表示从第i个节点起，经历S集合中所有的点，到达终点的最短路径长度。因此有：e(i,S)=min(d(i,j)+e(j,S-j))
     第二部分，回溯，找到最优的路径，需要将S集合一一对应一个数字（类似于编码，一般用二进制），不如S={1,2,3}->2^1+2^2+2^3，然后比如从节点i等于0开始，未经历集合为S={1,2,3}，
而下一步最优的节点 j 等于2，那么M[i][S]=j，回溯时只用从M[0][S]向后推即可，例如M[0][S]=2->M[2][S-2]=3->M[3][S-2-3]，代码如下：
--------------------- 
原文：https://blog.csdn.net/yg838457845/article/details/81127697 

'''

# tsp问题
class Solution:
    def __init__(self,X,start_node):
        self.X = X #距离矩阵
        self.start_node = start_node #开始的节点
        self.array = [[0]*(2**len(self.X)) for i in range(len(self.X))] #记录处于x节点，未经历M个节点时，矩阵储存x的下一步是M中哪个节点
    def transfer(self,sets):
        su = 0
        for s in sets:
            su = su + 2**s # 二进制转换
        return su
    # tsp总接口
    def tsp(self):
        s = self.start_node
        num = len(self.X)
        cities = list(range(num)) #形成节点的集合
        past_sets = [s] #已遍历节点集合
        cities.pop(cities.index(s)) #构建未经历节点的集合
        node = s #初始节点
        return self.solve(node,cities) #求解函数
    def solve(self,node,future_sets):
        # 迭代终止条件，表示没有了未遍历节点，直接连接当前节点和起点即可
        if len(future_sets) == 0:
            return self.X[node][self.start_node]
        d = 99999
        # node如果经过future_sets中节点，最后回到原点的距离
        distance = []
        # 遍历未经历的节点
        for i in range(len(future_sets)):
            s_i = future_sets[i]
            copy = future_sets[:]
            copy.pop(i) # 删除第i个节点，认为已经完成对其的访问
            distance.append(self.X[node][s_i] + self.solve(s_i,copy))
        # 动态规划递推方程，利用递归
        d = min(distance)
        # node需要连接的下一个节点
        next_one = future_sets[distance.index(d)]
        # 未遍历节点集合
        c = self.transfer(future_sets)
        # 回溯矩阵，（当前节点，未遍历节点集合）——>下一个节点
        self.array[node][c] = next_one
        return d
D = [[-1,10,20,30,40,50],[12,-1,18,30,25,21],[23,19,-1,5,10,15],[34,32,4,-1,8,16],[45,27,11,10,-1,18],[56,22,16,20,12,-1]]
S = Solution(D,0)
print (S.tsp())
# 开始回溯
M = S.array
lists = list(range(len(S.X)))
start = S.start_node
while len(lists) > 0:
    lists.pop(lists.index(start))
    m = S.transfer(lists)
    next_node = S.array[start][m]
    print (start,"--->" ,next_node)
    start = next_node
