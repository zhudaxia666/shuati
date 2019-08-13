'''
分圈操作
先找出左上角和右下角的行和列，然后打印它们的边界，然后在往对角线移动
'''
# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        res=[]
        tr=0
        tl=0
        dr=len(matrix)-1
        dl=len(matrix[0])-1
        while tr<=dr and tl<=dl:
            self.printedge(matrix,tr,tl,dr,dl,res)
            tr+=1
            tl+=1
            dr-=1
            dl-=1
        return res
    def printedge(self,matrix,tr,tc,dr,dc,res):
        if tr==dr:
            for i in range(tc,dc+1):
                res.append(matrix[tr][i])
        elif tc==dc:
            for i in range(tr,dr+1):
                res.append(matrix[i][dc])
        else:
            curc=tc
            curr=tr
            while curc!=dc:
                res.append(matrix[tr][curc])
                curc+=1
            while curr!=dr:
                res.append(matrix[curr][dc])
                curr+=1
            while curc!=tc:
                res.append(matrix[dr][curc])
                curc-=1
            while curr!=tr:
                res.append(matrix[curr][tc])
                curr-=1