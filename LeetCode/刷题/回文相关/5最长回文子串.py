'''
三种思路：

思路 1：
把每个字母当成回文串的中心
这里要考虑两种情况，回文串的长度为奇数或者偶数情况。
思路 2： 把每个母当成回文串的结束
思路 3： 动态规划
dp[i][j] 表示字符串从 j 到 i 是否是为回文串，即当 s[j] == s[i] 如果 dp[i-1][j+1] 也是回文串，那么字符串从 j 到 i 也是回文串，即 dp[i][j] 为真。
'''
#马拉车算法
class Solution2:
    def longestPalindrome(self, s: str):
        if not str or len(s)==0:
            return ''
        char=self.manache(s)
        p=[0]*len(char)#回文半径数组
        c=-1#回文中心
        r=-1#右边界
        m=-float('inf')#记录全局最大值
        t=-1#记录最大值对应的回文中心
        for i in range(len(char)):
            p[i]=min(p[2*c-i],r-i) if r>i else 1
            while i+p[i]<len(char) and i-p[i]>=0:
                if char[i+p[i]]==char[i-p[i]]:
                    p[i]+=1
                else:
                    break
            if i+p[i]>r:
                r=i+p[i]
                c=i
            if m<p[i]:
                m=p[i]
                t=i
        return ''.join(char[t-p[t]+1:t+p[t]]).replace('#','')
    def manache(self,s):
        n=len(s)
        res=[0]*(2*n+1)
        index=0
        for i in range(len(res)):
            if i%2==0:
                res[i]='#'
            else:
                res[i]=s[index]
                index+=1
        return res



def longest(s):
    n=len(s)
    res=""
    def helper(i,j):
        while i>=0 and j<n and s[i]==s[j]:
            i-=1
            j+=1
        if len(res)<j-i-1:
            res=s[i+1:j]
    for i in range(n):
        helper(i,i)
        helper(i,i+1)
    return res

class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 1
        start = 0
        n = len(s)
        #遍历每一个字符，并假设为回文数的尾字符
        for i in range(1,n):
            #偶数取序号i前面 max_len个字符，奇数取i前面max_len+1个字符。i+1表示取到序号i字符
            even = s[i - max_len : i+1]
            odd  = s[i - max_len - 1 : i+1]
            # 1 判断 取到的字数组下标，并且是回文数
            # 2 给start赋值，奇数字串max_len加2,偶数字串max_len加1
            if i-max_len >=0 and even == even[::-1] :
                start = i-max_len
                max_len += 1
            elif i-max_len - 1 >= 0 and odd == odd[::-1] :
                start = i - max_len -1
                max_len += 2
        
        return s[start:start+max_len]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s :
            return ''
        #动态规范法
        n = len(s)
        #若dp[i][j] 等于1，代表字符j到i是回文，若为0，则不是。*注意i>j
        dp = [[0]*n for i in range(n)]
        max_len = 0
        #两个for循环，实现:对每一个i,使得j取值范围为[0,i]。即[0,i],[1,i] ... [i,i]
        for i in range(n):
            for j in range(i,-1,-1):
                #在上面所讲的i,j取值内，有s[i] == s[j] 。这个是设定的触发条件，两个值相等才能是回文数
                #设条件x为: i-j <2 ，代表j可以取值i,i-1    程序刚执行时，确保任意i对应单个字符为回文，
                #设条件y为: dp[i-1][j+1]值为1 ,代表可以抛弃 i-j<2 的条件。j可以取到所有值[0,i]
                if s[i] == s[j] and (i-j <2 or dp[i-1][j+1]) :
                    dp[i][j] = 1
                # 第一遍循环 max_len = 1 
                if dp[i][j] == 1 and max_len < i-j+1 :
                    res = s[j:i+1]
                    max_len =i-j+1
                #对于回文为偶数个,'jkllkj', 程序在i取到右边的l时，比较左边的l相等，触发条件同时x条件成立。后面依次比较
                #。。。。。奇数个,'abpba' , 程序在i取到右边的b时，比较左边的b相等，触发条件同时y条件成立。后面依次比较
        return res
def longestPalindrome1(s):
    size=len(s)
    if size<=1:
        return s
    # # 二维 dp 问题
        # 状态：dp[l,r]: s[l:r] 包括 l，r ，表示的字符串是不是回文串
        # 设置为 None 是为了方便调试，看清楚代码执行流程
    dp=[[False for _ in range(size)] for _ in range(size)]
    longest=1
    res=s[0]
     # 因为只有 1 个字符的情况在最开始做了判断
        # 左边界一定要比右边界小，因此右边界从 1 开始
    for r in range(1,size):
        for l in range(r):
             # 状态转移方程：如果头尾字符相等并且中间也是回文
                # 在头尾字符相等的前提下，如果收缩以后不构成区间（最多只有 1 个元素），直接返回 True 即可
                # 否则要继续看收缩以后的区间的回文性
                # 重点理解 or 的短路性质在这里的作用
        '''
        只要 s[l + 1, r - 1] 至少包含两个元素，就有必要继续做判断，否则直接S根据左右边界是否相等就能得到原字符串的回文性。
        而“s[l + 1, r - 1] 至少包含两个元素”等价于 l + 1 < r - 1，整理得 l - r < -2，或者 r - l > 2
        ''''
            if s[r]==s[l] and (r-l<=2 or dp[l+1][r-1]):
                dp[l][r]=True
                curlen=r-l+1
                if curlen>longest:
                    longest=curlen
                    res=s[l:r+1]
    return res

# 链接：https://leetcode-cn.com/problems/two-sum/solution/zhong-xin-kuo-san-dong-tai-gui-hua-by-liweiwei1419/
