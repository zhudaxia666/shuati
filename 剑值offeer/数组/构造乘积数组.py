'''
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
'''
# -*- coding:utf-8 -*-
from functools import reduce
class Solution:
    def multiply(self, A):
        # write code here
        B = []
        if len(A) == 0:
            return B
        else:
            for i in range(len(A)):
                tmp = A[i]
                A[i] = 1
                B.append(reduce(lambda x,y:x*y, A))
                A[i] = tmp
        return B

#不妨设定C[i]=A[0]*A[1]*...*A[i-1]，D[i]=A[i+1]*...*A[n-2]*A[n-1]。C[i]可以用自上而下的顺序计算出来，即C[i]=C[i-1]*A[i-1]。
# 类似的，D[i]可以用自下而上的顺序计算出来，即D[i]=D[i+1]*A[i+1]。
# -*- coding:utf-8 -*-
class Solution2:
    def multiply(self, A):
        # write code here
        if not A:
            return []
        # 计算前面一部分
        num = len(A)
        B = [None] * num
        B[0] = 1
        for i in range(1, num):
            B[i] = B[i-1] * A[i-1]
        # 计算后面一部分
        # 自下而上
        # 保留上次的计算结果乘本轮新的数,因为只是后半部分进行累加，所以设置一个tmp,能够保留上次结果
        tmp = 1
        for i in range(num-2, -1, -1):
            tmp *= A[i+1]   
            B[i] *= tmp
        return B