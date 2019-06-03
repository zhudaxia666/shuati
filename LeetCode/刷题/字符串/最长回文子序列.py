def longestPalindromeSubseq(s):
    # write your code here
    if len(s)<2 or s==s[::-1]:
        return len(s)
    max1=0
    # tem=''
    for i in range(len(s)):
        for j in range(i+1,len(s),1):
            if s[i:j+1]==s[i:j+1][::-1]:
                # tem=s[i:j]
                if len(s[i:j+1])>max1:
                    tem=s[i:j+1]
                    max1=len(tem)
    return max1 

s='abcbd'
print(longestPalindromeSubseq(s))  

#动态规划
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


'''

从头到尾扫描字符串，每增加一个新的字符，判断以这个字符结尾，且长度为maxLen+1或者maxLen+2的子串是否为回文，如果是，更新。
'''

class Palindrome:
    def getLongestPalindrome(self, A, n):
        # write code here
        maxLen=1
        if A==A[::-1]:return n
         #遍历每一个字符，并假设为回文数的尾字符
        for i in range(n):
            
            if i-maxLen>=1 and A[i-maxLen-1:i+1]==A[i-maxLen-1:i+1][::-1]:
                maxLen+=2
                continue
            if i-maxLen>=0 and A[i-maxLen:i+1]==A[i-maxLen:i+1][::-1]:
                maxLen+=1
        return maxLen

'''
基本思路是对任意字符串，如果头和尾相同，那么它的最长回文子串一定是去头去尾之后的部分的最长回文子串加上头和尾。如果头和尾不同，
那么它的最长回文子串是去头的部分的最长回文子串和去尾的部分的最长回文子串的较长的那一个。 
P[i,j]P[i,j]表示第i到第j个字符的回文子串数 
dp[i,i]=1dp[i,i]=1 
dp[i,j]=dp[i+1,j−1]+2|s[i]=s[j]dp[i,j]=dp[i+1,j−1]+2|s[i]=s[j] 
dp[i,j]=max(dp[i+1,j],dp[i,j−1])|s[i]!=s[j]

'''
def longestPalindrome(s):
    n = len(s)
    maxl = 0
    start = 0
    for i in range(n):
         #偶数取序号i前面 max_len个字符，奇数取i前面max_len+1个字符。i+1表示取到序号i字符
              # 1 判断 取到的字数组下标，并且是回文数
            # 2 给start赋值，奇数字串max_len加2,偶数字串max_len加1
        if i - maxl >= 1 and s[i-maxl-1: i+1] == s[i-maxl-1: i+1][::-1]:
            start = i - maxl - 1
            maxl += 2
            continue
        if i - maxl >= 0 and s[i-maxl: i+1] == s[i-maxl: i+1][::-1]:
            start = i - maxl
            maxl += 1
    return s[start: start + maxl]