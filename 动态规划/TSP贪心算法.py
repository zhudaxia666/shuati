'''
贪心算法非常容易理解，是一种解决实际问题中的常用方法，经常用来和其他算法进行比较。所谓贪心算法是指，
在对问题求解时，总是做出在当前看来是最好的选择。也就是说，不从整体最优上加以考虑，他所做出的仅是在某种意义上的局部最优解。
贪心算法没有固定的算法框架，算法设计的关键是贪心策略的选择。必须注意的是，贪心算法不是对所有问题都能得到整体最优解，
选择的贪心策略必须具备无后效性，即某个状态以后的过程不会影响以前的状态，只与当前状态有关。
在TSP问题上，假设城市集合为B，我们每次只选择距离当前城市最近的城市移动。同时集合s记录已经遍历过得城市，
下次从集合(B-s)中选择。
--------------------- 
原文：https://blog.csdn.net/h9f3d3/article/details/80806699 
'''

#贪心法
import pandas as pd
import numpy as np
import math
import time

def tsp():
    dataframe = pd.read_csv("./data/TSP100cities.tsp",sep=" ",header=None)
    v = dataframe.iloc[:,1:3]
    
    train_v= np.array(v)
    train_d=train_v
    dist = np.zeros((train_v.shape[0],train_d.shape[0]))
    
    #计算距离矩阵
    for i in range(train_v.shape[0]):
        for j in range(train_d.shape[0]):
            dist[i,j] = math.sqrt(np.sum((train_v[i,:]-train_d[j,:])**2))
    """
    s:已经遍历过的城市
    dist：城市间距离矩阵
    sumpath:目前的最小路径总长度
    Dtemp：当前最小距离
    flag：访问标记
    """
    i=1
    n=train_v.shape[0]
    j=0
    sumpath=0
    s=[]
    s.append(0)
    start = time.clock()
    while True:
        k=1
        Detemp=10000000
        while True:
            l=0
            flag=0
            if k in s:
                flag = 1
            if (flag==0) and (dist[k][s[i-1]] < Detemp):
                j = k
                Detemp=dist[k][s[i - 1]]
            k+=1
            if k>=n:
                break
        s.append(j)
        i+=1
        sumpath+=Detemp
        if i>=n:
            break
    sumpath+=dist[0][j]
    end = time.clock()
    print("结果：")
    print(sumpath)
    for m in range(n):
        print("%s-> "%(s[m]),end='')
    print()
    print("程序的运行时间是：%s"%(end-start))