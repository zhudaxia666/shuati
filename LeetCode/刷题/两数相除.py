'''
1.本题不允许采用除法直接计算。所以我们可以采用加法逼近的方法 。也就是把多少个除数相加以后最近接被除数 则得到的多少个除数的这个数字
就是相除后的商举例来说，例如 23/3=7 这个除法我们就是让 3+3+3+ 。。。。。+3 N个3相加得到不大于23且最接近23 的的数字时候，
这个时候需要用到的数字N就是商，这里我们可以看到3X7=21 3X8=24 即商为7 即7个3累加的时候最接近23且 余数2  。
2.如何找到数字N呢,如果采用一个循环不停地做3的累加直到最近接被除数为止的话这样可以得到答案但是需要循环 23/3次复杂度为O（N）
显然计算速度太慢。有没有更快的办法的呢？可以采用类似折半查找的办法，这里我们可以用翻倍逼近的办法来做如下操作。
用被除数不断地乘上2做数字的翻倍的操作直到超过被除数后 ，然后对剩下的余数做类似操作 ，直至得到的余数小于被除数或者为0
回到例子来说 23/3  :
a .  3翻倍：3•2=6    余数17
b.   再次翻倍 6•2=12 ;   余数11
c.   再次翻倍128•2=24  此时24 大于23 了 返回b 此时3×2^2 余数为11 加权值p=2
d    用11/3继续上述操作直至余数小于3 此时为3×2^1 余数为5   加权值p=1，
5/3   继续上述操作直至余数小于3 此时为3*2^0 余数为2 此时循环结束  加权值p=0 每一步得到一个每一位数的权值序列：【2,1,0】
最后商的数字为2^2 + 2^1 + 2^0 = 4+2+1 =7
'''
def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = -1 if (divisor>0)^(dividend>0)  else 1
        if abs(dividend)<abs(divisor) : return  0
        if abs(dividend)== abs(divisor) :return sign
        #r 是余数 ，n是除数 bit记录每一个加权位指数位数例如
        # 23/3  23=3*2^2+3*2^1 +3*2^0 =21 最后余2 商为2^2+2^1+2^0 = 7 3*7=21 余数2
        def recurvediv(r,n,bit):
            if r<n :return
            i = 0
            divsor = n
            maxval = 0
            while(divsor<=r):
                if divsor <=r:
                    i+=1
                    maxval = divsor
                divsor<<=1

            r = r-maxval
            bit.append(i)
            recurvediv(r,n,bit)
        res = []
        result = 0
        recurvediv(abs(dividend),abs(divisor),res)
        for i in res:
            result += 2**(i-1)
        result*=sign    
        if result >=-1*2**31 and result <=2**31-1:
            return result
        else:
            return 2**31-1
#使用递归和二进制移位
def divide1(self, dividend, divisor):
    i, a, b = 0, abs(dividend), abs(divisor)
    if a == 0 or a < b:
        return 0
    
    while b <= a:
        b = b << 1
        i = i + 1
    else:
        res = (1 << (i - 1)) + self.divide1(a - (b >> 1), abs(divisor))
        if (dividend ^ divisor) < 0:
            res = -res
        return min(res, (1 << 31) - 1)
