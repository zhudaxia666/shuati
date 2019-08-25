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

'''
滑动窗口：
1.使用容器(数组)-最直观的滑动窗口法
时间复杂度和空间复杂度都是O(n)
'''
def lengthsub(s):
    if not s:
        return 0
    window=[]#滑动窗口数组
    max_length=0
    for c in s:
        #如果字符不在滑动窗口内，就拓展滑动窗口
        if c not in window:
            window.append(c)
        # 如果字符在滑动窗口中，则
            # 1. 从窗口中移除重复字符及之前的字符串部分
            # 2. 再扩展窗口
        else:
             # 从窗口中移除重复字符及之前的字符串部分，新字符串即为无重复字符的字符串
            window[:]=window[window.index(c)+1:]
            window.append(c)
        max_length=max(len(window),max_length)
    return max_length if max_length!=0 else len(s)
'''
2.使用指针 - 滑动窗口优化 - 双指针法 - 使用数组索引，标记滑动窗口
直观的滑动窗口方法需要维护数组的增删，实际上比较耗时
使用双指针（索引），记录滑动窗口起始和结束的索引值，可以减除数组增删操作，提高效率
代码结构和上一种方法基本一致，只不过使用指针位移以及从原数组中截取，代替原来的窗口元素增删操作

'''
def lengthsub1(s):
    if not s:
        return 0
    max_length=0 # 滑动窗口数组
    l,r=0,0  # 双指针
    for c in s:
         # 如果字符不在滑动窗口中，则直接扩展窗口
        if c not in s[l:r]:
            # 右指针右移一位
            r+=1
        # 如果字符在滑动窗口中，则
        # 1. 从窗口中移除重复字符及之前的字符串部分
        # 2. 再扩展窗口
        else:
          # 在滑动窗口范围内中找出对应的首个字符的索引X，对应的新的左指针位置为X + 1
                # 左指针右移 索引X增一 位
            l+=s[l:r].index(c)+1
            # 右指针右移一位
            r+=1
        max_length=max(r-l,max_length)
    return max_length if max_length!=0 else len(s)


b='abcdaefwsa'
print(lengthsub1(b))




# a=Solution()
# b="ddddd"
# print(a.lengthOfLongestSubstring(b))