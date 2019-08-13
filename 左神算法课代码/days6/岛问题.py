''''
布隆过滤器
认识一致性哈希
'''
'''
一个矩阵中只有0和1两种值，每个位置都可以和自己的上下左右四个位置相连，如果有一片1连在一起，这个部分叫做一个岛，求一个矩阵中有多少个岛
思路：遍历每个点，如果节点为1，就递归在上下左右找是否有相连的节点，如果有，就改为2
'''
def countisland(matrix):
    if not matrix:
        return 0
    row=len(matrix)
    col=len(matrix[0])
    res=0
    for i in range(row):
        for j in range(col):
            if matrix[i][j]==1:
                res+=1
                infect(matrix,i,j,row,col)
    return res

def infect(matrix,i,j,r,c):
    if i<0 or i>=r or j<0 or j>=c or matrix[i][j]!=1:
        return
    matrix[i][j]=2
    infect(matrix,i+1,j,r,c)
    infect(matrix,i-1,j,r,c)
    infect(matrix,i,j+1,r,c)
    infect(matrix,i,j-1,r,c)