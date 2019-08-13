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

'''
字符串全排列（递归版）
思路：
把s[0]固定在位置0上，[1,n-1]位置的数字全排（递归） 
把s[1]固定在位置0上（把s[1]和s[0]交换），[1,n-1]位置的数字全排（递归） 
…… 
如果第i个数字在前面出现过，则跳过 
…… 
把s[n-1]固定在位置0上（把s[n-1]和s[0]交换），[1,n-1]位置的数字全排（递归）

原文链接：https://blog.csdn.net/weixin_42018258/article/details/80683826
'''
from copy import deepcopy

def Permutation(li,size,n,res):
    """
    [n,size]位置的数字全排
    :param li:字符串数组
    :param size: 字符串长度
    :param n: 要交换的位置
    :param result: 保留结果
    :return:
    """
    if n==size-1:
        res.append(deepcopy(li))
        return
    for i in range(n,size):# 分别把(size-n)个数字固定到位置n
        if li[i] in li[n:i]:# 如果位置n出现过数字li[i]，跳过
            continue
        li[i],li[n]=li[n],li[i]# 把s[n]和s[i]交换，把s[i]固定到位置n
        Permutation(li,size,n+1,res)# [n+1,size-1]位置的数字全排
        li[i],li[n]=li[n],li[i]## 把s[n]和s[i]交换回来
'''
非递归版
思路：
起点：字典序最小的排列，例如122345。起点为正序 
终点：字典序最大的排列，例如543221。终点为倒序 
过程：按当前的排列找出刚好比它大的下一个排列 
如：524321的下一个排列是531224 
如何计算？ 
我们从后向前找第一双相邻的递增数字，”21”、”32”、”43”都是非递增的，”24”即满足要求，称前一个数字2为替换数，替换数的下标称为替换点，再从后面找一个比替换数大的最小数（这个数必然存在），1、2都不行，3可以，将3和2交换得到”534221”，然后再将替换点后的字符串”4221”颠倒即得到”531224”。 
对于像”543221”这种已经是最“大”的排列，返回false。 
这样，一个while循环再加上计算字符串下一个排列的函数就可以实现非递归的全排列算法。

步骤：后找、小大、交换、翻转
后找：字符串中最后一个升序的位置i，即：S[i]<S[i+1]； 
查找(小大)：S[i+1…N-1]中比S[i]大的最小值S[j]； 
交换：S[i]，S[j]；交换操作前和操作后，S[i+1…N-1]一定都是降序的 
翻转：S[i+1…N-1]
'''
def reverse(li, i, j):
    """
    翻转
    :param li: 字符串数组
    :param i: 翻转开始位置
    :param j: 翻转结束位置
    """
    if li is None or i < 0 or j < 0 or i >= j or len(li) < j + 1:
        return
    while i < j:
        li[i],li[j]=li[j],li[i]
        j -= 1
        i+=1
def get_next(li,size):
    #后找：字符串中最后一个升序的位置i，即：S[i]<S[i+1]
    i=size-2
    while i>=0 and li[i]>=li[i+1]:
        i-=1
    if i<0:
        return False
    #查找(小大)：S[i+1…N-1]中比S[i]大的最小值S[j]
    j=size-1
    while li[j]<=li[i]:
        j-=1
    #交换s[i],s[j]
    li[i],li[j]=li[j],li[i]
    #翻转li[i+1,n-1]
    # li=li[:i+1]+li[i+1:size][::-1]
    reverse(li, i + 1, size - 1)
    return True



if __name__=='__main__':
    li = ['a', 'b', 'c']
    li.sort()
    size = len(li)
    res=[deepcopy(li)]
    while get_next(li,size):
        res.append(deepcopy(li))
    # n = 0
    # result = []
    # Permutation(li, size, n, result)
    for i in res:
        print(i)
    