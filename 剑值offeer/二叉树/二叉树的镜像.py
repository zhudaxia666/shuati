'''
操作给定的二叉树，将其变换为源二叉树的镜像。
先交换根节点的两个子结点之后，我们注意到值为10、6的结点的子结点仍然保持不变，因此我们还需要交换这两个结点的左右子结点。
做完这两次交换之后，我们已经遍历完所有的非叶结点。此时变换之后的树刚好就是原始树的镜像
'''
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if root==None or (root.left==None and root.right==None):
            return None
        root.left,root.right=root.right,root.left
        if root.left:
            self.Mirror(root.left)
        if root.right:
            self.Mirror(root.right)

'''
别人的
'''
class Solution1:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root!=None:
            root.left,root.right=root.right,root.left
            self.Mirror(root.left)
            self.Mirror(root.right)