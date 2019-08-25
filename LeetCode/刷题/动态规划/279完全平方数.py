'''
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
示例 1:

输入: n = 12
输出: 3 
解释: 12 = 4 + 4 + 4.
示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9.

思路：
这道题是一个典型的背包问题，当前正整数n的结果对应于n去掉一个完全平方数之后的子问题结果加一，但是去掉哪一个完全平方数才能达到最佳结果呢，这就需要我们自己去进行一个遍历，然后取最小的值即可。
动态规划递推公式如下：
dp[i] = min(dp[i], dp[i-j*j]+1)
'''
def numSquares(n):#超时
    dp=[i for i in range(n+1)]
    for i in range(1,n+1):
        j=1
        while i-j*j>=0:
            dp[i]=min(dp[i],dp[i-j*j]+1)
            j+=1
    return dp[n]
'''
BFs
使用python的动态规划会超时，我们换一种思路，采取BFS，每次遍历一轮n-ii的节点，将其加入队列中，然后进行下一轮的遍历，这样的话，当我们找到n-ii=0时，
一定是经历了最短的那个step（BFS采取一层一层的遍历）,
'''
class Node:
    def __init__(self,val,step=0):
        self.val=val
        self.step=step
class Solution:
    def numSquares(self,n):
        queue=[]
        step=0
        queue.append(Node(n))
        visited=[False for _ in range(n)]
        while len(queue)>0:
            root=queue.pop(0)
            num,step=root.val,root.step
            for i in range(1,n+1):
                if num-i*i<0:
                    break
                if num-i*i==0:
                    return step+1
                if visited[num-i*i]==False:
                    visited[num-i*i]=True
                    queue.append(Node(num-i*i,step+1))
        return -1


