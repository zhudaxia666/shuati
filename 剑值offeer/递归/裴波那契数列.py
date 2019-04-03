'''
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。（n<=39）

'''
class Solution:
    def Fibonacci(self, n):
        if n==0:
            return 0
        if n==1:
            return 1
        f1=0
        f2=1
        for i in range(2,n+1,1):
            t=f2
            f2=f1+f2
            f1=t
        return f2

'''
别人的
'''
# -*- coding:utf-8 -*-
class Solution1:
    def Fibonacci(self, n):
        # write code here
        if n <= 1:
            return n
        first, second, third = 0, 1, 0
        for i in range(2, n+1):
            third = first + second
            first = second
            second = third
        return third

# -*- coding:utf-8 -*-
class Solution2:
    def Fibonacci(self, n):
        a = [0,1,1]
        if n<3:
            return a[n]
        for i in range(3,n+1):
            a.append(a[i-1]+a[i-2])
        return a[n]