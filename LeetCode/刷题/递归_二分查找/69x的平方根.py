'''
实现 int sqrt(int x) 函数。
计算并返回 x 的平方根，其中 x 是非负整数。
由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        l = 1
        r = x // 2

        while l < r:
            # 注意：这里一定取右中位数，如果取左中位数，代码可能会进入死循环
            mid = l + (r - l + 1) // 2
            square = mid * mid

            if square > x:
                r = mid - 1
            else:
                l = mid
        return l