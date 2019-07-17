'''
解释一下这个公式怎么来的 (count[25] - 1) * (n + 1) + maxCount： 1.假设数组 ["A","A","A","B","B","C"]，n = 2，A的频率最高，记为count = 3，
所以两个A之间必须间隔2个任务，才能满足题意并且是最短时间（两个A的间隔大于2的总时间必然不是最短），因此执行顺序为： A->X->X->A->X->X->A，这里的X表示除了A以外其他字母，
或者是待命，不用关心具体是什么，反正用来填充两个A的间隔的。上面执行顺序的规律是： 有count - 1个A，其中每个A需要搭配n个X，再加上最后一个A，
所以总时间为 (count - 1) * (n + 1) + 1； 2.要注意可能会出现多个频率相同且都是最高的任务，比如 ["A","A","A","B","B","B","C","C"]，
所以最后会剩下一个A和一个B，因此最后要加上频率最高的不同任务的个数 maxCount；
 3.公式算出的值可能会比数组的长度小，如["A","A","B","B"]，n = 0，此时要取数组的长度。

 思路
完成所有任务的最短时间取决于出现次数最多的任务数量。
看下题目给出的例子
输入: tasks = ["A","A","A","B","B","B"], n = 2
输出: 8
执行顺序: A -> B -> (待命) -> A -> B -> (待命) -> A -> B.
因为相同任务必须要有时间片为 n 的间隔，所以我们先把出现次数最多的任务 A 安排上（当然你也可以选择任务 B）。例子中 n = 2，那么任意两个任务 A 之间都必须间隔 2 个单位的时间：
A -> (单位时间) -> (单位时间) -> A -> (单位时间) -> (单位时间) -> A
中间间隔的单位时间可以用来安排别的任务，也可以处于“待命”状态。当然，为了使总任务时间最短，我们要尽可能地把单位时间分配给其他任务。现在把任务 B 安排上：
A -> B -> (单位时间) -> A -> B -> (单位时间) -> A -> B
很容易观察到，前面两个 A 任务一定会固定跟着 2 个单位时间的间隔。最后一个 A 之后是否还有任务跟随取决于是否存在与任务 A 出现次数相同的任务。
该例子的计算过程为：
(任务 A 出现的次数 - 1) * (n + 1) + (出现次数为 3 的任务个数)，即：
(3 - 1) * (2 + 1) + 2 = 8
所以整体的解题步骤如下：

计算每个任务出现的次数
找出出现次数最多的任务，假设出现次数为 x
计算至少需要的时间 (x - 1) * (n + 1)，记为 min_time
计算出现次数为 x 的任务总数 count，计算最终结果为 min_time + count
特殊情况
然而存在一种特殊情况，例如：

输入: tasks = ["A","A","A","B","B","B","C","C","D","D"], n = 2
输出: 10
执行顺序: A -> B -> C -> A -> B -> D -> A -> B -> C -> D
此时如果按照上述方法计算将得到结果为 8，比数组总长度 10 要小，应返回数组长度。

作者：jalan
链接：https://leetcode-cn.com/problems/two-sum/solution/python-xiang-jie-by-jalan/
来源：力扣（LeetCode）
'''

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        length = len(tasks)
        if length <= 1:
            return length
        
        # 用于记录每个任务出现的次数
        task_map = dict()
        for task in tasks:
            task_map[task] = task_map.get(task, 0) + 1
        # 按任务出现的次数从大到小排序
        task_sort = sorted(task_map.items(), key=lambda x: x[1], reverse=True)
        
        # 出现最多次任务的次数
        max_task_count = task_sort[0][1]
        # 至少需要的最短时间
        res = (max_task_count - 1) * (n + 1)
        
        for sort in task_sort:
            if sort[1] == max_task_count:
                res += 1
        
        # 如果结果比任务数量少，则返回总任务数
        return res if res >= length else length

 

# from collections import defaultdict
# def leastInterval(tasks, n):
#     """
#     :type tasks: List[str]
#     :type n: int
#     :rtype: int
#     """
#     if len(tasks)<2:
#         return len(tasks)
#     res=[]
#     res.append(tasks.pop())
#     print(tasks)
#     while len(tasks)>0:
#         l=len(res)
#         for i in range(len(tasks)) :
#             if tasks[i] in res:
#                 if (len(res)-find_index(res,tasks[i]))<n+1:
#                     continue
#                 else:
#                     res.append(tasks[i])
#             else:
#                 res.append(tasks[i])
#         if len(res)!=l:
#             for i in res[l:]:
#                 tasks.remove(i)
#         if len(tasks)!=0:
#             res.append('0')
#         print(res)
#         print(tasks)
#     return len(res)
# def find_index(res,num):
#     dd=defaultdict(list)
#     for k,va in [(v,i) for i,v in enumerate(res)]:
#         dd[k].append(va)
#     return dd[num][-1]
# tasks = ["A","A","A","B","B","B"]
# n=2
# print(leastInterval(tasks,n))
# cc=[1,2,3,4,2]
# print(find_index(cc,2))