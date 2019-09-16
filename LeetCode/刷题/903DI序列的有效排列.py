'''
我们给出 S，一个源于 {'D', 'I'} 的长度为 n 的字符串 。（这些字母代表 “减少” 和 “增加”。）
有效排列 是对整数 {0, 1, ..., n} 的一个排列 P[0], P[1], ..., P[n]，使得对所有的 i：

如果 S[i] == 'D'，那么 P[i] > P[i+1]，以及；
如果 S[i] == 'I'，那么 P[i] < P[i+1]。
有多少个有效排列？因为答案可能很大，所以请返回你的答案模 10^9 + 7.

dp[i][j]表示i+1个数据(0,1,2....i)根据序列S[0:i]排序后以j结尾的组合数
过程：
dp[i][j]
= dp[i-1][j]+dp[i][j+1] if S[i-1] == 'D'
= dp[i-1][j-1]+dp[i][j-1] if S[i-1] == 'I'

'''
class Solution:
    def numPermsDISequence(self, S: str) -> int:
        le = len(S)
        dp = [[0]*(le+3) for _ in range(le+1)]
        dp[0][1] = 1
        for i in range(1,le+1):
            if S[i-1] == 'D':
                for j in range(i+1,0,-1):
                    dp[i][j] = (dp[i-1][j]+dp[i][j+1])%1000000007
            else:
                for j in range(1,i+2):
                    dp[i][j] = (dp[i-1][j-1]+dp[i][j-1])%1000000007
        return sum(dp[-1])%1000000007
