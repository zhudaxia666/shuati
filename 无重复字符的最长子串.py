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
        说明： j 表示子串终止位置，i表示字串起始位置 当未出现重复时，字符串的长度即为字符串的结束位置减去起始位置。
        发生重复时，重新利用字符串的结束位置j减去新的起始位置i，并与之前的未重复字串的长度作比较取较大者
        :type s: str
        :rtype: int
        """
        st = {}
        i, ans = 0, 0
        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]], i)#这里当出现多个相同的字符时，选取最靠后的字符做起始位置
            ans = max(ans, j - i + 1)
            st[s[j]] = j + 1
        return ans




a=Solution()
b="ddddd"
print(a.lengthOfLongestSubstring(b))