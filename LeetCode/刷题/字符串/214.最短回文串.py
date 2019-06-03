'''
给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。
输入: "aacecaaa"
输出: "aaacecaaa"

输入: "abcd"
输出: "dcbabcd"
'''
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        for i in range(n - 1, -1, -1):
            if s[0:i+1] == s[i::-1]:
                return s[-1:i:-1] + s
        return ""

#先逆序，然后截取逆序后的前i个字符拼接到原串上，取满足回文条件最小的i
class Solution1:
    def shortestPalindrome(self, s: str) -> str:
        length=len(s)
        if length==0:
            return ""
        rs = s[::-1]
        i = 0
        while True:
            if rs[i:]==s[:length-i]:
                break
            i+=1
        return rs[:i]+s