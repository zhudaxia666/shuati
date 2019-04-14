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
'''

从头到尾扫描字符串，每增加一个新的字符，判断以这个字符结尾，且长度为maxLen+1或者maxLen+2的子串是否为回文，如果是，更新。
'''

class Palindrome:
    def getLongestPalindrome(self, A, n):
        # write code here
        maxLen=1
        if A==A[::-1]:return n
        for i in range(n):
            if i-maxLen>=1 and A[i-maxLen-1:i+1]==A[i-maxLen-1:i+1][::-1]:
                maxLen+=2
                continue
            if i-maxLen>=0 and A[i-maxLen:i+1]==A[i-maxLen:i+1][::-1]:
                maxLen+=1
        return maxLen

'''
基本思路是对任意字符串，如果头和尾相同，那么它的最长回文子串一定是去头去尾之后的部分的最长回文子串加上头和尾。如果头和尾不同，那么它的最长回文子串是去头的部分的最长回文子串和去尾的部分的最长回文子串的较长的那一个。 
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
        if i - maxl >= 1 and s[i-maxl-1: i+1] == s[i-maxl-1: i+1][::-1]:
            start = i - maxl - 1
            maxl += 2
            continue
        if i - maxl >= 0 and s[i-maxl: i+1] == s[i-maxl: i+1][::-1]:
            start = i - maxl
            maxl += 1
    return s[start: start + maxl]