'''
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
就是斐波那契数列
'''
# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        if number<=0:
            return 0
        a=1
        b=1
        for i in range(number):
            a,b=b,a+b
        return a