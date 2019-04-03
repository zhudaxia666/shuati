'''
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
要查找树A中是否存在和树B结构一样的子树，我们可以分为两步：第一步在树A中找到和B的根结点的值一样的结点R，
第二步再判断树A中以R为根节点的子树是不是包含和树B一样的结构。

这里使用递归的方法即可。
'''
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if pRoot1==None or pRoot2==None:
            return None
        return self.HasSubtree(pRoot1.left,pRoot2) or self.HasSubtree(pRoot1.right,pRoot2) or self.subtree(pRoot1,pRoot2)
    def subtree(self,A,B):
        if not B:
            return True
        if not A or A.val!=B.val:
            return False
        return self.subtree(A.left,B.left) and self.subtree(A.right,B.right)