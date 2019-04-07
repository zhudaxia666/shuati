'''
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
思路：将每层的节点左右字数循环打印。
'''
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        res=[]
        tmp=[pRoot]
        while tmp:
            size=len(tmp)
            row=[]
            for i in tmp:
                row.append(i.val)
            res.append(row)
            for i in range(size):
                node=tmp.pop(0)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
        return res