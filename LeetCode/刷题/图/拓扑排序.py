'''
使用邻接矩阵表示图的拓扑排序
'''
import numpy as np

def top_sort(g):
    n=len(g)
    #获取所有入度为0的节点
    q=[]
    for i in range(n):
        flag=True
        for j in range(n):
            if g[j][i]==1:
                flag=False
                break
        if flag:
            q.insert(0,i)
    li=[]#记录结果
    while len(q)>0:
        #p出队，将从p出度的数据置为0
        p=q.pop()
        li.append(p)
        for i in range(n):
            if g[p][i]==1:
                g[p][i]=0
                count=0
                for u in g:
                    if u[i]==1:
                        count+=1
                if count==0:
                    q.insert(0,i)
    return li

#用邻接表表示图的拓扑排序
def top_sort1(g):
    n=len(g)
    #计算所有节点的入度
    in_degree=[0]*n
    for i in range(n):
        for k in g[i]:
            in_degree[k]+=1
    #记录入度为0的节点
    in_degree0=[]
    for i in range(n):
        if in_degree[i]==0:
            in_degree0.insert(0,i)
    
    li=[]#记录结果
    while len(in_degree0)>0:
        #p出队
        p=in_degree0.pop()
        li.append(p)
        for k in g[p]:
            #对应的节点的入度减1
            in_degree[k]-=1
            if in_degree[k]==0:
                in_degree0.insert(0,k)
    return li


if __name__ == "__main__":
    # 用邻接矩阵表示图
    # 初始化图的数据，连通的标记为1
    g = np.zeros(shape=(13, 13), dtype='int')
    # g[i][j] = 1 表示 i -> j
    g[0][1] = g[0][5] = g[0][6] = 1
    g[2][0] = g[2][3] = 1
    g[3][5] = 1
    g[5][4] = 1
    g[6][4] = g[6][9] = 1
    g[7][6] = 1
    g[8][7] = 1
    g[9][10] = g[9][11] = g[9][12] = 1
    g[11][12] = 1
    result = top_sort(g)
    print(result)

    #使用邻接表表示图
    g2 = [[]] * 13
    g2[0] = [1, 5, 6]
    g2[2] = [3]
    g2[3] = [5]
    g2[5] = [4]
    g2[6] = [4, 9]
    g2[7] = [6]
    g2[8] = [7]
    g2[9] = [10, 11, 12]
    g2[11] = [12]

    result1 = top_sort1(g2)
    print(result1)