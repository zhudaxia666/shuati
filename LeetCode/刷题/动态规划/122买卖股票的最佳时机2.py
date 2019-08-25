'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

只要第二天股票上升了，卖了就是赚了。实际上这种想法获得的利润跟上面的一样。基于这种想法，我们就可以写出状态转移方程：
dp[i] = dp[i-1] if prices[i]<=prices[i-1] else dp[i-1]+(prices[i]-prices[i-1])

也就是说：如果今天比昨天价更高，则dp[i] = dp[i-1]+高出的价格；反之，则不变
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                res += (prices[i]-prices[i-1])
        return res