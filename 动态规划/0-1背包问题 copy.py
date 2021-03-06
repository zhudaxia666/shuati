'''
0-1背包问题。
背包问题抽象化（X1，X2，…，Xn，其中 Xi 取0或1，表示第 i 个物品选或不选）。
1、建立模型，即求max(V1X1+V2X2+…+VnXn)；
2、寻找约束条件，W1X1+W2X2+…+WnXn<capacity；
3、寻找递推关系式，面对当前商品有两种可能性：
包的容量比该商品体积小，装不下，此时的价值与前i-1个的价值是一样的，即V(i,j)=V(i-1,j)；
还有足够的容量可以装该商品，但装了也不一定达到当前最优价值，所以在装与不装之间选择最优的一个，即V(i,j)=max｛V(i-1,j)，V(i-1,j-w(i))+v(i)｝。
其中V(i-1,j)表示不装，V(i-1,j-w(i))+v(i) 表示装了第i个商品，背包容量减少w(i)，但价值增加了v(i)；
由此可以得出递推关系式：
j<w(i)      V(i,j)=V(i-1,j)
j>=w(i)     V(i,j)=max｛V(i-1,j)，V(i-1,j-w(i))+v(i)｝
这里需要解释一下，为什么能装的情况下，需要这样求解（这才是本问题的关键所在！）：
可以这么理解，如果要到达V(i,j)这一个状态有几种方式？
肯定是两种，第一种是第i件商品没有装进去，第二种是第i件商品装进去了。没有装进去很好理解，就是V(i-1,j)；装进去了怎么理解呢？如果装进去第i件商品，那么装入之前是什么状态，肯定是V(i-1,j-w(i))。由于最优性原理（上文讲到），V(i-1,j-w(i))就是前面决策造成的一种状态，后面的决策就要构成最优策略。两种情况进行比较，得出最优。

首先初始化边界条件，V(0,j)=V(i,0)=0；
 ———————————————— 
原文链接：https://blog.csdn.net/qq_38410730/article/details/81667885
'''
def bags(v,w,bagv):#参数表示物品体积，重量和背包容量
    row=len(v)
    col=bagv
    #dp[i][j]表示当前背包容量 j，前 i 个物品最佳组合对应的价值
    dp=[[0]*(col+1) for i in range(row+1)]
    for i in range(1,row):
        for j in range(1,col+1):
            if j<w[i]:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-w[i]]+v[i])
    #递推装入背包的物体
    j = bagv
    x=[False]*row
    for i in range(row, 0, -1):
        if dp[i][j] > dp[i - 1][j]:
            x[i] = True
            j = j - w[i]
    print(x)
    # print(dp)
    print(dp[row-1][col])
'''
优化空间复杂度从O(cn)可以优化为O(c)
思路：尾部迭代，每个状态表示上一次的最佳结果
'''
def bag2(n, c, w, v):
    values = [0 for i in range(c+1)]
    for i in range(1, n + 1):
        for j in range(c, 0, -1):
            # 背包总容量够放当前物体，遍历前一个状态考虑是否置换
            if j >= w[i-1]:
                values[j] = max(values[j-w[i-1]]+v[i-1], values[j])
                print(values[j],end=',')
        print()
    print(values)
    # return values
n = 6  #物品的数量，
c = 10 #书包能承受的重量，
w = [2, 2, 3, 1, 5, 2] #每个物品的重量，
v = [2, 3, 1, 5, 4, 3] #每个物品的价值
bags(v,w,c)
bag2(n, c, w, v)
# w=[0,15,10,12,8]
# v=[0,12,8,9,5]
# bagv=30
# bags(v,w,bagv)