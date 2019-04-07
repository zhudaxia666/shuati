'''
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
'''
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        if not pRoot:
            return True
        return self.isSys(pRoot,pRoot)
    def isSys(self,root1,root2):
        if not root1 and not root2:
            return True
        if (not root1) ^ (not root2):
            return False
        if root1.val!=root2.val:
            return False
        return self.isSys(root1.left,root2.right) and self.isSys(root1.right,root2.left)

'''
别人的
'''
class Solution1:
    def isSymmetrical(self, pRoot):
        # write code here
        def is_same(p1,p2):
            if not p1 and not p2:
                return True
            if (p1 and p2) and p1.val==p2.val:
                return is_same(p1.left,p2.right) and is_same(p1.right,p2.left)
            return False
        if not pRoot:
            return True
        if pRoot.left and not pRoot.right:
            return False
        if not pRoot.left and pRoot.right:
            return False
        return is_same(pRoot.left,pRoot.right)