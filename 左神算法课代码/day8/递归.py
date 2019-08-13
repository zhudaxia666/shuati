'''
打印一个字符串所有子序列
'''
def pringallchar(s,i,res):
    if i==len(s):
        print(res)
        return
    pringallchar(s,i+1,res)
    pringallchar(s,i+1,res+s[i])

string='abc'
pringallchar(string,0,'')

'''
给你一个二维数组，二维数组中每个数都是正数，要求从左上角走到右下角，每一步只能向右或者向下，沿途经过的数字要累加起来，返回最小的路径和
思路1：暴力递归

'''
def walk(matrix,i,j):
    if i==len(matrix) and j==len(matrix[0]):#已经到达右下角，直接返回
        return matrix[i][j]
    if i==len(matrix)-1:#到达最后一行
        return matrix[i][j]+walk(matrix,i,j+1)#当前值加上右边的部分
    if j==len(matrix[0])-1:#到达最后一列，向下方走
        return matrix[i][j]+walk(matrix,i+1,j)
    right=walk(matrix,i,j+1)#右边位置到左下角的最短路径和
    down=walk(matrix,i+1,j)#下边位置到右下角的最短路径
    return matrix[i][j]+min(right,down)

'''
给你一个数组arr，和一个整数aim，如果可以任意选择arr中的数字，能不能累加得到aim，返回true或者，false
'''
def isSum(arr,i,sum,aim):
    if i==len(arr):
        return sum==aim
    return isSum(arr,i+1,sum,aim) or isSum(arr,i+1,sum+arr[i],aim)#要当前值和不要当前值
