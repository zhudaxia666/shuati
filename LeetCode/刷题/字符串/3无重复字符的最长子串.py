"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        record = dict()#记录每个字母最后一次出现的下标,key是字母，val是下标
        res, start = 0, 0
        for end in range(len(s)):
            if s[end] in record:#出现过
                start = max(start, record[s[end]] + 1)
            record[s[end]] = end #刷新最新下标
            res = max(res, end - start + 1)  #刷新res        
        return res
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


#滑动窗口
'''
什么是滑动窗口？
其实就是一个队列,比如例题中的 abcabcbb，进入这个队列（窗口）为 abc 满足题目要求，当再进入 a，队列变成了 abca，这时候不满足要求。所以，我们要移动这个队列！
如何移动？
我们只要把队列的左边的元素移出就行了，直到满足题目要求！
一直维持这样的队列，找出队列出现最长的长度时候，求出解！
时间复杂度：O(n)O(n)
'''
class Solution2:
    def lengthOfLongestSubstring(self, s):
        if not s:return 0
        left = 0
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:max_len = cur_len
            lookup.add(s[i])
        return max_len

a=Solution()
b="ddddd"
print(a.lengthOfLongestSubstring(b))