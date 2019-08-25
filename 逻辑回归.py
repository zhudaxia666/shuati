import numpy as np
def sigmoid(z):
    return 1/(1+np.exp(-z))
#梯度上升
def grad_descent(data,label):
    data=np.mat(data)#(m,n)
    label=np.mat(label).transpose()
    m,n=np.shape(data)
    weights=np.ones((n,1))#初始化回归系数（n,1)
    alpha=0.001#步长
    maxcycle=500#最大循环次数
    for i in range(maxcycle):
        h=sigmoid(data*weights)
        weights=weights+alpha*data*(label-h)
    return weights
