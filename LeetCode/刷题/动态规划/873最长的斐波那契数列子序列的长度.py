'''
如果序列 X_1, X_2, ..., X_n 满足下列条件，就说它是 斐波那契式 的：
n >= 3
对于所有 i + 2 <= n，都有 X_i + X_{i+1} = X_{i+2}
给定一个严格递增的正整数数组形成序列，找到 A 中最长的斐波那契式的子序列的长度。如果一个不存在，返回  0 。

（回想一下，子序列是从原序列 A 中派生出来的，它从 A 中删掉任意数量的元素（也可以不删），而不改变其余元素的顺序。例如， [3, 5, 8] 是 [3, 4, 5, 6, 7, 8] 的一个子序列）

'''
#思路1：暴力法
class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        s=set(A)
        n=len(A)
        m=0
        for i in range(n-1):
            for j in range(i+1,n):
                a,b=A[i],A[j]
                c=2
                while a+b in s:
                    a,b=b,a+b
                    c+=1
                    m=max(m,c) 
        return m if m>2 else 0
'''
思路2：动态规划
我们假设dp[i][j]是以A【i】与A【j】结尾的数列（因为默认了Ai<Aj）。
所以对于类似......A[i],A[j]这个数列如果有A[k]==A[i]+A[j]，那么这数列就变成了.....A[i],A[j],A[k].
dp[j][k]=dp[i][j]+1
上述式子便是转移方程。
我们考虑初始化的情况：对于dp[i][i]意思是两个相同的数字做结尾，是不存在的！因此dp[i][i]=0

而其他的情况，只要处于两个不同的式子，那么长度就是2.所以dp【i】【j】=2，
'''
import collections
def lenLongestFibSubseq(A):
    vset = set(A)
    dp = collections.defaultdict(lambda: collections.defaultdict(int))
    size = len(A)
    ans = 0
    for i in range(size):
        x = A[i]
        for j in range(i + 1, size):
            y = A[j]
            if x + y not in vset: continue
            dp[y][x + y] = max(dp[y][x + y], dp[x][y] + 1)
            ans = max(dp[y][x + y], ans)
    return ans and ans + 2 or 0
