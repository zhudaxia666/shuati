'''
一个矩阵中只有0和1两种值，每个位置都可以和自己的上下左右四个位置相连，如果有一片1连在一起，这个部分叫做一个岛，求一个矩阵中有多少个岛
思路：遍历每个点，如果节点为1，就递归在上下左右找是否有相连的节点，如果有，就改为2
'''
'''
消消乐是当下十分火爆的一个脑力游戏。
游戏是这样的，有一个5*5的正方形网格，每个格子中有一个大于0且小于4的整数，对于一个确定的局面，若一个格子与它上下左右四个方向的某个格子（如果存在） 数字相同，则称这两个格子是连通的，并且这种连通具有传递性
每次，你可以选择一个格子，若与这个格子连通的格子（包括自己）数大于等于 3，你就可以选择消掉这个格子，与此同时，与这个格子连通的所有格子会一起消失
如果仅仅是这样，那太简单了，因为无论如何消，最后的结果都是一样的，所以我 们引入了重力系统，每次选择消掉某个格子，并将与那个格子相连通的所有格子都消掉后将会有一些格子失去支撑，此时那些格子就会因重力而下落
那么怎样玩才能使得最后剩下的不能消掉的格子尽量少
'''
import numpy as np
def countisland(matrix):
    if not matrix:
        return 0
    row=len(matrix)
    col=len(matrix[0])
    res=0
    for i in range(row):
        for j in range(col):
            if matrix[i][j]==2:
                return infect(matrix,i,j,row,col,res)
    return res

def infect(matrix,i,j,r,c,res):
    if i<0 or i>=r or j<0 or j>=c or matrix[i][j]!=1:
        return res
    res+=1
    res+=infect(matrix,i+1,j,r,c,res)
    res+=infect(matrix,i-1,j,r,c,res)
    res+=infect(matrix,i,j+1,r,c,res)
    res+=infect(matrix,i,j-1,r,c,res)
matr=[]
for i in range(5):
    tmp=list(map(int,input().split()))
    matr.append(tmp)
print(countisland(matr))
print(np.array(matr))