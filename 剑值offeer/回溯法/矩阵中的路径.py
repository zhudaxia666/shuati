'''
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，
每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。 
例如 a b c e s f c s a d e e 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，
因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。

思路：
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，
每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。 
例如在下面的3x4的矩阵中包含一条字符串"bcced"的路径（路径中的字母用斜体表示）。但是矩阵中不包含"abcb"路径，
因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子
'''
# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        for i in range(rows):
            for j in range(cols):
                if matrix[i*cols+j]==path[0]:
                    if self.find(list(matrix),rows,cols,path[1:],i,j):#注意矩阵改成list类型的，不然通不过
                        return True
        return False
    def find(self,matrix,rows,cols,path,i,j):
        if not path:
            return True
        matrix[i*cols+j]='0'
        if (j+1)<cols and matrix[i*cols+j+1]==path[0]:
            return self.find(matrix,rows,cols,path[1:],i,j+1)
        elif (j-1)>=0 and matrix[i*cols+j-1]==path[0]:
            return self.find(matrix,rows,cols,path[1:],i,j-1)
        elif (i+1)<rows and matrix[(i+1)*cols+j]==path[0]:
            return self.find(matrix,rows,cols,path[1:],i+1,j)
        elif (i-1)>=0 and matrix[(i-1)*cols+j]==path[0]:
            return self.find(matrix,rows,cols,path[1:],i-1,j)
        else:
            False

#回溯法遍历矩阵中每一个位置
class Solution1:
    def hasPath(self,matrix,rows,cols,path):
        if not matrix:
            return False
        if not path:
            return True
        x=[list(matrix[cols*i:cols*i+cols]) for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if self.exist(x,i,j,path):
                    return True
        return False
    def exist(self,matrix,i,j,p):
        if matrix[i][j]==p[0]:
            if not p[1:]:
                return True
            matrix[i][j]=''
            if i>0 and self.exist(matrix,i-1,j,p[1:]):
                return True
            if i<len(matrix)-1 and self.exist(matrix,i+1,j,p[1:]):
                return True
            if j>0 and self.exist(matrix,i,j-1,p[1:]):
                return True
            if j<len(matrix)-1 and self.exist(matrix,i,j+1,p[1:]):
                return True
            matrix[i][j]=p[0]
            return False
        else:
            return False

# 链接：https://www.nowcoder.com/questionTerminal/c61c6999eecb4b8f88a98f66b273a3cc
# 来源：牛客网

# -*- coding:utf-8 -*-
#回溯法
#遍历矩阵中的每一个位置
class Solution3:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if not matrix:
            return False
        if not path:
            return True
        x = [list(matrix[cols*i:cols*i+cols]) for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if self.exist_helper(x, i, j, path):
                    return True
        return False
    def exist_helper(self, matrix, i, j, p):
        if matrix[i][j] == p[0]:
            if not p[1:]:
                return True
            matrix[i][j] = ''
            if i > 0 and self.exist_helper(matrix, i-1, j, p[1:]):
                return True
            if i < len(matrix)-1 and self.exist_helper(matrix, i+1, j ,p[1:]):
                return True
            if j > 0 and self.exist_helper(matrix, i, j-1, p[1:]):
                return True
            if j < len(matrix[0])-1 and self.exist_helper(matrix, i, j+1, p[1:]):
                return True
            matrix[i][j] = p[0]
            return False
        else:
            return False