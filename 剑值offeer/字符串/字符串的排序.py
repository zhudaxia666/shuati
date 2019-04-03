'''
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,
则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
使用回溯法
首先固定第一个字符，求后面所有字符的排列。这个时候我们仍把后面的所有字符分为两部分：
后面的字符的第一个字符，以及这个字符之后的所有字符。然后把第一个字符逐一和它后面的字符交换。
'''
# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if len(ss)<=0:
            return []
        res=list()
        self.perm(ss,res,'')
        res=list(set(res))
        return sorted(res)
    def perm(self,ss,res,path):
        if ss=='':
            res.append(path)
        else:
            for i in range(len(ss)):
                self.perm(ss[:i]+ss[i+1:],res,path+ss[i])



'''
代码2
'''
# -*- coding:utf-8 -*-
class Solution1:
    def __init__(self):
        self.result = []
    def Permutation(self, ss):
        # write code here
        if len(ss) == 0:
            return []
        self.PermutationCore(ss, 0)
        sorted(self.result)
        return self.result
    def PermutationCore(self, str_, begin):
        if begin == len(str_):
            self.result.append(str_)
            return
        for i in range(begin, len(str_)):
            if i != begin and str_[i] == str_[begin]:
                continue
            str_list = list(str_)
            str_list[i], str_list[begin] = str_list[begin], str_list[i]
            str_ = ''.join(str_list)
            self.PermutationCore(str_, begin+1)