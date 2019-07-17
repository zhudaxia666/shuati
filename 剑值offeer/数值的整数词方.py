'''
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
当指数为负数的时候，可以先对指数求绝对值，然后算出次方的结果之后再取倒数。如果底数为0，则直接返回0。此时的次方在数学上是没有意义的。
'''
class Solution:
    def Power(self, base, exponent):
        if base==0:
            return False
        flag=0
        result=1
        if exponent<0:
            flag=1
        for i in range(abs(exponent)):
            result*=base
        if flag==1:
            return 1/result
        else:
            return result


'''
使用快速幂算法
详细见链接：https://blog.csdn.net/qq_19782019/article/details/85621386
'''
class Solution:
    def Power(self, base, exponent):
        # write code here
        if base==0:
            return False
        if exponent==0:
            return 1
        res=1
        tmp=abs(exponent)
        while tmp:
            if tmp&1:
                res*=base
            tmp >>=1
            base*=base
        return res if exponent>0 else 1/res