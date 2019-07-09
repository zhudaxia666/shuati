'''
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
如果没有任何一种硬币组合能组成总金额，返回 -1。
示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3 
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1

'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[-1]*(amount+1)
        dp[0]=0#金额0最优解0
        for i in range(amount+1):
            for j in range(len(coins)):#循环各个面值，找到dp[i]最优解
                if (i-coins[j])>=0 and dp[i-coins[j]]!=-1:#递推条件
                    if dp[i]==-1 or dp[i]>dp[i-coins[j]]+1:
                        dp[i]=dp[i-coins[j]]+1
        return dp[amount]

''''
假设 f(n) 代表要凑齐金额为 n 所要用的最少硬币数量，那么有：
f(n) = min(f(n - c1), f(n - c2), ... f(n - cn)) + 1
其中 c1 ~ cn 为硬币的所有面额
'''
class Solution1(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        res = [0 for _ in range(amount + 1)]
        
        for i in range(1, amount + 1):
            cost = float('inf')
            for c in coins:
                if i - c >= 0:
                    cost = min(cost, res[i - c] + 1)
            res[i] = cost
        
        if res[amount] == float('inf'):
            return -1
        else:
            return res[amount]
