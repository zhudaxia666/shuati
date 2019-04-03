'''
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''
# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        s=list(s)
        n=len(s)
        for i in range(n):
            if s[i]==' ':
                s[i]="%20"
        return ''.join(s)


'''
思路2
'''
# -*- coding:utf-8 -*-
class Solution1:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        res = ''
        for ele in s:
            if ele.strip():
                res += ele
            else:
                res += '%20'
        return res