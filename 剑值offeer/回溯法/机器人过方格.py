''''
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
'''
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.res=0
    def movingCount(self, threshold, rows, cols):
        block=[[0 for _ in range(cols)] for _ in range(rows)]
        def num_sum(r,c):
            s=sum(map(int,str(r)+str(c)))
            return s>threshold
        def tranfor(r,c):
            if not (0<=r<rows and 0<=c<cols):
                return
            if block[r][c]!=0:
                return
            if block[r][c]==-1 or num_sum(r,c):
                block[r][c]=-1
                return
            block[r][c]=1
            self.res+=1
            tranfor(r+1,c)
            tranfor(r-1,c)
            tranfor(r,c+1)
            tranfor(r,c-1)
        tranfor(0,0)
        return self.res
'''
思路：
思路：将地图全部置1，遍历能够到达的点，将遍历的点置0并令计数+1.这个思路在找前后左右相连的点很有用，
比如leetcode中的海岛个数问题/最大海岛问题都可以用这种方法来求解。
'''
class Solution:
    def __init__(self):
        self.count=0
    def movingCount(self, threshold, rows, cols):
        # write code here
        arr=[[1 for _ in range(cols)] for _ in range(rows)]
        self.findpath(arr,0,0,threshold)
        return self.count
    def findpath(self,arr,i,j,k):
        if i<0 or j<0 or i>=len(arr) or j>=len(arr[0]):
            return
        tmpi=list(map(int,list(str(i))))
        tmpj=list(map(int,list(str(j))))
        if sum(tmpi)+sum(tmpj)>k or arr[i][j]!=1:
            return
        arr[i][j]=0
        self.count+=1
        self.findpath(arr,i-1,j,k)
        self.findpath(arr,i+1,j,k)
        self.findpath(arr,i,j-1,k)
        self.findpath(arr,i,j+1,k)