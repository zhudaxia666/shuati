'''
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.

'''
# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        if len(s)==0:
            return -1
        query={}
        for i in range(len(s)):
            if s[i] not in query:
                query[s[i]]=1
            else:
                query[s[i]]+=1
        for i in range(len(s)):
            if query[s[i]]==1:
                return i
        return -1

# -*- coding:utf-8 -*-
class Solution1:
    def FirstNotRepeatingChar(self, s):
        return s.index(list(filter(lambda c:s.count(c)==1,s))[0]) if s else -1
        