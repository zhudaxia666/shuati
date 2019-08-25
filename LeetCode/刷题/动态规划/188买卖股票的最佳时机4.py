'''
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
'''
'''
Python T123股票最大收益问题要求的是最多k=2次交易，这里对k取值不再限制，因此说是对T123股票最大收益问题的推广。
在T123中如果采用的是四个变量的解法（参考评论中最精简的解答，就是采用b1,s1,b2,s2四个变量记录遍历过程），
按照这个思路很容易推广到k个的情形，注意b[i]与s[i-1]-price相关，而s[i]与b[i]+price相关联。
然后注意一下边界条件就可以很自然的写出啦。
另外注意一下，当k超过prices的长度（特别地，超过长度的一半）时，问题就转换为了任意交易次数，对应问题T122。
这里说是长度的一半是因为，每一笔交易都不能相互重叠（体会一下），因此如果是k笔交易，那就需要2*k天的股票价格，
这就很自然可以确定超过长度一半的时候问题就变简单了。
'''
class Solution1(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k==0 or len(prices)<2:
            return 0
        if k>len(prices)//2:
            maxProfit = 0
            for i in range(1,len(prices)):
                if prices[i]>prices[i-1]:
                    maxProfit+=prices[i]-prices[i-1]
            return maxProfit
        else:
            buy = [float('-inf') for _ in range(k)]
            sell = [float('-inf') for _ in range(k)]
            for price in prices:
                buy[0] = max(buy[0],-price)
                sell[0] = max(sell[0],buy[0]+price)
                for i in range(1,k):
                    buy[i] = max(buy[i],sell[i-1]-price)
                    sell[i] = max(sell[i],buy[i]+price)
            return sell[-1]

class Solution(object):
    def maxProfit(self,k,prices):
        if k==0 or len(prices)<2:
            return 0
        if k>len(prices)//2:
            maxPro=0
            for i in range(1,len(prices)):
                if prices[i]>prices[i-1]:
                    maxPro+=prices[i]-prices[i-1]
            return maxPro
        else:
            dp_i_0=0
            dp_i_1=-float('inf')
            for i in range(len(prices)):
                tmp=dp_i_0
                dp_i_0=max(dp_i_0,dp_i_1+prices)
                dp_i_1=max(dp_i_1,tmp-prices)
            return dp_i_0
