'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
思路：
首先我们考虑最简单的情况。如果只有1级台阶，那么显然只一种跳法。如果有2级台阶，那就有两种跳法：
一种是分两次跳，每次跳1级；另一种是一次跳2级。
接着，我们来讨论一般情况。我们把n级台阶时的跳法看成是n的函数，记为f(n)。当n>2时，第一次跳的时候就有两种不同的选择：
一是第一次只跳1级，此时跳法数目等于后面剩下的n-1级台阶的跳法数目，即为f(n-1)；另外一种选择是跳一次跳2级，
此时跳法数目等于后面剩下的n-2级台阶的跳法数目，即为f(n-2)。因此n级台阶的不同跳法的总数f(n)=f(n-1)+f(n-2)。
分析到这里，我们不难看出这实际上就是斐波那契数列了。
'''
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        if number<=0:
            return 0
        if number==1:
            return 1
        if number==2:
            return 2
        f1,f2,f3=1,2,0
        for i in range(3,number+1):
            f3=f1+f2
            f1=f2
            f2=f3
        return f3

"""
别人的
"""
# -*- coding:utf-8 -*-
class Solution1:
    def jumpFloor(self, number):
        # write code here
        a = 1
        b = 1
        for i in range(number):
            a,b = b,a+b
        return a