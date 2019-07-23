'''
给定一个无向图graph，当这个图为二分图时返回true。

如果我们能将一个图的节点集合分割成两个独立的子集A和B，并使图中的每一条边的两个节点一个来自A集合，一个来自B集合，我们就将这个图称为二分图。

graph将会以邻接表方式给出，graph[i]表示图中与节点i相连的所有节点。每个节点都是一个在0到graph.length-1之间的整数。这图中没有自环和平行边： graph[i] 中不存在i，并且graph[i]中没有重复的值。


示例 1:
输入: [[1,3], [0,2], [1,3], [0,2]]
输出: true
解释: 
无向图如下:
0----1
|    |
|    |
3----2
我们可以将节点分成两组: {0, 2} 和 {1, 3}。

示例 2:
输入: [[1,2,3], [0,2], [0,1,3], [0,2]]
输出: false
解释: 
无向图如下:
0----1
| \  |
|  \ |
3----2
我们不能将节点分割成两个独立的子集。
'''
''''
思路：一个节点染成红色,我们把它相连的节点染成蓝色,如果当两种颜色相同的也连接了,说明不是二分图.
采用BFS或者DFS都可以解决此题。首先所有结点的初始状态都为为染色状态，用0表示。依次遍历邻接表中每个结点的邻接结点是否与当前状态以及邻接结点的邻接结….
是否发生冲突，
即当前节点与邻接结点用1和-1表示代表已经染色，如果当前节点与其邻接结点已经染色并且染色号相同即代表不能把他们分别放到两个空间内此时返回false。 
'''
#dfs
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [0] * n
        # 0 未被染色的 1 是红色 -1 是蓝色
        def dfs(i,color):
            if colors[i] != 0:
                return colors[i] == color
            colors[i] = color
            for j in graph[i]:
                if not dfs(j,-color):
                    return False
            return True
        for  i in range(n):
            if colors[i] == 0 and not dfs(i,1):
                return False
        return True
#bfs
class Solution1:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        from collections import deque
        n = len(graph)
        colors = [0] * n
        # 0 未被染色的 1 是红色 -1 是蓝色
        for i in range(n):
            if colors[i] != 0:
                continue
            colors[i] = 1
            q = deque()
            q.appendleft(i)
            while q:
                cur = q.pop()
                for tmp in graph[cur]:
                    if colors[tmp] == 0:
                        colors[tmp] = -colors[cur]
                        q.appendleft(tmp)
                    elif colors[tmp] == colors[cur]:
                        return False
        return True
class Solution2(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n=len(graph)
        colors=[0]*n
        for i in range(n):
            if colors[i]!=0:
                continue
            colors[i]=1
            q=[]
            q.insert(0,i)
            while q:
                cur=q.pop()
                for tmp in graph[cur]:
                    if colors[tmp]==0:
                        colors[tmp]=-colors[cur]
                        q.insert(0,tmp)
                    elif colors[tmp]==colors[cur]:
                        return False
        return True
        

