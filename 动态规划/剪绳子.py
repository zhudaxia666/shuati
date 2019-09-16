'''
给你一根长度为n的绳子，请把绳子剪成m段(n>1,m>1)，
每段绳子的长度即为k[0],k[1]....k[m],请问k[0]*k[1]*..*k[m]可能的最大乘积是多少
'''
#动态规划：
'''
定义函数f(n)为把长度为n的绳子剪成若干段后各段长度乘积的最大值。在见第一刀的时候，我们有n-1中选择，也就是剪出来的第一大段绳子的可能长度分别是1,2...n-1.因此f(n)=max(f(i)*f(n-i)).
这是一个自上而下的递归方式，递归出重复的子问题，从而有大量不必要的重复计算，一个更好的办法是按照从下而上的顺序计算，也就是先得到f(2),f(3),再得到f(4),f(5)直到f(n)
'''
class Solution:
    def dynamic_programming(self,n):
        if n<2:
            return 0
        if n==2:
            return 1
        if n==3:
            return 2
        tem=[0,1,2,3]
        for i in range(4,n+1):
            max=0
            for j in range(1,i//2+1,1):#从j处切
                t=tem[j]*tem[i-j]
                if max<t:
                    max=t
            tem.append(max)
        return tem[n]

# 我发可以发现当n<=3时如果再剪一刀那么结果肯定小于未剪时的值，而当n>3时继续剪肯定会存在大于等于未剪时的数
# 即我们将长为n的数一直剪下去知道碰到剩下的小于4时结束

    def greedy_algorithm(self, n):
        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        multi_3 = 0
        while n > 4:
            multi_3 += 1
            n -= 3
        return 3**multi_3*n
    
#当n>=5时，我们尽量多的剪长度为3的绳子，当剩下的绳子长度为4时，把绳子剪成两段长度为2的绳子
#贪心算法时间和空间复杂度是O(1)
'''
证明这种思路的正确性。首先，当n>=5时，我们可以证明2(n-2)>n和3(n-3)>n 也就是说当绳子剩余的长度大于或者等于5的时候，我们就把他们剪成3或2的绳子段。
另外3(n-3)>2(n-2)，因此我们应尽量多剪长度为3的绳子
'''
def tanxin(self,n):
    if n<2:
        return 0
    if n==2:
        return 1
    if n==3:
        return 2
    timesof3=n//3#尽可能多的减去长度为3的绳子段
    #当绳子最后还剩4的时候，不能再减去长度为3的绳子段
    #此时更好的办法是把绳子剪成长度为2的两段，
    if (n-timesof3*3)==1:
        timesof3-=1
    timesof2=(n-timesof3*3)/2
    return int(pow(3,timesof3)*pow(2,timesof2))


s = Solution()
print(s.dynamic_programming(11))
print(s.greedy_algorithm(11))
print(s.tanxin(11))
