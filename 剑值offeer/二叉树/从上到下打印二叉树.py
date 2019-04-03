'''
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
'''
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if not root:
            return []
        node=[]
        result=[]
        node.append(root)
        while node:
            a=node.pop(0)
            result.append(a.val)
            if a.left:
                node.append(a.left)
            if a.right:
                node.append(a.right)
        return result

