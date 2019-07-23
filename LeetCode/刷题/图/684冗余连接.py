'''
在本问题中, 树指的是一个连通且无环的无向图。
输入一个图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。
结果图是一个以边组成的二维数组。每一个边的元素是一对[u, v] ，满足 u < v，表示连接顶点u 和v的无向图的边。
返回一条可以删去的边，使得结果图是一个有着N个节点的树。如果有多个答案，则返回二维数组中最后出现的边。答案边 [u, v] 应满足相同的格式 u < v。
示例 1：
输入: [[1,2], [1,3], [2,3]]
输出: [2,3]
解释: 给定的无向图为:
  1
 / \
2 - 3
示例 2：
输入: [[1,2], [2,3], [3,4], [1,4], [1,5]]
输出: [1,4]
解释: 给定的无向图为:
5 - 1 - 2
    |   |
    4 - 3

思路：使用并查集
实现了并查集查找根节点的代码，并且做了路径压缩，防止树太高导致查找根节点缓慢。
具体到这个题，虽然说是返回最后一个边，但我们知道只需要去除一条边就够了，之前的边不会构成环，直至多余的那条边出现。
另外要注意，当一条边的左右节点的根节点不同时，要把他们设置相同，这样等下次判断某条边的左右节点相同的情况时，说明是多余的那条边了。

关于并查集对知识见链接：https://blog.csdn.net/niushuai666/article/details/6662911
'''
class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        tree = [-1] * (len(edges) + 1)
        for edge in edges:
            a = self.findRoot(edge[0], tree)
            b = self.findRoot(edge[1], tree)
            if a != b:
                tree[a] = b
            else:
                return edge
        
        
    def findRoot(self, x, tree):
        if tree[x] == -1: return x
        else:
            root = self.findRoot(tree[x], tree)
            tree[x] = root
            return root