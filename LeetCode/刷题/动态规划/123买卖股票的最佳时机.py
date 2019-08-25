'''
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
'''
l=len(prices)
if l<2:
    return 0
res=0
#先算一个dp1数组
#dp1[i]表示截止到第i-1天只进行一次买卖的最大利润
dp1=[0 for i in range(l)]
max_price,min_price=prices[0],prices[0]
for i in range(1,l):
    dp1[i]=max(dp1[i-1],prices[i]-min_price)
    #对于第i天来说，1.如果当天卖：最大利润即当前卖出价格
    #减去之前的最小买入价格，2如果不卖：最大利润和前一天的
    #最大利润相同
    min_price=min(min_price,prices[i])  #更新当前最小买入价格
    max_price=max(max_price,prices[i])  #更新当前最大卖出价格
#对于任意k，dp1[k]表示k卖出的最大利润，
#那么需要求剩下k+1到n-1的最大利润
#倒着求，因为右边界不变始终为l-1，左边界在变化
#dp2[i]表示从i开始到最后只进行一次买卖的最大利润
res=dp1[-1]
# print(res)
dp2=[0 for i in range(l)]
max_price=prices[-1]
for i in range(l-2,-1,-1):
    dp2[i]=max(dp2[i+1],max_price-prices[i])
    #对于第i天，1.若当天买，则最大利润即之后的最大卖出价格减去
    #当前买入价格，2.若当天不买，最大利润和后一天的最大利润相同
    max_price=max(max_price,prices[i])  #更新当前最大卖出价格
    res=max(res,dp1[i-1]+dp2[i]) if i>=1 else max(res,dp2[i])
# print(dp1)
# print(dp2)
return res
'''
一个方法团灭6道股票问题
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/yi-ge-fang-fa-tuan-mie-6-dao-gu-piao-wen-ti-by-l-3/

'''

'''
dp[k][i]到第i天经过k次交易得到最大的利润.
动态方程: dp[k][i] = max(dp[k][i-1], dp[k-1][j-1] + prices[i] - prices[j]) 0 <=j <= i
有一个小技巧技术 把dp[k-1][j-1] - prices[j]看成一个整体, 因为j独立与i,可以减少最内侧的循环.
换句话说,就是先求dp[k-1][j-1] - prices[j]最大值, 再求+ prices[i]的最大值, 


链接：https://leetcode-cn.com/problems/two-sum/solution/dong-tai-gui-hua-by-powcai-7/
'''
def maxProfit(prices):
    if not prices:
        return 0
    n=len(prices)
    dp=[[0]*n for _ in range(3)]
    for k in range(1,3):
        premax=-prices[0]
        for i in range(1,n):
            premax=max(premax,dp[k-1][i-1]-prices[i])
            dp[k][i]=max(dp[k][i-1],prices[i]+premax)
    return dp[-1][-1]
#时间复杂度为O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        k=2
        buy = [float('-inf') for _ in range(k)]
        sell = [float('-inf') for _ in range(k)]
        for price in prices:
            buy[0] = max(buy[0],-price)
            sell[0] = max(sell[0],buy[0]+price)
            for i in range(1,k):
                buy[i] = max(buy[i],sell[i-1]-price)
                sell[i] = max(sell[i],buy[i]+price)
        return sell[-1]