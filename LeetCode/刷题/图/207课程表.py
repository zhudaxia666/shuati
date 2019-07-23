'''
拓扑排序实际上应用的是贪心算法。贪心算法简而言之：每一步最优，全局就最优。
具体到拓扑排序，每一次都输出入度为 00 的结点，并移除它、修改它指向的结点的入度，依次得到的结点序列就是拓扑排序的结点序列。如果图中还有结点没有被移除，则说明“不能完成所有课程的学习”。
拓扑排序保证了每个活动（在这题中是“课程”）的所有前驱活动都排在该活动的前面，并且可以完成所有活动。拓扑排序的结果不唯一。拓扑排序还可以用于检测一个有向图是否有环。相关的概念还有 AOV 网，这里就不展开了。
具体做如下：
1、在开始排序前，扫描对应的存储空间（使用邻接表），将入度为 00 的结点放入队列。
2、只要队列非空，就从队首取出入度为 00 的结点，将这个结点输出到结果集中，并且将这个结点的所有邻接结点（它指向的结点）的入度减 11，在减 11 以后，如果这个被减 11 的结点的入度为 00 ，就继续入队。
3、当队列为空的时候，检查结果集中的顶点个数是否和课程数相等即可。

思考这里为什么要使用队列？（马上就会给出答案。）
在代码具体实现的时候，除了保存入度为 0 的队列，我们还需要两个辅助的数据结构：
1、邻接表：通过结点的索引，我们能够得到这个结点的后继结点；
2、入度数组：通过结点的索引，我们能够得到指向这个结点的结点个数。
'''

class Solution(object):

    # 思想：该方法的每一步总是输出当前无前趋（即入度为零）的顶点

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        :type numCourses: int 课程门数
        :type prerequisites: List[List[int]] 课程与课程之间的关系
        :rtype: bool
        """
        # 课程的长度
        clen = len(prerequisites)
        if clen == 0:
            # 没有课程，当然可以完成课程的学习
            return True

        # 步骤1：统计每个顶点的入度
        # 入度数组，记录了指向它的结点的个数，一开始全部为 0
        in_degrees = [0 for _ in range(numCourses)]
        # 邻接表，使用散列表是为了去重
        adj = [set() for _ in range(numCourses)]

        # 想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
        # [0, 1] 表示 1 在先，0 在后
        # 注意：邻接表存放的是后继 successor 结点的集合
        for second, first in prerequisites:
            in_degrees[second] += 1
            adj[first].add(second)

        # 步骤2：拓扑排序开始之前，先把所有入度为 0 的结点加入到一个队列中
        # 首先遍历一遍，把所有入度为 0 的结点都加入队列
        queue = []
        for i in range(numCourses):
            if in_degrees[i] == 0:
                queue.append(i)

        counter = 0
        while queue:
            top = queue.pop(0)
            counter += 1
            # 步骤3：把这个结点的所有后继结点的入度减去 1，如果发现入度为 0 ，就马上添加到队列中
            for successor in adj[top]:
                in_degrees[successor] -= 1
                if in_degrees[successor] == 0:
                    queue.append(successor)

        return counter == numCourses

def canFinish(self,numCourses,prep):
    if len(prep)==0:
        return True
    in_degrees=[0 for _ in range(numCourses)]
    adj=[[] for _ in range(numCourses)]

    for a,b in prep:
        in_degrees[a]+=1
        adj[b].append(a)
    queue=[]
    for i in range(numCourses):
        if in_degrees[i]==0:
            queue.append(i)
    
    count=0
    while queue:
        top=queue.pop(0)
        count+=1
        for i in adj[top]:
            in_degrees[i]-=1
            if in_degrees[i]==0:
                queue.append(i)
    return count==numCourses