'''
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
'''
from collections import defaultdict

def isanagram(s,t):
    s_dic=defaultdict(int)
    for i in s:
        s_dic[i]+=1
    t_dic=defaultdict(int)
    for i in t:
        t_dic[i]+=1
    if len(s_dic)!=len(t_dic):
        return False
    else:
        for i in s_dic:
            if s_dic[i]!=t_dic.get(i):
                return False
    return True


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        res=[0]*26
        for i in range(len(t)):
            res[ord(s[i])-ord('a')]+=1
            res[ord(t[i])-ord('a')]-=1
        for i in res:
            if i!=0:
                return False
        return True
        