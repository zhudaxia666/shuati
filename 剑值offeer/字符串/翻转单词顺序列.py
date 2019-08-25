'''
牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，
但却读不懂它的意思。例如，“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，
正确的句子应该是“I am a student.”。Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？
'''
# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if not s:
            return ''
        s=s.split(' ')
        return " ".join(s[::-1])

'''
方法2
'''
# -*- coding:utf-8 -*-
class Solution1:
    def ReverseSentence(self, s):
        # write code here
        if  not s:
            return s
        s1=s.split()
        if len(s1)==0:
            return s
        else:
            s2=[]
            for i in s1:
                s2.append(i)
                s2.append(' ')
            s2.reverse()
            return ''.join(s2).strip()
'''
思路3：两次翻转，第一次整个字符串翻转，第二次对每个单词进行翻转，即对两个“ ”内的单词
'''
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if len(s)==0 or " " not in s:
            return s
        s=s[::-1]
        l=0
        res=""
        r=s.index(" ")
        while r<len(s):
            res+=s[l:r][::-1]+" "
            l=r+1
            r+=1
            while r<len(s) and s[r]!=" ":
                r+=1
        res+=s[l:r][::-1]
        return res
 