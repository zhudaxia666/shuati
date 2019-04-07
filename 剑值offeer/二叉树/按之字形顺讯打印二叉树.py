'''
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
思路：
和按行打印差不多，只是每层加入的顺序需要注意一下
'''
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        if not pRoot:
            return []
        depth=0
        res=[]
        l=[pRoot]
        while l:
            length=len(l)
            depth+=1
            row=[]
            for tem in l:
                row.append(tem.val)
            if depth%2==1:
                res.append(row)
            else:
                res.append(row[::-1])
            for i in range(length):
                root=l.pop(0)
                if root.left:
                    l.append(root.left)
                if root.right:
                    l.append(root.right)
        return res
'''
别人的
'''
class Solution1:
    def Print(self, pRoot):
        # write code here
        root=pRoot
        if not root:
            return []
        level=[root]
        result=[]
        lefttoright=False
        while level:
            curvalues=[]
            nextlevel=[]
            for i in level:
                curvalues.append(i.val)
                if i.left:
                    nextlevel.append(i.left)
                if i.right:
                    nextlevel.append(i.right)
            if lefttoright:
                curvalues.reverse()
            if curvalues:
                result.append(curvalues)
            level=nextlevel
            lefttoright=not lefttoright
        return result