"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len=0
        sub_str=[]
        if len(s)==0:
            return max_len
        i=0
        j=len(s)
        while(i<j):
            if max_len>(len(s[i:j])):
                break
            if(len(s[i:j])==len(set(s[i:j])) and max_len<len(s[i:j])):
                max_len=j-i
            else:
                j=j-1
                if(j==i+1):
                    i=i+1
                    j=len(s)
        return max_len

class Solution1:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = {}
        i, ans = 0, 0
        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]], i)
            ans = max(ans, j - i + 1)
            st[s[j]] = j + 1
        return ans




a=Solution()
b="ddddd"
print(a.lengthOfLongestSubstring(b))