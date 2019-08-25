'''
把n个骰子扔在地上，所有骰子朝上一面的点数之和为S。输入n，打印出S的所有可能的值出现的概率

思路：
动态规划：
解题思路： 
第一步，确定问题解的表达式。可将f(n, s) 表示n个骰子点数的和为s的排列情况总数。 
第二步，确定状态转移方程。n个骰子点数和为s的种类数只与n-1个骰子的和有关。因为一个骰子有六个点数，
那么第n个骰子可能出现1到6的点数。所以第n个骰子点数为1的话，f(n,s)=f(n-1,s-1)，当第n个骰子点数为2的话，f(n,s)=f(n-1,s-2)，…，依次类推。在n-1个骰子的基础上，再增加一个骰子出现点数和为s的结果只有这6种情况！那么有：
f(n,s)=f(n-1,s-1)+f(n-1,s-2)+f(n-1,s-3)+f(n-1,s-4)+f(n-1,s-5)+f(n-1,s-6) ，0< n<=6n 
f(n,s)=0, s< n or s>6n
上面就是状态转移方程，已知初始阶段的解为： 
当n=1时, f(1,1)=f(1,2)=f(1,3)=f(1,4)=f(1,5)=f(1,6)=1。
'''
def getsumcount(n,s):#获取n个骰子指定点数和s出现的次数
    if n<1 or s<n or s>6*n:
        return 0
    if n==1:
        return 1
    count=0
    count=getsumcount(n-1,s-1)+getsumcount(n-1,s-2)+getsumcount(n-1,s-3)+getsumcount(n-1,s-4)+getsumcount(n-1,s-5)+getsumcount(n-1,s-6)
    return count
#给定n个骰子，求各个点数和出现的概率就不难求，只需要除以总的排列数6n就可以了
n=3
total=pow(float(6),n)
for i in range(n,6*n+1,1):
    ratio=getsumcount(n,i)/total
    print(i,ratio)
def get_ans(n):
    dp = [[0 for i in range(6*n)] for i in range(n)]
 
    for i in range(6):
        dp[0][i] = 1
    # print dp
    for i in range(1,n):  #1，相当于2个骰子。
        for j in range(i,6*(i+1)):   #[0,i-1]的时候，频数为0（例如2个骰子不可能投出点数和为1）
            dp[i][j] = dp[i-1][j-6] + dp[i-1][j-5] +dp[i-1][j-4]+\
                            dp[i - 1][j - 3] +dp[i-1][j-2] +dp[i-1][j-1]
 
    count = dp[n-1]
    return count  #算得骰子投出每一个点数的频数。再除以总的排列数即可得到频率
 
print(get_ans(3))  #括号中的数字为骰子的个数。此代码为3个骰子时的情况。