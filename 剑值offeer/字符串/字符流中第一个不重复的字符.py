'''
请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，
第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
'''
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.s=''
    # 返回对应char
    def FirstAppearingOnce(self):
        # write code here
        if self.s:
            if len(filter(lambda c:self.s.count(c)==1,self.s))==0:
                return '#'
            else:
                return filter(lambda c:self.s.count(c)==1,self.s)[0]
            
    def Insert(self, char):
        # write code here
        self.s+=char
        
'''
思路2:
将字节流保存起来，通过哈希表统计字符流中每个字符出现的次数，顺便将字符流保存在string中，然后再遍历string，从哈希表中找到第一个出现一次的字符。
'''
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.s = ''
        self.count = {}
    # 返回对应char
    def FirstAppearingOnce(self):
        # write code here
        length = len(self.s)
        for i in range(length):
            if self.count[self.s[i]] == 1:
                return self.s[i]
        return '#'
    def Insert(self, char):
        # write code here
        self.s += char
        if char not in self.count:
            self.count[char] = 1
        else:
            self.count[char] += 1