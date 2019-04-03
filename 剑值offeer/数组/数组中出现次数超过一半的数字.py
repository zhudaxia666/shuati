'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0
'''
# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        from collections import defaultdict
        dic=defaultdict(int)
        l=len(numbers)
        for i in numbers:
            dic[i]+=1
        for key,value in dic.items():
            if value>l//2:
                return key
        return 0

'''
别人的
'''
import collections
class Solution2:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        tmp = collections.Counter(numbers)
        x = len(numbers)/2
        for k, v in tmp.items():
            if v > x:
                return k
        return 0